# Challenges in Machine learning

1. **Data collection**
 - Fetch data using API
 - Web scrapping

2. **Insufficient Data/ Label data**
  - data having a=100 rows and b=10 lakh rows, so the B will perform more well because of more data

**Note** If we have huge ammount of data, algorithm is not matter the most

3. **Non Representative data**
 - when we make the model trained on baised data. example conduct survey on how's gonna win the world cup in pakistan, the most answer will be pakistan so the prediction will gone wrong.
 - we dont take the data from just one place
 - Its called sampling noise
 - so for good representation we have to ask equal number of peoples of all the nations

4. **Poor Quality of data**
 - Data have many outliers
 - have many missing values
 - have many duplicate values

5. **Irrelevant Features**
Means that we have many columns having no role in prediction
 - **Garbage IN is Garbage OUT*
## Examples:
Who is gonna win marathone
we have features: weight, height and location.
in this data we dont predict using the location feature but we can predict using weight and height of the person

6. **OverFitting**
 - Model is memorise the data, it only perform well on training data but perform poor on new data.
 **Example**:

7. **UnderFitting**:
 - Very simplest model, not good on training data nor on testing data

8. **Software integration**:
Software integration is difficult in ML mainly because ML systems behave very differently from traditional software. Unlike normal code, which is deterministic and always gives the same output for the same input, ML models are probabilistic and depend heavily on data — meaning failures can come from bad, biased, or drifted data rather than bugs in the code itself. Models are also usually built in one environment (like Python notebooks for experimentation) but need to be deployed in a completely different production environment with real-time speed and reliability requirements, which creates a gap between research code and production-ready code. On top of that, ML systems are harder to version, since you have to track not just the code but also the data, model weights, and configuration together. They also tend to fail silently, slowly degrading in performance instead of crashing outright, which makes issues harder to catch early. And because data changes over time, models often need continuous retraining and monitoring, unlike traditional software that's just patched occasionally. All of this adds up to a much more complex integration process, which is why the field of MLOps emerged specifically to manage these challenges.

9. **Offline learning and deployment:**
 - Model is not updating regularly
 - Deployment is costly

10. **Cost involved (Biggest challenges till now)**
  - Deploment is costly
  - when you make the model to come to live server, there is huge amount is required.
