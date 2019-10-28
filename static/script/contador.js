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


function swap(myArr1, myArr2, myArr3, indexOne, indexTwo) {
    var tmpVal1 = myArr1[indexOne];
    myArr1[indexOne] = myArr1[indexTwo];
    myArr1[indexTwo] = tmpVal1;

    var tmpVal2 = myArr2[indexOne];
    myArr2[indexOne] = myArr2[indexTwo];
    myArr2[indexTwo] = tmpVal2;

    var tmpVal3 = myArr3[indexOne];
    myArr3[indexOne] = myArr3[indexTwo];
    myArr3[indexTwo] = tmpVal3;

    return {
        primero: myArr1,
        segundo: myArr2,
        tercero: myArr3
    };
}

function bubbleSort(myArr1, myArr2, myArr3) {
    var size = myArr1.length;

    for (var pass = 1; pass < size; pass++) {
        for (var left = 0; left < (size - pass); left++) {
            var right = left + 1;
            if (myArr1[left] > myArr1[right]) {
                swap(myArr1, myArr2, myArr3, left, right);
            }
        }
    }

    return {
        primero: myArr1,
        segundo: myArr2,
        tercero: myArr3
    };
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
            var n_errores = 0;

            for (let i = 0; i < lista.length - 3; i++) {
                console.log(lista[i]);


                if ((i % 3) == 1) {
                    if (lista[i] == false) {
                        let cadena_aux = "<span class=\"palabra-mala\" onclick=\"sugerencias(this);\" " +
                            "id=\"" + lista[i - 1] + "-" + lista[i] + "-" + lista[i + 1] + "-" + n_errores + "\" " +
                            "style=\"color:rgb(254,0,0); " +
                            "border-radius: 5px; " +
                            "font-family: 'Times New Roman', Times, serif; " +
                            "font-size: 18px; " +
                            "cursor: pointer;\">" + "</span>";

                        tamaños.push(cadena_aux.length);

                        cadena_rec = cadena_rec +
                            "<span class=\"palabra-mala\" onclick=\"sugerencias(this);\" " +
                            "id=\"" + lista[i - 1] + "-" + lista[i] + "-" + lista[i + 1] + "-" + n_errores + "\" " +
                            "style=\"color:rgb(254,0,0); " +
                            "border-radius: 5px; " +
                            "font-family: 'Times New Roman', Times, serif; " +
                            "font-size: 18px; " +
                            "cursor: pointer;\">" + lista[i - 1] + "</span>";

                        n_errores++;
                    } else {
                        cadena_rec = cadena_rec + lista[i - 1];
                    }
                }
            }
            cadena_rec = cadena_rec + "&nbsp";
            helado = cadena_rec;

            for (let i = 0; i < tamaños.length; i++) {
                console.log("-" + tamaños[i]);
            }
        });



        $.ajax({
            url: "/background_process_test2/" + text + "/"
        }).done(function(res) {

            var cadena_rec = helado;

            console.log("Cadena con estilos rojos: \n" + cadena_rec);
            //console.log("helado chido 3: " + cadena_rec.length);
            console.log("Arreglo de tamaños: ");
            for (let i = 0; i < tamaños.length; i++) {
                console.log("*" + tamaños[i]);
            }

            console.log("Arreglo de lista de signos mal: ");
            var lista = res.aerr;
            for (let i = 0; i < lista.length; i++) {
                console.log(lista[i]);
            }

            var listaC = [];
            var listaP = [];
            var listaE = [];

            for (let i = 0; i < lista.length; i++) {
                if ((i % 3) == 0) {
                    listaC.push(lista[i]);
                }
                if ((i % 3) == 1) {
                    listaP.push(lista[i]);
                }
                if ((i % 3) == 2) {
                    listaE.push(lista[i]);
                }
            }

            var val = bubbleSort(listaP, listaC, listaE);

            console.log("Arreglo de lista de signos mal ordenado: ");

            listaC = val.segundo;
            listaP = val.primero;
            listaE = val.tercero;

            var cadena = "";
            var aux = 0;
            var valor = 0;
            var aux_tam = 0;
            var flg = 0;
            var flg2 = 0;


            if (lista.length != 0) {
                for (let i = 0; i < cadena_rec.length; i++) {
                    if (i == listaP[aux]) {
                        if (cadena_rec[i] == listaC[aux]) {

                            let caracter;

                            if (listaC[aux] == '"') {
                                caracter = "3";
                            } else {
                                caracter = listaC[aux];
                            }

                            cadena = cadena +
                                "<span class=\"spanlabel\" onclick=\"sugerencias(this);\" " +
                                "id=\"" + caracter + "-" + listaP[aux] + "-" + listaE[aux] + "\" " +
                                "style=\"color:#439bff; " +
                                "border-radius: 5px; " +
                                "font-family: 'Times New Roman', Times, serif; " +
                                "font-size: 18px; " +
                                "cursor: pointer;\"'>" + listaC[aux] + "</span>";
                            flg = 1;
                            aux++;
                            aux_tam = 0;
                        } else {
                            for (let j = 0; j < listaP.length; j++) {
                                listaP[j] = listaP[j] + tamaños[aux_tam];
                            }
                            aux_tam++;
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

            //console.log(cadena);
            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena);
            document.getElementById("text-area-div").setAttribute("text-align", "none");
        });

        tamaños = [];

    }
}