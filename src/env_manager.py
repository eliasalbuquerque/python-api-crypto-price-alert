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
        Adiciona uma nova linha no arquivo .env, garantindo que a chave seja escrita em letras maiúsculas.

        Args:
            key (str): Chave da variável.
            value (str): Valor da variável.
        """
        logging.debug(f'Adicionando "{key.upper()}" e seu valor no arquivo .env...')
        with open(self.env_dir, 'a', encoding='UTF-8') as f:
            f.write(f"{key.upper()}={value}\n")
            logging.debug('Variavel adicionada no arquivo .env.')

    def edit_env(self, key, new_value):
        """
        Edita o valor de uma variável existente no arquivo .env.

        Args:
            key (str): Chave da variável.
            new_value (str): Novo valor da variável.
        """
        logging.debug(f'Editando a variável "{key.upper()}" no arquivo .env...')

        updated = False
        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        with open(self.env_dir, 'w', encoding='UTF-8') as f:
            for line in lines:
                if line.startswith(f"{key}="):
                    f.write(f"{key.upper()}={new_value.upper()}\n")
                    updated = True
                    logging.debug(f'Variável "{key.upper()}" atualizada para "{new_value}".')
                else:
                    f.write(line)

        if not updated:
            logging.warning(f'Variável "{key.upper()}" não encontrada.')

    def remove_from_env(self, key):
        """
        Remove uma variável do arquivo .env.

        Args:
            key (str): Chave da variável a ser removida.
        """
        logging.debug(f'Removendo a variável "{key.upper()}" do arquivo .env...')

        removed = False
        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

        with open(self.env_dir, 'w', encoding='UTF-8') as f:
            for line in lines:
                if not line.startswith(f"{key.upper()}="):
                    f.write(line)
                else:
                    removed = True
                    logging.debug(f'Variável "{key.upper()}" removida.')

        if not removed:
            logging.warning(f'Variável "{key.upper()}" não encontrada.')

    def check_env(self, key):
        """
        Verifica se uma variável existe no arquivo .env.

        Args:
            key (str): Chave da variável a ser verificada.
        """
        logging.debug(f'Verificando se a variável "{key.upper()}" existe no arquivo .env...')

        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            for line in f:
                if line.startswith(f"{key.upper()}="):
                    logging.debug(f'Variável "{key.upper()}" encontrada.')
                    return True

        logging.debug(f'Variável "{key.upper()}" não encontrada.')
        return False

    def list_all_env(self):
        """
        Lista todas as chaves do arquivo .env.
        """
        logging.debug('Listando todas as chaves do arquivo .env...')

        keys = []
        with open(self.env_dir, 'r', encoding='UTF-8') as f:
            for line in f:
                key, _ = line.strip().split("=", 1)  # Ignora o valor
                keys.append(key)
        return keys

    def clear_env(self):
        """
        Limpa todas as variáveis do arquivo .env.
        """
        logging.debug('Limpando o arquivo .env...')
        
        with open(self.env_dir, 'w', encoding='UTF-8') as f:
            f.write("")
            logging.debug('Arquivo .env limpo.')

if __name__ == '__main__':
    # inicia a aplicacao
    from logging_setup import LoggingSetup
    logger = LoggingSetup()
    
    # cria o objeto env
    env = EnvManager()

    env.add_to_env("TESTE", "testado-com-sucesso")
    env.add_to_env("TESTE2", "testado-com-sucesso-novamente")
    env.add_to_env("EMAIL", "user@email.com")
    env.edit_env("EMAIL", "anotheruser@email.com")

    check_env = env.check_env("EMAIL")
    print(f'2. Variavel "EMAIL" existe? {check_env}')

    list_all_env = env.list_all_env()
    print(f'3. Consegue listar as variaveis existentes? {list_all_env}')

    env.remove_from_env("TESTE2")

    list_all_env_after_remove_from_env = env.list_all_env()
    print(f'4. Listar variaveis existentes apos remover "TESTE2"? {list_all_env}')