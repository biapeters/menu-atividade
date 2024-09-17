import json


def mostrar_menu_principal():
    print('\033[1m-------- MENU PRINCIPAL --------\033[m\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(9) Sair.\n')


def mostrar_menu_secundario(grupos):
    print(f'\n\033[1m***** MENU DE {grupos} *****\033[m\n')
    print('(1) Incluir.')
    print('(2) Listar.')
    print('(3) Atualizar.')
    print('(4) Excluir.')
    print('(9) Voltar ao menu principal.')


def incluir(nome_arquivo, opcao):
    try:
        lista_itens = ler_arquivo(nome_arquivo)  # Lendo a lista do arquivo
        if opcao == 1 or opcao == 2:
            codigo = int(input('Digite o código: '))
            if any(cadastro['Código'] == codigo for cadastro in lista_itens):
                print(f'\033[31mCódigo {codigo} já existe. Escolha um código diferente.\033[m')
                return
            cadastro = {
                'Código': codigo,
                'Nome': input('Digite o nome: '),
                'CPF': input('Digite o CPF: ')
            }
        elif opcao == 3:
            codigo = int(input('Digite o código: '))
            if any(cadastro['Código'] == codigo for cadastro in lista_itens):
                print(f'\n\033[31mCódigo {codigo} já existe. Escolha um código diferente.\033[m')
                return
            cadastro = {
                'Código': codigo,
                'Nome': input('Digite o nome da disciplina:')
            }
        elif opcao == 4:
            codigo = int(input('Digite o código da turma: '))
            if any(cadastro['Código'] == codigo for cadastro in lista_itens):
                print(f'\033[31mCódigo {codigo} já existe. Escolha um código diferente.\033[m')
                return
            cadastro = {
                'Código': codigo,
                'Código Professor': int(input('Digite o código do(a) professor(a): ')),
                'Código disciplina': int(input('Digite o código da disciplina: '))
            }
        elif opcao == 5:
            codigo = int(input('Digite o código da matrícula: '))
            if any(cadastro['Código'] == codigo for cadastro in lista_itens):
                print(f'\033[31mCódigo {codigo} já existe. Escolha um código diferente.\033[m')
                return
            cadastro = {
                'Código': codigo,
                'Código Turma': int(input('Digite o código da turma: ')),
                'Código estudante': int(input('Digite o código do estudante: '))
            }
        lista_itens.append(cadastro)
        salvar_arquivo(lista_itens, nome_arquivo)
        print(f'\n\033[32mCadastro incluído(a) com sucesso!\033[m')
    except ValueError:
        print('\n\033[31mDigite apenas números.\033[m')
        return


def listar(nome_arquivo, opcao):
    lista_itens = ler_arquivo(nome_arquivo)
    if not lista_itens:
        print(f'\033[31mNão há cadastros.\033[m\n')
        return

    if opcao == 1:
        print(f'\033[1mLista de estudantes:\033[m')
        for cadastro in lista_itens:
            print(f'- Código: {cadastro.get("Código")}, Nome: {cadastro.get("Nome")}, CPF: {cadastro.get("CPF")}')
    elif opcao == 2:
        print(f'\033[1mLista de professores:\033[m')
        for cadastro in lista_itens:
            print(f'- Código: {cadastro.get("Código")}, Nome: {cadastro.get("Nome")}, CPF: {cadastro.get("CPF")}')
    elif opcao == 3:
        print(f'\033[1mLista de disciplinas:\033[m')
        for cadastro in lista_itens:
            print(f'- Código: {cadastro.get("Código")}, Nome: {cadastro.get("Nome")}')
    elif opcao == 4:
        print(f'\033[1mLista de turmas:\033[m')
        for cadastro in lista_itens:
            print(f'- Código: {cadastro.get("Código")}, Código Professor: {cadastro.get("Código Professor")}, Código Disciplina: {cadastro.get("Código disciplina")}')
    elif opcao == 5:
        print(f'\033[1mLista de matrículas:\033[m')
        for cadastro in lista_itens:
            print(f'- Código: {cadastro.get("Código")}, Código Turma: {cadastro.get("Código Turma")}, Código Estudante: {cadastro.get("Código estudante")}')
    else:
        print(f'\033[31mOpção inválida.\033[m')


