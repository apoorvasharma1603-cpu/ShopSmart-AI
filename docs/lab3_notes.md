1.	Why do we split the data into a training set and a test set, and why does the scaler learn only from the training set?
- We split the data into training set and test set so that we can analyze how well the model will predicts outputs for data it has not seen or known. The tarining set data is used to train the model and the test set data is used to test the accuracy of the model when given unseen data. The scaler must learn only from the training dataset to prevent data leakage, if the model learns from test dataset then it will influence the training process of the model and make the model appear better than it actually is.

2.	What does stratify=y do? Look at the two churn rates printed in Step 3. What do they show?
- Stratify=y amkes sure that both the training dataset and the test dataset have the similar rate of customers who have churned and the similar rate of customers who have stayed. In step 3 the training churn rate is 2.45 and the test churn rate is 2.44 whuch shows that in both the datasets the number of churned customers are similar which helps maintain the fairness of the model and prevents either od the dataset from having either unusually high or low churn rates.

3.	Compare the random forest’s training and test accuracy at max_depth=6 with its scores at max_depth=None. What does the difference tell you? 
- The Random Forset scores at max_depth=6
train: 0.812 and test: 0.780 
=== RANDOM FOREST: how much each feature mattered ===
tenure_months             0.338
app_engagement            0.178
monthly_charges           0.164
support_tickets           0.104
late_payments             0.101
contract_type_Monthly     0.065
contract_type_Two-Year    0.030
contract_type_Annual      0.021
dtype: float64
The random forest scores at max_depth= None
train: 1.000  test: 0.766
=== RANDOM FOREST: how much each feature mattered ===
tenure_months             0.262
app_engagement            0.261
monthly_charges           0.257
support_tickets           0.095
late_payments             0.075
contract_type_Monthly     0.025
contract_type_Two-Year    0.013
contract_type_Annual      0.011
dtype: float64
As we can see from the above score the Random forset score for max_depth=None shows training accuracy rate as 1.000 which shows overfitting where the model has learned the dataset too well inculding all the random noise and unnecessary details and the test accuracy rate is 0.766 which is 76.6% which shows that the model cannot work well with unseen data.
4.	Both models beat the baseline of 0.756. Why is “80% accurate” less impressive than it sounds for this data?
- The baseline accuracy shows 0.756 because approximately 75.6% of the customers stayed and a simple model predicts that all the customers will stay 75.6% of times without predicting the percent of customers who may churn. The logistic regression of training dataset shows 0.787 and for the test dataset shows 0.804 which is does no0t show much margin difference from baseline of 0.756.Hence if a midel is 80% accurate does not mean the model is good at identifying the customers who may churn.

5.	Which two features did the logistic regression treat as the strongest signs a customer will leave, and which feature most strongly signals a customer will stay? Does this agree with the charts you drew in Lab 2?
- In the logistic regression the strongest sign that the customer will leave is seen in late_payments= 0.43 and support_tickets= 0.35 so the customers who make late_payments and raise more support tickets are usually the once will will churn. The strongest sign that a customer will not leave is seen in tenure_months= -1.03 and app_engagement= -0.29 so the cutomers with a specific number of months as thier tenure period are less likely to churn.
