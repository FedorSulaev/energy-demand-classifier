## EDA & Feature Engineering Review

### Top 5 Most Important Features
Based on mutual information, chi-square analysis, and correlation insights:
1. **hour_sin** – strongest daily cycle signal.  
2. **hour_cos** – complements sine for unique hourly positions.  
3. **dow_sin** – captures weekday vs weekend differences.  
4. **month_cos** – reflects seasonal demand variation.  
5. **dow_cos** – adds nuance to weekly cycle patterns.  

### Class Imbalance
- No significant imbalance observed.  
- Low/Medium/High demand tiers were created with quantile binning, ensuring ~1/3 samples per class (~18k each).  
- No oversampling/undersampling required at this stage.  

### Feature Set Size
- Final feature set: **6 engineered features** (sine/cosine encodings of hour, day, month).  
- Compact size supports a wide range of algorithms, from simple baselines (logistic regression) to tree ensembles and neural nets.  

### Constraints
- **Interpretability:** Important for stakeholder trust (grid operators, policymakers). Models like decision trees or interpretable feature importance scores are valuable.  
- **Prediction Speed:** Not a critical constraint; hourly predictions allow for flexible model complexity. However, lightweight models are still preferable for deployment efficiency.  