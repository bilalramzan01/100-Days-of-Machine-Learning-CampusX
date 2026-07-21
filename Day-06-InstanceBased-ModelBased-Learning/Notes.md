# Types of machine learning on the base of how the machine learning model learns.

Machine learning model learn in two forms
1. Instance based learning - Memorizing ( Ratta system) 
2. Model based learning - Generalizing (Learning concepts and patterns)

## Instance Based learning
Instance-Based Learning (also called Memory-Based Learning or Lazy Learning) is a machine learning approach where the model doesn't build an explicit general rule or function during training. Instead, it simply memorizes the training data, and when a new prediction is needed, it compares the new instance to the stored training instances and makes a decision based on similarity.

**Core idea:** Unlike model-based learning (like linear regression, which learns a formula/equation from the data and then discards the raw data), instance-based learning keeps the entire training dataset in memory and defers all the actual "work" until prediction time. It doesn't try to generalize into a compact model — it just says "let me look at similar examples I've already seen and decide based on those.

**Students data:**
IQ | CGPA | Placement
70 | 3.83 | Yes

when new data comes it compare the data with its nearest 5 neighbors and give the prediction of the most same neighbors

**Example**
- KNN
- kernal functions

## Model Based learning
Model-Based Learning (also called Eager Learning) is a machine learning approach where the model analyzes the training data during training and builds a generalized mathematical model or function that captures the underlying patterns. Once training is complete, the raw training data is no longer needed — the model relies purely on what it has learned (its parameters) to make predictions.

Core idea: Instead of memorizing individual data points like instance-based learning does, model-based learning tries to find an underlying rule, equation, or structure that explains the relationship between inputs and outputs. This generalized model can then predict outcomes for completely new, unseen data — often very quickly, since it doesn't need to compare against the original dataset.

**Students data:**
IQ | CGPA | Placement
70 | 3.83 | Yes

when new data comes it decide on the base of pattern or mathematical equation it learns during the model training.
Example. it draw a line on graph that one side of grapph represent the students having placement and other side represent no placement so it will decide quickly new data fall in which side.

after that we even dont need the training that because model already learn the pattern.

**Example**
- Linear regression
- Logitic regression
- Decision trees

# Key Differences between instance and model based.
| Usual/Conventional Machine Learning | Instance Based Learning |
| :--- | :--- |
| Prepare the data for model training | Prepare the data for model training. No difference here |
| Train model from training data to estimate model parameters i.e. discover patterns | Do not train model. Pattern discovery postponed until scoring query received |
| Store the model in suitable form | There is no model to store |
| Generalize the rules in form of model, even before scoring instance is seen | No generalization before scoring. Only generalize for each scoring instance individually as and when seen |
| Predict for unseen scoring instance using model | Predict for unseen scoring instance using training data directly |
| Can throw away input/training data after model training | Input/training data must be kept since each query uses part or full set of training observations |
| Requires a known model form | May not have explicit model form |
| Storing models generally requires less storage | Storing training data generally requires more storage |

