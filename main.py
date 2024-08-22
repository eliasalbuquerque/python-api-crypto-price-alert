# title: 'controller'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'

# from decouple import config

import logging
from src.logging_setup import LoggingSetup
from src.env_manager import EnvManager
from app import App

class Main:
    def __init__(self):
        self.logger = LoggingSetup()
        self.env = EnvManager()

        self.app = None  # Inicializa o app depois das verificações.

    def run(self):
        if not self.env.check_env('USER_EMAIL'):  
            self.app = App(self)  
            self.app.show_login_config()  # Exibe a tela de login
        else:
            self.app = App(self) 
            self.app.show_main_screen()  # Exibe a tela principal

        self.app.mainloop() 

    def user_registration(self, email, password, report_email):
        logging.info('Registrando usuário pela primeira vez...')

        self.env.add_to_env('USER_EMAIL', email)
        self.env.add_to_env('USER_PASSWORD', password)
        self.env.add_to_env('REPORT_EMAIL', report_email)

        if self.env.check_env('USER_EMAIL'):
            logging.info('Usuário cadastrado com sucesso`.')
            self.app.show_main_screen() 
        else: 
            logging.error('Não foi possível cadastrar o usuário.')

        

if __name__ == '__main__':
    main_app = Main()
    main_app.run()  # Inicia o processo
