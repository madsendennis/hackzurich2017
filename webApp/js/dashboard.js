$(document).ready(function () {
    var getCameraImageUrl = "http://172.30.0.63:5000/captureImage";
    var sendImageToMagicBoxUrl = "http://localhost:5000/receiveImage";
    var imageBase64String = "";

    $("#takeImage").show();
    $("#contaminationReport").hide();
    $("#getContaminationReport").hide();

    // Get Grain Image content
    $("#getGrainImage").click(function () {
        alert("Getting Image!");
        $.ajax({
            url: getCameraImageUrl,
            success: function (data) {
                // Send grain image content to Magic Box
                imageBase64String = data;
                $("#getContaminationReport").show();
            },
            error: function () {

            },
            async: false
        });
    });
    
    $("#getContaminationReport").click(function () {
        $.ajax({
            url: sendImageToMagicBoxUrl,
            type: "POST",
            data: {
                imageString: imageBase64String
            },
            success: function (data) {
                $("#contaminationReport").show();                
            },
            error: function () {

            },
            async: false
        });
    });
});