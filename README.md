# 💻 Laptop Price Predictor

A Machine Learning web application that predicts the price of a laptop based on its specifications.

The model is built using **Gradient Boosting Regression** and deployed using **Streamlit**.

## 🚀 Live Demo

Coming soon...

## 📌 Features

- Predict laptop prices based on specifications
- Interactive Streamlit interface
- Machine Learning regression model
- Data preprocessing and feature engineering
- One-hot encoding for categorical features
- Log transformation of the target variable

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib
- Seaborn

## 🤖 Machine Learning

Several regression algorithms were evaluated, including:

- Linear Regression
- Ridge Regression
- Lasso Regression
- KNN Regression
- Decision Tree Regression
- SVR
- Random Forest Regression
- Extra Trees Regression
- Gradient Boosting Regression
- XGBoost Regression

The final model uses **Gradient Boosting Regression** with hyperparameter tuning using `RandomizedSearchCV`.

### Model Performance

| Metric | Score |
|---|---:|
| R² Score (log-price) | 0.869 |
| MAE (log-price) | 0.169 |
| MAE (actual price) | ~₹10,146 |

## 📂 Project Structure

```text
Laptop-Price-Predictor/
│
├── app.py
├── laptop_data.csv
├── laptop_price_predictorModel.ipynb
├── pipe.pkl
├── df.pkl
├── requirements.txt
├── .gitignore
└── README.md
