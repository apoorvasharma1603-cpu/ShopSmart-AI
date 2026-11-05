1.	In the Step 3 results, the logistic regression has an accuracy of 0.804 but a recall of 0.303. Explain what each number means and why the accuracy was misleading.
- The logistic regression being 0.804 means the model correctly predicts 80.4% of the times the model predicts correctly, where as recall=0.303 means out of the all the customers who actually left 30% of customers were predicted to leave by the model.
2.	Explain what a false positive and a false negative are for this model, and say which one costs ShopSmart more.
- False Positive is when the model says the customer will stay but actually leave and False Negative is when the model says the customer will leave but they actually stay. For our ShopSmart AI  both the predictions will be a problem because: in False Positive, if the model predicts a cusotomer will stay and the customer leaves then we loose a customer; but in FAlse Negative if the model predicts that a customer will leave then we will provide the customer with unnecessary discounts assuming the customer will leave but the customer had no plan of leaving because of which we face a loss in money.

3.	Look at the threshold table. What happens to precision and recall as the threshold goes down, and why?
- From the Threshold table 
LOGISTIC REGRESSION: changing the threshold for 'will leave'
threshold | precision | recall | f1    | customers flagged
----------|-----------|--------|-------|------------------
      0.2 |     0.389 |  0.787 | 0.520 |              247
      0.3 |     0.488 |  0.648 | 0.556 |              162
      0.4 |     0.626 |  0.508 | 0.561 |               99
      0.5 |     0.740 |  0.303 | 0.430 |               50
      0.6 |     0.684 |  0.107 | 0.184 |               19
From the above table we can see that as the threshold decreases the precision decreases which tells us that out the customers flagged as leaving actually left, the precision decreases showing that the model is not correctly flagging the leaving customers and the recall increases which shows that out of the customers who actually left the model has predicted them to leave.
4.	What threshold did you choose in Step 5, and why? Use numbers from your results.
- I chose threshold= 0.6 since it provides a good balance between identifying the customers who are likly to leave to avoid incorrect predictions. With threshold 0.6 the test results were
FINAL TEST RESULTS for Logistic regression at threshold 0.6
accuracy  0.770
precision 0.684
recall    0.107
f1        0.184
roc_auc   0.783 
And out of 122 leavers 13 leavers were caught by the model and the model gave only 6 false alarms. 

5.	Why did we tune using cross-validation on the training data instead of using the test set?
- We use cross-validation to tune the training data and not the test data set to avoid data leakage and to ensure fair evaluation. Crsoss-Validation is used to tune the model and select the best parameters using different settings of the training data set, and if we use cross-validation to tune the test set then we would have used different setting of th test set to make a decision, and can no longer provide fair evaluations. 