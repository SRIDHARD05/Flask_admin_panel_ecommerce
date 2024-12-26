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


// $(document).ready(function () {
//     $("#test-btn").click(function () {
//         loader_start('no')
//         $.ajax({
//             url: "/test/functions",
//             type: "GET",
//             contentType: "application/json",
//             success: function (response) {
//                 if (response['status'] === '200') {
//                     loader_end()
//                     console.log("success");
//                 }
//             },
//             error: function (xhr, status, error) {
//                 alert(error);
//             }
//         });
//     });
// });

// window.onbeforeunload = function () {
//     return "Are you sure you want to leave? Unsaved changes may be lost.";
// };

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',   
        events: [
            { title: 'Event 1', date: '2024-12-28' },
            { title: 'Event 2', date: '2024-12-29' }
        ]
    });

    // Render the calendar
    calendar.render();
});