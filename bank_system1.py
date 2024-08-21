import random

SENHA = 12
CONTA = 1
VALOR = random.randint(100,1000)


for n in range(0,3):
    print('Digite seu acesso:')
    conta = int(input('Conta:'))
    senha = int(input('senha:'))
    if senha ==  SENHA and conta  == CONTA:
       print('Acesso autorizado')
       print('''
            (1) deposito
            (2) saque
            (3) ver extrato  
       
       ''') 
       opcao = input('>>')   
       if  opcao == '1':
           valor_depositado = float(input('R$ >>'))
           VALOR =  VALOR + valor_depositado
           print('O valor foi depositado - R$', float(VALOR))
           for n in range(2):
               print('deseja voltar ao sistema? s/n')
               s_n = input('>>')
               if s_n == 's':
                  print('Até logo') 

       elif opcao == '2':
           valor_sacado = float(input('R$ >>'))
           if VALOR < valor_sacado:
              print('SALDO INSUFICIENTE')
              for n in range(2):
                  print('deseja voltar ao sistema? s/n')
                  s_n = input('>>')
                  if s_n == 's':
                     print('Até logo') 
           else:     
              VALOR =  VALOR - valor_sacado
              print('O valor foi sacado - R$', float(VALOR))  
              for n in range(2):
                  print('deseja voltar ao sistema? s/n')
                  s_n = input('>>')
                  if s_n == 's':
                     print('Até logo')                     
           
       elif opcao == '3':
            print('R$', float(VALOR)) 
       break

    else:
        print('Não autorizado')
print(f'Valor: {VALOR}')

n = input('clique enter sair')
