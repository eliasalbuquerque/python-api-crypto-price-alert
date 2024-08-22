# title: 'view'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'

import logging
import customtkinter as ctk
from src.utils import Utils


class App(ctk.CTk):
    def __init__(self, main_ctrl):
        super().__init__()
        self.title("Rastreador de Criptomoedas")
        self.main_ctrl = main_ctrl
        self.utils = Utils()

        self.user_system = self.utils.get_current_user()

    def show_main_screen(self):
        logging.info('Iniciando tela principal do app...')

        self.geometry("400x500")

        # Label - titulo
        self.label_title = ctk.CTkLabel(self, text="Digite o valor mínimo do Bitcoin\npara o recebimento do e-mail:")
        self.label_title.pack(pady=20)

        # Frame input relatorio
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.pack(pady=20)

        # Label e campo para valor limite
        self.label_value = ctk.CTkLabel(self.action_frame, text="Valor Limite do Bitcoin:")
        self.label_value.grid(row=0, column=0, padx=5, pady=5)

        self.entry_value = ctk.CTkEntry(self.action_frame)
        self.entry_value.grid(row=0, column=1, padx=5, pady=5)

        # Botão para iniciar o rastreamento
        self.button_iniciar = ctk.CTkButton(self, text="Iniciar Rastreamento", command=self.__process_value)
        self.button_iniciar.pack(pady=5)

        # Frame info
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(padx=20, pady=20, expand=True, fill="both")

        # Área de informações
        self.info_label = ctk.CTkLabel(self.info_frame, text="Informações da Aplicação", wraplength=300)
        self.info_label.pack(pady=5)

    def __process_value(self):
        bitcoin_input = self.entry_value.get()
        bitcoin_value = self.utils.process_value(bitcoin_input)
        logging.info(f'O valor mínimo inserido foi de {bitcoin_value}')

    def __get_test(self):
        print('-----teste-----')

    def show_login_config(self):
        logging.info('Solicitando dados do usuário...')

        self.geometry("400x500")
            
        # Labels - input de login e senha
        message = f'Olá {self.user_system.capitalize()}!'
        self.login_label_wellcome = ctk.CTkLabel(self, text=f"{message}.")
        self.login_label_wellcome.pack(pady=10)
        self.login_label_explanation = ctk.CTkLabel(self, text="Para enviar o e-mail do relatório\nprecisamos de um e-mail válido para o envio.")
        self.login_label_explanation.pack(pady=10)
        self.login_label = ctk.CTkLabel(self, text="Digite seu e-mail e senha:")
        self.login_label.pack(pady=10)

        # Frame - input de login e senha
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=20)
        
        # Input
        ctk.CTkLabel(self.login_frame, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        self.email_entry = ctk.CTkEntry(self.login_frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.login_frame, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label - email do relatorio
        self.login_label = ctk.CTkLabel(self, text="Agora digite um e-mail para receber o relatório:")
        self.login_label.pack(pady=10)

        # Frame - email do relatorio
        self.report_email_frame = ctk.CTkFrame(self)
        self.report_email_frame.pack(pady=20)

        # Input
        ctk.CTkLabel(self.report_email_frame, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        self.report_email_entry = ctk.CTkEntry(self.report_email_frame)
        self.report_email_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Button - cadastrar
        self.register_button = ctk.CTkButton(self, text="Cadastrar", command=self.__user_registration)
        self.register_button.pack(pady=10)


    def __user_registration(self):
        user_email = self.email_entry.get()
        password = self.password_entry.get()
        report_email = self.report_email_entry.get()

        self.main_ctrl.user_registration(user_email, password, report_email)

        self.__widgets_destroy()
        self.show_main_screen()

    def __widgets_destroy(self):
        for widget in self.winfo_children():
            widget.destroy()
        



if __name__ == "__main__":
    app = App()
    app.mainloop()