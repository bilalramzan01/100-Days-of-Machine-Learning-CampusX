# Online Learning
Online Learning is a machine learning approach where the model learns incrementally, updating itself continuously as new data arrives — one instance or small mini-batch at a time — rather than being trained once on the entire dataset like in batch learning.

Core idea: Instead of waiting to collect a full dataset and retraining from scratch every time new data comes in, the model keeps learning "on the fly." Each new piece of data is used to slightly adjust and improve the model, and then it can typically be discarded (no need to store it), which makes online learning very memory-efficient.

- Model is being trained on production level or at server.
- Some part of data -> model trained -> test -> Server -> perdiction on new data and also learning on new data

**Example:**
- Chatbots - They are deployed on server, they are chatting on new data also learning from new data
- Product performance improved by using more and more of that product.
- Swift keyboard - Dynamically getting become personalized accoring to me
- Youtube feed become according to my interest

## When to use online learning

**WHERE concept of drift**
- when the nature of problem change over time, like stock exchange, ecommerce platform.
- Cost effective (Because working on small chunks)
- Faster solution. Mini patches trained fast and faster.

## How to impliment

Implementation is done using the dedicated libraries or algorithms 
- Scikit learn
- Rivers
- creme

## Learning Rate

we must give the model correct rate of learning, its not good that model should learn on every incoming point. in this way model forget old data. its also not good that model learn things after long.
so we model should learn after the correct time or correct rate.

## Out of core learning
Out-of-Core Learning is a machine learning technique used to train models on datasets that are too large to fit into a computer's RAM (memory) all at once. Instead of loading the entire dataset into memory, the data is processed in small chunks — one chunk at a time — with the model updating incrementally on each chunk.

**Core idea:** Normally, when you train a model, you load your entire dataset into memory (RAM) and then train on it. But what if your dataset is 500GB and your computer only has 16GB of RAM? You simply can't load it all at once. Out-of-core learning solves this by streaming the data from disk in manageable chunks, training the model incrementally on each chunk, then discarding that chunk before loading the next one.

- This is the concept of online learning but its implemented offline or in Batch learning.

## Disadvantages

**Tricky to use** ( Its unstable)
**Risky** (as open to change according to the new data so if the data become wrong then its goining to be giving wrong output)