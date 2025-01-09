$(document).ready(function () {
    $(".product-save").on('click', function () {
        var product_id = $(".product-save").data('key');
        $.ajax({
            url: "/save/collection/show",
            type: "GET",
            success: function (response) {
                $(document.body).append(response);
                console.log(response)
                $("#user-save-collections-show").modal('show');

                $('#user-save-collections-show').on('hidden.bs.modal', function () {
                    $(this).remove();
                });

                $("#user-show-collection-submit").on('click', function () {
                    $("#user-save-collections-show").modal('hide');
                    var collection_id = $('input[name="collection"]:checked').data('id');
                    var data = JSON.stringify({
                        'collection_id': collection_id,
                        'product_id': product_id
                    })
                    console.log(data);
                    $.ajax({
                        url: "/save/posts/save",
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
                $("#user-show-collection-cancel").on('click', function () {
                    $("#user-save-collections-show").modal('hide');
                })

            },
            error: function (xhr, status, error) {
                alert(error);
            }
        });


    })
})

$(document).ready(function () {
    $('.user-save-collection-create').click(function () {
        $.ajax({
            url: "/save/collection/create/modal",
            type: "GET",
            success: function (response) {
                $("#user-save-collections-create").remove();

                $(document.body).append(response);
                $("#user-save-collections-create").modal('show');

                $('#user-save-collections-create').on('hidden.bs.modal', function () {
                    $(this).remove();
                });

                $('#submit-btn-user-collections').on('click', function () {
                    var collection_name = $('#user-collection-create').val().trim();

                    if (!collection_name) {
                        alert("Collection name cannot be empty!");
                        return;
                    }
                    $.ajax({
                        url: "/save/collection/create",
                        type: "POST",
                        data: JSON.stringify({ 'name': collection_name }),
                        contentType: "application/json",
                        success: function (response) {
                            if (response.status === 200) {
                                alert("Collection Created Successfully");
                                $("#user-save-collections-create").modal('hide');
                            } else {
                                console.log(response.message)

                            }
                        },
                        error: function (xhr, status, error) {
                            console.log(xhr.responseText);
                        }
                    });
                });
            },
            error: function (xhr, status, error) {
                alert("Error loading modal: " + xhr.responseText);
            }
        });
    });

    $(".clickable-card").on("click", function () { 
        var collection_name = $(this).data("key");
        $.ajax({
            url: `/save/posts/saved_post/${collection_name}`,  
            type: "GET",
            success: function (response) {
                window.location.href = `/save/posts/saved_post/${collection_name}`;  
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
            }
        });
    });
    
});


