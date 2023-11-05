from colorama import Fore
from time import sleep

nome = ''
senha = ''


def upper(msg):
    if any(i.isupper() for i in msg):
        return True
    else:
        return False


def arquivo_existe(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print(Fore.LIGHTRED_EX + 'Houve uma falha na criação do arquivo' + Fore.RESET)
    else:
        print(Fore.LIGHTGREEN_EX + f'Arquivo {name} criado com sucesso' + Fore.RESET)


def linha(tam=42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print(Fore.LIGHTRED_EX + 'Digite apenas opções válidas' + Fore.RESET)
            continue
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + '\nO usúario perfiriu não digitar as informações' + Fore.RESET)
            exit()
            return 0
        else:
            return n


def menu(lista):
    cabecalho('MENU DO SISTEMA')
    sleep(0.7)
    c = 0
    for item in lista:
        print(Fore.CYAN + f'{c + 1} - {item}' + Fore.RESET)
        c += 1
    print(linha())
    opc = leiaint(Fore.CYAN + 'Sua opção: ' + Fore.RESET)
    sleep(0.3)
    return opc


def login():
    print(linha())
    try:
        nome = str(input(Fore.CYAN + 'Nome: ' + Fore.RESET))
        senha = str(input(Fore.CYAN + 'Senha: ' + Fore.RESET))
    except KeyboardInterrupt:
        print(Fore.LIGHTRED_EX + '\nO usúario perfiriu não digitar as informações' + Fore.RESET)
        exit()
    return nome, senha


def novo_usuario():
    while True:
        try:
            print(linha())
            print(Fore.CYAN + 'Requisitos para um nome:\n'
                              '*Ter pelo menos 8 caracteres\n'
                              '*Ter pelo menos uma letra maiúsula' + Fore.RESET)
            print(linha())
            nome = str(input(Fore.CYAN + 'Nome: ' + Fore.RESET))
            if len(nome) <= 7:
                print(Fore.RED + 'Por favor, insira um nome dentro dos requisitos' + Fore.RESET)
            elif not upper(nome):
                print(Fore.LIGHTRED_EX + 'Por favor, insira um nome com pelo menos uma letra maiúscula' + Fore.RESET)
            else:
                break
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + '\nO usúario perfiriu não digitar as informações' + Fore.RESET)
            exit()
    while True:
        try:
            print(linha())
            print(Fore.CYAN + 'Requisitos para uma senha:\n'
                              '*Ter pelo menos 8 caracteres\n'
                              '*Ter pelo menos uma letra maiuscula' + Fore.RESET)
            print(linha())
            senha = str(input(Fore.CYAN + 'Senha: ' + Fore.RESET))
            if len(senha) <= 7:
                print(Fore.LIGHTRED_EX + 'Por favor, insira uma senha com pelo menos 8 caracteres' + Fore.RESET)
            elif not upper(senha):
                print(Fore.LIGHTRED_EX + 'Por favor, insira uma senha com pelo menos uma letra maiúscula' + Fore.RESET)
            else:
                break
        except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX + '\nO usúario perfiriu não digitar as informações' + Fore.RESET)
            exit()
    return (nome, senha)


def buscar_usuarios(login, senha):
    usuarios = []
    try:
        with open('SistemaCadastro.txt', 'rt', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False


arq = 'SistemaCadastro.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resp = menu(['Novo cadastro', 'Login', 'Sair'])
    if resp == 1:
        while True:
            nome, senha = novo_usuario()
            user = buscar_usuarios(nome, senha)
            if nome == senha:
                print(Fore.LIGHTRED_EX + 'A senha não pode ser igual o nome' + Fore.RESET)
                continue
            elif user:
                print(Fore.LIGHTRED_EX + 'Usúario ja existe' + Fore.RESET)
                continue
            else:
                with open('SistemaCadastro.txt', 'at', encoding='Utf-8', newline='') as arquivo:
                    arquivo.write(f'{nome} {senha}\n')
                print(Fore.LIGHTGREEN_EX + 'Cadastro feito com sucesso!' + Fore.RESET)
                break
    elif resp == 2:
        while True:
            try:
                nome, senha = login()
                if buscar_usuarios(nome, senha):
                    print(Fore.LIGHTGREEN_EX + f'Seja bem vindo(a) {nome}!' + Fore.RESET)
                    exit()
                else:
                    print(Fore.LIGHTRED_EX + 'Você digitou o nome e/ou senha errado' + Fore.RESET)
            except KeyboardInterrupt:
                print(Fore.RED + '\nO usúario prefiriu não dgitar as informações' + Fore.RESET)
                exit()
    elif resp == 3:
        print(Fore.LIGHTGREEN_EX + 'Saindo do sistema... Ate logo!' + Fore.RESET)
        sleep(1)
        exit()
    else:
        print(Fore.LIGHTRED_EX + 'Digite apenas opções válidas' + Fore.RESET)
        sleep(0.3)
