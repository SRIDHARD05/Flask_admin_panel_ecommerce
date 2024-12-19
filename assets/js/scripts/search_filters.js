$(document).ready(function () {
    let starting_id = "";
    let ending_id = "";
    // TODO: Also load the starting id and ending id when the user uses search filters

    $(document).keydown(function (event) {
        if (event.key === "ArrowUp" || event.key === "ArrowDown") {
            console.log("Arrow key pressed!");

            let new_starting_id = "new_starting_value";
            let new_ending_id = "new_ending_value";

            starting_id = new_starting_id;
            ending_id = new_ending_id;

            $.ajax({
                url: "/search_filters/load_data",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({
                    "starting_id": starting_id,
                    "ending_id": ending_id
                }),
                success: function (response) {
                    $("#load_assets_container").append(response['template']);
                    $('.product-uuid').click(function () {
                        var productUuid = $(this).data('id');
                        console.log('Product UUID:', productUuid);
                    });
                },
                error: function (xhr, status, error) {
                    console.error("Error:", error);
                }
            });
        }
    });

    $("#load_data_assets").click(function () {
        let new_starting_id = "new_starting_value";
        let new_ending_id = "new_ending_value";

        starting_id = new_starting_id;
        ending_id = new_ending_id;

        $.ajax({
            url: "/search_filters/load_data",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                "starting_id": starting_id,
                "ending_id": ending_id
            }),
            success: function (response) {
                $("#load_assets_container").append(response['template']);
                // console.log(response['template']);
                $('.product-uuid').on('click', function () {
                    var productUuid = $(this).data('id');
                    console.log('Product UUID: ' + productUuid);
                });
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
});


$(document).ready(function () {
    $('.product-uuid').click(function () {
        var productUuid = $(this).data('id');
        console.log('Product UUID:', productUuid);
    });
});


