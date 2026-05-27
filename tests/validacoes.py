def validar_login(email, senha):

    if email == "" or senha == "":
        return "Campos obrigatórios"

    if (
        email == "admin@email.com"
        and
        senha == "123456"
    ):
        return "Login realizado"

    return "Login inválido"