# CMPE 255 — Assignment 1

## Predicting Student Dropout and Academic Success with Machine Learning

This repository contains my end-to-end data science project for **CMPE 255 Assignment 1**.  
The project uses the popular Kaggle dataset **Predict Students' Dropout and Academic Success** and follows the **CRISP-DM** methodology from business understanding through model evaluation and deployment recommendations.

**Dataset:** https://www.kaggle.com/datasets/satyajeetbedi/students-dropout-and-academic-success

---

## Project Goal

The goal is to predict a student's academic outcome as one of three classes:

- **Dropout**
- **Enrolled**
- **Graduate**

The project also studies which factors are associated with student success and discusses how a model like this could be used responsibly as an early-warning support system.

---

## CRISP-DM Workflow

### 1. Business Understanding
Defined the student-retention problem, stakeholders, prediction objective, success metrics, and responsible-use considerations.

### 2. Data Understanding
Performed:
- dataset inspection and profiling
- missing-value and duplicate checks
- data-quality validation
- descriptive statistics
- class-imbalance analysis
- exploratory data analysis
- outlier review
- correlation analysis

### 3. Data Preparation
Performed:
- cleaning hidden BOM/tab characters from column names
- separation of nominal, binary, ordinal, and true numerical variables
- leakage-safe stratified 80/20 train-test split
- one-hot encoding for nominal features
- scaling for scale-sensitive models
- model-specific preprocessing pipelines

### 4. Feature Selection
Compared:
- Mutual Information
- correlation among true numerical features
- tree-based feature importance

Semester academic-performance variables were the strongest predictors, especially approved curricular units and semester grades.

### 5. Modeling
Models evaluated:
- DummyClassifier baseline
- Logistic Regression
- Random Forest
- XGBoost
- Neural Network (MLP)

### 6. Evaluation
Primary metric: **Macro F1**, because the target classes are imbalanced.

| Model | Test Accuracy | Test Macro F1 |
|---|---:|---:|
| DummyClassifier | 0.4994 | 0.2221 |
| Logistic Regression | 0.7706 | 0.6969 |
| Random Forest | **0.7729** | 0.6757 |
| XGBoost | 0.7650 | **0.7013** |
| Neural Network | 0.7446 | 0.6727 |

The **Enrolled** class was consistently the hardest to predict.

### 7. Cross-Validation and Tuning
Stratified 5-fold cross-validation confirmed that XGBoost and Logistic Regression were the strongest and most stable candidates.

Approximate mean CV Macro F1:
- XGBoost: **~0.716**
- Logistic Regression: **~0.701**
- Random Forest: **~0.673**

Light XGBoost tuning improved CV performance only slightly but did not improve the untouched test-set Macro F1, so the original XGBoost configuration remained the preferred candidate.

---

## Key Findings

- Academic progress after enrollment was the strongest predictor of final outcome.
- First- and second-semester approved units and grades clearly separated graduates from dropouts.
- Students whose tuition fees were not up to date had a much higher dropout proportion in this dataset.
- Scholarship holders showed a substantially higher graduation proportion.
- Admission grades were useful but much less discriminative than semester performance.
- The Enrolled class was the most difficult because it is smaller and overlaps behaviorally with both Dropout and Graduate students.
- High predictive power from second-semester features creates a timing limitation: these features cannot be used for a true enrollment-time early-warning system.

---

## Responsible Data Science Considerations

This model should be used only as a **decision-support tool** for supportive interventions such as advising, tutoring, mentoring, and financial-aid outreach.

Important limitations include:
- class imbalance
- temporal leakage risk if late-semester variables are presented as enrollment-time predictors
- fairness concerns involving demographic and socioeconomic variables
- limited generalizability beyond the institution represented in the dataset
- need for privacy controls, monitoring, drift detection, and periodic retraining

---

## Repository Structure

```text
CMPE255_Assignment1/
├── README.md
├── Student_Dropout.ipynb
├── images/
│   ├── 01_target_distribution.png
│   ├── 02_age_by_outcome.png
│   ├── 03_tuition_status_outcomes.png
│   ├── 04_first_semester_grade.png
│   ├── 05_second_semester_grade.png
│   ├── 06_approved_units.png
│   ├── 07_model_comparison.png
│   ├── 08_cross_validation_macro_f1.png
│   └── 09_tuned_xgboost_confusion_matrix.png
└── data.csv

```

---

## How to Run

The notebook was designed for **Google Colab**.

1. Open `Student_Dropout_Prediction_CRISPDM.ipynb` in Google Colab.
2. Run the cells in order.
3. If prompted, upload `data.csv`.
4. Install XGBoost if the environment does not already provide it.
5. Review the EDA, model evaluation, cross-validation, and tuning outputs.

---

## Assignment Deliverables

### Part 1
- [x] Kaggle dataset selected
- [x] End-to-end data science analysis with ChatGPT assistance
- [x] Deep-learning model included
- [x] Colab notebook
- [x] GitHub README and project artifacts
- [x] ChatGPT transcript PDF 
- [x] Medium article published 
- [x] YouTube walkthrough published 

**ChatGPT Link:** [Walkthrough](https://chatgpt.com/share/6a960a80-1624-83ea-bdf7-ae17bf966e80)

**Medium Article:** [Can Machine Learning Help Identify Students at Risk?
](https://medium.com/@nehlinshanila/can-machine-learning-help-identify-students-at-risk-a97b8303c197?postPublishedType=initial)  

**YouTube Walkthrough:** ADD_YOUTUBE_LINK_HERE

---

## Final Model Recommendation

The original **XGBoost** model is the strongest current candidate because it achieved the best balanced multiclass performance (Macro F1) and handled the difficult Enrolled class better than the other initial models.

Logistic Regression remains an important alternative because its performance was very close while being simpler and easier to interpret.

---

## Tools and Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, XGBoost, Google Colab, ChatGPT, GitHub, Kaggle, Medium.
