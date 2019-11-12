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
    if ((e.keyCode == 32) || (e.keyCode == 190)) {
        let text = $(".hijo").text();
        //console.log("V1: "+text);

        //console.log("V2: "+text);
        text = encodeURIComponent(text);
        var arreglo_err_sig;
        var arreglo_pal_val_mym;
        var arreglo_dicc;

        /*Corrección de mayusculas, minusculas y números*/

        $.ajax({
            url: "/validacion_minusculas_mayusculas/" + text + "/"
        }).done(function(res) {
            var arreglo_pal = res.lista;
            arreglo_pal_val_mym = arreglo_pal;
        });

        /*Corrección de signos de puntuación*/

        $.ajax({
            url: "/validacion_signos/" + text + "/"
        }).done(function(res) {
            var arreglo_pal = res.aerr;
            arreglo_err_sig = arreglo_pal;
        });

        /*Validacion en el diccionario las palabras*/

        $.ajax({
            url: "/validar_palabra/" + text + "/"
        }).done(function(res) {
            var cadena = "";
            var n_errores = 0;
            var id_pal = 0;
            var contador = 0;

            arreglo_dicc = res.validar;

            for (let i = 0; i < arreglo_pal_val_mym.length; i++) {

                if ((i % 3) == 1) {
                    let color;
                    let mal_bien;
                    let sugerencias;
                    let caracter, correcto, tipo_err;
                    let palabra_id;

                    caracter = arreglo_pal_val_mym[i - 1];
                    correcto = arreglo_pal_val_mym[i];
                    tipo_err = arreglo_pal_val_mym[i + 1];
                    palabra_id = caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal;

                    if (arreglo_pal_val_mym[i] == true) {
                        color = "color: black;";
                        mal_bien = "palabra-buena";
                        caracter = arreglo_pal_val_mym[i - 1];
                        correcto = arreglo_pal_val_mym[i];
                        tipo_err = arreglo_pal_val_mym[i + 1];
                        palabra_id = caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal;
                        //sugerencias = "buscar('" + palabra_id + "');";
                        sugerencias = " ";
                    }

                    if (arreglo_dicc[i] == 0) {
                        color = "color: rgb(195, 0, 235);";
                        mal_bien = "palabra-no-encontrada";
                        n_errores++;
                        caracter = arreglo_pal_val_mym[i - 1];
                        correcto = arreglo_pal_val_mym[i];
                        tipo_err = arreglo_pal_val_mym[i + 1];
                        palabra_id = caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal;
                        sugerencias = "sugerencias(this,'" + palabra_id + "',0);";
                    }

                    if (arreglo_pal_val_mym[i] == false) {
                        color = "color: rgb(254, 0, 0);";
                        mal_bien = "palabra-mala";
                        n_errores++;
                        caracter = arreglo_pal_val_mym[i - 1];
                        correcto = arreglo_pal_val_mym[i];
                        tipo_err = arreglo_pal_val_mym[i + 1];
                        palabra_id = caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal;
                        sugerencias = "sugerencias(this,'" + palabra_id + "',0);";
                    }

                    for (let j = 0; j < arreglo_err_sig.length; j++) {
                        if ((j % 3) == 1) {
                            if (contador == arreglo_err_sig[j]) {
                                color = "color:#439bff;";
                                mal_bien = "spanlabel";
                                n_errores++;
                                if (arreglo_err_sig[j - 1] == '"') {
                                    caracter = "♥"
                                } else {
                                    caracter = arreglo_err_sig[j - 1];
                                }

                                correcto = arreglo_err_sig[j];
                                tipo_err = arreglo_err_sig[j + 1];
                                palabra_id = caracter + "-" + correcto + "-" + tipo_err + "-" + n_errores + "-" + id_pal;
                                sugerencias = "sugerencias(this,'" + palabra_id + "',0);";
                            }
                        }
                    }

                    cadena = cadena +
                        "<span class=\"" + mal_bien + "\" onclick=\"" + sugerencias + "\" " +
                        "id=\"" + palabra_id + "\" " +
                        "style=\"" + color + " " +
                        "border-radius: 5px; " +
                        "font-family: 'Times New Roman', Times, serif; " +
                        "font-size: 18px; " +
                        "cursor: pointer;\">" + arreglo_pal_val_mym[i - 1] + "</span>";


                    id_pal++;
                    contador = contador + arreglo_pal_val_mym[i - 1].length;
                }
            }



            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena);
            document.getElementById("text-area-div").setAttribute("text-align", "none");

        });


        // Verifica la escructura de las oraciones 

        $.ajax({
            url: "/oraciones_validar/" + text + "/"
        }).done(function(res) {
            var f_val = res.validar;
            console.log("Lo validado: " + f_val);
        });

    }
}