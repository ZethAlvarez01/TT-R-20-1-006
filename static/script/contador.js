function contar() {
    let num = parseInt($("#text-area-div").text().length)
    document.getElementById("n-caracteres").innerHTML = "Número de caracteres: " + num
    document.getElementById("text-area-div").click();
}

function cambiar(elemento, nombre) {
    var spnlabel = document.getElementById(nombre);
    spnlabel.innerText = $(elemento).text();
    spnlabel.style.color = "black";
}

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
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var arreglo_pal = res.lista;
            lista = arreglo_pal;
        });

        /*Corrección de signos de puntuación*/

        $.ajax({
            url: "/background_process_test2/" + text + "/"
        }).done(function(res) {
            var cadena = "";
            var n_errores = 0;
            var id_pal = 0;
            var ctrl_err = 0;
            var contador = 0;
            arreglo_ser = res.aerr;

            for(let i=0;i<lista.length;i++){
                console.log(lista[i]);
            }

            for(let i=0;i<arreglo_ser.length;i++){
                console.log(arreglo_ser[i]);
            }

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