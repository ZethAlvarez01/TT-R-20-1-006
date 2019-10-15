function contadorCaracter(obj) {
    var max = 100;
    document.getElementById("n-caracteres").innerHTML = 'Número de caracteres: ' + $("#" + obj).text().length;
    let texto = $("#" + obj).text();
    let aux = "";
    for (let i = 0; i < max; i++) {
        aux = aux + texto[i];
    }
    document.getElementById(obj).innerHTML = aux;
}

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46)) {
        let text = document.getElementById('texto-area').value;
        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var lista = res.lista
            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i]);
            }

        });
    }
}

function descargar() {
    var texto = document.getElementById("texto-area").value

    var combo = document.getElementById("combo-opciones");
    var selected = combo.options[combo.selectedIndex].value;
    var opcion;
    if (selected == 'txt') {
        opcion = 0;
    } else {
        opcion = 1;
    }

    texto = texto.replace(" ", "%20")
    texto = texto.replace("?", "%3F")
    texto = texto.replace("/", "%2F")

    let res = texto;

    url = "/return_file/" + res + "/" + opcion
    document.getElementById("download").setAttribute("href", url);

}