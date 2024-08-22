# title: 'utils'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-21'
# update: '2024-08-21'


import os
import re
import logging


class Utils:

    def get_current_user(self):
        """Retorna o nome de usuário do sistema atual."""
        logging.info('Obtendo o nome do usuário do sistema...')

        return os.getlogin()

    def process_value(self, bitcoin_value):
        """
        Trata um valor recebido para o formato "300.000,00".

        Args:
            bitcoin_value (str): O valor a ser tratado.

        Returns:
            str: O valor formatado como "300.000,00".
        """
        logging.info('Processando valor mínimo recebido...')
        
        # Remove espaços em branco
        bitcoin_value = bitcoin_value.strip()
        bitcoin_value = re.sub(r'[.,]', '', bitcoin_value[:-3]) + bitcoin_value[-3:]  
        
        try:
            value = float(bitcoin_value.replace(",", "."))
            
            formatted_value = "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
        except ValueError as e:
            logging.error(f"Erro ao converter valor: {e}")
            raise

        return formatted_value