import nlpositionality
import utils

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

def run_experiments(dataset_type):
    utils.download_dataset(nlpositionality.SOCIAL_ACCEPTABILITY, dataset_type=dataset_type)
    utils.download_dataset(nlpositionality.TOXICITY, dataset_type=dataset_type)

    for task, dataset_or_model in experiments:
        print(task, dataset_or_model)
        df = nlpositionality.get_pearson_rs(task, dataset_or_model, dataset_type=dataset_type)
        print(df)

if __name__ == "__main__":
    dataset_type = "raw" # Dataset with raw demographic values
    # dataset_type = "processed" # Dataset with processed demographic values
    run_experiments(dataset_type)