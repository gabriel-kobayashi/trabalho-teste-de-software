from validacoes import (
    validar_login,
    validar_contato
)


def test_login_sucesso():

    resultado = validar_login(
        "admin@gmail.com",
        "123123"
    )

    assert resultado == "Login realizado"


def test_login_invalido():

    resultado = validar_login(
        "teste@gmail.com",
        "123456"
    )

    assert resultado == "Login inválido"


def test_login_vazio():

    resultado = validar_login(
        "",
        ""
    )

    assert resultado == "Campos obrigatórios"


def test_contato_sucesso():

    resultado = validar_contato(
        "Gabriel",
        "gabriel@gmail.com",
        "Olá"
    )

    assert resultado == "Mensagem enviada"


def test_contato_vazio():

    resultado = validar_contato(
        "",
        "",
        ""
    )

    assert resultado == "Preencha todos os campos"