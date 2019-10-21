function contar() {
    let num = parseInt($("#text-area-div").text().length)
    document.getElementById("n-caracteres").innerHTML = "Número de caracteres: " + num
    document.getElementById("text-area-div").click();
}

function limitar(e, contenido, caracteres) {
    var unicode = e.keyCode ? e.keyCode : e.charCode;

    if (unicode == 8 || unicode == 46 /*|| unicode == 13*/ || unicode == 9 || unicode == 37 || unicode == 39 || unicode == 38 || unicode == 40)
        return true;

    if (contenido.length >= caracteres) {
        return false;
    }
    return true;
}

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46) || (e.keyCode == 13)) {
        let text = $(".hijo").text();
        console.log(text);
        text = encodeURIComponent(text);
        console.log(text);

        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var lista = res.lista
            var cadena_rec = "";

            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i]);

                if ((i % 3) == 1) {
                    if (lista[i] == false) {
                        cadena_rec = cadena_rec +
                            "<span style=\"color:rgb(194,0,0); " +
                            "border-radius: 5px; " +
                            "font-family: 'Times New Roman', Times, serif; " +
                            "font-size: 18px; " +
                            "cursor: pointer;\">" + lista[i - 1] + "</span>&nbsp";
                    } else {
                        cadena_rec = cadena_rec + lista[i - 1] + "&nbsp";
                    }
                }
            }

            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena_rec);
            document.getElementById("text-area-div").setAttribute("text-align", "none");


        });
    }
}

function descargar() {
    var texto = document.getElementById("texto-area").value;

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
    texto = texto.replace("/", "//")

    let res = texto;

    url = "/return_file/" + res + "/" + opcion
    document.getElementById("download").setAttribute("href", url);

}