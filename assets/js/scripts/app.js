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


// document.addEventListener('DOMContentLoaded', () => {
//     var dropdown = new Dropdown({
//         buttonSelector: '#my-drop-down',  
//         items: [
//             { name: 'Action', class: 'btn-primary', id: 'action1', href: 'https://youtube.com', data: { key: 'value1' } },
//             { name: 'Another Action', class: 'another-class', id: 'action2', href: '#', data: { key: 'value2' } },
//             { name: 'Something else here', class: '', id: 'action3', href: '#', data: { key: 'value3' } },
//         ],
//         onItemClick: function (item) {
//             console.log('Item clicked:', item.id, item.name, item.data);
//             alert(`You clicked on: ${item.name} (ID: ${item.id}) with data: ${JSON.stringify(item.data)}`);
//         }
//     });
// });

function loader_start() {
    $.ajax({
        url: "/loader",
        type: "GET",
        contentType: "application/json",
        success: function (response) {
            $(document.body).append(response);
            $("#loader-modal").modal('show');
            $('#loader-modal').on('show.bs.modal', function () {
                $(this).removeAttr('inert');
            });
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
        loader_start()
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
