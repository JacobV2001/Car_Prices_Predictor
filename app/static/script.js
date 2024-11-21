$(document).ready(function() {
    // execute following when form is triggered
    $('#predict-form').submit(function(event) {
        event.preventDefault(); // stops page from refreshing

        // get form data into string
        var formData = $(this).serialize();

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.prediction) {
                    $('#prediction-result').html('<h3>' + response.prediction + '</h3>');
                } else {
                    $('#prediction-result').html('<h3>' + response.error + '</h3>');
                }
            },
            error: function() {
                $('#prediction-result').html('<h3>Error: Could not get a prediction!</h3>');
            }
        });
    });
});
