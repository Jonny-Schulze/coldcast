# coldcast

**Project Goal:** To build a system that predicts the daily risk of respiratory tract infections for individuals based on their location and time, leveraging various data sources.

**Key Components and Discussion Points:**

1. **Data Sources:** The project aims to integrate data from multiple sources, including:
    - Sentinel surveillance data on respiratory infections.
    - Hospitalization data related to respiratory illnesses.
    - Sewage data indicating community-level viral presence.
    - Mobility data reflecting population movement.
    - Meteorological data (weather conditions).
2. **Risk Prediction Model (Model 1):**
    - The primary goal is to build a model that accurately predicts the overall risk of respiratory infection for a given location and time.
    - The choice of model can prioritize accuracy, potentially including complex models like neural networks or ensemble methods.
3. **Risk Factor Explanation Model (Model 2):**
    - A separate, interpretable model will be used to identify and explain the key factors contributing to the risk predicted by Model 1 for a specific user query.
    - This model will analyze the current input parameters (e.g., current sentinel data, mobility, weather) to determine which factors are most influential in driving the predicted risk up or down at that moment.
    - Interpretable models like linear regression, GAMs, or Explainable Boosting Machines are suitable for this task.
4. **Output and User Interface:**
    - The system would ideally provide a user-friendly interface, potentially a dashboard or a Bluesky bot.
    - When a user queries the system with their location, it would return:
        - A predicted daily risk of respiratory infection for that location.
        - The top 2-3 most significant factors contributing to that risk at the time of the query, along with an indication of whether they are increasing or decreasing the risk.
***

**In essence, the project aims to create a location-aware system that not only predicts the risk of respiratory infection but also provides valuable context by explaining the key factors driving that risk at any given time.** The two-model approach is a key strategy to achieve both accurate predictions and transparent, understandable explanations for the end-user.

***
used data products:
