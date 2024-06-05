function add_carro() {
    const container = document.getElementById("form-carro");

    const html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa'> </div> <div class='col-md'><input type='number' placeholder='Ano' class='form-control' name='ano'> </div></div>"


    container.innerHTML += html;
}


function exibir_form(tipo) {
    const add_cliente = document.getElementById("add_cliente");
    const att_cliente = document.getElementById("att_cliente");

    if(tipo == "1"){
        console.log(tipo, add_cliente, att_cliente);
        att_cliente.style.display = "none";
        add_cliente.style.display = "block";
    } else if(tipo == "2"){
        console.log(tipo, add_cliente, att_cliente);
        add_cliente.style.display = "none";
        att_cliente.style.display = "block";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Seleciona o elemento de erro
    var erroMessage = document.getElementById("erro-message");

    // Se o elemento existir, define um timer para ocultá-lo após 5 segundos
    if (erroMessage) {
        setTimeout(function() {
            erroMessage.style.display = 'none';
        }, 2000);
    }
});
