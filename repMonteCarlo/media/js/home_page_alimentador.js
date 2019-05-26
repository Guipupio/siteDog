$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

$("#alimentar-agora").click(function() {
    var currentURL = window.location.pathname.split("/")[1];
    $.ajax({
        method: "POST",
        url: "/" + currentURL + "/" + "sinal_alimentacao",
        data: { csrfmiddlewaretoken: csrf_token ,sinal_id: "1"},
        success: function(result) {
            $("#aviso-ultima-refeicao").text = "Última Refeição ocorreu às: " + result.data_sinal;
            console.log("Refeicao Realizada com Sucesso!");
        },
        error: function(result){
            console.log("Erro durante a requisicao!");
        }

    });
});
