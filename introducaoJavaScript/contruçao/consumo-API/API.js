const apiurl = "http://jsobolaceholder.typicode.com/users/";

async function fetchUsers() {
    try{
        const response = awit fetch(apiUrl);

        if (!response.ok){
            throw new error("erro ao recuperar usuarios");
        }
        const user = awit response.json();
            
        console.log('usuarios:',users);
    } cath (erros) {
        console.error("erro:",error);
    }
}

fetchUsers();