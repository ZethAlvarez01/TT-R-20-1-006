function descargar() {

    var texto = $("#text-area-div").text();
    console.log("Descargar: " + texto);

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
    alert("¡El documento se descargo con éxito!");
}