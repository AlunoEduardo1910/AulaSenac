import pytest
from app.produto import Produtos

@pytest.fixture
def produto_padrao():
    return Produtos('PC Gamer', 4000, 1000)

@pytest.mark.parametrize('quantidade_vendida,esperado', [(1,999),(100,900)])
def test_venda(quantidade_vendida,esperado,produto_padrao):
    produto_padrao.vender(quantidade_vendida)
    assert produto_padrao.estoque == esperado

#Concluiu em menos de um segundo a verificação de estoque
@pytest.mark.parametrize('novo_estoque,esperado', [(1,1),(1000,1000),(1000000,1000000)])
def test_adicionar_estoque(novo_estoque,esperado):
    produto = Produtos('Abacaxi', 10, 0)
    produto.adicionar_estoque(novo_estoque)
    assert produto.estoque == esperado