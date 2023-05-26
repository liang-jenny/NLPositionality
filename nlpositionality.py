import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # Supress pandas warnings
from scipy import stats
from statsmodels.stats.multitest import multipletests

SOCIAL_ACCEPTABILITY = "social-acceptability"
TOXICITY = "toxicity"

SOCIAL_CHEM = "socialchem"
DELPHI = "delphi"
GPT4 = "gpt4"
DYNAHATE = "dynahate"
HATEROBERTA = "hateroberta"
PERSPECTIVE_API = "perspective"
REWIRE = "rewire"

def get_pearson_rs(task, model_or_dataset_name):
    """
        Inputs:
            - task (string): Task name (either "social acceptability" or "toxicity")
            - model_or_dataset_name (string): Name of a model or dataset (either "socialchem", "delphi", "gpt4", "dynahate",
              "hateroberta", "perspective", or "rewire")
        Returns:
            - pearson_rs (DataFrame): DataFrame representing the Pearson's r coefficients and p-values between the dataset 
              labels/model scores and LabintheWild volunteer annotations by demographic.
              
    """
    is_valid_social_acceptability = task == SOCIAL_ACCEPTABILITY and model_or_dataset_name in [SOCIAL_CHEM, DELPHI, GPT4]
    is_valid_toxicity = task == TOXICITY and model_or_dataset_name in [GPT4, DYNAHATE, HATEROBERTA, PERSPECTIVE_API, REWIRE]
    if is_valid_toxicity or is_valid_social_acceptability:
        df = pd.read_csv('data/{}_{}.csv'.format(task, "05-25-2023"))
    else:
        raise ValueError('Invalid task name or model or dataset name')

    results = {}
    pvalues = []
    for c in ['country_longest', 'education', 'ethnicity', 'gender', 'native_language', 'age', 'country_residence', 'religion']:
        demo = list(df[c].unique()) # Get all the demographics under a category
        demo.sort()
        
        if 'None' in demo:
            demo.remove('None')
            
        for d in demo:
            ndf = df[df[c] == d] # Get all the instances from a demographic group
            dndf = __mean_df__(ndf, model_or_dataset_name) # Average responses in a demographic group
            r, p = stats.pearsonr(dndf['litw'], dndf[model_or_dataset_name]) # Compute Pearson R values
            
            results[c + '_' + d] = r
            pvalues.append(p)

    assert(len(results) == len(pvalues))
        
    # Apply Berforroni stepwise correction
    alpha = 0.001
    hypotheses, pvalues, _, new_alpha = multipletests(pvalues, alpha, method='bonferroni', is_sorted=False, returnsorted=False)

    data = []
    for key, p, h in zip(results.keys(), pvalues, hypotheses):
        # Convert p-values and Pearson's rs to strings
        p = str(p)
        
        value = str(round(results[key], 2))
        if len(value) == 3:
            value += "0"
        value = value + '' + ('*' if h == True else '')

        data.append({
            "demographic": key,
            "pearson's r": value,
            "p-value": p
        })
        
    pearson_rs = pd.DataFrame(data=data) # Convert the data to a DataFrame
    return pearson_rs

def __mean_df__(df, model_or_dataset_name):
    ddf = df.groupby(['action']).mean()[['litw', model_or_dataset_name]].reset_index()
    ddf['litw'] = ddf['litw'].apply(lambda x: round(x))
    return ddf