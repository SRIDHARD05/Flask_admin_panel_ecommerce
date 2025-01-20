// // TODO: If this system is moved to production, enable all features to disable the developer tools.
// window.addEventListener('contextmenu', function (e) {
//     e.preventDefault();
// }, true);

// $(document).ready(function () {
//     let devToolsOpened = false;
//     let devToolsTimeout;
//     let countdownTimer;
//     let countdownValue = 10;

//     function detectDevTools() {
//         const threshold = 160;
//         const widthDiff = window.outerWidth - window.innerWidth;
//         const heightDiff = window.outerHeight - window.innerHeight;

//         if (widthDiff > threshold || heightDiff > threshold) {
//             if (!devToolsOpened) {
//                 devToolsOpened = true;
//                 $.ajax({
//                     url: "/dev_tools_loader",
//                     type: "GET",
//                     success: function (response) {
//                         $(document.body).append(response);
//                         console.log(response)
//                         $("#dev-tools-loader-modal").modal('show');

//                         $('#dev-tools-loader-modal').on('hidden.bs.modal', function () {
//                             $(this).remove();
//                         });
//                         $('#dev-tools-loader-modal').modal({
//                             backdrop: true,
//                             keyboard: true
//                         });
//                     },
//                     error: function (xhr, status, error) {
//                         alert(error);
//                     }
//                 });
//                 startTimer();
//             }
//         } else {
//             if (devToolsOpened) {
//                 clearTimeout(devToolsTimeout);
//                 devToolsOpened = false;
//                 $('#dev-tools-loader-modal').modal('hide');
//                 $('#dev-tools-loader-modal').on('hidden.bs.modal', function () {
//                     $(this).remove();
//                 });
//                 $('#dev-tools-loader-modal').modal({
//                     backdrop: true,
//                     keyboard: true
//                 });
//                 stopTimer();
//             }
//         }
//     }

//     function startTimer() {
//         countdownTimer = setInterval(function () {
//             countdownValue--;
//             $("#dev-tools-loader-modal .timer").text(`${countdownValue}s remaining`);
//             if (countdownValue <= 0) {
//                 clearInterval(countdownTimer);
//                 resetTimer();
//                 window.location.href = "/users/deauth";
//             }
//         }, 1000);
//     }

//     function stopTimer() {
//         clearInterval(countdownTimer);
//         resetTimer();
//         console.log("Timer stopped because dev tools were closed.");
//     }

//     function resetTimer() {
//         countdownValue = 10;
//         $("#dev-tools-loader-modal .timer").text(`${countdownValue}s remaining`);
//     }
//     setInterval(detectDevTools, 1000);
// });


$(document).ready(function () {
    function calculateAdvancedProfit() {
        const productCost = parseFloat($('#product-cost').val()) || 0;
        const advertisingCost = parseFloat($('#advertising-cost').val()) || 0;
        const shippingCost = parseFloat($('#shipping-cost').val()) || 0;
        const otherCost = parseFloat($('#other-cost').val()) || 0;

        const sellingPrice = parseFloat($('#selling-price').val()) || 0;
        const shippingRevenues = parseFloat($('#shipping-revenues').val()) || 0;
        const productDiscounts = parseFloat($('#product-discounts').val()) || 0;

        const totalCosts = productCost + advertisingCost + shippingCost + otherCost;
        const totalRevenues = sellingPrice + shippingRevenues - productDiscounts;

        const profit = totalRevenues - totalCosts;
        const profitMargin = totalRevenues > 0 ? ((profit / totalRevenues) * 100).toFixed(2) : 0;

        $('#total-costs').text(totalCosts.toFixed(2));
        $('#total-revenues').text(totalRevenues.toFixed(2));
        $('#profit').text(profit.toFixed(2));
        $('#profit-margin').text(profitMargin);
    }
    $('#profit-calculator-form input').on('input', calculateAdvancedProfit);

    function calculateProfit() {
        const productCost = parseFloat($('#product-cost').val()) || 0;
        const sellingPrice = parseFloat($('#selling-price').val()) || 0;

        const profit = sellingPrice - productCost;
        const profitMargin = sellingPrice > 0 ? ((profit / sellingPrice) * 100).toFixed(2) : 0;

        $('#profit').text(profit.toFixed(2));
        $('#profit-margin').text(profitMargin);
    }
    $('#product-cost, #selling-price').on('input', calculateProfit);


    $("#shopify-store-detection-submit").on('click', function () {
        $("#shopify-store-detection-submit").text('Detecting...');
        var store_url = $("input[name='shopify-store-detection-url']").val();

        if (store_url.trim() === "") {
            alert("Please enter a valid URL.");
            return;
        }

        $.ajax({
            url: "/tools/store/theme_detector",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ 'url': store_url }),
            success: function (response) {
                $("#shopify-store-detection-submit").text('Check Now');
                $("#shopify-theme-body").empty();
                if (response['status'] == 200) {
                    var theme_name = response['theme_name']
                    var theme_version = response['theme_version']
                    var template = `<ul class="list-unstyled">
                        <li><strong>Shopify Theme Name:</strong> <span class="text-success">${theme_name}</span></li>
                        <li><strong>Shopify Theme Version:</strong> <span class="text-success">${theme_version}</span></li>
                    </ul>`;
                    $("#shopify-theme-body").append(template);
                } else {
                    var template = `<div class="d-flex justify-content-start mt-2 text-danger">
                        ${store_url} is not built with Shopify
                    </div>`;
                    $("#shopify-theme-body").append(template);
                }
            },
            error: function (xhr, status, error) {
                alert("Error: " + error);
            }
        });
    });
});


