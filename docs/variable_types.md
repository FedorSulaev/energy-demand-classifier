# Variable Types – Electricity Demand Dataset

| Feature Name     | Variable Type      | Description |
|------------------|--------------------|-------------|
| `datetime`       | Raw (time)         | Hourly timestamp |
| `hour`           | Engineered         | Hour of day (0–23) |
| `day_of_week`    | Engineered         | Day of week (Mon–Sun) |
| `month`          | Engineered         | Month (1–12) |
| `season`         | Engineered         | Season (Winter, Spring, Summer, Autumn) |
| **`demand_class`** | Target (Low/Med/High) | Demand tier label, based on tertiles of `consumption` |