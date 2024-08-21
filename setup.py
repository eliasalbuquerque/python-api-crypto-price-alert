# title: 'setup cx_freeze'
# author: 'Elias Albuquerque'
# version: '0.1.0'
# created: '2024-08-14'
# update: '2024-08-20'


import sys
import os
from cx_Freeze import setup, Executable

# Dados para o executável
executables = [Executable(
    script="app.py",
)]

# Defina os pacotes necessários para a aplicação
packages = [
    # colocar as bibliotecas
]

# Inclua os arquivos e diretórios necessários
include_files = [
    ("src", "src"), 
    ("LICENSE", "LICENSE"), # remover se nao houver licensa
    ("README.md", "README.md")
]

# Inclua os arquivos do pacote "requirements.txt"
# requirements = ["python-docx==1.1.2", "selenium==4.23.1", "cx_Freeze==7.2.0"]

# Crie o arquivo de configuração para o cx_Freeze
build_exe_options = {
    "packages": packages,
    "include_files": include_files,
    "include_msvcr": True,
    "silent_level": 3
}

# Crie o arquivo de configuração para o cx_Freeze
setup(
    name="teste",
    version="1.0",
    author="Elias Albuquerque",
    description="teste",
    url="https://github.com/eliasalbuquerque/url_do_repositorio",
    license="MIT", # alterar para o tipo de licensa
    license_files=["LICENSE"], # remover se nao houver
    executables=executables,
    options={"build_exe": build_exe_options},
    # install_requires=requirements
)

# NOTE:
# pip install cx-freeze
# python .\setup.py build
