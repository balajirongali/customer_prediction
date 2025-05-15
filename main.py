from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load your trained model
model = joblib.load("gbc_model.pkl")  # rename if needed

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SalesInput(BaseModel):
    invoice_id: float
    branch: float
    city: float
    customer_type: float
    product_line: float
    unit_price: float
    quantity: float
    tax_5_percent: float
    total: float
    date: float
    time: float
    payment: float
    cogs: float
    gross_margin_percentage: float
    gross_income: float
    rating: float

@app.post("/predict")
def predict(data: SalesInput):
    input_data = np.array([[
        data.invoice_id,
        data.branch,
        data.city,
        data.customer_type,
        data.product_line,
        data.unit_price,
        data.quantity,
        data.tax_5_percent,
        data.total,
        data.date,
        data.time,
        data.payment,
        data.cogs,
        data.gross_margin_percentage,
        data.gross_income,
        data.rating
    ]])
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}
