Customer churn Findings 
1. churn_distribution:
    More than 1400 customers have retained their contracts and less than 600 customers have churned their contracts.

2. churn_by_contracts:
    Customers with a longer tenure of their contracts have less churn rate.
    - Customers with 2 year contracts have the least churn rate of 0.10-0.15.
    - Customers with yearly or annual contracts have a churn rate of 0.15-0.20.
    - Customers with monthly contracts have the highest churn rate of > 0.30.\

3. tenure_by_churn:
    - Retained customers:
        > Customers with the tenure period of 0 to 30 months have a high retain rate of with 60-160.
        > Customers with 70 months tenure peroid have the retain rate with about  140-160.
    - Churned customers:
        > Customers with a tenure period of 0-40 months have a churn rate of 0-120 customers.
        > Customers with a tenure period of 40-70 months have the least churn rate with less than 20 customers.

4. churn_by_tickets:
    The more number of support tickets raised by the customers the higher the churn rate. It may be caused because of the customer queores not beiong answered or solved which leads to them raising more tickets, or it may be a issue with the business which made the customer raise many support tickets which led to the customers leaving.

5. daily_orders:
    - The daily orders show the fluctuations throughout a week showing a weekly pattern.
    - The fluctuations in the weekly orders show a pattern repeated per month
    - The orders have continously increased from September 2025. 

1. What did the system message change about the reply, compared with your Lab 1 reply?
- The hello_llm output during the first lab was "hello! I'm here fully operational. How can i help you." and now the ouput reply is "Hello! I'm here and ready to help you with your shopping needs!".

2. Look at response.usage. How many tokens did your request use, and how many did the reply use?
- the Request tokens is 96, the reply tokens is 63 and the total tokens used is 159.
3. Run it three times with temperature=0, then three times with temperature=1. Which setting gave more varied replies?
- With temperature=0 the reponse was " Hello! I'm here and ready to help you with your shopping needs!" all the 3 times and with temperature=1 the responses are "Hello, I'm working and ready to help you today!", "Hello! I’m here and ready to help you with anything you need today!" and "Hello! I'm here and ready to help you shop!".

4. Make the user message much longer (paste in a paragraph) and run it again. What happened to the token count?
- After making the changes in system content by adding answer in paragraph and explain what you can do and keeping the temperature=0 the reponse is "Hello! I’m here and fully operational, ready to help you with anything you need for your shopping experience. Whether you’re looking for product recommendations, need help navigating our catalog, want to place or track an order, or have questions about returns, shipping, or payment options, I’ve got you covered. Just let me know what you’d like to do, and I’ll guide you through it with a smile!".
After changing the temperature=1 the reponse is "Hello! I’m here and ready to help you out with anything you need. As a cheerful assistant for this online store, I can answer questions about product availability, pricing, and shipping options; guide you through the checkout process; help you track orders or update shipping addresses; and provide information on returns, exchanges, and refunds. I’m also happy to offer styling tips, suggest complementary items, or help you find exactly the product that fits your needs. Whatever you need, just let me know and I’ll do my best to make your shopping experience smooth and enjoyable!.
The request and reply tokens increased compared to the one line response.
The reply tokens reduced  when the temperature changed from 0 to 1.

