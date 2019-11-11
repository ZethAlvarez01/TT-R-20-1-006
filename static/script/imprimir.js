function descargar() {

    var texto = $("#text-area-div").text();
    var html = $("#text-area-div").html();

    html = String(html);
    console.log("Imprimir: "+ String(html))
    //console.log("Descargar: " + texto);

    for(let i = 0;i < html.length; i++){
        html = html.replace("/","|");
    }


    var combo = document.getElementById("combo-opciones");
    var selected = combo.options[combo.selectedIndex].value;
    var opcion;
    if (selected == 'txt') {
        opcion = 0;
    } else {
        opcion = 1;
    }

    let res = encodeURIComponent(texto);

    url = "/return_file/" + res + "/" + opcion + "/" + html
    document.getElementById("download").setAttribute("href", url);
    alert("¡El documento se descargo con éxito!");
}