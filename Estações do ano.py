#entrada
mes = int(input('Informe o mês:'))
dia = int(input('Informe o dia:'))

#Processamento
if mes in (1, 2, 3):
    print('verao')
    if(mes == 3 and dia >= 20):
        print('outono')
elif mes in (4, 5, 6):
    print('outono')

elif mes in (7, 8, 9):
    print('inverno')

elif mes in (10, 11, 12):
    print('primavera')







