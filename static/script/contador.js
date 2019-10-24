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

function sugerencias(elemento) {
    var cte = elemento.getAttribute('id');
    var lista = cte.split("-");
    let oog = 0;
    var correcta;

    var tarjeta = document.getElementById("tarjeta-ortg");

    if (oog == 0) {

        tarjeta.style.visibility = "visible";

        $("#tarjeta-ortg").css("background-color", "white");
        $("#tarjeta-ortg").css("transition", "0.8s");

        $("#tarjeta-ortg").hover(function() {
            $(this).css("background-color", "#f4f6f6");
            $(this).css("transition", "0.8s");
            $(this).css("cursor", "pointer");
        }, function() {
            $(this).css("background-color", "white");
            $(this).css("transition", "0.8s");
            $(this).css("cursor", "pointer");
        });

        console.log(lista[0] + "  " + lista[1] + " " + lista[2]);


        if (lista[1] == "false") {
            $("#linea").css("border", "3px solid #fa0f4e");
            $("#linea").css("border-radius", "5px");

            document.getElementById("tipo-error").innerText = "Alerta de ortografía";
            document.getElementById("sugerencia").innerText = "Quizás quisiste decir: ";
            if (lista[2] == '1') {
                document.getElementById("error").innerText = "La palabra utiliza mal mayúsculas y minúsculas.";

                document.getElementById("mala-buena1").innerText = lista[0].toUpperCase();
                document.getElementById("mala-buena1").setAttribute("onclick",
                    "cambiar(this,'" + cte + "')");
                document.getElementById("mala-buena2").innerText = lista[0].toLowerCase();
                document.getElementById("mala-buena2").setAttribute("onclick",
                    "cambiar(this,'" + cte + "')");

            } else if (lista[2] == '2') {
                document.getElementById("error").innerText = "Primer caracter despues de un punto debe ser mayúscula.";
                var textoL = lista[0];
                var textoLV = "";
                for (let i = 0; i < textoL.length; i++) {
                    if (i == 0) {
                        textoLV = textoLV + textoL[0].toUpperCase();
                    } else {
                        textoLV = textoLV + textoL[i];
                    }
                }
                document.getElementById("mala-buena1").innerText = textoLV;
                document.getElementById("mala-buena1").setAttribute("onclick",
                    "cambiar(this,'" + cte + "')");
                document.getElementById("mala-buena2").innerText = "";
                document.getElementById("mala-buena2").setAttribute("onclick",
                    "");

            } else if (lista[2] == '3') {
                document.getElementById("error").innerText = "La palabra contiene números.";
                var textsn = lista[0];
                textsn = textsn.replace(/[0-9]+/g, '');

                document.getElementById("mala-buena1").innerText = textsn;
                document.getElementById("mala-buena1").setAttribute("onclick",
                    "cambiar(this,'" + cte + "')");
                document.getElementById("mala-buena2").innerText = "";
                document.getElementById("mala-buena2").setAttribute("onclick",
                    "");


            }

        } else {

            $("#linea").css("border", "3px solid #3498DB");
            $("#linea").css("border-radius", "5px");

            document.getElementById("tipo-error").innerText = "Alerta de ortografía";
            document.getElementById("mala-buena1").innerText = "Error de signo " + lista[0];
            document.getElementById("mala-buena1").setAttribute("onclick",
                "");
            document.getElementById("mala-buena2").innerText = "";
            document.getElementById("mala-buena2").setAttribute("onclick",
                "");

            document.getElementById("sugerencia").innerText = "El error esta en: ";
            if (lista[2] == '1') {
                document.getElementById("error").innerText = "El uso del punto \".\"";
            } else if (lista[2] == '2') {
                document.getElementById("error").innerText = "El uso de la coma \",\"";
            } else if (lista[2] == '3') {
                document.getElementById("error").innerText = "El uso del guión \"-\"";
            } else if (lista[2] == '4') {
                document.getElementById("error").innerText = "El uso de los dos puntos \":\"";
            } else if (lista[2] == '5') {
                document.getElementById("error").innerText = "El uso del punto y coma \".\"";
            } else if (lista[2] == '6') {
                document.getElementById("error").innerText = "El uso de las comillas \".\"";
            } else if (lista[2] == '7') {
                if (lista[0] == '¿' || lista[0] == '?') {
                    document.getElementById("error").innerText = "El uso de los \"¿ ?\"";
                }
                if (lista[0] == '¡' || lista[0] == '!') {
                    document.getElementById("error").innerText = "El uso de los \"¡ !\"";
                }
                if (lista[0] == '(' || lista[0] == ')') {
                    document.getElementById("error").innerText = "El uso de los \"( )\"";
                }
                if (lista[0] == '"' || lista[0] == '"') {
                    document.getElementById("error").innerText = "El uso de las comillas \" \"";
                }
            } else if (lista[2] == '8') {
                if (lista[0] == '¿' || lista[0] == '?') {
                    document.getElementById("error").innerText = "No se cerro el signo \"¿ ?\"";
                }
                if (lista[0] == '¡' || lista[0] == '!') {
                    document.getElementById("error").innerText = "No se cerro el signo  \"¡ !\"";
                }
                if (lista[0] == '(' || lista[0] == ')') {
                    document.getElementById("error").innerText = "No se cerro el signo  \"( )\"";
                }
                if (lista[0] == '"' || lista[0] == '"') {
                    document.getElementById("error").innerText = "No se cerro el signo  \" \"";
                }
            }
        }




    } else {

    }


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

var tamaños = [];

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46) || (e.keyCode == 13)) {
        let text = $(".hijo").text();
        //console.log(text);
        text = encodeURIComponent(text);
        //console.log(text);
        var helado = null;

        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var lista = res.lista;
            var cadena_rec = "";

            for (let i = 0; i < lista.length - 3; i++) {
                console.log(lista[i]);

                if ((i % 3) == 1) {
                    if (lista[i] == false) {
                        let cadena_aux = "<span class=\"palabra-mala\" onclick=\"sugerencias(this);\" " +
                            "id=\"" + lista[i - 1] + "-" + lista[i] + "-" + lista[i + 1] + "\" " +
                            //"id=\"" + "constante" + "\" " +
                            "style=\"color:rgb(254,0,0); " +
                            "border-radius: 5px; " +
                            "font-family: 'Times New Roman', Times, serif; " +
                            "font-size: 18px; " +
                            "cursor: pointer;\">" + "</span>";

                        tamaños.push(cadena_aux.length);

                        cadena_rec = cadena_rec +
                            "<span class=\"palabra-mala\" onclick=\"sugerencias(this);\" " +
                            "id=\"" + lista[i - 1] + "-" + lista[i] + "-" + lista[i + 1] + "\" " +
                            //"id=\"" + "constante" + "\" " +
                            "style=\"color:rgb(254,0,0); " +
                            "border-radius: 5px; " +
                            "font-family: 'Times New Roman', Times, serif; " +
                            "font-size: 18px; " +
                            "cursor: pointer;\">" + lista[i - 1] + "</span>";

                        //Palabra-Correcta-Tipo
                    } else {
                        cadena_rec = cadena_rec + lista[i - 1];
                    }
                }
            }
            cadena_rec = cadena_rec + "&nbsp";
            //console.log("cadena_rec: " + cadena_rec);
            helado = cadena_rec;

            for (let i = 0; i < tamaños.length; i++) {
                console.log("-" + tamaños[i]);
            }

            //console.log("helado: " + helado);
        });

        //console.log("helado_chido: " + helado);


        $.ajax({
            url: "/background_process_test2/" + text + "/"
        }).done(function(res) {

            var cadena_rec = helado;

            //console.log("helado chido 2: " + cadena_rec);
            //console.log("helado chido 3: " + cadena_rec.length);
            //console.log("Arreglo de tamaños: ");
            for (let i = 0; i < tamaños.length; i++) {
                //console.log("*" + tamaños[i]);
            }

            var lista = res.aerr;
            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i]);
            }
            var cadena = "";
            var aux = 0;
            var valor = 0;
            var aux_tam = 0;
            var flg = 0;

            if (lista.length != 0) {
                for (let i = 0; i < cadena_rec.length; i++) {
                    if (i == lista[aux + 1]) {
                        if (cadena_rec[i] == lista[aux]) {
                            cadena = cadena +
                                "<span class=\"spanlabel\" onclick=\"sugerencias(this);\" " +
                                "id=\"" + lista[aux] + "-" + lista[aux + 1] + "-" + lista[aux + 2] + "\" " +
                                "style=\"color:#439bff; " +
                                "border-radius: 5px; " +
                                "font-family: 'Times New Roman', Times, serif; " +
                                "font-size: 18px; " +
                                "cursor: pointer;\"'>" + lista[aux] + "</span>";
                            flg = 1;
                            if ((aux + 3) > lista.length) {
                                // nothing
                            } else {
                                aux = aux + 3;

                            }
                            valor = 0;
                            aux_tam = 0;

                        } else {
                            let e = 0;
                            //console.log(cadena_rec[(i + valor)] + " " + lista[aux]);
                            while (cadena_rec[(i + valor)] != lista[aux]) {
                                valor = valor + tamaños[aux_tam];
                                aux_tam++;
                                //console.log(e);
                                e++;
                                if (e > helado.length) {
                                    console.log("roto como pistache");
                                    break;
                                }
                            }
                            lista[aux + 1] = i + valor;
                        }
                    }
                    if (flg == 0) {
                        cadena = cadena + cadena_rec[i];
                    }
                    flg = 0;

                }
            } else {
                cadena = cadena_rec;
            }


            //////////////////////////////////
            //console.log(cadena);
            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena);
            document.getElementById("text-area-div").setAttribute("text-align", "none");
        });

        tamaños = [];

    }
}

function descargar() {

    var texto = document.getElementById("text-area-div").value

    var combo = document.getElementById("combo-opciones");
    var selected = combo.options[combo.selectedIndex].value;
    var opcion;
    if (selected == 'txt') {
        opcion = 0;
    } else {
        opcion = 1;
    }

    let res = encodeURIComponent(texto);

    url = "/return_file/" + res + "/" + opcion
    document.getElementById("download").setAttribute("href", url);

}