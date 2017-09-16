$(document).ready(function () {
    var getCameraImageUrl = "http://172.31.1.17:5000/captureImage";
    var sendImageToMagicBoxUrl = "http://localhost:5000/receiveImage";
    var imageBase64String;

    $("#takeImage").show();
    $("#contaminationReport").hide();
    $("#getContaminationReport").hide();

    // Get Grain Image content
    $("#getGrainImage").click(function () {

        $.ajax({
            url: getCameraImageUrl,
            type: "GET",
            dataType:"image/jpeg",
            success: function (data) {
                alert("response");
                // Send grain image content to Magic Box
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