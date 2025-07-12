import pandas as pd
import numpy as np
import pickle 
import gradio as gr # type: ignore

# Load the model 
rfr_reloded = pickle.load(open("rfr_model.pkl", "rb"))
scaler_reloded = pickle.load(open("scaler.pkl", "rb"))

# Prediction funtion
def predict_gold_rate(usd_inr):
    input_df = pd.DataFrame([[usd_inr]], columns=["USD_INR"])
    scaled_input = scaler_reloded.transform(input_df)
    predict = rfr_reloded.predict(scaled_input)[0]
    
    return f"₹ {round(predict, 2)}"

# Creating interface
interface = gr.Interface(
    fn = predict_gold_rate,
    inputs = gr.Number(label = "Enter USD to INR Rate (e.g: 86.5)"),
    outputs = gr.Textbox(label ="Predicted Gold Price (INR per gram)"),
    title = "🪙 Gold Price Predictor - India",
    description = """
    This model predicts the **gold price per gram in INR** based on the current **USD to INR exchange rate**.
    Built using **Random Forest Regressor** trained on real world financial data (2024-2025).
    
    **Note:**  
    - This model achieves around **85%** accuracy using USD-INR rates.
    - However, gold prices are influenced by multiple economic and seasonal factors such as crude oil prices, inflation, stock market trends, festivals, and taxes.
    """,
    theme = "soft",
    examples = [[85.5], [86.5], [84.86]]
)

# Lauch the app
interface.launch(share=True)