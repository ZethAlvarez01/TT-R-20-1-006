function sugerencias(elemento) {
    var cte = elemento.getAttribute('id');
    console.log("Sugerencias: "+cte);
    var lista = cte.split("-");
    let oog = 0;
    var tarjeta = document.getElementById("tarjeta-ortg");

    if (oog == 0) {

        tarjeta.style.visibility = "visible";

        $("#mala-buena2").css("visibility", "hidden");

        if (lista[1] == "false") {
            $("#linea").css("border", "2px solid rgba(250, 15, 78, 0.3)");
            $("#linea").css("border-radius", "5px");
            $("#linea").css("transition", "0.8s");
        } else {
            $("#linea").css("border", "2px solid rgba(52, 152, 219, 0.3)");
            $("#linea").css("border-radius", "5px");
            $("#linea").css("transition", "0.8s");
        }

        $("#tarjeta-ortg").css("background-color", "white");
        $("#tarjeta-ortg").css("transition", "0.8s");

        $("#mala-buena1").css("font-size", "12px");
        $("#mala-buena1").css("text-align", "center");
        $("#mala-buena1").css("padding", "2px 5px");
        $("#mala-buena1").css("cursor", "pointer");

        $("#mala-buena2").css("font-size", "12px");
        $("#mala-buena2").css("text-align", "center");
        $("#mala-buena2").css("padding", "2px 5px");
        $("#mala-buena2").css("cursor", "pointer");


        $("#mala-buena1").hover(function() {
            if (lista[1] == "false") {
                $("#mala-buena1").css("background", "rgba(250, 15, 78, 0.3)");
            } else {
                $("#mala-buena1").css("background", "rgba(52, 152, 219, 0.3)");
            }
            $("#mala-buena1").css("transition", "0.5s");
            $("#mala-buena1").css("padding", "2px 5px");
            $("#mala-buena1").css("border-radius", "5px");
        }, function() {
            $("#mala-buena1").css("background", "white");
        });


        $("#mala-buena2").hover(function() {
            if (lista[1] == "false") {
                $("#mala-buena2").css("background", "rgba(250, 15, 78, 0.3)");
            } else {
                $("#mala-buena2").css("background", "rgba(52, 152, 219, 0.3)");
            }
            $("#mala-buena2").css("transition", "0.5s");
            $("#mala-buena2").css("padding", "2px 5px");
            $("#mala-buena2").css("border-radius", "5px");
        }, function() {
            $("#mala-buena2").css("background", "white");

        });

        $("#tarjeta-ortg").hover(function() {
            $(this).css("background-color", "rgb(240, 242, 252)");
            $(this).css("transition", "0.8s");
            $(this).css("cursor", "pointer");

            if (lista[1] == "false") {
                $("#linea").css("border", "2px solid #fa0f4e");
                $("#linea").css("border-radius", "5px");
                $("#linea").css("transition", "0.8s");
            } else {
                $("#linea").css("border", "2px solid #3498DB");
                $("#linea").css("border-radius", "5px");
                $("#linea").css("transition", "0.8s");
            }


        }, function() {
            $(this).css("background-color", "white");
            $(this).css("transition", "0.8s");
            $(this).css("cursor", "pointer");

            if (lista[1] == "false") {
                $("#linea").css("border", "2px solid rgba(250, 15, 78, 0.3)");
                $("#linea").css("border-radius", "5px");
                $("#linea").css("transition", "0.8s");
            } else {
                $("#linea").css("border", "2px solid rgba(52, 152, 219, 0.3)");
                $("#linea").css("border-radius", "5px");
                $("#linea").css("transition", "0.8s");
            }
        });

        console.log(lista[0] + "  " + lista[1] + " " + lista[2]);


        if (lista[1] == "false") {

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
                $("#mala-buena2").css("visibility", "visible");

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
                $("#mala-buena2").css("visibility", "hidden");
                document.getElementById("mala-buena2").innerText = "  ";
                document.getElementById("mala-buena2").setAttribute("onclick",
                    "");


            } else if (lista[2] == '3') {
                document.getElementById("error").innerText = "La palabra contiene números.";
                var textsn = lista[0];
                textsn = textsn.replace(/[0-9]+/g, '');

                document.getElementById("mala-buena1").innerText = textsn;
                document.getElementById("mala-buena1").setAttribute("onclick",
                    "cambiar(this,'" + cte + "')");

                $("#mala-buena2").css("visibility", "hidden");
                document.getElementById("mala-buena2").innerText = "  ";
                document.getElementById("mala-buena2").setAttribute("onclick", "");
            }

        } else {

            document.getElementById("tipo-error").innerText = "Alerta de ortografía";

            let caracter;
            if (lista[0] == '3') {
                caracter = '"';
            } else {
                caracter = lista[0];
            }

            document.getElementById("mala-buena1").innerText = "Error de signo " + caracter;
            document.getElementById("mala-buena1").setAttribute("onclick", "");

            $("#mala-buena2").css("visibility", "hidden");
            document.getElementById("mala-buena2").innerText = "  ";
            document.getElementById("mala-buena2").setAttribute("onclick", "");

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
                document.getElementById("error").innerText = "El uso de las comillas \" \"";
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
                if (lista[0] == '3' || lista[0] == '3') {
                    document.getElementById("error").innerText = "El uso de las comillas \" \"";
                }
            } else if (lista[2] == '8') {
                if (lista[0] == '¿' || lista[0] == '?') {
                    if (lista[0] == '¿') {
                        document.getElementById("error").innerText = "No se cerró el signo \"" + lista[0] + "\"";
                    } else {
                        document.getElementById("error").innerText = "No se abrió el signo \"" + lista[0] + "\"";
                    }
                }
                if (lista[0] == '¡' || lista[0] == '!') {
                    if (lista[0] == '¡') {
                        document.getElementById("error").innerText = "No se cerró el signo \"" + lista[0] + "\"";
                    } else {
                        document.getElementById("error").innerText = "No se abrió el signo \"" + lista[0] + "\"";
                    }
                }
                if (lista[0] == '(' || lista[0] == ')') {
                    if (lista[0] == '(') {
                        document.getElementById("error").innerText = "No se cerró el signo \"" + lista[0] + "\"";
                    } else {
                        document.getElementById("error").innerText = "No se abrió el signo \"" + lista[0] + "\"";
                    }
                }
                if (lista[0] == '3' || lista[0] == '3') {
                    if (lista[0] == '3') {
                        document.getElementById("error").innerText = "No se cerró el signo \"";
                    } else {
                        document.getElementById("error").innerText = "No se abrió el signo \"";
                    }
                }
            }
        }




    } else {

    }


}