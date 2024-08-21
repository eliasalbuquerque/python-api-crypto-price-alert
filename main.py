# title: 'controller'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'


from decouple import config
from src.logging_setup import LoggingSetup

class Main():
    def __init__(self):

        self.logger = LoggingSetup()



if __name__ == '__main__':
    app = Main()