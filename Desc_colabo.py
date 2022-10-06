# Pograma desconto
print("SABER O VALOR DO DESCONTO PARA PRODUTOS OU VENDAS\n")
while True:
    try:
        pr = float(input("Insira o valor do produto/venda: "))

        if pr != 0:
            IVA = float(input("Insira o valor do IVA: "))/100
            ML = float(input("Insira o valor da margem de lucro: "))/100

            # Formulas de calculo para saber desconto
            prsiva = pr - pr*IVA
            pcsiva = prsiva - prsiva*ML
            pciva = pcsiva + pcsiva*IVA

            Pcusto = round(pciva, 2)
            print(f"O preço de custo com IVA a {IVA*100}% é de {Pcusto}€.")

            Desco = pr - pciva
            fdesco = round(Desco, 2)
            print(f"\nO valor do desconto é de {fdesco}€.\n")
        else:
            print("Programa terminado!")
            break

    except:
        print("Erro! O valor inserido tem de ser numérico!\n")
        continue
