const express = require('express')
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');


const SECRET_KEY = 'your-secret-key';
const PORTA = 3000
const app = express()
app.use(bodyParser.json());


app.get('/', (req, res) => {
    const mensagem = {
        message: 'OLA MUNDO',
        to: 'aqui'
    }
    
    res.send(mensagem)
})

app.get('/teste', (req, res) => {
    res.send('SOU TEST')
})

app.post('/login', (req, res) => {
    const {usuario, senha} = req.body

    if (usuario === 'usuario' && senha === 'senha') {
        const token = jwt.sign({ usuario, senha }, SECRET_KEY, { expiresIn: '1h' });
        res.json({ token: token })
    } else {
        res.status(401).json({ message: 'Login invalido' });
    }
})

app.listen(PORTA, () => {
  console.log(`Servidor rodando na porta http://localhost:${PORTA}`)
})
