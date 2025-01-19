$(document).ready(function () {
    $('#shopifyAppForm').submit(function (e) {
        e.preventDefault();

        // Serialize the form data
        var formData = $(this).serialize();

        // Make a POST request to 'shopify-apps/db/save'
        $.ajax({
            url: 'shopify-apps/db/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                alert('App saved successfully!');
            },
            error: function (xhr, status, error) {
                alert('Error saving app. Please try again.');
            }
        });
    });
});