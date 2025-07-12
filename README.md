# 🪙 Gold Price Predictor - India (Gradio App)

A Machine Learning-powered application that predicts the **22K gold price per gram (INR)** in India based on the **USD to INR exchange rate**.

> 🚀 Built as a job-ready ML project to demonstrate skills in data scraping, preprocessing, model building, evaluation, and web deployment using Gradio.

---

## 💡 Problem Statement

Gold prices in India fluctuate daily and are strongly influenced by the USD to INR exchange rate. This project:
- Collects historical gold prices (22K per gram) and USD/INR rates.
- Trains a regression model to predict daily gold price.
- Deploys the prediction interface using Gradio for real-time input/output.

---

## 📊 Data Sources

- **Gold Price Data**: Scraped using `requests` and `re` (from `exchange-rates.org`)
- **USD to INR Data**: Downloaded via `yfinance`

---

## ⚙️ Tools & Libraries Used

| Category             | Tools / Libraries                          |
|----------------------|--------------------------------------------|
| Language             | Python                                     |
| Data Collection      | `requests`, `re`, `yfinance`, `pandas`     |
| Visualization        | `matplotlib`, `seaborn`, `plotly.express`  |
| Data Scaling         | `StandardScaler`                           |
| ML Models            | `LinearRegression`, `RandomForestRegressor`|
| Model Selection      | `train_test_split`                         |
| Evaluation Metrics   | `MAE`, `MSE`, `R² Score`                   |
| Interface / UI       | `Gradio`                                   |
| Serialization        | `pickle`                                   |

---

## ✅ Features

- 📈 Predicts **22K gold price per gram in INR**.
- 🏦 User inputs the **current USD to INR exchange rate**.
- 🧠 Trained using **Random Forest Regressor** for higher accuracy.
- 🌍 Deployed using Gradio for interactive web access.

---

## 📉 Model Performance

| Metric     | Score     |
|------------|-----------|
| MAE        | 262.26    |
| MSE        | 186,641.77|
| R² Score   | 0.8563    |

> 🎯 Achieved strong accuracy with just one feature (USD to INR), demonstrating practical modeling skills and potential for further enhancement.

---

## 🌐 Live Demo

Try it out:  
🔗 [https://huggingface.co/spaces/sankarans2001/gold-price-predictor](https://huggingface.co/spaces/sankarans2001/gold-price-predictor)  
*(Replace with your actual Space URL)*

---

## 🗂 Project Files
📁 gold-price-predictor/
├── gold_dataset.csv # Web-scraped dataset
├── scaler.pkl # Pre-fitted StandardScaler
├── rfr_model.pkl # Trained RandomForestRegressor
├── app.py # Gradio interface logic
├── gold-prediction.pdf # End-to-end notebook pdf: data → model → evaluation
├── README.md # Project documentation
