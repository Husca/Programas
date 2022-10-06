# Pograma desconto
print("SABER O VALOR DO DESCONTO PARA PRODUTOS OU VENDAS\n")
while True:
    try:
        pr = float(input("Insira o valor do produto/venda: "))

        if pr != 0:
            pdesc = float(input("Insira o valor do desconto: "))
            desco = pr * (pdesc / 100)
            fdesc = round(desco, 2)
            print(f"O desconto é de {fdesc}.\n")
        else:
            print("Programa terminado!")
            break

    except:
        print("Erro! O valor tem de ser numérico!\n")
        continue
