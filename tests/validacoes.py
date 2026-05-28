def validar_login(email, senha):

    if email == "" or senha == "":
        return "Campos obrigatórios"

    if (
        email == "admin@gmail.com"
        and
        senha == "123123"
    ):
        return "Login realizado"

    return "Login inválido"

def validar_contato(nome, email, mensagem):

    if nome == "" or email == "" or mensagem == "":
        return "Preencha todos os campos"

    return "Mensagem enviada"