// Função Tradicional (Declaração de Função)
// function fun1() { }

// Função armazenada em uma variavel (Function Expression)
// const minhaFuncao = function () { }

// Função armazenada em um array
// const lista = [function (a,b) { return a+b }, fun1, minhaFuncao]
// console.log(lista[0](2,3))

// Função armazenada em um atributo de um objeto
// const obj = { }
// obj.acao = funtion () { return 'Ola Mundo' }
// console.log(obj.acao())

// Função como parametro de outra função
// function executa(fun) {
//     fun()
// }

// executa(function () { console.log('Olha eu aqui...') })

// Função pode retornar/conter outra função
// function falar(palavra1) {
//     return function (palavra2) {
//         console.log(palavra1 + palavra2)
//     }
// }

// const olaMundo = falar('Olá')
// olaMundo('Mundo')

// falar('Olá')('Mundo')


// function saudacao(nome) {
//     return "Olá, " + nome + "!";
// }

// let mensagem = saudacao("João");
// console.log(mensagem); // Saída: Olá, João!


// -------------------------------------------------------------------
// Parâmetros
// Os parâmetros são variáveis listadas na definição da função
// Os argumentos são os valores passados para a função quando ela é chamada.
// No exemplo da função saudacao, nome é um parâmetro da função saudacao, e "João" é o argumento passado para esse parâmetro
// Arguments
// Em JavaScript toda função tem um array interno que possui todos os argumentos que forem passados durante a sua execussão, mesmo que nenhum parametro tenha sido nomeado na sua assinatura.
// Este array é chamado de arguments, caso nenhum parametro seja passado na execussão, ele fica vazio.


// function somar() {
//     let soma = 0

//     for(i in arguments) {
//         soma += arguments[i]
//     }
//     return soma
// }

// console.log(somar())
// console.log(somar(1,2))
// console.log(somar(1.1, 2.2, 3.3))
// console.log(somar('olá', 'mundo'))
// console.log(somar(3, 4, 'ja deu'))

// Valores padrão para parâmetros
// Funções podem ter valores padrão (default) para seus parametros
// Em JavaScript, existem varias formas de se ter valores padrão


// function somar(a, b, c) {
//     a = a || 0  // valor que veio do parametro ou ZERO, se nenhum for passado
//     b = b || 0
//     c = c || 0

//     return a + b + c
// }

// console.log(somar())

// function somar(a, b, c) {
//     a = a != undefined ? a : 0  // verifica se o parametro a esta atribuido, ou seja, diferente de nulo ou undefined, se sim, ele recebe o valor de a, senao recebe o valor padrão ZERO
//     b = 1 in arguments ? b : 0  // verifica se o array arguments possui o indice 1, se sim, ele recebe o valor de b, senão recebe o valor padrão ZERO
//     c = isNaN(c) ? 0 : c  // verifica se o parametro c não é um valor numerico (NaN = Not a Number), se sim, ele recebe o valor padrão ZERO, senão recebe o valor de c

//     return a + b + c
// }

// Forma mais moderna e recomendada de se criar valores padrão
// function somar(a='a', b='b', c='c') {
//     return a + b + c
// }

// console.log(somar())

function soma(a, b) {
    console.log(`O valor de a é ${a}`)  // é executado
    return a + b;
    console.log(`O valor de b é ${b}`)  // não é executado
}

let resultado = soma(3, 5);
console.log(resultado); // Saída: 8

