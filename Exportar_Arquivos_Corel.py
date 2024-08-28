# EXPORTAR ARQUIVOS COREL
import time
import pyautogui as py
from pynput.mouse import Listener

while True:
    # coleta a quantidade de arquivos
    def qnt_arquivos():
        quantidade = int(input('Digite a quantidade: '))
        #print(quantidade)
        return quantidade

    # coleta o prefixo(tamanho molde) do arquivo
    def prefixo():
        nome_arquivo = input('Digite o prefixo: ')
        #print(nome_arquivo)
        return nome_arquivo

    quantidade = qnt_arquivos()
    nome_arquivo = prefixo()

    # variaveis globais
    posicao_mouse = (0, 0)
    clique_detectado = False

    # detecta a posição do mouse atraves do click
    def on_click(x, y, button, pressed):
        global posicao_mouse, clique_detectado
        if pressed:
            posicao_mouse = x, y
            clique_detectado = True
            listener.stop()  # Interrompe o loop do listener

    # Iniciar o listener do mouse
    with Listener(on_click=on_click) as listener:
        listener.join()

    # Exportar arquivos, nomea-los após detecção do clique
    if clique_detectado:
        print(posicao_mouse)
        time.sleep(3)
        qnt_item = 0
        for item in range(quantidade):
            qnt_item += 1
            quantidade = nome_arquivo
            py.hotkey('ctrl', 'e')
            py.write(nome_arquivo)
            py.write(str(qnt_item))
            py.press('enter')
            py.press('enter')
            py.hotkey('tab')
    else:
        print("Nenhum clique detectado.")

    print()
    print(f'{qnt_item} Arquivos exportados com sucesso!')
    print()

    finalizar = input("Digite '0' para finalizar o programa: ")
    if finalizar == '0':
        break

print()