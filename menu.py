import json
from pathlib import Path
import encrypter as crpy
import os

class menu:
    mapa=[
        [">","•","•","•"], # Menu 1
        [">","•"] # Menu 2
    ]
    size=3
    selected=[0,-1]
    selected_menu=0
    cancel="-cancel"
    listener_bug=False # Serve pra corrigir o erro do listener que está dando uma volta no while sem ter pressionado nada após finalizar uma operação nesta classe

    def has_cancelled(self,text):
        return text == self.cancel

    def get_valid_path(self): # Obtêm do input um path que exista, não aceitando outros inexistentes
        path=input("> ")
        if self.has_cancelled(path):
            return self.cancel
        file=Path(path)
        while not file.is_file():
            print("* Arquivo não encontrato. Por favor verifique se o caminho passado está correto *")
            path=input("> ")
            if self.has_cancelled(path):
                return self.cancel
            file=Path(path)
        return path

    def reset(self,bug=True):
        self.mapa=[
            [">","•","•","•"], # Menu 1
            [">","•"] # Menu 2
        ]
        self.selected=[0,-1]
        self.selected_menu=0
        self.size=3
        self.listener_bug=bug
        

    def show_menu(self):
        print(f"{self.mapa[0][0]} Criptografar um Texto") # Criar novo arquivo de texto / arquivo de criptografia
        if self.selected[0] == 0 and self.selected_menu == 1:
            print(f"\t{self.mapa[1][0]} Criar uma Nova Cifra")
            print(f"\t{self.mapa[1][1]} Utilizar Cifra Existente")
        print(f"{self.mapa[0][1]} Criptografar um Arquivo") # Utilizar arquivo de criptografia existente / criar uma nova
        if self.selected[0] == 1 and self.selected_menu == 1:
            print(f"\t{self.mapa[1][0]} Criar uma Nova Cifra")
            print(f"\t{self.mapa[1][1]} Utilizar Cifra Existente")
        print(f"{self.mapa[0][2]} Descriptografar um Arquivo")

    def show_option(self):
        encrypt=crpy.encrypter()
        encrypt.create()
        
        print("* Digite -cancel para cancelar *\n")
        if self.selected[0] == 0:
            # self.flush(2)
            print("> Criptografar um Texto")
            if self.selected[1] == 0:
                print("\t> Criar uma Nova Cifra\n")
                print("* Digite o texto a ser criptografado *")
                text=input("> ")
                if self.has_cancelled(text):
                    return self.reset()
                result=encrypt.encrypt(text, False)
                print(f"- Texto Original: {result[0]}\n- Texto Criptografado: {result[1]}")
                os.system("pause")
            else:
                print("\t> Utilizar Cifra Existente\n")
                print("* Diretório do arquivo da cifra *")
                cipher=self.get_valid_path()
                print("* Digite o texto a ser criptografado *")
                text=input("> ")
                if self.has_cancelled(text):
                    return self.reset()
                encrypt.load_cipher(cipher)
                result=encrypt.encrypt(text, False)
                print(f"- Texto Original: {result[0]}\n- Texto Criptografado: {result[1]}")
                os.system("pause")
        elif self.selected[0] == 1:
            # self.flush(2)
            print("> Criptografar um Arquivo")
            if self.selected[1] == 0:
                print("\t> Criar uma Nova Cifra\n")
                print("* Diretório do arquivo de texto *")
                path=self.get_valid_path()
                if self.has_cancelled(path):
                    return self.reset()
                result=encrypt.encrypt(path,True)
                print(f"- Texto Original: {result[0]}\n- Texto Criptografado: {result[1]}")
                os.system("pause")
            else:
                print("\t> Utilizar Cifra Existente\n")
                print("* Diretório do arquivo de texto *")
                path=self.get_valid_path()
                if self.has_cancelled(path):
                    return self.reset()
                print("* Diretório do arquivo da cifra *")
                cipher=self.get_valid_path()
                if self.has_cancelled(cipher):
                    return self.reset()
                encrypt.load_cipher(cipher)
                result=encrypt.encrypt(path,True)
                print(f"- Texto Original: {result[0]}\n- Texto Criptografado: {result[1]}")
                os.system("pause")
        elif self.selected[0] == 2:
            # self.flush(1)
            print("> Descriptografar um Arquivo\n")
            print("* Diretório do arquivo de texto *")
            path=self.get_valid_path()
            if self.has_cancelled(path):
                return self.reset()
            print("* Diretório do arquivo da cifra *")
            cipher=self.get_valid_path()
            if self.has_cancelled(cipher):
                return self.reset()
            encrypt.load_cipher(cipher)
            result=encrypt.decrypt(path,True)
            print(f"- Texto Original:\n{result[0]}\n")
            print(f"- Texto Criptografado:\n{result[1]}")
            os.system("pause")
        else:
            print("*Opção não reconhecida*")

        self.reset()

    def next(self, menu):
        self.mapa[menu][self.selected[menu]]="•"
        self.selected[menu]+=1
        if self.selected[menu] >= self.size:
            self.selected[menu] = 0
        self.mapa[menu][self.selected[menu]]=">"

    def prev(self, menu):
        self.mapa[menu][self.selected[menu]]="•"
        self.selected[menu]-=1
        if self.selected[menu] < 0:
            self.selected[menu] = self.size-1
        self.mapa[menu][self.selected[menu]]=">"
    
    def select(self):
        if self.listener_bug:
            self.listener_bug=False
            return
        self.selected_menu=0
        if self.selected[0] == 0 or self.selected[0] == 1:
            if self.selected[1] == -1: # Se menu 2 não tiver selecionado
                self.selected[1]=0
                self.size=2
                self.selected_menu=1
                return
            else:
                self.selected_menu=1
        self.show_option()