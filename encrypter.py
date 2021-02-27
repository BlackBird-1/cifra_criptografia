import json
import random
import codecs

class characters:
    path="D:\\htdocs\\Projetos no Visual Studio\\Python\\Criptografia\\map-scheme.json"
    keys_type=4 # Total de tipos de chaves possíveis
    keys_count=None
    map_scheme=None
    invalid=['\\', '/', '|', '<', '>', '*', ':', '“', '?']
    chars=[
        'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z',
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y',
        'Z', # Letras
        'á', 'à', 'â', 'ã',
        'é', 'è', 'ê',
        'í', 'ì', 'î',
        'ó', 'ò', 'ô', 'õ',
        'ú', 'ù', 'û',
        'ç',
        'Á', 'À', 'Â', 'Ã',
        'É', 'È', 'Ê',
        'Í', 'Ì', 'Î',
        'Ó', 'Ò', 'Ô', 'Õ',
        'Ú', 'Ù', 'Û',
        'Ç', # Acentos
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '0', # Números
        ',', '.', '<', '>', ':',
        ';', '~', '^', '´', '`',
        '[', ']', '{', '}', 'ª',
        'º', '/', '|', '\\', '?',
        '°', '!', '@', '#', '$',
        '%', '¨', '&', '*', '(',
        ')', '-', '_', '=', '+',
        '§', '¹', '²', '³', '£',
        '¢', '¬', '\"', '\'', " ",
        '\n','\r','\t' # Caracteres especiais
    ]

    def __init__(self):
        with open(self.path,"rt") as file:
            mapScheme=file.read()
        self.map_scheme=json.loads(mapScheme)
        self.keys_count=len(self.map_scheme)

    def remove_invalid_chars(self,text):
        for char in self.invalid:
            if char in text:
                text.replace(char,"")
        return text

class encrypter:
    chars=characters.chars
    keysType=characters.keys_type
    keys_count=characters.keys_count

    encrypter=characters.map_scheme # Guarda a letra original como chave e a substituta como valor (para criptografar)
    decrypter=dict() # Guarda a letra substituta como chave e a original como valor (para descriptografar)

    def __init__(self):
        char=characters()
        self.keys_count=char.keys_count
        self.encrypter=char.map_scheme

    def create(self):
        keyList=random.sample(range(self.keys_count),self.keys_count)
        iterator=iter(keyList)
        for key in self.encrypter:
            char=self.chars[next(iterator)]
            self.encrypter[key]=char
            self.decrypter[char]=key

    def encrypt(self,file_path,create):
        # text=file_path
        text=""
        encrypted=""

        if create: # Caso for criar um arquivo .txt, consequentemente já teria passado um arquivo original pra ler
            # with open(file_path, "rt") as file:
            #     text=file.read()
            with codecs.open(file_path, "rb", encoding="utf-8") as file:
                for line in file:
                    text+=line

        for key in text:
            encrypted+=self.encrypter[key]

        if create: # Se for pra gerar um arquivo .txt
            start_ext=file_path.rfind(".") # Guarda a posição onde se inicia o texto da extensão do arquivo
            encrypted_file=file_path[0:start_ext]+"_encrypted.txt"
            with open(encrypted_file, "wt") as file:
                file.write(encrypted)

            cipher_file=file_path[0:start_ext]+"_cifra.json"
            json_file=json.dumps([self.encrypter, self.decrypter])
            with open(cipher_file, "wt") as file:
                file.write(json_file)
        
        return (text, encrypted)

    def decrypt(self,file_path,create):
        text=""
        decrypted=""

        with open(file_path, "rt") as file:
            text=file.read()

        for key in text:
            decrypted+=self.decrypter[key]

        if create: # Se for pra gerar um arquivo .txt
            start_ext=file_path.rfind(".") # Guarda a posição onde se inicia o texto da extensão do arquivo
            decrypted_file=file_path[0:start_ext]+"_decrypted.txt"
            with open(decrypted_file, "wt") as file:
                file.write(decrypted)
        
        return (text, decrypted)

    def load_cipher(self,path):
        with open(path,"rt") as file:
            crypt_list=json.loads(file.read())
            self.encrypter=crypt_list[0]
            self.decrypter=crypt_list[1]
    
    def create_cipher(self,file_path):
        start_ext=file_path.rfind(".") # Guarda a posição onde se inicia o texto da extensão do arquivo
        cipher_path=file_path[0:start_ext]+"_cifra.json"
        cipher=json.dumps([self.encrypter,self.decrypter])
        with open(cipher_path,"wt") as file:
            file.write(cipher)