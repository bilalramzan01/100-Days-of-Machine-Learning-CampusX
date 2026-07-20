# Types of ML

1. Supervised learning
2. Unsupervised learning
3. Semisupervised learning
4. Reinforcement learning

## Supervised learning
 Learning using the label data, means that when we have data with the correct output. Training model using this data is fall in supervised learning.

 ## Types of Supervised learning

 1. Regression
 2. Classification

 First of all we have to learn about data

 ## Data
 Data have two types

 # 1. Numerical data
 - age
 - CGPA

 # 2.Categorical data
 - Gender
 - Nation

 # Regression
 Regression is a supervised machine learning technique used to predict a continuous numerical value based on one or more input variables (features), by modeling the relationship between them.
 ## Example:
 - Salary prediction using education, experience and skills.
 - House price prediction
 - Weather forcasting
 - stock market analysis


 # Classfication
 Classification is a supervised machine learning technique used to predict a categorical (discrete) label or class for a given input, rather than a continuous number.
## Example
- Email is spam or not
- predict chances of placement using IQ and CGPA in yes/not class

# Unsupervised machine learning
 Oppsite of supervised. It only have input data and the model learn the patterns by itself.
 so if we dont doing prediction here what we will do.

 1. Clustring
 2. Dimensionaly reduction
 3. Anomoly reduction
 4. Association rule learning

##  Clustring
Clustering is an unsupervised machine learning technique used to group a set of data points into clusters, such that data points within the same cluster are more similar to each other than to points in other clusters — without ever being told in advance what the groups should be.
**Core idea:** There's no "correct answer" given to the algorithm. It looks at the data purely **based on similarity** (usually measured by distance, like Euclidean distance) and figures out the natural groupings on its own.
example:
having students data, it will categories data:
1. having good cgpa
2. having good IQ

## Dimensionaly reduction
Dimensionality Reduction is an unsupervised machine learning technique used to reduce the number of input features (dimensions) in a dataset, while trying to preserve as much of the important information/structure as possible.

**Core idea:** Real-world datasets often have a huge number of features — sometimes hundreds or thousands (think: an image dataset where every pixel is a feature). Many of these features are redundant, correlated, or add noise rather than useful information. Dimensionality reduction compresses this high-dimensional data into a smaller number of dimensions, making it easier and faster to work with — without losing the essential patterns.

- using multiple columns make the one columns
- Higher dimension to lower dimension to show data on graph

## Anomoly reduction
Anomaly (also called an outlier) is a data point, event, or observation that significantly deviates from the normal pattern or expected behavior in a dataset.
Most data follows a general pattern or distribution. An anomaly is something that doesn't fit that pattern — it's unusual, rare, or unexpected compared to the rest of the data.

Anomaly Detection is the machine learning task of identifying these unusual data points automatically. It's widely used in:

Fraud detection (banking, credit cards)
Network security (detecting intrusions/attacks)
Manufacturing (detecting faulty products)
Healthcare (detecting abnormal patient vitals)
IoT/sensor monitoring (detecting equipment failure)

## Association rule learning
Association Rule Learning (also called Association Rule Mining) is an unsupervised machine learning technique used to discover interesting relationships, patterns, or associations between variables in large datasets.
It finds rules that describe how the presence of one item or event tends to be associated with the presence of another — answering questions like "if a customer buys X, how likely are they to also buy Y?

# Semi-Supervised learning
Semi-Supervised Learning is a machine learning approach that sits between supervised learning and unsupervised learning — it uses a combination of a small amount of labeled data and a large amount of unlabeled data to train a model.
**Core idea:** Labeling data is often expensive, time-consuming, or requires expert knowledge (think: doctors labeling medical scans, or humans manually tagging millions of images). Semi-supervised learning solves this by using the small labeled portion to guide the model, while leveraging the much larger pool of unlabeled data to learn the underlying structure of the data.

**Example**
Google photos classfication, we just tell on one picture that he is this person, google photos classifie all other pic of that person in the telling class

# Reinforcement Learning (Agent)
Reinforcement Learning (RL) is a machine learning approach where an agent learns to make decisions by interacting with an environment, receiving rewards or penalties based on its actions, and improving its behavior over time to maximize cumulative reward.
- Self driving car