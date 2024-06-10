const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = 3000;
const SECRET_KEY = 'minha-chave-secreta';

app.use(bodyParser.json());

app.post('/login', (req, res) => {
  const { usuario, senha } = req.body;

  if (usuario === 'usuario' && senha === 'senha') {
    const token = jwt.sign({ usuario }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
  } else {
    res.status(401).json({ message: 'Usuario ou senha invalido'});
}
});

