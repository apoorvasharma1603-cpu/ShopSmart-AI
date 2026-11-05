# Churn Model Card

## What this model does
This model predicts how many customers are about to leave which helps use to persuade the customers to stay

## Data
The model is trained on synthetic data created for evaluating ShopSmart-AI
size =2000
features = tenure in months, app engagement, monthly charges, support tickets, late payments, contract type. 
label = churned to determine if the customer left or stayed.

## Model
Random forset was tuned using 5-fold cross-validation, testing the maximum depts at 2,3,4,6,8 and 12. The best random forset depth was at 4 with a mean ROC-AUC of 0.758.
Logistic Regression achieved a mean ROC-AUC of 0.777 at the max_depth of 4.
So comparing both the models and seeing that logistic regression has a higher ROC-AUC at the same max_depth LOGISTIC REGRESSION WAS SELECTED AS THE FINAL MODEL.

## How well it works (test set)
threshold=
| Metric | Score |
|---|---|
| Accuracy | |
| Precision | |
| Recall | |
| F1 | |
| ROC-AUC | |
| Baseline accuracy (always predict "stays") | 0.756 |

## Limits and risks
i. As the model is trained on synthetic data it may not work as well as it works on sythetic data with actual customer data.
ii. As the model tries to read patterns to predict customer behaviour and customer bhaviour may change over time so the madel will be needed to evaluated and updated regularly.
iii. The model's predictions may not always be correct.
iv. With a threshold of 0.4 the model missed 60 out of 122 customers who actually left with 37 false alarms.


## Intended use
The model should be used as a decision making model to help predict customers who maybe at risk at leaving.
