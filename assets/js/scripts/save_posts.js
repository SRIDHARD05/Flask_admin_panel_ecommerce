$(document).ready(function () {
    $(".test-data-btn").on('click', function () {
        var product_id = $(".test-data-btn").data('key');
        var data = JSON.stringify({
            'product_id': product_id
        })
        // TODO: add the model to get the collection name to store the post 
        $.ajax({
            url: "/save/user_save",
            type: "POST",
            data: data,
            contentType: "application/json",
            success: function (response) {
                if (response['status'] === 200) {
                    alert("Success")
                }
            },
            error: function (xhr, status, error) {
                alert(error);
            }
        });
    })
})