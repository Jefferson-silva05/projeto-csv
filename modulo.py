import csv
def cabecalho(text):
    for n, v in enumerate(text):
        print(f"[ {n+1} ] {v}")
    print("-="*23)
    
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print("ERRO! Digite um valor Numérico!")
            
def validText(msg):  
    while True:
        nome = str(input(msg)).strip()
        if nome:
            return nome
        print("ERRO! nome nao pode estar em branco!")
        
def validNota():
    c = 0
    notas = list()
    while True:
        c += 1
        try:
            num = float(input(f"Nota do {c}° Bimestre: "))
            notas.append(num)
        except:
            print("ERRO! Digite apenas numeros")
        if c == 4:
            return notas
            
def criarId(arq):
    maior_id = 0
    try:
        with open(arq, "r", encoding="utf-8", newline="") as a:
            dados = csv.DictReader(a)
            
            for linha in dados:
                id_atual = int(linha["id"])
                if id_atual > maior_id:
                    maior_id = id_atual
        return maior_id + 1
    except Exception as e:
        print(f"ERRO! {e}")
        
def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except:
            print("ERRO! Digite um valor Numérico!")
     