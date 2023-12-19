# gerenciamento de estoque
# 1- Cadastro de produtos: É importante que o sistema permita o cadastramento de todos os produtos que serão armazenados no estoque, incluindo informações como nome, descrição, código de barras, fornecedor, preço, quantidade mínima e máxima, entre outros dados relevantes.

# 2- Controle de entrada e saída: O sistema deve permitir registrar as entradas e saídas de produtos do estoque de forma precisa. Isso inclui a atualização do saldo disponível, a identificação de responsáveis pela movimentação, a data e a hora das operações, além de possibilitar a geração de relatórios de movimentação.

# 3- Gestão de fornecedores: O sistema deve possibilitar o cadastro e o gerenciamento de informações sobre os fornecedores, como nome, endereço, telefone, e-mail, prazos de entrega, condições de pagamento, entre outros. Isso ajudará a manter um relacionamento eficiente com os fornecedores e facilitar a reposição dos produtos.

# 4- Controle de estoque mínimo e máximo: É importante que o sistema permita a definição de estoque mínimo e máximo para cada produto. Dessa forma, é possível estabelecer alertas automáticos quando um produto estiver próximo do estoque mínimo ou quando estiver acima do estoque máximo, evitando problemas de falta ou excesso de produtos.

# 5- Rastreabilidade: O sistema deve permitir rastrear a origem e o destino de cada produto no estoque. Isso é útil para identificar possíveis problemas, como produtos vencidos ou com defeito, e também para facilitar a auditoria interna.

# 6- Relatórios e análises: O sistema deve fornecer relatórios e análises que ajudem na tomada de decisões estratégicas. Isso inclui relatórios de vendas, giro de estoque, produtos mais vendidos, produtos menos vendidos, entre outros indicadores que auxiliem no planejamento e na gestão do estoque.

# 7- Integração com outros sistemas: É importante que o sistema de gerenciamento de estoque seja capaz de se integrar com outros sistemas da empresa, como o sistema de vendas, o sistema de compras e o sistema financeiro. Isso facilitará o fluxo de informações entre os diferentes setores da empresa e evitará retrabalhos.

# 8- Essas são algumas das principais características que um sistema de gerenciamento de estoque deve ter. É importante ressaltar que a escolha de um sistema adequado dependerá das necessidades específicas de cada empresa e do porte do negócio.

#====================================================================================================
from builtins import enumerate, float, input, int, len, print, property
from datetime import datetime as dt
import sqlite3

# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute()


# 1- Cadastro de produtos: É importante que o sistema permita o cadastramento de todos os produtos que serão armazenados no estoque, incluindo informações como nome, descrição, código de barras, fornecedor, preço, quantidade mínima e máxima, entre outros dados relevantes.

class Produtos:
     def __init__(self, nome, quantidade, preço, codigodb, fornecedor):
         self.nome = nome.title()
         self.quantidade = int(quantidade)
         self.preço = float(preço)
         self.codigodb = int(codigodb)
         self.fornecedor = fornecedor
         self.data = dt.now()

     def __str__(self): 
         return f'Nome: {self.nome}, Quantidade: {self.quantidade},  {self.preço}R$, Código de barras: {self.codigodb}, Fornecedor: {self.fornecedor}, data: {self.data.strftime("%Y-%m-%d %H:%M:%S")}'


# ---------------------------------------------------------------------
# Juntar (class)Produtos e (class)Estoque?
# Código com arquitetura harmonica ou funcional?
# Method? Como?


# ---------------------------------------------------------------------


# 2- Controle de entrada e saída: O sistema deve permitir registrar as entradas e saídas de produtos do estoque de forma precisa. Isso inclui a atualização do saldo disponível, a identificação de responsáveis pela movimentação, a data e a hora das operações, além de possibilitar a geração de relatórios de movimentação.
#====================================================================================================
class Estoque:
     
     def __init__(self, nome, prod):
        self.nome = nome.title()
        self.data = dt.now()
        self.prod = prod
        self.produtos = []
        self.saldo = 0

     def add_prod(self):
        produto = Produtos(
            nome= input('Nome do produto: '),
            quantidade= int(input('Quantidade de produtos: ')), 
            preço= float(input('Preço: ')), 
            codigodb= int(input('Código de barras: ')),
            fornecedor= input('Fornecedor: '),
        )
        self.produtos.append(produto)

        return produto
     
     def delete(self, produto):
        return f"produto {produto.nome} removido"

     def __getitem__(self, item):
        return self.prod[item]

     @property
     def listagem(self):
        return self.produtos
    
     def __len__(self):
        return len(self.prod)

lista = Estoque('Estoque', [])

while True:

    print('1- Novo Produto')
    print('2- Remover produto')
    print('3- Break')
    
    escolha = input(':')

    
    index = 0
    if escolha == '1':

        produto = lista.add_prod()
        if produto in lista:
            index =+ 1
            
    print('++++++++++++++++++++++++')
    for n in enumerate(lista):
        print(n)
    # for i in lista.listagem:
    #     print(i)
    print('-----------------------')

    if escolha == '2':
        n = input("Produto: ")
        lista.delete(n)

        
    if escolha == '3':
        break



# for indice,item in enumerate(produto):
#             indentificador = f"ID_{indice+1}"


        


