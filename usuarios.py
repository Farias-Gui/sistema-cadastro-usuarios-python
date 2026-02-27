from os import system
from time import sleep
Dados = []

def cadastro():
    Usuarios = {}
    system('cls')
    print('='*30)
    print('CADASTRO DE USUARIOS'.center(30))
    print('='*30)
    Usuarios['Nome'] = str(input('Nome Completo: ')).title()
    Usuarios['Idade'] = int(input('Idade: '))
    Usuarios['Email'] = str(input('Email: '))
    Dados.append(Usuarios)
    print('\nCADASTRO CONCLUIDO COM SUCESSO!'.center(30))
    sleep(1.5)
    system('cls')


def listar():
    system('cls')
    cont = 0
    print('='*30)
    print('LISTANDO USUARIOS...'.center(30))
    print('='*30)
    sleep(1.5)
    print(f'[Foram cadastrados {len(Dados)} usuarios]\n')
    for dicionario in Dados:
        for k, v in dicionario.items():
            print(f'{k} >> {v}')
        print('--'*20)
    sleep(4)

def remover(valor):
    system('cls')
    print('='*30)
    print('REMOVENDO O USUARIO...'.center(30))
    print('='*30)
    sleep(1.5)
    if len(Dados) > 0:
        for usuario in Dados:
            if usuario['Nome'] == valor:
                Dados.remove(usuario)
                print(f'Usuario {valor} removido com sucesso!')
                break
        else:
            print('Usuario não encontrado')
    else:
        print('Nenhum usuario adicionado')
    sleep(2)