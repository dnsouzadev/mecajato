function apagarServicoAdicional(id) {

    fetch('/servicos/apagar_servico_adicional/' + id, {
        method: 'GET'
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        location.reload()
    })
}
