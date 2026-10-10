"""


What is machine learning?
-------------------------

Machine learning is a field of computer science that uses statistical techniques to give 
computer systems the ability to "learn" with data, without being explicitly programmed.



Traditional Programming


                    ------------------------------
Data ------------>  |                            |
                    |       Computer             |
Program --------->  |                            |---------> output
                    |                            |
                    ------------------------------



Machine Learning


                    ------------------------------
Data ------------>  |                            |
                    |       Computer             |
Output ---------->  |                            |---------> Program
                    |                            |
                    ------------------------------

                    

Use case of machhine learning
-----------------------------

1. Email Spam Classifier

2. Data Mining







AI  V/s  ML  V/s  DL
=====================




 

type of machine learning algorithum 
===================================

type of machine learning algorithum based on amount of supervision required to tain machine learning algorithum.

1. Supervised Learning
2. Unsupervised Learning
3. Rainforcement Learning


1. Supervised Learning
-----------------------

Ideal for task with labeled data where the desired output is known.

input + output

eg: gpt give perfect example


Supervised Learning is devided into two part

(i) Regression
(ii) Classification

(i) Regression : If output column in supervised learning is numeric called regression.

(ii) Classification : If output column in supervised learning is categorical called classification.


gpt give example table iq, cgpa, placement 




2. Unsupervised Learing
------------------------

Suitable for identifying patterns in unlabeled data without explicit guidance.

input 

eg: we have only two column iq, cgpa 
    gpt give table


Unsupervised Learning is devided into foure type

(i). Clustering
(ii). Dimentionality Reduction
(iii). Anomoly Detection
(iv). Assosiation Rule learning


gpt give example of each type 




3. Semi Supervised Learning
---------------------------






4. Rainforcement Learning
-------------------------

Best for training agents to make decisions through interaction with an enviornment.


here we didn't give data 








Type of machine learning based on training on production


1. Batch Machine Learning
2. Online Machine Learning


1. Batch/Offline Machine Learning

   In Batch machine learning we train model with entire data (New + Historical).

   gpt give flow diagram

   When to use?

   Problem : When new data generate(gpt give correct way)

   Disadvantage 
       (i) Lots of Data
       (ii) Hardware Limitation
       (iii) Availability

       
2. Online Machine Learning

   Online machine learning train model encrementaly.

   gpt give flow diagram

   When to use?
       (i). Where there is a concept drift
       (ii). Cost Effective
       (iii). Faster Solution


   Disadvantage
       (i). Tricky to use
       (ii). Risky



Gpt give diff b/w Batch Vs Online learning



"""









