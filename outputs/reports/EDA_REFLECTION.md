## EDA Reflection

The most surprising pattern surfaced in the **consumption anomaly timeline plot**, which revealed a structural shift: earlier anomalies clustered around extreme winter peaks, while recent anomalies were mostly sustained low dips. This suggested that the dataset is **non-stationary**, with demand patterns evolving over time.  

This insight will influence my feature engineering by encouraging me to **incorporate temporal context more explicitly** — for example, adding lag features and trend indicators that capture structural shifts, rather than relying only on static cyclical encodings of time. It also highlighted the importance of validating tier thresholds across different years.  

The external resource that supported my learning the most was **scikit-learn’s feature selection and inspection documentation** (particularly `mutual_info_classif` and permutation importance). It provided both the conceptual grounding and practical tools to quantify feature relevance beyond simple correlations, which was crucial for interpreting the predictive value of time features in this dataset.