# Projeto para cadastro, listagem e remoção de usuarios
#Projeto visa treinamento das estruturas principais da linguagem Python

import usuarios
from os import system


while True:
    system('cls')
    print('='*30)
    print('MENU DE OPÇÕES\n'.center(30))
    print('[1] CADASTRAR NOVO USUARIO\t')
    print('[2] LISTAR USUARIOS\t')
    print('[3] REMOVER USUARIO\t')
    print('[4] SAIR')
    while True:
        resp = int(input('Escolha: '))
        if resp > 0 and resp <= 4:
            break
        else:
            print('INVALIDO!', end=' ')
    print('='*30)

    if resp == 1:
        usuarios.cadastro()

    elif resp == 2:
        usuarios.listar()
    
    elif resp == 3:
        U = str(input('Digite o nome para remover ')).title()
        usuarios.remover(U)

    else:
        print('SAINDO...')
        break

print('Obrigado! Volte sempre')