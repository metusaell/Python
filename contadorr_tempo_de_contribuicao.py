
from datetime import datetime, timedelta

data_format = "%d/%m/%Y"

resultado = timedelta()

while True:
    try:
        option = int(input("""
Escolha sua opção:
1 - para incluir uma data
2 - para ver o resultado
0 - para encerrar
Digite: """))
        try:
            if option == 1:
                data_inicial = input("Digite a data inicial no formato de dd/mm/aaaa: ")
                data_inicial = datetime.strptime(data_inicial, data_format)

                data_final = input("Digite a data final no formato de dd/mm/aaaa: ")
                data_final = datetime.strptime(data_final, data_format)
                
                diferenca = data_final - data_inicial
                resultado += diferenca
            
            elif option == 2:
                anos = (resultado.total_seconds())/(365.25 * 24 * 3600)
                anos_int = int(anos)
                dias = (anos - anos_int) * 365.25
                print(f"Soma do tempo de contribuião: {anos:.0f} ano(s) e {dias:.0f} dias")

            elif option == 0:
                break
        except:
            print("Formato de data inválido, preencha de nesse padrão -> dd/mm/aaaa")
            continue
    except ValueError:
        option = input("""
Opção inválida.
1 - inserir data
0 - para sair
Digite: """)
        continue
    


    
    