# title: 'view'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2024-08-20'
# update: '2024-08-20'


import customtkinter as ctk
from threading import Thread
from main import Main


# Initialize the CustomTkinter window
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("dark-blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Rastreador de Criptomoedas com Relatórios Diários")
        self.geometry("500x500")
        
        # Create UI elements
        self.label = ctk.CTkLabel(self, text="Digite seu e-mail:")
        self.label.pack(pady=10)
        
        self.input_email = ctk.CTkEntry(self, width=400)
        self.input_email.pack(pady=10)

        self.label = ctk.CTkLabel(self, text="Digite sua senha:")
        self.label.pack(pady=10)
        
        self.palavra_chave = ctk.CTkEntry(self, width=200)
        self.palavra_chave.pack(pady=10)
        
        self.start_button = ctk.CTkButton(self, text="Iniciar Automação", command=self.start_automation)
        
        self.output_text = ctk.CTkTextbox(self, width=400, height=300)
        self.output_text.pack(pady=10)
    
    def start_automation(self):
        self.start_button.configure(state="disabled")
        
        input_email = self.input_email.get()
        self.write_output(f"Seu e-mail é: {input_email}\n")
        self.start_button.configure(state="normal")
        
        thread = Thread(target=Main, daemon=True, args=(palavra_chave, self))
        thread.start()
    
    def write_output(self, text):
        self.output_text.insert("end", text)
        self.output_text.yview("end")  # Scroll to the end of the output

if __name__ == "__main__":
    app = App()
    app.mainloop()