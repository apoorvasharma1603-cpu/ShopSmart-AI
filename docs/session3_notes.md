1.	Explain the train/test split using your own analogy (not the exam one in this guide).
- Consider a student is weak in Maths so the teacher takes a few problems and explains the concept and how to solve it to the student and after the teacher explains it to the student the teacher gives a new set of problems to solve with the same concept but different solving method to check if the student understood the concept or just learnt the first explained problems. Similarly a training data set is used to train the model and a test dataset is used to test the model for its accuracy.

2.	What is overfitting? Describe a situation, real or made up, where you would be fooled by it.
- Overfitting is when a model learns the training dataset too well, including the unnecessary details, random noise, etc; instead of learning the pattern which can help understand the any new data.
Lets consider the similar Maths example if the student is not able to solve the newly given problems by the teacher which has the same concept as the problems which the teacher exaplained then the student just practiced the probloems explained by the teacher and did not understand the concept which is overfitting.

3.	Explain the difference between logistic regression and a random forest to a friend who knows nothing about AI.
- Logistic Regression assigns weights to each characteristics of different customers, such as support tickets, late payments, customer's tenure etc. It will combine the weights of the characterisctics to analyze the probablity of which customer will leave. Random forset is a ml algorithm that combines the decision trees of all the characteristics of the customers and predict whether the customer will churn or stay.

4.	Why is 79% accuracy less impressive than it sounds for a dataset where 24.4% of customers leave?
- In the dataset 75.6% of customers stay and the rest leave. A simple model that predicts that every customer will stay would achieve a 75.6% accuracy and will not identify a single customer who leaves. If a model has 79% accuracy which is only 3.4% margin tahn the baseline, it may still fail to identify the many customers that may leave. Other methods such as precision and recall can help determine the efficiency of the model.

