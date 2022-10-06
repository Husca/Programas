#Programa para preparação de solução alcoolica#
from datetime import datetime
from dateutil.relativedelta  import relativedelta

print("PREPARAÇÃO DE SOLUÇÃO ANTISSÉPTICA DE BASE ALCOÓLICA (SABA) - VALIDADE DE 3 MESES")

while True:
    volume = int(input("Insira o volume final pretendido de SABA (mL): "))

    if volume != 0:
        v_al = volume * 0.8333
        val = round(v_al,0)

        v_aox = volume * 0.0417
        vaox = round(v_aox,0)

        v_gli = volume * 0.0145
        vgl = round(v_gli,0)

        v_ap = volume * 0.1105
        vap = round(v_ap,0)

        print(f"É necessário adicionar {val} mL de Álcool 96º.")
        print(f"É necessário adicionar {vaox} mL de Água Oxigenada 10 volumes.")
        print(f"É necessário adicionar {vgl} mL de Glicerina.")
        print(f"É necessário adicionar {vap} mL de Água Purificada.\n")

        date_after_month = datetime.today() + relativedelta(months=3)
        print('Hoje: ', datetime.today().strftime('%d/%m/%Y'))
        print('Válido até:', date_after_month.strftime('%d/%m/%Y'))
        print("\n")

    else:
        print("Programa terminado!")
        break
