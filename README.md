# Electricity Demand Classification in Romania

## Project Overview
This project applies machine learning to the task of **classifying hourly electricity demand in Romania** into **Low, Medium, and High tiers**. The dataset includes hourly measurements of electricity consumption and additional context features. 

The goal is to build a predictive model that supports **grid stability, renewable integration, and sustainability goals**.

---

## Problem Statement
**Predict whether an hourly electricity consumption measurement will fall into Low, Medium, or High demand tier using data available up to that time (hour, day, season, weather) so that grid operators can plan ahead, reduce reliance on fossil fuels, and optimize imports/exports.**

---

## Hypothesis
Electricity demand follows **predictable temporal and external patterns**:
- Peaks during certain **hours of the day** (e.g., mornings, evenings).  
- Higher on **weekdays** compared to weekends.  
- Seasonal variations: **winter heating** and **summer cooling** drive consumption.  

By capturing these patterns, the model can classify demand tiers accurately.

---

## Features
- **Hour of day** (0–23)  
- **Day of week** (Mon–Sun)  
- **Month / Season**  
- **Consumption (MWh)** – historical values used for labeling demand tiers  

⚠️ *Note:* Supply-side variables (production mix, imports/exports) are not used as predictors to avoid label leakage. They are outcomes of demand, not drivers.