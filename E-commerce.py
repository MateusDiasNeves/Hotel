print('Bem Vindo ao E-commerce')
print('---------' *10)
print("Cadastre-se:")
print('        ' *10)
input('Nome:'),input('Insira sua Data de nascimento')
login,senha=input('Insira seu Email:'),input('Crie uma Senha:')
dadosdelogin={
"login": login,
'senha':senha
}
print('---------' *10)
print("Por favor, faça seu login:")
print('        ' *10)
login1,senha1=input('Email:'),input('Senha:')
if login==login1 and senha==senha1:
    print('---------' *10)
    print('Bem Vindo ao E-commerce')
    print('---------' *10)
    produtos = ['Farinha', 'Açucar', 'Leite', 'Fermento', 'Ovo']
    precos = [1.50, 2.00, 3.20, 2.50, 5.00]
    carrinho = []
    total = 0
    print("Produtos disponíveis:")
    print("1. FARINHA  - R$ 1.50")
    print("2. AÇUCAR   - R$ 2.00")
    print("3. LEITE    - R$ 3.20")
    print("4. FERMENTO - R$ 2.50")
    print("5. OVO      - R$ 5.00")
    print('--------' *10)
    escolha1 = input("Escolha o número do produto que deseja adicionar ao carrinho")
    print('---------' *10)
    if escolha1 == '1':
        carrinho.append(produtos[0])
        total += precos[0]
    elif escolha1 == '2':
        carrinho.append(produtos[1])
        total += precos[1]
    elif escolha1 == '3':
        carrinho.append(produtos[2])
        total += precos[2]
    elif escolha1 == '4':
        carrinho.append(produtos[3])
        total += precos[3]
    elif escolha1 == '5':
        carrinho.append(produtos[4])
        total += precos[4]
    escolha2 = input("Escolha o número do produto que deseja adicionar ao carrinho")
    print('---------' *10)
    if escolha2 == '1':
        carrinho.append(produtos[0])
        total += precos[0]
    elif escolha2 == '2':
        carrinho.append(produtos[1])
        total += precos[1]
    elif escolha2 == '3':
        carrinho.append(produtos[2])
        total += precos[2]
    elif escolha2 == '4':
        carrinho.append(produtos[3])
        total += precos[3]
    elif escolha2 == '5':
        carrinho.append(produtos[4])
        total += precos[4]
    escolha3 = input("Escolha o número do produto que deseja adicionar ao carrinho")
    print('---------' *10)
    if escolha3 == '1':
        carrinho.append(produtos[0])
        total += precos[0]
    elif escolha3 == '2':
        carrinho.append(produtos[1])
        total += precos[1]
    elif escolha3 == '3':
        carrinho.append(produtos[2])
        total += precos[2]
    elif escolha3 == '4':
        carrinho.append(produtos[3])
        total += precos[3]
    elif escolha3 == '5':
        carrinho.append(produtos[4])
        total += precos[4]
    print('--------' *10)
    print("\nVocê comprou:")
    print('---------' *10)
    if len(carrinho) > 0:
        print(carrinho)
        print(f"Total: R$ {total:.2f}")
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
    else:
        print("Nenhum produto comprado.")