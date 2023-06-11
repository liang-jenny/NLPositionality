import json
import nlpositionality
import pandas as pd
import requests
from io import StringIO

def download_dataset(task, dataset_type="raw"):
    """
        Inputs:
            - task (string): Task name (either "social-acceptability" or "toxicity")
        Outputs:
            - Downloads the dataset corresponding to the task name from the LabintheWild API.
    """
    url = "https://{}-litw.apps.allenai.org/api/dataset?type={}".format(
        task if task == nlpositionality.TOXICITY else "delphi", 
        dataset_type)
    response = requests.get(url)
    
    df = pd.read_csv(StringIO(response.text), sep=",")
    df.to_csv('./data/nlpositionality_{}_{}.csv'.format(task, dataset_type), index=False)

def process_litw_data(old_df):
    """
        Inputs:
            - old_df (DataFrame): Joined dataset with raw demographic values, LabintheWild and dataset annotations, and model predictions
        Outputs:
            - df (DataFrame): Joined dataset with processed demographic values for analysis
    """
    df = old_df.copy()
    df['age'] = df['age'].apply(__process_age__)
    df['gender'] = df['gender'].apply(__process_gender__)
    df['ethnicity'] = df['ethnicity'].apply(__process_ethnicities__)
    df['religion'] = df['religion'].apply(__process_religion__)
    df['education'] = df['education'].apply(__process_education__)
    df['native_language'] = df['native_language'].apply(lambda x: __filter_language_english__(__process_language__(x)))
    df['country_longest'] = df['country_longest'].apply(lambda x: __filter_country_sphere__(__process_country__(x)))
    df['country_residence'] = df['country_residence'].apply(lambda x: __filter_country_sphere__(__process_country__(x)))

    return df

def __process_age__(val):
    """
        Inputs:
            - val (int): age value to be processed
        Outputs:
            - (string): age group the value belongs to; "None" if the value is null
    """
    if pd.isnull(val):
        return 'None'
    if val >= 10 and val < 20:
        return '10-20'
    if val >= 20 and val < 30:
        return '20-30'
    if val >= 30 and val < 40:
        return '30-40'
    if val >= 40 and val < 50:
        return '40-50'
    if val >= 50 and val < 60:
        return '50-60'
    if val >= 60 and val < 70:
        return '60-70'
    if val >= 70 and val < 80:
        return '70-80'
    if val >= 80:
        return '> 80'
    return 'None'

def __process_gender__(val):
    """
        Inputs:
            - val (string): gender value to be processed
        Outputs:
            - (string): gender category the value belongs to ("man", "woman", "non-binary"); "None" if the value is null or not in one of the three categories
    """

    if val == 'man':
        return 'man'
    if val == 'woman':
        return 'woman'
    if val == 'non-binary':
        return 'non-binary'
    
    #removing nans before string operations
    if pd.isnull(val):
        return 'None'
    
    #we group them in non-binary for now
    if 'agender' in val.lower():
        return 'non-binary'
    if 'genderfluid' in val.lower():
        return 'non-binary'
    
    #otherwise none, includes random fillings and no response
    return 'None'
    
def __process_ethnicities__(val):
    """
        Inputs:
            - val (string): ethnicity value to be processed
        Outputs:
            - (string): ethnicity category the value belongs to; "None" if the value is null or not in one of the predefined categories
    """
    stored = ['white', 'asian, asian american', 'pacific islander, native australian', 'black, african american', 'latino/latina, hispanic', 'mixed', 'Arab-american', 'native american, american indian, alaska native']
    if val in stored:
        return val.split(',')[0].lower()
    return "None"

def __process_religion__(val):
    """
        Inputs:
            - val (string): religion value to be processed
        Outputs:
            - (string): religion category the value belongs to; "None" if the value is null or not in one of the predefined categories
    """

    if pd.isnull(val):
        return 'None'
    
    if val.lower() in ["roman catholic", "protestant", "orthodox", "christian", "baptist"] or "christian" in val.lower():
        return "christian"
    
    if val.lower() in ["agnostic theist", "spiritual", "paganism"]:
        return "spiritual"
    
    if val.lower() in ["hindu", "buddhist", "muslim", "jew"]:
        return val
    return "None"

def __process_education__(val):
    """
        Inputs:
            - val (string): education value to be processed
        Outputs:
            - (string): education category the value belongs to; "None" if the value is null or not in one of the predefined categories
    """
    if pd.isnull(val):
        return 'None'
    
    stored = ["college", "high school", "graduate school", "phd", "professional school", "pre-high school"]
    
    if val.lower() in stored:
        return val
    
    return "None"

def __process_language__(val):
    """
        Inputs:
            - val (string): language value to be processed
        Outputs:
            - (string): language value if it is not null; "None" if the value is null 
    """
    if pd.isnull(val):
        return 'None'
    return val

def __filter_language_english__(val):
    """
        Inputs:
            - val (string): language value to be processed
        Outputs:
            - (string): language category the value belongs to ("english", "not english"); "None" if the value is null or not in one of the predefined categories 
    """
    if val == 'None':
        return val
    
    if val == 'English':
        return 'english'
    
    return 'not english'

def __process_country__(val):
    """
        Inputs:
            - val (string): country value to be processed
        Outputs:
            - (string): country value if it is not null; "None" if the value is null 
    """
    if pd.isnull(val):
        return 'None'
    return val

def __filter_country_sphere__(val):
    """
        Inputs:
            - val (string): country value to be processed
        Outputs:
            - (string): country category the value belongs to based on cultural spheres; "None" if the value is null or not in one of the predefined categories 
    """
    spheres = json.load(open('./data/spheres.json'))
    if val not in spheres:
        return 'None'
    return spheres[val]