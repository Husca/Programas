 #quanto enconomico é a mota?
while True:
    try:
        kmper = float(input("Insira o número de km percorridos: "))
    except:
        print("valor não é o correto. Por favor repita")
        continue
    if kmper != 0:
        try:
            pr95 = float(input("Insira o valor do depósito: "))
            punit = float( input("Insira o preço por litro de combustível: "))
        except:
            print("valor não é o correto. Por favor repita")
            continue
    
        total = (pr95/kmper)*100
        tot = round(total,0)

        ptotal = tot * punit
        pt = round(ptotal, 0 )

        print(f"\nO consumo é de {tot} L por 100 km.")
        print(f"O seu veiculo gasta {pt} € por 100 km.\n")

    else:
        print("Programa terminado.")
        break

