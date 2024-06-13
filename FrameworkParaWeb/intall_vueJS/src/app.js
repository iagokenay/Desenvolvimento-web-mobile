const { createApp } = Vue

createApp({
  data() {
    return {
      message: 'Hello Vue! bem vindo !',
      nome: 'iago',
      idade: '25',
    }
  }
}).mount('#app');