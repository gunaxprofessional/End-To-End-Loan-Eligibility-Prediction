# Introduction:
The Loan Eligibility Prediction project is a machine learning-based application that predicts whether a loan application is eligible or not based on various parameters such as education, income, and credit history. The project was built using Python programming language, various machine learning algorithms, data analysis techniques, and the Optuna library for hyperparameter tuning. Then, I deployed the final model using the Streamlit cloud platform. The web app can be found here https://gunaxprofessional-end-to-end-loan-eligibil-streamlit-app-mo3bj5.streamlit.app/

# Dataset:
The dataset used in this project is the Loan Prediction Dataset, which contains information on loan applicants, such as gender, education, income, credit history, loan amount, loan term, and others.

# Algorithms:
In this project, 15 different machine learning algorithms were used to predict the eligibility of the loan application. The algorithms used in this project are Decision Tree, Random Forest, KNN, SVM, Naive Bayes, Logistic Regression, XGBoost, LightGBM, CatBoost, AdaBoost, Gradient Boosting, Extra Trees, MLP, LDA, and QDA.

![image](https://user-images.githubusercontent.com/66107066/233781575-0635eb47-fbb8-4349-9bf1-8a04e1e2d446.png)

# EDA:
EDA was performed using the pandas_profiling library, which provided an overall view of the dataset, including the number of variables, missing values, and correlations between variables.

# Hyperparameter Tuning:
After comparing the performance of all the algorithms, the Random Forest Classifier was selected as the best performing algorithm, and hyperparameter tuning was performed using Optuna. The best hyperparameters were then used to build the final model.

# Results:
The final model achieved an accuracy of 0.824673, precision of 0.795929, recall of 0.897356, F1-score of 0.839244, and ROC AUC of 0.887320.

# Conclusion:
The Loan Eligibility Prediction project shows the use of various machine learning algorithms, data analysis techniques, and hyperparameter tuning to predict the eligibility of a loan application. The project can be further enhanced by adding more features and improving the accuracy of the model.
