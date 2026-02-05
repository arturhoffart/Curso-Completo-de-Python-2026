#send mail with the purchase details (max 3 attempts )
# for confirmated purchase send 

compra_confirmada = True
dados_compra = 'Compra no valor de R$ 12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail.')
        break
    else:
        print('Falha na compra')