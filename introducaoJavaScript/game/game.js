const para = document.querySelector("p")
para.addEventListener("click", atualizarNome);

function atualizarNome() {
    var nome = prompt("Insisra um novo nome");
    para.textContent = "jogador 1: " + nome;
    if (nome == null || nome == ""){
        para.textContent = "jogador !";
    } else {
        document.querySelector("h1").textContent = "bem vindo ao city zombie " + nome + "!!";
    }
}