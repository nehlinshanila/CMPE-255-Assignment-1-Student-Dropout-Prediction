# Prompt Used

> Build an end-to-end GitHub-ready **anomaly detection** project using the popular Kaggle / ULB Credit Card Fraud Detection dataset.
>
> Follow the **CRISP-DM framework**:
> 1. Business Understanding
> 2. Data Understanding
> 3. Data Preparation
> 4. Modeling
> 5. Evaluation
> 6. Deployment
>
> Use popular anomaly-detection methods:
> - Isolation Forest
> - Local Outlier Factor
> - One-Class SVM
>
> Treat fraud labels as evaluation labels, not modeling inputs.
>
> Because the dataset is extremely imbalanced, do not use accuracy as the main success metric. Evaluate using:
> - Average Precision / PR-AUC
> - ROC-AUC
> - precision
> - recall
> - F1
> - top-k / review-queue fraud capture
>
> Frame deployment as a ranked fraud-investigation queue with a threshold driven by review capacity.
>
> Include a polished **data science admin dashboard** designed like a fraud-operations console. Show transaction volume, actual fraud, review queue size, fraud capture, model comparison, and operational recommendations.
>
> Keep the GitHub repository minimal. Include only:
> - one Jupyter notebook
> - README.md
> - prompt_used.md
> - images/
>
> The notebook should attempt to download the full public OpenML/Kaggle benchmark automatically. If internet is unavailable, it may use an explicitly labeled offline validation fallback, but fallback results must never be presented as Kaggle benchmark performance.
