function contar() {
    let num = parseInt($("#text-area-div").text().length)
    document.getElementById("n-caracteres").innerHTML = "Número de caracteres: " + num
    document.getElementById("text-area-div").click();
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

        $("#linea").css("border", "3px solid #3498DB");
        $("#linea").css("border-radius", "5px");


        document.getElementById("tipo-error").innerText = "Alerta de ortografía";
        document.getElementById("mala-buena").innerText = lista[0] + " --> " + correcta;
        document.getElementById("sugerencia").innerText = "La interpretacion correcta es...";
        if (lista[2] == '1') {
            document.getElementById("error").innerText = "La palabra utiliza mal mayúsculas y minúsculas.";
        } else if (lista[2] == '2') {
            document.getElementById("error").innerText = "Primer caracter despues de un punto debe ser mayúscula.";
        } else if (lista[2] == '3') {
            document.getElementById("error").innerText = "La palabra contiene números.";
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

function detecta(e) {
    if ((e.keyCode == 32) || (e.keyCode == 46) || (e.keyCode == 13)) {
        let text = $(".hijo").text();
        console.log(text);
        text = encodeURIComponent(text);
        console.log(text);

        $.ajax({
            url: "/background_process_test/" + text + "/"
        }).done(function(res) {
            var lista = res.lista;
            var cadena_rec = "";

            for (let i = 0; i < lista.length - 3; i++) {
                console.log(lista[i]);

                if ((i % 3) == 1) {
                    if (lista[i] == false) {
                        cadena_rec = cadena_rec +
                            "<span class=\"palabra-mala\" onclick=\"sugerencias(this);\"" +
                            "id='" + lista[i - 1] + "-" + lista[i] + "-" + lista[i + 1] + "'" +
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
            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena_rec);
            document.getElementById("text-area-div").setAttribute("text-align", "none");
        });

        $.ajax({
            url: "/background_process_test2/" + text + "/"
        }).done(function(res) {

            let text = $(".hijo").text();

            var lista2 = res.aerr;
            var cadena_rec2 = "";
            console.log(text);

            for (let i = 0; i < lista2.length; i++) {
                console.log(lista2[i]);
                for (let j = 0; j < text.length; j++) {
                    if ((i % 3) == 1) {
                        if (j == lista2[i]) {
                            cadena_rec2 = cadena_rec2 +
                                "<span class=\"palabra-mala\" " +
                                "id='" + lista2[i - 1] + "-" + lista2[i] + "-" + lista2[i + 1] + "'" +
                                "style=\"color:rgb(0,254,0); " +
                                "border-radius: 5px; " +
                                "font-family: 'Times New Roman', Times, serif; " +
                                "font-size: 18px; " +
                                "cursor: pointer;\">" + lista2[i - 1] + "</span>";
                        }
                    } else {
                        cadena_rec2 = cadena_rec2 + text[j];
                    }

                }
            }
            cadena_rec2 = cadena_rec2 + "&nbsp";
            document.getElementById("text-area-div").innerText = " ";
            document.execCommand("insertHTML", false, cadena_rec2);
            document.getElementById("text-area-div").setAttribute("text-align", "none");
        });

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