# Customer Gender Prediction 🎯

This project predicts the *gender* of a customer using a machine learning model built with a Gradient Boosting Classifier. The backend is powered by *Flask* and deployed using *Render*. A Flutter-based frontend is also available, making this a complete full-stack machine learning solution.

## 🔗 Live Backend

The backend API is live and hosted on Render:  
 *[https://customer-prediction.onrender.com](https://customer-prediction.onrender.com)*

---

## Project Structure
ML_proj_video/ # Contains demonstration video (Google Drive link)
├── pycache/ # Compiled Python files
├── README.md # Project documentation
├── gbc_model.pkl # Trained Gradient Boosting model
├── main.py # Flask app for serving predictions
├── requirements.txt # List of dependencies
---

##  Model Overview

- **Algorithm**: Gradient Boosting Classifier  
- **Purpose**: Predict the gender of the customer  
- **Model File**: `gbc_model.pkl`  
- **Inputs**: Customer behavioral and service-related features

---

##  Getting Started

### Prerequisites

- Python 3.7 or higher  
- pip (Python package manager)

### Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt


Running Locally
Run the Flask app:
python main.py

Visit http://localhost:5000 in your browser or use an API client like Postman.

 Frontend
We have built a frontend mobile application using Flutter to interact with this backend API.
This repository only includes the backend code, deployed via Render:
 https://customer-prediction.onrender.com

 Demo Video
The demonstration video is available in the ML_proj_video/ folder.
Alternatively, view it on Google Drive (insert actual link if available).

 
