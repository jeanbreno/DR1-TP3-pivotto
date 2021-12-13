#definindo funções
def verificar_situacao_eleitoral(idade):
    while idade < 0:
        print("Valor incorreto!")
        idade = int(input("Informe uma idade válida: "))
    if idade >= 0:
        if idade < 16:
            print("Não tem direito ao voto!")
        elif idade >= 16 and idade < 18:
            print("Voto facultativo!")
        elif idade >= 18 and idade < 70:
            print("Voto obrigatório!")
        if idade >= 70:
            print("Voto facultativo!")
            
#entrada de dados
qtd = int(input("Quantas consultas deseja realizar? "))
while qtd < 0:
    print("Valor incorreto!")
    qtd = int(input("Informe um valor válido: "))
if qtd == 0:
    print("Obrigado e até a próxima!")
    exit()
        
for indice in range(qtd):
    idade = int(input("Informe a sua idade: "))
    verificar_situacao_eleitoral(idade)#chamada da função
