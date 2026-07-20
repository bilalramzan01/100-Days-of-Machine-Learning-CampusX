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
Data will be plot on 2 cordicate graph
clustring algo detect that which data will go to which class
example:
having students data, it will categories data:
1. having good cgpa
2. having good IQ

## Dimensionaly reduction
When we have a lot of input columns like 1000+ input columns. In this scenrio algo worl slowly and after some point model stop improving after adding more columns. So dimensionally reduction remove that columns by which model is not improving. It merge columns having relation.
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