$(document).ready(function () {
    $('#shopifyAppForm').submit(function (e) {
        e.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            url: '/shopify//best-shoify-apps/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                if (response) {
                    console.log(response);
                }
            },
            error: function (xhr, status, error) {
                alert('Error saving app. Please try again.');
            }
        });
    });
});


// TODO: for Stores code
$(document).ready(function () {
    $('#shopifyStoresForm').on('submit', function (e) {
        e.preventDefault();
        var store_type = $('select[name=store_type]').val(); 
        const formData = {
            'stores-data': $('textarea[name="stores-data"]').val(),
            'store_type': store_type
        };

        console.log(store_type);
        $.ajax({
            url: '/stores/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                alert(response);
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.message || 'An error occurred while saving the stores.';
                alert(errorMsg);
            }
        });
    });
});

