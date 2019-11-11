function descargar() {

    var texto = $("#text-area-div").text();

    var Errores_rojos = $(".palabra-mala").map(function() {
        return $(this).text();
    }).get();

    console.log(Errores_rojos);

    var Errores_morados = $(".palabra-no-encontrada").map(function() {
        return $(this).text();
    }).get();

    console.log(Errores_morados);

    var Errores_azules = $(".spanlabel").map(function() {
        return $(this).text();
    }).get();

    console.log(Errores_azules);

    var Errores_rojosC = "|"
    var Errores_azulesC = "|"
    var Errores_moradosC = "|"

    for (let i = 0; i < Errores_rojos.length; i++) {
        Errores_rojosC = Errores_rojosC + Errores_rojos[i] + "|";
    }

    for (let i = 0; i < Errores_azules.length; i++) {
        Errores_azulesC = Errores_azulesC + Errores_azules[i] + "|";
    }

    for (let i = 0; i < Errores_morados.length; i++) {
        Errores_moradosC = Errores_moradosC + Errores_morados[i] + "|";
    }

    Errores_rojosC = encodeURIComponent(Errores_rojosC);
    Errores_azulesC = encodeURIComponent(Errores_azulesC);
    Errores_moradosC = encodeURIComponent(Errores_moradosC);

    var combo = document.getElementById("combo-opciones");
    var selected = combo.options[combo.selectedIndex].value;
    var opcion;
    if (selected == 'txt') {
        opcion = 0;
    } else {
        opcion = 1;
    }

    let res = encodeURIComponent(texto);

    url = "/return_file/" + res + "/" + opcion + "/" + Errores_rojosC + "/" + Errores_azulesC + "/" + Errores_moradosC
    document.getElementById("download").setAttribute("href", url);
    alert("¡El documento se descargo con éxito!");
}