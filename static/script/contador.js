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
        var arreglo;

        /*Corrección de mayusculas, minusculas y números*/

        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var arreglo_pal = res.lista;
            arreglo = arreglo_pal;
        });

        /*Corrección de signos de puntuación*/

        $.ajax({
            url: "/background_process_test2/" + text + "/"
        }).done(function(res) {
            arreglo_ser = res.aerr;
            console.log(arreglo);
            console.log(arreglo.length/3);
            console.log(arreglo_ser);
        });


    }
}