# title: 'logging setup'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'


import os
import logging.config

class LoggingSetup:
    """
    Classe para configurar o logging da aplicação.
    """

    def __init__(self, config_file="config.ini"):
        """
        Inicializa a classe com o caminho do arquivo de configuração.

        Args:
            config_file (str): Caminho para o arquivo 'config.ini'.
        """
        self.config_file = config_file
        self.create_log_dir()
        self.setup_logging()

    def _get_log_dir(self):
        """
        Retorna caminho da pasta 'log' da aplicação
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        log_dir = os.path.join(parent_dir, 'log')
        return log_dir

    def create_log_dir(self):
        """
        Cria a pasta 'log' se não existir.
        """
        log_dir = self._get_log_dir()
        os.makedirs(log_dir, exist_ok=True)

    def setup_logging(self):
        """
        Configura o logging da aplicação utilizando o arquivo 'config.ini'.
        """
        # Define o caminho absoluto para o arquivo 'config.ini'
        config_path = os.path.join(os.path.dirname(__file__), self.config_file)

        # Configura o logging utilizando o arquivo 'config.ini'
        logging.config.fileConfig(config_path, disable_existing_loggers=False)
        logging.warning('Aplicação iniciada.')

if __name__ == '__main__':
    logger = LoggingSetup()