# Sales & Demand Forecasting using Machine Learning

## Project Overview

This project predicts **weekly sales** for retail stores using Machine Learning techniques.
It helps businesses make better decisions in inventory planning, demand forecasting, and sales strategy.

---

##  Live Demo

 **Streamlit App:https://futureml01-fnxrryz8bjdhtta7zlwbea.streamlit.app/**

---

##  Dataset

* Dataset used: Walmart Sales Dataset
* Features include:

  * Store ID
  * Holiday Flag
  * Temperature
  * Fuel Price
  * CPI
  * Unemployment
  * Date

---

##  Data Preprocessing

* Converted `Date` column into datetime format
* Extracted time-based features:

  * Year, Month, Week
* Handled missing values
* Converted categorical data (Holiday_Flag)
* Defined features (X) and target (y)

---

##  Models Used

* Linear Regression (Baseline model)
* Random Forest Regressor (Final model)

---

##  Model Evaluation

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

 Random Forest performed better than Linear Regression, indicating non-linear patterns in sales data.

---

## Streamlit Web App

A user-friendly web application was built using Streamlit where users can input features and get predicted weekly sales in real time.

---

##  Run Locally

```bash
streamlit run app.py
```

---

##  Requirements

* streamlit
* pandas
* numpy
* scikit-learn

---

##  Key Learnings

* Time-series feature engineering
* Model building and evaluation
* Handling real-world business data
* Building ML-powered web apps

---

## Conclusion

This project demonstrates how Machine Learning can be applied to real-world business problems like sales forecasting.
Random Forest provided better predictions compared to Linear Regression.

---

##  Future Improvements

* Use advanced models like XGBoost / ARIMA
* Add interactive dashboards
* Deploy with real-time data

---

##  Author
**HUSSAIN BASHA**

---
