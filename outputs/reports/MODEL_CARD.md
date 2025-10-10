# Model Card – Electricity Demand Classification Model

## Purpose  
**What problem does this solve?**  
This model predicts whether overall electricity demand will be **Low**, **Medium**, or **High** at a given hour.  
It helps energy operators plan generation and distribution efficiently, reduce waste, and maintain a stable power supply.  
By anticipating demand shifts—especially during weekends and holidays—it supports sustainability and cost control.

---

## Performance  
**How accurate is it?**  
- **Overall accuracy:** ~74%  
- **Macro F1 score:** ~0.73 (balanced across all classes)  
- Performs best for **Medium demand** (F1 ≈ 0.81), moderate for **Low demand**, and slightly weaker for **High demand** (F1 ≈ 0.61).  
- Consistent results across cross-validation folds; no overfitting detected.

---

## Training Data  
**What data was used?**  
Historical electricity **consumption and production data** from the national grid (hourly records).  
Features include:
- Time indicators (hour, day of week, month)
- Seasonality encodings (sin/cos transforms)
- Public holiday flags (is_holiday, is_holiday_window)  
No personal or customer-level information was used.

---

## Limitations  
**What are its weaknesses?**  
- Struggles to distinguish **High demand** periods accurately when consumption spikes unexpectedly (e.g., extreme weather).  
- Does not account for external factors such as **temperature, major events, or sudden outages**.  
- Designed for short-term forecasting; long-range predictions are unreliable.  
- Should not be used for financial or policy decisions without expert validation.

---

## Bias Testing  
**Was it tested for fairness?**  
- Yes, fairness was assessed across **time segments and holiday vs non-holiday days**.  
- No systematic bias detected—performance remained stable across all time categories.  
- Because data is aggregated (no personal or regional attributes), risk of discrimination is minimal.

---

## Human Oversight  
**When do humans review decisions?**  
- Human operators **always review forecasts before operational actions** (e.g., grid load balancing or generation scheduling).  
- Analysts should investigate any **unexpected demand classifications**, especially High demand events.  
- Model outputs serve as **decision support**, not automation.  
- Continuous monitoring ensures accuracy and detects drift over time.

---

### Summary
This model supports smarter, greener energy management by predicting demand tiers in real time.  
It is accurate, explainable, and safe for operational use when paired with **human judgment and monitoring**.