"""



============================================================
                    MACHINE LEARNING
============================================================


# 1. What is Machine Learning?
# ============================================================

Machine Learning (ML) is a branch of Artificial Intelligence
that enables computers to learn patterns from data and make
predictions or decisions without being explicitly programmed
for every specific task.


Interview Answer:
-----------------

"Machine Learning is a subset of Artificial Intelligence that
allows machines to learn patterns from data and make predictions
or decisions without being explicitly programmed for every
possible situation."


# 2. Traditional Programming vs Machine Learning
# ============================================================

Traditional Programming:

    Data + Program -------------> Output


Machine Learning:

    Data + Expected Output -------> Learning Algorithm
                                         |
                                         v
                                       Model
                                         |
                                         v
                                  Prediction on New Data


Example:

Traditional Programming:

    Data + Rules -------------> Output


Machine Learning:

    Data + Output ------------> Model


The main difference is:

    Traditional Programming:
        Humans explicitly define the rules.

    Machine Learning:
        The model learns patterns/rules from data.


# 3. Applications / Use Cases of Machine Learning
# ============================================================

1. Email Spam Classification
   - Classify emails as Spam or Not Spam.

2. Data Mining
   - Discover useful patterns from large datasets.

3. Recommendation Systems
   - Recommend movies, products, or songs.

4. Fraud Detection
   - Detect potentially fraudulent transactions.

5. Customer Churn Prediction
   - Predict whether a customer may leave a service.

6. House Price Prediction
   - Predict house prices using different features.

7. Image Recognition
   - Identify objects or patterns in images.


# 4. AI vs ML vs DL
# ============================================================

                    Artificial Intelligence
                             |
                             |
                    Machine Learning
                             |
                             |
                      Deep Learning

                      
 -----------------------------------
 |     Artificial Intelligence     |
 |                                 |
 |   ---------------------------   |                               
 |   |   Machine learning      |   |
 |   |                         |   |
 |   |   ------------------    |   |
 |   |   |  Deep learning |    |   |
 |   |   ------------------    |   |
 |   |                         |   |
 |   ---------------------------   |
 |                                 |
 -----------------------------------





Artificial Intelligence (AI):
--------------------------------

AI is the broadest concept.

AI focuses on creating machines that can perform tasks
that normally require human intelligence.

Examples:
    - Reasoning
    - Decision making
    - Problem solving
    - Natural Language Processing
    - Computer Vision


Machine Learning (ML):
----------------------

ML is a subset of AI.

It enables machines to learn patterns from data and make
predictions or decisions.

Examples:
    - Spam detection
    - Fraud detection
    - Recommendation systems


Deep Learning (DL):
-------------------

DL is a subset of Machine Learning.

It mainly uses deep neural networks to learn complex
patterns from large amounts of data.

Examples:
    - Image recognition
    - Speech recognition
    - Large Language Models


Easy Interview Answer:
----------------------

"AI is the broader field of creating intelligent machines.
Machine Learning is a subset of AI where machines learn
from data. Deep Learning is a subset of Machine Learning
that uses deep neural networks to learn complex patterns."






# 5. Types of Machine Learning
# ============================================================

Machine Learning can be classified based on the type and
amount of supervision provided during training.

Main types:

1. Supervised Learning
2. Unsupervised Learning
3. Semi-Supervised Learning
4. Reinforcement Learning


# 1. Supervised Learning
# -----------------------

Supervised Learning is a type of Machine Learning where
the model is trained using labeled data.

Labeled data contains:

    Input / Features
            +
    Known Output / Target


Basic Structure:

    Input + Known Output
            |
            v
    Learning Algorithm
            |
            v
       Trained Model
            |
            v
       New Input
            |
            v
       Prediction


Example:
--------

Suppose we have student data:

+-----+------+-----------+
| IQ  | CGPA | Placement |
+-----+------+-----------+
| 90  | 6.5  | No        |
| 105 | 7.2  | Yes       |
| 110 | 7.5  | Yes       |
| 85  | 6.0  | No        |
| 120 | 8.1  | Yes       |
+-----+------+-----------+

Features:
    IQ
    CGPA

Target:
    Placement


The model learns the relationship between:

    IQ + CGPA ------------> Placement


Supervised Learning is mainly divided into:

    1. Regression
    2. Classification


# 1. Regression
# .............

Regression is used when the target variable is a continuous
numerical value.


Example:

+-----+------+----------+
| IQ  | CGPA | Salary   |
+-----+------+----------+
| 90  | 6.5  | 3.2 LPA  |
| 105 | 7.2  | 4.5 LPA  |
| 110 | 7.5  | 5.2 LPA  |
| 120 | 8.1  | 7.0 LPA  |
+-----+------+----------+

Features:
    IQ
    CGPA

Target:
    Salary


Salary is numerical and can have many possible values.

Therefore:

    Regression


Common Regression Examples:

    - House price prediction
    - Salary prediction
    - Sales prediction
    - Temperature prediction
    - Revenue prediction


Interview Answer:
-----------------

"If the target variable is a continuous numerical value,
the problem is generally considered a Regression problem."


# 2. Classification
# ..................

Classification is used when the target variable belongs
to predefined categories or classes.


Example:

+-----+------+-----------+
| IQ  | CGPA | Placement |
+-----+------+-----------+
| 90  | 6.5  | No        |
| 105 | 7.2  | Yes       |
| 110 | 7.5  | Yes       |
| 85  | 6.0  | No        |
| 120 | 8.1  | Yes       |
+-----+------+-----------+

Features:
    IQ
    CGPA

Target:
    Placement

Possible classes:

    Yes
    No


Therefore:

    Classification


Common Classification Examples:

    - Spam / Not Spam
    - Fraud / Not Fraud
    - Pass / Fail
    - Churn / No Churn
    - Disease / No Disease


Interview Answer:
-----------------

"If the target variable represents categories or classes,
the problem is generally considered a Classification problem."


# 3. Regression vs Classification
# --------------------------------

Regression:
    Target = Continuous numerical value

Classification:
    Target = Category / Class


Examples:

    House Price       -> Regression
    Salary            -> Regression
    Sales             -> Regression

    Spam / Not Spam   -> Classification
    Pass / Fail       -> Classification
    Fraud / Not Fraud -> Classification


Interview Question:
-------------------

Q. How do you identify whether a problem is Regression
   or Classification?

Answer:

"I look at the target variable. If the target is a continuous
numerical value, it is a Regression problem. If the target
represents categories or classes, it is a Classification problem."


# 2. Unsupervised Learning
# -------------------------

Unsupervised Learning is a type of Machine Learning where
the model is trained using unlabeled data.

Here:

    Input Data
        |
        X
    No Target / Output


Basic Structure:

    Unlabeled Data
          |
          v
    Learning Algorithm
          |
          v
    Patterns / Groups / Structure


Example:

Suppose we have only:

+-----+------+
| IQ  | CGPA |
+-----+------+
| 90  | 6.5  |
| 92  | 6.7  |
| 105 | 7.2  |
| 108 | 7.4  |
| 120 | 8.1  |
| 125 | 8.4  |
+-----+------+

There is no Placement column.

The algorithm tries to discover hidden patterns or groups.


Unsupervised Learning is mainly divided into:

    1. Clustering
    2. Dimensionality Reduction
    3. Anomaly Detection
    4. Association Rule Learning


# 1. Clustering
# ...............

Clustering groups similar data points together without
predefined labels.


Example:

Customer Data:

    Age + Spending Score
             |
             v
         Clustering
             |
             v
    +-------------------+
    | Customer Groups   |
    +-------------------+
             |
             +--> Low Spending
             +--> Medium Spending
             +--> High Spending


Real-World Example:

Customer Segmentation


Common Algorithm:

    K-Means Clustering


Applications:

    - Customer segmentation
    - Market segmentation
    - Document grouping
    - Image segmentation


# 2. Dimensionality Reduction
# ............................

Dimensionality Reduction reduces the number of features
while trying to preserve important information.


Example:

Original Dataset:

    100 Features
         |
         v
    Dimensionality Reduction
         |
         v
    10 Important Features


Why use Dimensionality Reduction?

    - Reduce computational cost
    - Remove redundant information
    - Reduce noise
    - Improve visualization
    - Improve model efficiency


Common Techniques:

    - PCA
    - t-SNE
    - UMAP


# 3. Anomaly Detection
# .....................

Anomaly Detection identifies unusual or abnormal data points
that significantly differ from normal observations.


Example:

Normal Transactions:

    Rs. 500
    Rs. 800
    Rs. 1,200

Possible Anomaly:

    Rs. 5,00,000


The system can flag the unusual transaction for investigation.


Applications:

    - Fraud detection
    - Network intrusion detection
    - Equipment failure detection
    - Unusual customer behavior


# 4. Association Rule Learning
#..............................

Association Rule Learning identifies relationships between
items in a dataset.


Example:

In a supermarket:

    Bread + Butter
          |
          v
      Frequently
          |
          v
         Milk


Possible Rule:

    Bread + Butter ---> Milk


Applications:

    - Market Basket Analysis
    - Product Recommendation
    - Cross-selling


Common Algorithm:

    Apriori


# 3. Semi-Supervised Learning
# ----------------------------

Semi-Supervised Learning uses a combination of:

    Small amount of labeled data
                    +
    Large amount of unlabeled data


Example:

    1,000 labeled images
             +
    100,000 unlabeled images
             |
             v
    Semi-Supervised Learning
             |
             v
           Model


Why use it?

Labeling data can be:

    - Expensive
    - Time-consuming
    - Difficult


Applications:

    - Image classification
    - Speech recognition
    - Web content classification


# 4. Reinforcement Learning
# --------------------------

Reinforcement Learning (RL) is a type of Machine Learning
where an agent learns by interacting with an environment.

The agent:

    Takes Action
         |
         v
    Environment
         |
         v
      Reward
         |
         v
    Learns Better Action


The objective is to maximize the total long-term reward.


Basic Structure:

              Environment
                   |
                   | State
                   v
                 Agent
                   |
                   | Action
                   v
              Environment
                   |
                   | Reward
                   v
                 Agent


Example:

Game Playing AI:

    Agent
      |
      | Makes Move
      v
    Game Environment
      |
      +--> Wins  -> Positive Reward
      |
      +--> Loses -> Negative Reward
      |
      v
    Agent learns better strategy


Important Terms:

    Agent:
        The learner or decision maker.

    Environment:
        The world in which the agent operates.

    State:
        The current situation of the environment.

    Action:
        The decision taken by the agent.

    Reward:
        Feedback received after taking an action.

    Policy:
        Strategy used by the agent to select actions.


Applications:

    - Robotics
    - Game playing
    - Autonomous systems
    - Recommendation systems
    - Resource optimization

    






#  Batch Machine Learning
# ========================

Batch Machine Learning is a training approach where the
model is trained periodically using a large batch of data.

It is also commonly called:

    Offline Learning


Flow:

    Historical Data
          |
          v
    Data Preparation
          |
          v
      Train Model
          |
          v
    Trained Model
          |
          v
       Deployment
          |
          v
      Prediction


Example:

Suppose an e-commerce company has:

    2023 Data
    2024 Data
    2025 Data

All available historical data can be used to train a model:

    Historical Data
          |
          v
      Train Model
          |
          v
    Trained Model
          |
          v
      Production


When new data arrives:

    New Data
       |
       X
    Model does NOT automatically learn


The model must be retrained periodically.


When to Use Batch Learning?

    - Data changes relatively slowly
    - Periodic retraining is sufficient
    - Continuous learning is not required
    - Training data is manageable


Limitations:

    1. Requires computational resources during training
    2. Large training datasets may require significant resources
    3. New data is not immediately incorporated
    4. Model may become outdated if data distribution changes


    
#  Online Machine Learning
# ==========================

Online Machine Learning trains the model incrementally.

Instead of retraining on the complete dataset,
the model learns from new data continuously or
in small batches.


Flow:

    Historical Data
          |
          v
    Initial Training
          |
          v
         Model
          |
          v
    New Data Arrives
          |
          v
    Incremental Training
          |
          v
    Updated Model
          |
          v
    New Predictions


Example:

A fraud detection system receives transactions continuously:

    Transaction 1 ---> Model Update
    Transaction 2 ---> Model Update
    Transaction 3 ---> Model Update
    Transaction 4 ---> Model Update
              ...
              |
              v
       Updated Model


The model learns incrementally instead of being retrained
from scratch on the complete dataset every time.


#  When to Use Online Learning?
# ------------------------------

Online Learning is useful when:

    1. Data arrives continuously
    2. Data volume is very large
    3. Frequent model updates are required
    4. Real-time adaptation is important
    5. Data distribution changes over time
    6. Concept drift is expected
    7. Full retraining is computationally expensive


# 20. Concept Drift
# ============================================================

Concept Drift occurs when the underlying relationship between
input data and the target changes over time.


Example:

A fraud detection model learns:

    Fraud Pattern in 2025
             |
             v
        Trained Model


Fraudsters change their behavior in 2026.

Now:

    Old Fraud Pattern != New Fraud Pattern


Therefore, model performance may decrease.


Online learning can help the model adapt to new patterns.


#  Advantages of Online Learning
# -------------------------------

1. Incremental training
2. Handles continuously arriving data
3. Can adapt to changing patterns
4. Lower memory requirement per update
5. Avoids complete retraining for every new data point


# Disadvantages of Online Learning
# ---------------------------------

1. More difficult to design and monitor
2. Sensitive to noisy data
3. Poor-quality incoming data can affect the model
4. Incorrect updates can degrade model performance
5. Requires monitoring and rollback strategies


#  Batch Learning vs Online Learning
# --------------------------------------

+----------------------+--------------------------+--------------------------+
| Feature              | Batch Learning           | Online Learning          |
+----------------------+--------------------------+--------------------------+
| Training             | Periodically             | Incrementally            |
| New Data             | Used during retraining   | Used continuously        |
| Model Updates        | Less frequent            | More frequent            |
| Data Processing      | Large batches            | Small chunks/instances   |
| Memory               | Usually higher           | Usually lower per update |
| Adaptation           | Slower                   | Faster                   |
| Concept Drift        | Less suitable            | More suitable            |
| Implementation       | Relatively simpler       | More complex             |
| Noise Sensitivity    | Lower per update         | Higher                   |
+----------------------+--------------------------+--------------------------+


Interview Answer:
-----------------

"Batch learning trains a model periodically using a large
dataset, whereas online learning updates the model
incrementally as new data arrives.

Batch learning is suitable when the data does not change
frequently and periodic retraining is sufficient.

Online learning is useful when data arrives continuously
or when the model needs to adapt quickly to changing
patterns, such as concept drift."



# 25. Most Important Interview Questions
# ============================================================

1. What is Machine Learning?
2. How is Machine Learning different from traditional
   programming?
3. What is the difference between AI, ML, and DL?
4. What are the different types of Machine Learning?
5. What is Supervised Learning?
6. What is Unsupervised Learning?
7. What is the difference between Supervised and
   Unsupervised Learning?
8. What is Regression?
9. What is Classification?
10. What is the difference between Regression
    and Classification?
11. Give a real-world example of Regression.
12. Give a real-world example of Classification.
13. What is Clustering?
14. What is Dimensionality Reduction?
15. What is Anomaly Detection?
16. What is Association Rule Learning?
17. What is Semi-Supervised Learning?
18. What is Reinforcement Learning?
19. What are Agent, Environment, State, Action, and Reward?
20. What is Batch Learning?
21. What is Online Learning?
22. What is the difference between Batch and Online Learning?
23. What is Concept Drift?
24. When would you choose Online Learning over Batch Learning?
25. Why can Online Learning be risky?
26. Why is labeled data important in Supervised Learning?
27. Give real-world examples of Unsupervised Learning.
28. What is the difference between Offline and Online Learning?




# ONE-MINUTE REVISION
# --------------------

Machine Learning:
    Machines learn patterns from data.

Supervised:
    Labeled data -> Input + Output

Unsupervised:
    Unlabeled data -> Find patterns

Semi-Supervised:
    Small labeled + Large unlabeled data

Reinforcement:
    Agent learns using actions and rewards

Regression:
    Predict continuous numerical values

Classification:
    Predict categories/classes

Clustering:
    Group similar data

Dimensionality Reduction:
    Reduce features

Anomaly Detection:
    Detect unusual observations

Association Rules:
    Find relationships between items

Batch Learning:
    Periodic training on large datasets

Online Learning:
    Incremental training on new data

Concept Drift:
    Data relationship changes over time
    
============================================================



"""