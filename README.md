# Abstract
Banks and financial institutions together from the industry that spends the most technology on an annual basis.  Financial industry is also really important to the technology sector:
>“Banks will spend 4.2% more on technology in 2014 than they did in 2013, according to IDC analysts. Overall IT spend in financial services globally will exceed $430 billion in 2014 and surpass $500 billion by 2020, the analysts say.” *– Crosman 2013*

**Financial and data analytics** refers to the displine of applying software and technology in combination with (possibly advanced) algorithms and methods to gather, process, and analyze data in order to gain insights, to make decisions, or to fulfill regulatory requirements.
Decisions often have to be made in milliseconds or even faster, making it necessary to build the respective analytics capabilities and to analyze large amount of data in real time.
In this paper, We've built a **website** of Stock Market Simulation based on *back-end SQL database* (which is more powerful) of historical stock prices by applying *Portfolio Risk Analysis, Technical Analysis* with various trading strategies for making decisions such as: *Moving Crossover Strategy, Bollinger Bands Indicator.* Moreover, We've used two approaches of various machine learning models for stock prediction:
- **First Approach:** Using *KNN, Linear Regression, Logistic Regression, SVM (Support Vector Machine), LSTM Neural Network, Backpropagation Neural Network.*
- **Second Approach:** Using *Sentimental Analysis* on Twitter news dataset for predicting stock price indicators.

---
# How to run:
## Initialization : -   
   * [Setup python 3.6](https://www.python.org/downloads/)
   * [Setup pip to cmd](https://packaging.python.org/tutorials/installing-packages/#install-pip-setuptools-and-wheel)
   * [Setup django library 2.0.2](https://www.djangoproject.com/download/)
   * [Setup allauth](http://django-allauth.readthedocs.io/en/latest/installation.html)
   * [Setup django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/install.html)
   * [Setup django-money](https://github.com/django-money/django-money)
   * [Setup psycopg2](https://pypi.python.org/pypi/psycopg2)  
   * [Setup Pillow](https://pypi.python.org/pypi/Pillow/2.2.1)  
---
## Run local server :-
   * *To run the server provided by the django :* 
    1. Install [pgadmin4](https://www.pgadmin.org/download/) (PostgreSQL).
    2. Create new database on your local server named (stockmarket).
    3. Open setting.py located in `(File-path\stock_market\src\websitefinal)`
        -  write your password in databases field.  
    4. Open cmd.
    5. Make sure that you changed directory to the src folder.
    6. Use this command `python manage.py makemigrations`.
    7. Use this command `python manage.py migrate`.
    8. Use this command `python manage.py runserver`.
    9. Copy the ip address from cmd to your browser.
 ---    
