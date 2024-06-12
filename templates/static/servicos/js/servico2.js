function alterarStatus(id) {
    console.log('vim')
    fetch('/servicos/alterar_status/' + id, {
        method: 'GET'
    }).then(function (result) {
        console.log(result)
        return result.json()
    }).then(function (data) {
        console.log(data)
        location.reload()
    })
}
