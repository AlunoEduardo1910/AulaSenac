import pytest
from app.cliente import Cliente


@pytest.fixture
def cliente_padrao():
    return Cliente("João", 30, True)

def test_pode_comprar(cliente_padrao):
    assert cliente_padrao.pode_comprar() is True


def test_desativar(cliente_padrao):
    cliente_padrao.desativar()
    assert cliente_padrao.ativo is False


def test_idade_invalida():
    cliente = Cliente("Ana", 25, True)
    with pytest.raises(ValueError) as e:
         cliente.atualizar_idade(-1)
    assert str(e.value) == "Idade inválida"

@pytest.mark.parametrize("idade,esperado", [(17, True), (18, True), (20, True),(80, True)])
def test_pode_comprar_param(idade, esperado):
    cliente = Cliente("Carlos", idade, True)
    assert cliente.pode_comprar() == esperado