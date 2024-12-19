$(document).ready(function () {
    let starting_id = "";
    let ending_id = "";
    // TODO: Also load the starting id and ending id when the user uses search filters

    $(document).keydown(function (event) {
        if (event.key === "ArrowUp" || event.key === "ArrowDown") {
            // console.log("Arrow key pressed!");

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
                    $(document).on('click', '.product-uuid', function () {
                        var uuid = $(this).data('id');
                        let product_data = response.data.find(function (product) {
                            return product.product_uuid === uuid;
                        });
                        // console.log(product_data);
                        if (product_data) {
                            $.ajax({
                                url: "/search_filters/side_bar_by_user",
                                type: "POST",
                                contentType: "application/json",
                                data: JSON.stringify(product_data),
                                success: function (response) {
                                    $(document.body).append(response['template']);
                                    const offCanvas = $('#offcanvas-' + uuid);
                                    if (offCanvas.length) {
                                        offCanvas.offcanvas({
                                            backdrop: true,
                                            keyboard: true,
                                            scroll: false
                                        });

                                        offCanvas.offcanvas('show');
                                        let product_show_url = `/products/${product_data['title'].toLowerCase().replace(/\s+/g, '-').replace(/[^\w\-]+/g, '')}/${uuid}/show`;
                                        product_data['url'] = product_show_url;

                                        // console.log("Generated product URL:", product_show_url);

                                        $(`#know-more-product-btn-${uuid}`).click(function (e) {
                                            e.preventDefault();
                                            $.ajax({
                                                url: product_show_url,
                                                type: 'POST',
                                                contentType: 'application/json',
                                                data: JSON.stringify(product_data),
                                                success: function (response) {
                                                    console.log("Response received:", response);
                                                    window.open(product_show_url, "_blank");
                                                },
                                                error: function (error) {
                                                    alert(error);
                                                    // console.error("Error sending data:", error);
                                                }
                                            });
                                        });

                                    }
                                    offCanvas.on('hidden.bs.offcanvas', function () {
                                        offCanvas.remove();
                                    });
                                },
                                error: function (xhr, status, error) {
                                    alert(error);
                                    // console.error("Error:", error);
                                }
                            });
                        } else {
                            // console.log('Product not found!');
                        }
                    });
                },
                error: function (xhr, status, error) {
                    alert(error);
                    // console.error("Error:", error);
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
                console.log(response['template']);
                $('.product-uuid').on('click', function () {
                    var productUuid = $(this).data('id');
                    // console.log('Product UUID: ' + productUuid);
                });
            },
            error: function (xhr, status, error) {
                alert(error);
                // console.error("Error:", error);
            }
        });
    });
});


$(document).ready(function () {
    $('.product-uuid').click(function () {
        var productUuid = $(this).data('id');
        // console.log('Product UUID:', productUuid);
    });
});




