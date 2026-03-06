from modelos.aluno import Aluno

def cadastrar_aluno():
    while True:
        nome = input("Digite o nome do aluno: ")
        if nome.strip().replace(" ", "").isalpha():
            break
        else:
            print("O nome não pode ser vazio nem conter números.")
        

    while True:
        try:
            idade = int(input("Digite a idade do aluno: "))
            if idade >= 6:
                break
            else:
                print("Idade mínima de 6 anos.")
            
        except ValueError:
            print("Apenas números inteiros.")
        
    
    while True:
        try:
            saldo = float(input("Saldo do aluno: "))
            if saldo >= 0:
                break
            else:
                print("O saldo não pode ser negativo.")
            
        except ValueError:
            print("Apenas números decimais ou inteiros.")
        
    return Aluno(nome=nome, idade=idade, saldo=saldo)
