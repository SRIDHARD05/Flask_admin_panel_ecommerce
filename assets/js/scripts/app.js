$(document).ready(function () {
    var current_path = window.location.pathname;

    function appendBreadcrumb(breadcrumbHtml) {
        $('.breadcrumb-design').append(breadcrumbHtml);
    }

    if (current_path === '/dashboard/') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">/ Dashboard</li>
        </ol>`;
        appendBreadcrumb(template);
    }
    else if (current_path === '/test') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">/ Test Page</li>
        </ol>`;
        appendBreadcrumb(template);
    }
    else if (current_path === '/pricing/') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/dashboard">Dashboard</a></li>
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">Pricing</li>
        </ol>`;
        appendBreadcrumb(template);
    }
    else if (current_path === '/saved_posts/') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/dashboard">Dashboard</a></li>
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">Saved Pages</li>
        </ol>`;
        appendBreadcrumb(template);
    }
    else if (current_path === '/credits/') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/dashboard">Dashboard</a></li>
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">Credits</li>
        </ol>`;
        appendBreadcrumb(template);
    }
    else if (current_path.match(/^\/products\/([^\/]+)\/([^\/]+)\/show/)) {
        // TODO: For Product Page get the Product Name from the URL and convert name url into product name append the data to brudcrumb
        // TODO: /products/product_name/show 
        // var regex = /^\/products\/([^\/]+)\/([^\/]+)\/show/;
        // var match = current_path.match(regex);
        // if (match && match.length > 2) {
        //     var product_id = match[1];
        //     var product_name = decodeURIComponent(match[2]);

        //     var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
        //         <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/dashboard">Dashboard</a></li>
        //         <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/products">Products</a></li>
        //         <li class="breadcrumb-item text-sm text-dark active" aria-current="page">${product_name}</li>
        //     </ol>`;
        //     appendBreadcrumb(template);
        // }
    }
});

function loader_start(response) {
    let hide = (response === "yes") ? "yes" : (response === "no" ? "no" : "default_value");

    $.ajax({
        url: "/loader",
        type: "GET",
        data: JSON.stringify({ 'hide': hide }),
        contentType: "application/json",
        success: function (response) {
            $(document.body).append(response);
            $("#loader-modal").modal('show');
            $('#loader-modal').on('show.bs.modal', function () {
                $(this).removeAttr('inert');
            });

            if (hide === "yes") {
                $('#loader-modal').modal({
                    backdrop: 'static',
                    keyboard: false
                });

                $('#loader-modal').on('click', function (e) {
                    if ($(e.target).is('#loader-modal')) {
                        $('#loader-modal').modal('hide');
                        $("#loader-modal").remove();
                    }
                });
            } else {

                $('#loader-modal').modal({
                    backdrop: true,
                    keyboard: true
                });
            }
        },
        error: function (xhr, status, error) {
            alert(error);
        }
    });

    $('#loader-modal').on('hide.bs.modal', function (event) {
        const triggerElement = $(event.relatedTarget);
        if (!triggerElement.hasClass('close-modal-btn')) {
            event.preventDefault();
        }
    });
}

function loader_end() {
    $("#loader-modal").modal('hide');
    $('#loader-modal').on('hide.bs.modal', function () {
        $(this).attr('inert', 'true');
    });
    $("#loader-modal").on('hidden.bs.modal', function (e) {
        $("#loader-modal").remove();
    })
}

$(document).ready(function () {
    $("#test-btn").click(function () {
        loader_start('no')
        $.ajax({
            url: "/test/functions",
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                if (response['status'] === '200') {
                    loader_end()
                    console.log("success");
                }
            },
            error: function (xhr, status, error) {
                alert(error);
            }
        });
    });
});

// window.onbeforeunload = function () {
//     return "Are you sure you want to leave? Unsaved changes may be lost.";
// };

// TODO: add the Custom Buttons inside the Calender and also add the 
// $(function () {
//     $('button[id="datetimes"]').daterangepicker(
//         {
//             opens: 'left',
//         },
//         function (start, end, label) {
//             console.log(
//                 'New date and time range selected: ' +
//                 start.format('YYYY-MM-DD HH:mm:ss') +
//                 ' to ' +
//                 end.format('YYYY-MM-DD HH:mm:ss') +
//                 ' (predefined range: ' + label + ')'
//             );
//         }
//     );

//     $('button[id="datetimes"]').on('show.daterangepicker', function (event, picker) {
//         const customButtons = `
//             <div class="custom-buttons" style="display: flex; flex-direction: column; align-items: stretch; gap: 10px; margin-bottom: 10px;">
//                 <button class="btn btn-sm btn-secondary" id="clear-dates">Clear Dates</button>
//                 <button class="btn btn-sm btn-warning" id="quick-select">Quick Select</button>
//             </div>
//         `;

//         // Append custom buttons to the top of the ranges container
//         if (!$('.daterangepicker .custom-buttons').length) {
//             $('.daterangepicker .ranges').prepend(customButtons);

//             // Add event listeners to the custom buttons
//             $('#clear-dates').on('click', function () {
//                 picker.setStartDate(moment());
//                 picker.setEndDate(moment());
//                 picker.updateView();
//                 console.log('Dates cleared!');
//             });

//             $('#quick-select').on('click', function () {
//                 const start = moment().subtract(3, 'days');
//                 const end = moment();
//                 picker.setStartDate(start);
//                 picker.setEndDate(end);
//                 picker.updateView();
//                 console.log('Quick Select applied: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
//             });
//         }
//     });
// });

