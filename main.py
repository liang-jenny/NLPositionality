import nlpositionality
import pandas as pd
import requests
from io import StringIO

def download_dataset(task):
    """
        Inputs:
            - task (string): Task name (either "social-acceptability" or "toxicity")
        Outputs:
            - Downloads the dataset corresponding to the task name from the LabintheWild API.
    """
    url = "https://{}-litw.apps.allenai.org/api/dataset".format(task if task == nlpositionality.TOXICITY else "delphi")
    response = requests.get(url)
    
    df = pd.read_csv(StringIO(response.text), sep=",")
    df.to_csv('./data/nlpositionality_{}.csv'.format(task), index=False)

if __name__ == "__main__":
    download_dataset(nlpositionality.SOCIAL_ACCEPTABILITY)
    download_dataset(nlpositionality.TOXICITY)

    experiments = [
        (nlpositionality.SOCIAL_ACCEPTABILITY, nlpositionality.SOCIAL_CHEM),
        (nlpositionality.SOCIAL_ACCEPTABILITY, nlpositionality.DELPHI),
        (nlpositionality.SOCIAL_ACCEPTABILITY, nlpositionality.GPT4),
        (nlpositionality.TOXICITY, nlpositionality.DYNAHATE),
        (nlpositionality.TOXICITY, nlpositionality.PERSPECTIVE_API),
        (nlpositionality.TOXICITY, nlpositionality.REWIRE),
        (nlpositionality.TOXICITY, nlpositionality.HATEROBERTA),
        (nlpositionality.TOXICITY, nlpositionality.GPT4),
    ]

    for task, dataset_or_model in experiments:
        print(task, dataset_or_model)
        df = nlpositionality.get_pearson_rs(task, dataset_or_model)
        print(df)