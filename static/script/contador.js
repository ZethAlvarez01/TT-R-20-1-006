function contadorCaracter(obj) {
    document.getElementById("n-caracteres").innerHTML = 'Número de caracteres: ' + obj.value.length;
}

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46)) {
        let text = document.getElementById('texto-area').value;
        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var lista = res.lista
            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i])
            }
        });
    }
}