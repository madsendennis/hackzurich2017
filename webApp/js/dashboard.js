$(document).ready(function () {
    var getCameraImageUrl = "http://172.30.0.63:5000/captureImage";
    
    $("#getGrainImage").show();
    $("#contaminationReport").hide();

    $("#getGrainImage").click(function () {
        alert("Getting Image!");
        $.ajax({
            url: getCameraImageUrl,
            success: function (data) {

            },
            error: function () {

            },
            async: false
          });
    });
});