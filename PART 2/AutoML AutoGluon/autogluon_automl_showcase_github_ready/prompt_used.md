# Prompt Used

> Build a GitHub-ready data-science project illustrating **AutoML with AutoGluon** across multiple common tabular tasks.
>
> Use the **CRISP-DM framework**:
> 1. Business Understanding
> 2. Data Understanding
> 3. Data Preparation
> 4. Modeling
> 5. Evaluation
> 6. Deployment / Selection
>
> Demonstrate at least:
> - binary classification
> - multiclass classification
> - regression
>
> Use popular, easily reproducible datasets and AutoGluon's `TabularPredictor`.
>
> For each task:
> - load and inspect the dataset;
> - create a train/test split;
> - choose a sensible evaluation metric;
> - train AutoGluon;
> - display the leaderboard;
> - evaluate on holdout data;
> - explain the winning model and ensemble behavior.
>
> Include a polished **Data Science Admin Dashboard** showing:
> - number of tasks;
> - datasets;
> - problem types;
> - AutoML workflow;
> - task portfolio;
> - evaluation and governance notes.
>
> Clearly explain that AutoML automates the modeling layer but does not replace business understanding, data-quality decisions, leakage prevention, evaluation design, or deployment governance.
>
> Keep GitHub minimal. Include only:
> - one notebook
> - README.md
> - prompt_used.md
> - images/
>
> The notebook should install `autogluon.tabular` automatically if it is not already available, making it easy to run in Google Colab.
