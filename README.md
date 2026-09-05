# 📊 Customer Churn Prediction System

A production-oriented **Machine Learning project** that predicts whether a customer is likely to churn based on customer demographic, service, contract, and billing information.

The project is being developed using a modular ML pipeline architecture with separate components for data ingestion, data transformation, model training, evaluation, and prediction.

---

## 🚀 Project Status

**Current Progress:**

* [x] Project structure created
* [x] Data Ingestion
* [x] Train/Test Split
* [x] Data Transformation & Preprocessing
* [x] Model Training
* [x] Model Evaluation
* [x] Model Selection
* [ ] Prediction Pipeline
* [ ] Web Application
* [ ] Deployment

---

## 🎯 Problem Statement

Customer churn is a major challenge for subscription-based businesses.

The objective of this project is to build a machine learning system that can identify customers who are likely to leave a service.

By predicting potential churners, businesses can take proactive actions such as:

* Customer retention campaigns
* Personalized offers
* Service improvements
* Targeted communication
* Customer support interventions

---

## 🧠 Machine Learning Objective

This project is a **Binary Classification** problem.

### Target Variable

```text
Churn
```

Possible values:

```text
Yes → Customer churned
No  → Customer did not churn
```

The final machine learning model will predict the probability/class of customer churn.

---

## 📂 Dataset

The project uses a customer churn dataset containing information related to:

### Customer Information

* Customer ID
* Gender
* Senior Citizen
* Partner
* Dependents

### Service Information

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

### Account Information

* Tenure
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

### Target

* Churn

---

# 🏗️ Project Architecture

The project follows a modular machine learning pipeline structure.

```text
Customer-Churn-Prediction-System/
│
├── artifacts/
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   └── data_transformation.py
│   │
│   ├── pipeline/
│   │
│   ├── exception.py
│   └── logger.py
│
├── app/
│   └── main.py
│
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

> The project structure will continue to evolve as model training, evaluation, prediction, and deployment components are added.

---

# 🔄 Current ML Pipeline

The implemented pipeline currently contains:

```text
Raw Dataset
     │
     ▼
Data Ingestion
     │
     ├── Load Dataset
     │
     ├── Train/Test Split
     │
     └── Save Train & Test Data
     │
     ▼
Data Transformation
     │
     ├── Handle Numerical Features
     │
     ├── Handle Categorical Features
     │
     ├── Convert Required Data Types
     │
     ├── Encode Binary Features
     │
     ├── One-Hot Encode Categorical Features
     │
     ├── Feature Scaling
     │
     └── Save Preprocessing Object
     │
     ▼
Transformed Data
```

---

# 🛠️ Data Ingestion

The **Data Ingestion** component is responsible for:

1. Reading the raw dataset.
2. Creating the required artifact directories.
3. Splitting the dataset into training and testing datasets.
4. Saving the resulting datasets for the next stage of the pipeline.

The project uses:

```python
train_test_split
```

from Scikit-learn.

The separation of data ingestion from transformation makes the pipeline modular and easier to maintain.

---

# 🔧 Data Transformation

The **Data Transformation** component handles the preprocessing required before feeding data into a machine learning model.

## Numerical Features

Numerical features are processed using appropriate preprocessing techniques such as:

* Missing-value handling
* Feature scaling

The transformation pipeline is designed using Scikit-learn's preprocessing utilities.

---

## 🏷️ Categorical Features

Categorical variables are divided into different types depending on their nature.

### Binary Features

Features containing two categories such as:

```text
Yes / No
```

are converted into numerical representations where appropriate:

```text
Yes → 1
No  → 0
```

This avoids unnecessary one-hot encoding for simple binary variables.

### Multi-Class Features

Categorical features containing multiple categories are handled using:

```text
OneHotEncoder
```

This converts categorical values into machine-learning-compatible numerical features.

---

# 💰 TotalCharges Data Cleaning

The dataset contains a `TotalCharges` feature that may initially be represented as an object/string data type.

The preprocessing pipeline handles the required conversion so that the feature can be treated as a numerical variable during machine learning.

This is an important preprocessing step because machine learning algorithms generally require numerical input.

---

# 🚫 Customer ID

`CustomerID` is an identifier rather than a meaningful predictive feature.

Therefore, it is excluded from the feature set used for model training.

The identifier can still be useful for tracking individual customers outside the model's feature matrix.

---

# 🛡️ Data Leakage Prevention

The project follows a proper preprocessing workflow to reduce the risk of **data leakage**.

The preprocessing transformations are fitted using the training data and then applied to the test data.

Conceptually:

```text
Training Data
     │
     ▼
fit_transform()
     │
     ▼
Learn preprocessing parameters


Test Data
     │
     ▼
transform()
     │
     ▼
Apply learned parameters
```

This ensures that information from the test dataset is not used while learning preprocessing parameters.

---

# 🧰 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📦 Project Dependencies

Main dependencies include:

```text
pandas
numpy
scikit-learn
```

Additional dependencies will be added as model training, application development, and deployment are implemented.

---

# 📝 Logging & Exception Handling

The project includes custom modules for:

### Logging

```text
src/logger.py
```

Used for tracking important events during pipeline execution.

### Exception Handling

```text
src/exception.py
```

Used for handling and reporting errors in a structured manner.

This improves debugging and makes the ML pipeline more production-oriented.

---

# 🔮 Upcoming Steps

The next stages of the project are:

### 1. Model Training

Train multiple classification algorithms such as:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Other suitable classification models

### 2. Model Evaluation

Evaluate models using metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

Since this is a churn prediction problem, special attention will be given to **Recall and False Negatives**, because failing to identify a customer who is actually going to churn can be costly for a business.

### 3. Model Selection

Compare different models and select the most appropriate model based on business and ML performance requirements.

### 4. Prediction Pipeline

Create an end-to-end prediction pipeline that accepts customer information and produces a churn prediction.

### 5. Application

Integrate the trained model with the application layer.

### 6. Deployment

Deploy the completed machine learning application so that predictions can be accessed through a user interface or API.

---

# 📈 Future Pipeline

The final architecture is planned to look like:

```text
                 Raw Dataset
                      │
                      ▼
              ┌───────────────┐
              │ Data Ingestion│
              └───────┬───────┘
                      │
                      ▼
            ┌───────────────────┐
            │ Data Transformation│
            └─────────┬─────────┘
                      │
                      ▼
              ┌──────────────┐
              │ Model Training│
              └───────┬──────┘
                      │
                      ▼
              ┌──────────────┐
              │ Model Evaluation
              └───────┬──────┘
                      │
                      ▼
                Best Model
                      │
                      ▼
              Prediction Pipeline
                      │
                      ▼
                 Application
                      │
                      ▼
                  Deployment
```

---

# 💡 Key Learning Areas

This project is designed to demonstrate practical understanding of:

* End-to-end Machine Learning workflows
* Data ingestion
* Train/Test splitting
* Data preprocessing
* Numerical feature transformation
* Categorical feature encoding
* One-hot encoding
* Feature scaling
* Data leakage prevention
* Scikit-learn pipelines
* Modular project architecture
* Logging
* Exception handling
* Model evaluation
* Classification metrics
* Model deployment

---

# 👨‍💻 Author

**Mohammad Asim**

This project is being developed as a practical end-to-end Machine Learning project with a focus on building a production-oriented ML pipeline.