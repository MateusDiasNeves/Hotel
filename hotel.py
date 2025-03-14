print(''' 
                   -------------------------------------------
                   |                                         |       
                   |         Bem Vindo ao Hotel.com!         |                   
                   |                                         |                                                      
                   -------------------------------------------

''')
print('''
      Cadastre-se:''')
print('        ' *10)
nome=input('''
    Nome:'''),
idade=input('''
    Insira Idade''')
login=input('''
    Insira seu Email:''')
senha=input('''
    Crie uma Senha:''')
cliente1={ 
'Nome' :nome,
'Idade':idade,     
'login':login,
'senha':senha
}
cliente2={ 
'Nome' :nome,
'Idade':idade,     
'login':login,
'senha':senha
}
cliente3={ 
'Nome' :nome,
'Idade':idade,     
'login':login,
'senha':senha
}
print('---------' *10)
print('        ' *10)
print('''  
                   -------------------------------------------
                   |                                         |       
                   |         Bem Vindo ao Hotel.com!         |                   
                   |                                         |                                                      
                   -------------------------------------------
                         Faça sua reserva agora mesmo!!
                          
''')
print('''
    Por favor, faça seu login:''')
tlogin=input('''
    Email:''')
tsenha=input('''
    Senha:''')
if login==tlogin and senha==tsenha:
   quartos = ['Simples', 'Duplo', 'Luxo']
   precos =  [100, 150, 250]
   total = 0
   print('---------' *10)
   print('     Escolha seu Quarto')
   print('---------' *10)
   print('''
         Escolha seu tipo de Quarto:
     -------------------------------------------
     |                                         |
     |         SIMPLES - R$ 100/dia            |
     |         DUPLO   - R$ 150/dia            |
     |         LUXO    - R$ 250/dia            |
     |                                         |
     -------------------------------------------
''')
   print('--------' *10)
   escolha1 = input('''Escolha Seu Quarto
(Escreva em Maiúsculo)
                    ''')
   print('---------' *10)
   if escolha1 == 'SIMPLES':
        total = precos[0]
   elif escolha1 == 'DUPLO':
        total = precos[1]
   elif escolha1 == 'LUXO':
        total = precos[2]
        
   print('Quantos dias você ira se hospedar?')
   dias = int(input())
   print('---------' *10)
   estadia=dias*total
   print('Total a se pagar:')
   print(estadia,'R$')
   print(f'''
    1 - PIX
    2 - CC
    3 - CD                    
    ''')
   forma_pag =  input('Digite a forma de pagamento')
   print('--------' *10)
  
   if forma_pag=='PIX':
            print('Chave PIX:21yuo2hu1h2u91y28y18n2y81y8ny8ony8o1s2yn82s182n7178s78')
            print('Pagamento efetuado com sucesso volte sempre!') 
   if forma_pag=='CD':
            input('Insira o CVV')
            print('Pagamento efetuado com sucesso volte sempre!') 
   if forma_pag=='CC':
            input('Insira o CVV')
            print('Pagamento efetuado com sucesso volte sempre!') 

   if forma_pag!='CC'and forma_pag!='CD' and forma_pag!='PIX':
            print('ERRO AO EFETUAR PAGAMENTO!')