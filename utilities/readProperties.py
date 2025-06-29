import configparser #predefined package which is available in python
import os

from Demos.win32ts_logoff_disconnected import username

# Get the root directory of the project (one level up from this file)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Build the config path
CONFIG_PATH = os.path.join(ROOT_DIR, 'Configurations', 'config.ini')

# Load the config
config = configparser.RawConfigParser()
config.read(CONFIG_PATH)

class ReadConfig: #just a python class, not a pytest
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password