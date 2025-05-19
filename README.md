🌫️ Air Quality Prediction using Random Forest
This project aims to predict Air Quality Index (AQI) using a machine learning model trained on pollutant data from Indian cities. The model uses a Random Forest Regressor and includes an interactive Jupyter Notebook UI for real-time AQI prediction.

🔍 Problem Statement
Air pollution is a major environmental issue affecting human health and quality of life. By predicting AQI based on pollutant levels, this project helps in forecasting pollution levels, enabling proactive decision-making for public safety and urban planning.

This project leverages pollutant data to build a robust AQI predictor with visual insights and a user-friendly interface.

🚀 Features
📊 Data preprocessing and feature engineering using pollutant and date features

🌡️ AQI approximation based on maximum pollutant concentration

⚙️ Model training using Random Forest Regressor

📈 Performance evaluation using R² score, RMSE, and MAE

🔥 Feature importance and correlation heatmap visualization

🧮 Residual plot for model error analysis

🧩 Jupyter-based interactive UI for real-time AQI prediction

💾 Model and scaler saved using joblib

📦 Tech Stack
Language:

Python

Libraries:

pandas, NumPy

scikit-learn

matplotlib, seaborn

joblib

ipywidgets (for interactive input UI)

🧠 Model
Algorithm Used:

Random Forest Regressor

Evaluation Metrics:

R² Score

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

Input Features:

PM2.5, PM10, NO2, CO, SO2, O3

Date Features: Year, Month, Day

🌐 Try the Live App: https://airqualityprediction-6ywhdsoucnyrq9rcd4i4cy.streamlit.app/

📊 Sample Inputs for AQI Prediction
Feature	Example Value
PM2.5-	83.2
PM10-	150.5
NO2-	40.7
CO-	1.4
SO2-	12.3
O3-	35.0
Year-	2025
Month-	5
Day-	19
