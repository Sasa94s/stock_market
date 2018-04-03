* # Initialization : -   
    * [Setup python 3.6](https://www.python.org/downloads/)
    * [Setup pip to cmd](https://packaging.python.org/tutorials/installing-packages/#install-pip-setuptools-and-wheel)
    * [Setup django library 2.0.2](https://www.djangoproject.com/download/)
    * [Setup allauth](http://django-allauth.readthedocs.io/en/latest/installation.html)
    * [Setup django-crispy-forms](http://django-crispy-forms.readthedocs.io/en/latest/install.html)
    * [Setup django-money](https://github.com/django-money/django-money)
    * [Setup psycopg2](https://pypi.python.org/pypi/psycopg2)  
    * [Setup Pillow](https://pypi.python.org/pypi/Pillow/2.2.1)  
---
* # Run local server :-
   * *To run the server provided by the django :* 
        1. Install pgadmin4 (PostgreSQL).
        2. Create new database on your local server named (stockmarket).
        3. Open setting.py located in (File-path\stock_market\src\websitefinal)
            -  write your password in databases part.  
        4. Open cmd.
        5. Make sure that you changed directory to the src folder.
        6. Use this command *"python manage.py makemigrations"*.
        7. Use this command *"python manage.py migrate"*.
        8. Use this command *"python manage.py runserver"*.
        9. Copy the ip address from cmd to your browser.
 ---    