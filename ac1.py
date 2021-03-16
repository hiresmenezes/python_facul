'''
Escreva uma função com o nome pertence, que recebe como argumentos de entrada
uma tupla e um item e retorna True, se o item estiver armazenado na tupla, e
False, caso contrário.
'''


def pertence(tupla, item):
    if item in tupla:
        return True
    else:
        return False


'''
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''


def substituir(lista, velho, novo):
    for i in range(len(lista)):
        if lista[i] == velho:
            lista[i] = novo
    return(lista)


'''
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todas os índices em que o
item aparece na lista.
'''


def posicoes_lista(lista, item):
    lista_2 = []
    for i in range(len(lista)):
        if lista[i] == item:
            lista_2.append(i)
    return lista_2



'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
'''


def aprovados(alunos):
    alunos_aprovados = []
    for key in alunos:
        media = sum(alunos[key]) / len(alunos[key])
        if media >= 6:
            alunos_aprovados.append(key)
    return alunos_aprovados


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
'''


def incluir_nota(alunos, nome, nota):
    for key in alunos:
        if key == nome:
            alunos[key].append(nota)
    return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maiores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
maior nota de cada aluno.
'''


def maiores_notas(alunos):
    maiores_notas = {}
    for key in alunos:
        maior = max(alunos[key])
        maiores_notas[key] = maior
    return maiores_notas
