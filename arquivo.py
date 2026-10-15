import csv

def add(arq, ID, nome, notas):
    novo_aluno = (ID, nome, notas[0], notas[1], notas[2], notas[3])
    try:
        with open(arq, "a", newline="", encoding="utf-8") as a:
            dados = csv.writer(a)
            
            dados.writerow(novo_aluno)
        return True
    except Exception as erro:
        print(f"ERRO! {erro}")
        
def lerArquivo(arq):
    try:
        with open(arq, "r", newline="", encoding="utf-8") as a:
            dados = csv.DictReader(a, delimiter=",")
            
            return list(dados)
    except Exception as e:
        print(f"ERRO! {e}")
        
def  Atualizar(arq, aluno_id, bimestre, nota):
    dados = lerArquivo(arq)
    bi = "nota" + str(bimestre)
    for linha in dados:
        if linha["id"] == str(aluno_id):
            linha[bi] = str(nota)
    salvar(arq, dados)

def salvar(arq, novos_dados):
    try:
        with open(arq, "w", newline="", encoding="utf-8") as a:
            fieldnames = ["id", "nome", "nota1", "nota2", "nota3", "nota4"]
            dados = csv.DictWriter(a, fieldnames=fieldnames)
            dados.writeheader()
            
            dados.writerows(novos_dados)
    except Exception as e:
        print(f"ERRO! {e}")
        
def excluir(arq, id_aluno):
    dados = lerArquivo(arq)
    
    for linha in dados:
        if linha["id"] == str(id_aluno):
            dados.remove(linha)
    salvar(arq, dados)