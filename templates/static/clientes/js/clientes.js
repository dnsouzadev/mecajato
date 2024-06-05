function add_carro() {
    const container = document.getElementById("form-carro");

    const html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'> </div> <div class='col-md'><input type='number' placeholder='Ano' class='form-control' name='ano'> </div></div>"


    container.innerHTML += html;
}


function exibir_form(tipo) {
    const add_cliente = document.getElementById("add_cliente");
    const att_cliente = document.getElementById("att_cliente");

    if(tipo == "1"){
        att_cliente.style.display = "none";
        add_cliente.style.display = "block";
    } else if(tipo == "2"){
        add_cliente.style.display = "none";
        att_cliente.style.display = "block";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const erroMessage = document.getElementById("erro-message");

    if (erroMessage) {
        setTimeout(function() {
            erroMessage.style.display = 'none';
        }, 2000);
    }
});

function dados_cliente() {
    const cliente = document.getElementById("cliente-select");
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = '/clientes/atualiza_cliente/';
    const id_cliente = cliente.value;

    const data = new FormData();
    data.append('id_cliente', id_cliente);

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
    },
    body: data
    })
    .then(response => response.json())
    .then(data => {
        const nome = document.getElementById("nome");
        const sobrenome = document.getElementById("sobrenome");
        const email = document.getElementById("email");
        const cpf = document.getElementById("cpf");

        form_att_cliente.style.display = "block";

        nome.value = data.nome;
        sobrenome.value = data.sobrenome;
        email.value = data.email;
        cpf.value = data.cpf;
    });
}
