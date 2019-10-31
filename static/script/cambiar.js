/*
Función que sistituye/cambia el error por la respuesta "correcta" dada en el cuadro de sugerencias.
Recibe: 
    -correccion: etiqueta con la sigerencia a cambiar.
    -tag_error: etiqueta donde se encientra el error a cambiar.

Regresa:
    Cambia el texto alojado en correccion y lo setea en el elemento tag_error.
*/

function cambiar(correccion, tag_error) {
    var spnlabel = document.getElementById(tag_error);
    spnlabel.innerText = $(correccion).text();
    spnlabel.style.color = "black";
}