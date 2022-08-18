from item import Item
from carrinho import Carrinho

item1 = Item('Carregador R$ ',
' Carrega celular ',
200.0)

item2 = Item(
valor=350.0,
nome='Stray R$ ',
descricao=' gato fodendo geral =)')

item3 = Item(
valor=350.0,
nome='Stray R$ ',
descricao=' gato fodendo geral =)')

carrinho = Carrinho()

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

# carrinho = Carrinho()

# print(item1 == item2)
# print(item1 == item1)
# print(item2 == item3)

print(item2 == carrinho)

carrinho.remover(item1)
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')