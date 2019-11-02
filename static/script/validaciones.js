
function limitar(e, contenido, caracteres) {
    var unicode = e.keyCode ? e.keyCode : e.charCode;

    if (unicode == 8 || unicode == 46 || unicode == 13 || unicode == 9 || unicode == 37 || unicode == 39 || unicode == 38 || unicode == 40)
        return true;

    if (contenido.length >= caracteres) {
        return false;
    }
    return true;
}

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46)) {
        let text = $(".hijo").text();
        text = encodeURIComponent(text);
        var arreglo_ser;
        var lista;

        /*Corrección de mayusculas, minusculas y números*/

        $.ajax({
            url: "/validacion_minusculas_mayusculas/" + text + "/"
        }).done(function(res) {
            var arreglo_pal = res.lista;
            lista = arreglo_pal;
        });

        /*Corrección de signos de puntuación*/

        $.ajax({
            url: "/validacion_signos/" + text + "/"
        }).done(function(res) {
            var cadena = "";
            var n_errores = 0;
            var id_pal = 0;
            var ctrl_err = 0;
            var contador = 0;
            var aux_arreglo_ser = [];
            arreglo_ser = res.aerr;
            console.log("Palabras");
            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i]);
            }
            console.log("Arreglo de errores de signo");
            for (let i = 0; i < arreglo_ser.length; i++) {
                console.log(arreglo_ser[i]);
                if (arreglo_ser[i] == " ") {
                    console.log("Espacio");
                }
            }

            console.log("------");
            for (let i = 0; i < (lista.length - 1); i++) {


                if ((i % 3) == 1) {
                    let color;
                    let mal_bien;
                    let sugerencias;
                    let caracter, correcto, tipo_err;

                    if (lista[i] == true) {
                        color = "color: black;";
                        mal_bien = "palabra-buena";
                        caracter = lista[i - 1];
                        correcto = lista[i];
                        tipo_err = lista[i + 1];
                        sugerencias = "buscar(this);";
                    } else if (lista[i] == false) {
                        color = "color: rgb(254, 0, 0);";
                        mal_bien = "palabra-mala";
                        n_errores++;
                        sugerencias = "sugerencias(this);";
                        caracter = lista[i - 1];
                        correcto = lista[i];
                        tipo_err = lista[i + 1];
                    }

                    for (let j = 0; j < arreglo_ser.length; j++) {
                        if (contador == arreglo_ser[j]) {
                            color = "color:#439bff;";
                            mal_bien = "spanlabel";
                            n_errores++;
                            sugerencias = "sugerencias(this);";
                            caracter = arreglo_ser[0];
                            correcto = arreglo_ser[1];
                            tipo_err = arreglo_ser[2];
                        }
                    }

                    cadena = cadena +
                        "<span class=\"" + mal_bien + "\" onclick=\"" + sugerencias + "\" " +
                        "id=\"" + caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal + "\" " +
                        "style=\"" + color + " " +
                        "border-radius: 5px; " +
                        "font-family: 'Times New Roman', Times, serif; " +
                        "font-size: 18px; " +
                        "cursor: pointer;\">" + lista[i - 1] + "</span>";


                    id_pal++;
                    contador = contador + lista[i - 1].length;
                }
            }

            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena);
            document.getElementById("text-area-div").setAttribute("text-align", "none");

        });
    }
}