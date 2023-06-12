# NLPositionality

## Project
This is the project repository for the NLPositionality project. To learn more about the project, please read our [paper](https://arxiv.org/abs/2306.01943) or visit our [project page](http://nlpositionality.cs.washington.edu/), which has the most up-to-date analysis results and visualizations.

## Paper
__NLPositionality: Characterizing Design Biases of Datasets and Models__<br>
Sebastin Santy*, Jenny T. Liang*, Ronan Le Bras, Katharina Reinecke, Maarten Sap<br>
_ACL 2023_

(* denotes equal contribution)

### Bibtex
```
@inproceedings{santyliang2023nlpositionality,
  title={NLPositionality: Characterizing Design Biases of Datasets and Models},
  author={Santy, Sebastin and Liang, Jenny T. and Le Bras, Ronan and Reinecke, Katharina and Sap, Maarten},
  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2023}
}
```

## Dataset

### Download
You can download the NLPositionality data annotations gathered on [LabintheWild](https://labinthewild.org) by clicking any of the following links:

#### Social Acceptability
* **[https://delphi-litw.apps.allenai.org/api/dataset?type=raw](https://delphi-litw.apps.allenai.org/api/dataset?type=raw)**. The dataset annotations with the **demographic information unprocessed**.
* **[https://delphi-litw.apps.allenai.org/api/dataset?type=processed](https://delphi-litw.apps.allenai.org/api/dataset?type=processed)**. The dataset annotations with the **demographic information processed** in the same way done in the NLPositionality paper and website.

#### Hate Speech & Toxicity
* **[https://toxicity-litw.apps.allenai.org/api/dataset?type=raw](https://toxicity-litw.apps.allenai.org/api/dataset?type=raw)**. The dataset annotations with the **demographic information unprocessed**.
* **[https://toxicity-litw.apps.allenai.org/api/dataset?type=processed](https://toxicity-litw.apps.allenai.org/api/dataset?type=processed)**. The dataset annotations with the **demographic information processed** in the same way done in the NLPositionality paper and website.

### Format

#### Social Acceptability
| Column Name | Description |
| :--- | :---- | 
| action | An action from the [Social Chemsitry](https://maxwellforbes.com/social-chemistry/) dataset. | 
| situation* | The situation corresponding to the action, as determined by the [Social Chemistry](https://maxwellforbes.com/social-chemistry/) dataset. | 
| session_id | The [LabintheWild](https://labinthewild.org) annotator's unique session ID. |
| litw | The [LabintheWild](https://labinthewild.org) annotator's annotation for the action (-2, -1, 0, 1, 2). |
| socialchem | The mean of the [Social Chemistry](https://maxwellforbes.com/social-chemistry/) annotator's labels of the action (between -2 and 2). |
| delphi | The [Delphi](https://delphi.allenai.org/) model's prediction of the action (-1, 0 1).|
| gpt4 | The [GPT-4](https://openai.com/gpt-4) model's prediction of the action (-1, 0 1). |
| age | The age of the [LabintheWild](https://labinthewild.org) annotator. |
| gender | The gender of the [LabintheWild](https://labinthewild.org) annotator. |
| ethnicity | The ethnicity of the [LabintheWild](https://labinthewild.org) annotator. If there are multiple ethnicities, there are multiple entries for the user. |
| religion | Religion the [LabintheWild](https://labinthewild.org) annotator practices. |
| education | The highest level of education the [LabintheWild](https://labinthewild.org) annotator attained. |
| country_longest | The country the [LabintheWild](https://labinthewild.org) annotator lived in the longest. |
| country_residence | The country the [LabintheWild](https://labinthewild.org) annotator currently lives in. |
| native_language | The native language of the [LabintheWild](https://labinthewild.org) annotator. |

\* We do not use situation significantly in our analysis, as annotators only annotate the situation, not the action. There is a 1:1 mapping of actions to situations.

#### Hate Speech & Toxicity
| Column Name | Description |
| :--- | :---- | 
| action | An instance from the [Dynahate](https://aclanthology.org/2021.acl-long.132.pdf) dataset. | 
| session_id | The [LabintheWild](https://labinthewild.org) annotator's unique session ID. |
| litw | The [LabintheWild](https://labinthewild.org) annotator's annotation for the action (-1, 0, 1). |
| dynahate | The [Dynahate](https://aclanthology.org/2021.acl-long.132.pdf) annotator's label of the action (0, 1). |
| perspective | The [Perspective API](https://perspectiveapi.com/) model's prediction of the action (between 0 and 1).|
| rewire | The [Rewire API](https://rewire.online/rewire-api-access/) model's prediction of the action (between 0 and 1).|
| hateroberta | The [ToxiGen RoBERTa](https://aclanthology.org/2022.acl-long.234.pdf) model's prediction of the action (between -1 and 1).|
| gpt4 | The [GPT-4](https://openai.com/gpt-4) model's prediction of the action (0, 1). |
| age | The age of the [LabintheWild](https://labinthewild.org) annotator. |
| gender | The gender of the [LabintheWild](https://labinthewild.org) annotator. |
| ethnicity | The ethnicity of the [LabintheWild](https://labinthewild.org) annotator. If there are multiple ethnicities, there are multiple entries for the user. |
| religion | Religion the [LabintheWild](https://labinthewild.org) annotator practices. |
| education | The highest level of education the [LabintheWild](https://labinthewild.org) annotator attained. |
| country_longest | The country the [LabintheWild](https://labinthewild.org) annotator lived in the longest. |
| country_residence | The country the [LabintheWild](https://labinthewild.org) annotator currently lives in. |
| native_language | The native language of the [LabintheWild](https://labinthewild.org) annotator. |

## Code
This code will assist in downloading the most up-to-date data and replicating our analyses featured in our [paper](https://arxiv.org/abs/2306.01943) and [website](http://nlpositionality.cs.washington.edu/).

To replicate our analyses, please follow these steps:
1. **Clone this repository**. `git clone https://github.com/liang-jenny/NLPositionality.git`
2. **Install the required dependencies for this project**. `pip install requirements.txt`
3. **Run `main.py`**. `python main.py` <br> 
Note there are two options for this script: using the raw dataset (i.e., with unprocessed demographic data) or the processed dataset (i.e., processed in the same way as in our analyses). Please ensure that `dataset_type` variable is set to the correct value (i.e., `"raw"` or `processed`). 

### Quick Tour
* `main.py` contains all the experiments ran in the NLPositionality paper.
* `utils.py` contains the code used to process demographics.
* `nlpositionality.py` contains the code used for calculating the Pearson's r correlation between demographics and model predictions / dataset labels, including the Bonferroni stepwise correction.