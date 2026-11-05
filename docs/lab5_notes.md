1. Why can’t we split a time series at random? What did we do instead?
- We cannot spilt the time series randomly because it may mix the past and future data, which can cause data leakage. This means the model will learn the future data while predicting the past. In ShopSmart AI to avoid this issue we use a chronological split , the training data is from January 1 to December 17 2025 which is 351 days and the testing data is the next 14 dyas which is from December 18 to Decembr 31, 2025.

2. Describe the trend, the weekly pattern and the noise in ShopSmart’s orders, using numbers from Step 3.
- From the output of Step 3 of ShopSmart AI we can see that there is an increase in the number of orders per day in the trend near the starting was 99.0 orders per days where as the trend towards the end shows 135.6 orders per day.
We can see that: 
i. Friday has 14.7 orders more than the trend.
ii. Thursday has 12.3 orders more than the trend.
ii. Wednesday (+0.3) and Saturday (+7.2) have a slight increase in the number of orders compared to the trend.
iv. Sunday (-8.3) and Tuesday(-11.3) have a slight decrease in the number of orders compared to the trend.
v. Monday has a 14.9 orders less than the trend.

3. Compare the MAE of the three forecasts in Step 4. What does the comparison tell you about the weekly pattern, and about the baseline?
- This is the MAE of the three foecasts:
                                    MAE   
baseline (same day last week)      6.64   
Holt-Winters, no weekly pattern    8.92  
Holt-Winters, with weekly pattern  3.13 
from the above data we can see that the MAE of the Holt-Winters with weekly pattern has an MAE of 3.13 which shows that it has the best performance which shows that including the weekly performance improves the forecasting accuracy. baseline has an MAE of 6.64 which is still less than the Holt-Winters, no weekly pattern which shows us that a simple method can aslo be used to provide useful predictions.

4. Explain in plain words what an MAE of about 3 orders a day means. If you were advising the operations team, how many extra orders’ worth of riders or stock would you suggest they keep as a buffer, and why?
- An MAE of 3.13 (considering the Holt-Winters, with weekly pattern forecast) per day shows that the forecast is off by only approximately 3 orders per day than the actudal number of orders. I would suggest a buffer of about 4-6 extra orders worth of riders ad stock capoacity per day. This will provide us protection against forecast errors, while making sure that excessive unused resources are not wasted. This buffer can be altered based on the actual demand and business requirements.

5. Why is it important to compare a forecast with a simple baseline before trusting it?
- Comparing a forecast with a baseline helps us understand whether the advanced model actually performs better than a simple prediction method. If this comparison is not done then we may asssume that the advanced model's forecast is correct even if a basic method performs better. In this we can see that Holt-winters forecast has an MAE of 3.13 compared to the baseline MAE of 6.64 proiving that Holts-Winters provides a better forecast for the ShopSmart AI.