def atualizar(nome_arquivo, opcao):
    lista_itens = ler_arquivo(nome_arquivo)
    try:
        codigo_atualizar = int(input('Digite o código do cadastro que deseja atualizar: '))
        for cadastro in lista_itens:
            if codigo_atualizar == cadastro['Código']:
                if opcao == 1 or opcao == 2:
                    cadastro['Código'] = int(input('Digite o novo código: '))
                    cadastro['Nome'] = input('Digite o novo nome: ')
                    cadastro['CPF'] = input('Digite o novo CPF: ')
                elif opcao == 3:
                    cadastro['Código'] = int(input('Digite o novo código: '))
                    cadastro['Nome'] = input('Digite o novo nome: ')
                elif opcao == 4:
                    cadastro['Código'] = int(input('Digite o novo código: '))
                    cadastro['Código Professor'] = int(input('Digite o novo código do(a) professor(a): '))
                    cadastro['Código disciplina'] = int(input('Digite o novo código da disciplina: '))
                elif opcao == 5:
                    cadastro['Código'] = int(input('Digite o novo código: '))
                    cadastro['Código Estudante'] = int(input('Digite o novo código do estudante: '))
                    cadastro['Código Turma'] = int(input('Digite o novo código da turma: '))
                print(f'\033[32mCódigo {cadastro} atualizado com sucesso!\033[m\n')
                salvar_arquivo(lista_itens, nome_arquivo)
                return
        print(f'\n\033[31mNão foi encontrado o código {codigo_atualizar} na lista.\033[m')
    except ValueError:
        print('Digite apenas números.')


def excluir(nome_arquivo):
    lista_itens = ler_arquivo(nome_arquivo)
    try:
        codigo = int(input('Digite o código de cadastro que deseja excluir: '))
        for cadastro in lista_itens:
            if codigo == cadastro['Código']:
                confirmar = input('Tem certeza que deseja excluir esse código (s/n)? ').lower()
                if confirmar == 's':
                    print(f'\n\033[32mCadastro com o código {codigo} excluído com sucesso!\033[m\n')
                    lista_itens.remove(cadastro)
                    salvar_arquivo(lista_itens, nome_arquivo)
                    return
                elif confirmar == 'n':
                    print('\n\033[33mOperação de exclusão cancelada. Retornando ao menu...\033[m\n')
                    return
                else:
                    print('\n\033[31mOpção inválida. Operação cancelada.\033[m\n')
                    return
        print(f'\n\033[31mCadastro com código {codigo} não encontrado.\033[m\n')
    except ValueError:
        print('\n\033[31mDigite apenas números.\033[m')


def salvar_arquivo(lista_itens, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista_itens, arquivo_aberto, ensure_ascii=False, indent=4)


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista_itens = json.load(arquivo_aberto)
        return lista_itens
    except FileNotFoundError:
        return []


arquivo_estudante = "Cadastro estudantes.json"
arquivo_professores = "Cadastro professores.json"
arquivo_disciplina = "Cadastro disciplinas.json"
arquivo_turma = "Cadastro turmas.json"
arquivo_matricula = "Cadastro matriculas.json"

while True:
    mostrar_menu_principal()
    opcao = input('Informe a opção desejada: ')
    print(f'Você escolheu a opção: {opcao}')

    if opcao == '1':
        grupo = 'ESTUDANTES'
        arquivo = arquivo_estudante
    elif opcao == '2':
        grupo = 'PROFESSORES'
        arquivo = arquivo_professores
    elif opcao == '3':
        grupo = 'DISCIPLINAS'
        arquivo = arquivo_disciplina
    elif opcao == '4':
        grupo = 'TURMAS'
        arquivo = arquivo_turma
    elif opcao == '5':
        grupo = 'MATRÍCULAS'
        arquivo = arquivo_matricula
    elif opcao == '9':
        print('\n\033[1mVocê saiu.\033[m\n')
        break
    else:
        print('\n\033[31mVocê digitou uma opção inválida.\033[m\n')
        continue

    while True:
        mostrar_menu_secundario(grupo)
        opcao2 = input('\nDigite uma opção: ')
        print(f'Você escolheu a opção: {opcao2}')

        if opcao2 == '1':
            print('\n\033[1m-=-=-=- INCLUIR -=-=-=-\033[m\n')
            incluir(arquivo, int(opcao))
        elif opcao2 == '2':
            print('\n\033[1m-=-=-=- LISTAGEM -=-=-=-\033[m\n')
            listar(arquivo, int(opcao))
        elif opcao2 == '3':
            print('\n\033[1m-=-=-=- ATUALIZAR -=-=-=-\033[m\n')
            atualizar(arquivo, int(opcao))
        elif opcao2 == '4':
            print('\n\033[1m-=-=-=- EXCLUIR -=-=-=-\033[m\n')
            excluir(arquivo)
        elif opcao2 == '9':
            print('\n\033[1mVoltando ao menu principal...\033[m\n')
            break
        else:
            print('\n\033[31mOpção inválida.\033[m\n')

