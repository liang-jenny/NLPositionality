import nlpositionality

if __name__ == "__main__":
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