from customer_churn.logger import logging
from customer_churn.exception import CustomerchurnException
import sys

logging.info("Welcome to our custom log") 


try:
    a = 2/0
except Exception as e:
    raise CustomerchurnException(e, sys)