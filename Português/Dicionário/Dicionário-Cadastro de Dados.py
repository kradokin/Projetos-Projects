from datetime import date
dados = {}
while True:
    dados['nome'] = input('Nome: ').title()
    idade = int(input('Ano de nascimento: '))
    dados['idade'] = date.today().year - idade
    dados['carteira'] = int(input('Carteira de trabalho: (0 se não tem) '))
    if dados['carteira'] == 0:
        break
    else:
        dados['contrato'] = int(input('Ano da contratação: '))
        dados['salario'] = float(input('Salário atual: R$'))
        dados['Aposentadoria'] = dados['contrato'] + 35
        if dados['salario'] > 0:
            break
    print()
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
