# Machine Learning Types
## Batch Machine Learning | Offline Vs Online Learning

**Note** In these types we have learn how the ML models Train especially at production.

## What is production Environment
Its the server where the code is run. Its called production environment.

## Batch Machine Learning | Offline
Batch Machine Learning (Offline Learning) is an approach where the model is trained on the entire dataset all at once, rather than learning continuously from new data as it arrives.

**Why Offline** Because we are using whole data so having a big data to train on server will be costly and time taking process. So generally trained the model on offline on local environemnt then trained model will be deploye on server or production environment.

Data -> Model -> Trained -> Test -> Deploy on server

**Limitations:** It's not well suited to fast-changing environments (like stock prices or fraud detection) since the model only reflects the data available up to its last training cycle. Retraining on very large datasets can also be slow and computationally expensive.
- If Big data cant be trained in one time
- Hardware limitation
- Availability ( As batch learning update data after a period so the availablity of the data is late or not updated on time )

## Example
A spam filter that's retrained weekly on a fresh batch of labeled emails

