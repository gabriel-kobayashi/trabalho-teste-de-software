function login() {
  const email = document.getElementById("email").value;

  const senha = document.getElementById("senha").value;

  if (email === "" || senha === "") {
    document.getElementById("resultadoLogin").innerText = "Campos obrigatórios";

    return;
  }

  if (email === "admin@email.com" && senha === "123456") {
    document.getElementById("resultadoLogin").innerText = "Login realizado";
  } else {
    document.getElementById("resultadoLogin").innerText = "Login inválido";
  }
}

function enviarMensagem() {
  const nome = document.getElementById("nome").value;

  const email = document.getElementById("emailContato").value;

  const mensagem = document.getElementById("mensagem").value;

  if (nome === "" || email === "" || mensagem === "") {
    document.getElementById("resultadoContato").innerText =
      "Preencha todos os campos";
  } else {
    document.getElementById("resultadoContato").innerText = "Mensagem enviada";
  }
}
