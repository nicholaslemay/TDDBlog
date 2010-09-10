from settings import *
import os
import sys
sys.path.append(os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
TEST_HOST = "http://127.0.0.1:8000"
SELENIUM_HOST = 'localhost'
SELENIUM_PORT = 4444
SELENIUM_BROWSER_START_COMMAND = '*firefox'