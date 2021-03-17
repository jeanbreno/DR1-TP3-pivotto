def vencedor():
    nota_vencedor = -1
    for qtd in range(1,6):
        participante = input(f"Informe o nome do {qtd}º participante: ")
        nota = float(input(f"Informe a nota do {qtd}º participante: "))
        while nota < 0 or nota > 10:
            nota = float(input(f"Valor inválido! Informe a nota do {qtd}º participante novamente: "))
        if nota > nota_vencedor:
            nome_vencedor = participante
            nota_vencedor = nota
    print (f"O vencedor foi o(a) {nome_vencedor}, com a nota {nota_vencedor} !")

vencedor()
