# title: '.env file manager'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'


import os
import logging

class EnvManager:
    """
    Classe para gerenciar um arquivo .env.
    """

    def __init__(self, env_file=".env"):
        """
        Inicializa a classe com o caminho para o arquivo .env.

        Args:
            env_file (str): Caminho para o arquivo .env (opcional, ".env" por padrão).
        """
        logging.debug('Iniciando gerenciador do arquivo .env...')
        self.env_file = env_file
        self.env_dir = self.__get_env_dir()
        self.__create_env_file()

    def __get_env_dir(self):
        """
        Retorna caminho do arquivo .env
        """
        logging.debug('Montando diretório do arquivo .env...')

        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        env_dir = os.path.join(parent_dir, self.env_file)

        logging.debug(f'Retorna diretório .env: {env_dir}')
        return env_dir

    def __create_env_file(self):
        """
        Cria um arquivo .env vazio se não existir.
        """
        logging.debug('Criando arquivo .env...')
        if not os.path.isfile(self.env_dir):
            with open(self.env_dir, 'w') as f:
                logging.debug('Arquivo .env criado.')
                pass  # Cria um arquivo vazio

    def add_to_env(self, key, value):
        """
        Adiciona uma nova linha no arquivo .env.

        Args:
            key (str): Chave da variável.
            value (str): Valor da variável.
        """
        logging.debug(f'Adicionando "{key}" e seu valor no arquivo .env...')
        with open(self.env_dir, 'a', encoding='UTF-8') as f:
            f.write(f"{key}={value}\n")
            logging.debug('Variavel adicionada no arquivo .env.')

    def edit_env(self, key, new_value):
        """
        Edita o valor de uma variável existente no arquivo .env.

        Args:
            key (str): Chave da variável.
            new_value (str): Novo valor da variável.
        """
        logging.debug(f'Editando a variável "{key}" no arquivo .env...')
        if not os.path.isfile(self.env_dir):
            logging.error("Arquivo .env não encontrado.")
            return

        updated = False
        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        with open(self.env_dir, 'w', encoding='UTF-8') as f:
            for line in lines:
                if line.startswith(f"{key}="):
                    f.write(f"{key}={new_value}\n")
                    updated = True
                    logging.debug(f'Variável "{key}" atualizada para "{new_value}".')
                else:
                    f.write(line)

        if not updated:
            logging.warning(f'Variável "{key}" não encontrada.')

    def remove_from_env(self, key):
        """
        Remove uma variável do arquivo .env.

        Args:
            key (str): Chave da variável a ser removida.
        """
        logging.debug(f'Removendo a variável "{key}" do arquivo .env...')
        if not os.path.isfile(self.env_dir):
            logging.error("Arquivo .env não encontrado.")
            return

        removed = False
        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        with open(self.env_dir, 'w', encoding='UTF-8') as f:
            for line in lines:
                if not line.startswith(f"{key}="):
                    f.write(line)
                else:
                    removed = True
                    logging.debug(f'Variável "{key}" removida.')

        if not removed:
            logging.warning(f'Variável "{key}" não encontrada.')

if __name__ == '__main__':
    from logging_setup import LoggingSetup
    logger = LoggingSetup()
    env = EnvManager()
    env.add_to_env("EMAIL", "user@email.com")
    env.edit_env("EMAIL", "anotheruser@email.com")
    env.remove_from_env("EMAIL")