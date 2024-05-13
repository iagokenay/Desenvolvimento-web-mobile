const http = require('http');

const port = 2000;

const host = 'localhost';

const botao = "console.log('to no front')";

const resposta = `

<html lang="pt-br">
    <head>
        <title>Exemplo Client-Side</title>
    </head>
    <body>
        <button id="meuBotao">clique aqui</button>
        <script>${botao}</script>
    </body>
</html>`

const requestListener = function(req, res) {
    const {method, url } = req;
    console.log(url)
    console.log("chegou uma requisição")

    res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'});
    res.end(resposta);
    
}

const server = http.createServer();
server.on('request',requestListener)


server.listen(port, () =>{
    console.log(`Servidor rodando em http://${host}:${port}/`);

});