def test_example():
    assert True

def test_soma():
    resultado = 2 + 3
    assert resultado == 5

def test_string_contem():
    texto = "devops"
    assert "ops" in texto

def test_lista_vazia():
    lista = []
    assert len(lista) == 0

def test_dict_chave():
    d = {"nome": "Cristhian"}
    assert "nome" in d
