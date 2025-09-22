## EDA Focus Questions

### Target Variable
- What is the distribution of demand classes (Low/Medium/High)?  
- Do classes follow expected temporal patterns (daily, weekly, seasonal)?  
- Are there abrupt anomalies or unstable class boundaries due to outliers?  

### Feature Distributions & Missingness
- Do time features (`hour`, `day_of_week`, `month`) cover all expected values?  
- Do production features show surprising distributions (e.g., negative, extreme, or zero outputs)?  
- Are there missing values? If yes, are they systematic (e.g., solar at night) or random?  

### Data Types
- Are all datetime fields parsed as `datetime64`?  
- Are numeric fields (consumption, production, encodings) correctly stored as `int` or `float`?  
- Are there any numeric fields mistakenly parsed as strings?  