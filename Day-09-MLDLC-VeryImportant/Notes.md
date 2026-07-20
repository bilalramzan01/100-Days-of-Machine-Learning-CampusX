# Machine Learning Development Life Cycle
MLDLC (Machine Learning Development Life Cycle) is a structured, step-by-step process followed to build, deploy, and maintain a machine learning project — similar to the SDLC (Software Development Life Cycle) in traditional software engineering, but adapted for the data-driven nature of ML projects.

Core idea: Building an ML model isn't just about writing code and training a model — it's a full lifecycle involving understanding the business problem, collecting and preparing data, building and evaluating models, deploying them, and maintaining them over time.

1. **Problem/Framing the Business Problem**
Understand the actual business need — what problem are you solving, and can it genuinely be solved with ML? Define the objective clearly (e.g., "predict customer churn" rather than just "use ML").

2. **Data Gathering**
Collect relevant data from various sources — databases, APIs, web scraping, CSV/JSON files, third-party providers, etc. (This connects to Days 15–18 of the CampusX course you looked at earlier.)

3. **Data Preprocessing**
Clean and prepare the raw data — handling missing values, removing duplicates, fixing inconsistent formats, handling outliers, encoding categorical variables, etc.

4. **Exploratory Data Analysis (EDA)**
Analyze and visualize the data to understand patterns, relationships, and distributions before modeling — univariate/bivariate analysis, correlation checks, etc.
Balance the dataset

5. **Feature Engineering and Selection**
Create new meaningful features, transform existing ones, and select the most relevant features to improve model performance (scaling, encoding, PCA, etc.).
- Add or remove the columns
- Merge the multiple columns to one

6. **Model Training, Selection, and Evaluation**
Train multiple candidate models, tune hyperparameters, and evaluate them using appropriate metrics (accuracy, RMSE, F1-score, etc.) to select the best-performing one.
- Train the data on multiple algorithms

7. **Model Deployment**
Deploy the trained model into a production environment — as an API, embedded in an app, or integrated into a business system — so it can start making real predictions.

8. **Testing**
Test the deployed model in the real-world environment to ensure it performs as expected before or after full rollout (sometimes done via A/B testing or shadow deployment).

9. **Optimization and Monitoring**
Continuously monitor the model's performance in production, watch for data drift or performance degradation, and retrain/update the model as needed over time.