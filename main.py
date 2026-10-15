from arquivo import *
from module import *

arq = "alunos.csv"
while True:
    cabecalho(["Adicionar Aluno", "Listar Alunos", "Atualizar Nota", "Remover Aluno", "Sair"])
    opc = leiaInt("Sua Opção: ")
    match opc:
        case 1:
            nome = validText("Nome Aluno(a): ")
            notas = validNota() # lista com notas
            ID = criarId(arq)
            info = add(arq, ID, nome, notas)
            if info:
                print(f"Aluno {nome} Adicionado!")
        case 2:
            dados = lerArquivo(arq)
            for linha in dados:
                print(linha)
        case 3:
            aluno = leiaInt("ID do aluno(a): ")
            bimestre = leiaInt("Deseja mudar nota de qual Bimestre: ")
            nota = leiaFloat("Nota do Aluno(a): ")
            Atualizar(arq, aluno, bimestre, nota)
        case 4:
            aluno = leiaInt("ID do Aluno(a): ")
            excluir(arq, aluno)
        case 5:
            print("Saindo...")
            break