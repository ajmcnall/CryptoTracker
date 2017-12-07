# CryptoTracker
Tracks cryptocurrencies via gdax api
https://docs.gdax.com

# Setup
Utilizes pipenv, "pip install pipenv"
Then "pipenv install" to install the packages required, located in Pipfile
This runs packages inside a virtualenv.  Alternatively you can just install
the packages listed in Pipfile using pip.

Must have a running mysql server

# Running
If pipenv was used, run using "pipenv run python main.py"

Otherwise "python main.py"

#TODO
-Implement storing data via mysql
