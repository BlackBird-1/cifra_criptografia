# *********** Imports ***********
import os
import msvcrt
from pynput.keyboard import Key,Listener,Controller
from encrypter import encrypter
from menu import menu

# *********** Vars ***********
encrypt = encrypter()
menu=menu()
global key; key=None

# *********** Methods ***********
def on_release(keyP):
    while msvcrt.kbhit(): # Obs: o stdin.flush() da lib 'sys' não funcionou, e esse funcionou perfeitamente
        msvcrt.getch() # Basicamente ele verifica se alguma tecla está esperando pra ser lida, se sim, ele lê, resolvendo o problema do input() ficar lendo

    global key; key=keyP
    return False

def show_menu():
    while key != Key.esc:
        if key == Key.down:
            menu.next(menu.selected_menu)
        elif key == Key.up:
            menu.prev(menu.selected_menu)
        elif key == Key.enter or key == Key.right:
            menu.select()
        elif key == Key.backspace or key == Key.left:
            menu.reset()
        
        print("- Navega pelas opções com os direcionais para cima ↑ e para baixo ↓")
        print("- Selecione uma opção com ENTER ou o direcional para direita →")
        print("- Para voltar utilize a tecla BACKSPACE ou o direcional para esquerda ←\n")
        menu.show_menu()

        with Listener(on_release=on_release) as listener:
            listener.join()
        os.system("cls")

# *********** Main ***********
show_menu()
print("Finalizado...")