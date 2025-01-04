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

function loader_start(is_hide) {
    let hide = (is_hide === "yes") ? "yes" : (is_hide === "no" ? "no" : "default_value");

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


function show_password_toggle(input_toggle_id, icon_toggle_id, eye_icon_id) {
    var $passwordInput = $(input_toggle_id);
    var $toggleButton = $(icon_toggle_id);
    var $eyeIcon = $(eye_icon_id);

    $toggleButton.on('click', function () {
        if ($passwordInput.attr('type') === 'password') {
            $passwordInput.attr('type', 'text');
            $eyeIcon.removeClass('fa-eye').addClass('fa-eye-slash');
        } else {
            $passwordInput.attr('type', 'password');
            $eyeIcon.removeClass('fa-eye-slash').addClass('fa-eye');
        }
    });
}

function validatePassword(password) {
    const regexLength = /.{8,}/;
    const regexUpperCase = /[A-Z]/;
    const regexLowerCase = /[a-z]/;
    const regexNumber = /\d/;
    const regexSpecialChar = /[!@#$%^&*(),.?":{}|<>]/;

    const isLengthValid = regexLength.test(password);
    const hasUpperCase = regexUpperCase.test(password);
    const hasLowerCase = regexLowerCase.test(password);
    const hasNumber = regexNumber.test(password);
    const hasSpecialChar = regexSpecialChar.test(password);

    if (isLengthValid) {
        $('#minLength').html('<i class="fas fa-check text-success"></i> Minimum 8 characters');
    } else {
        $('#minLength').html('<i class="fas fa-times text-danger"></i> Minimum 8 characters');
    }

    if (hasUpperCase) {
        $('#uppercase').html('<i class="fas fa-check text-success"></i> At least one uppercase letter');
    } else {
        $('#uppercase').html('<i class="fas fa-times text-danger"></i> At least one uppercase letter');
    }

    if (hasLowerCase) {
        $('#lowercase').html('<i class="fas fa-check text-success"></i> At least one lowercase letter');
    } else {
        $('#lowercase').html('<i class="fas fa-times text-danger"></i> At least one lowercase letter');
    }

    if (hasSpecialChar) {
        $('#symbol').html('<i class="fas fa-check text-success"></i> At least one symbol (@$!%*?&)');
    } else {
        $('#symbol').html('<i class="fas fa-times text-danger"></i> At least one symbol (@$!%*?&)');
    }

    if (isLengthValid && hasUpperCase && hasLowerCase && hasNumber && hasSpecialChar) {
        return $('#password-signup-password').val()
    } else {
        console.log("Please enter the valid password");
    }
}

function checkPasswordMatch(password, repeatPassword) {
    $(".password-on-equal").empty();

    if (password === repeatPassword && repeatPassword !== '') {
        const template = `
            <div class="valid-message" style="color: green;">
                <i class="fas fa-check-circle"></i> Passwords match completely.
            </div>`;
        $(".password-on-equal").append(template);

        setTimeout(function () {
            $(".password-on-equal").empty();
        }, 1500);

    } else if (repeatPassword === '') {
        const template = `
            <div class="info-message" style="color: orange;">
                <i class="fas fa-info-circle"></i> Repeat password is empty.
            </div>`;
        $(".password-on-equal").append(template);
    } else {
        const template = `
            <div class="invalid-message" style="color: red;">
                <i class="fas fa-times-circle"></i> Passwords do not match.
            </div>`;
        $(".password-on-equal").append(template);
    }
}

$(document).ready(function () {
    show_password_toggle('#password-signin-password', '.toggle-signin-password', '.signin-password-eye-icon');
    show_password_toggle('#password-signup-password', '.toggle-signup-password', '.password-eye-icon');
    show_password_toggle('#password-signup-repassword', '.toggle-signup-repassword', '.repeat-password-eye-icon');

    let current_password = '';
    $('#password-signup-password').on('input', function () {
        const userInput = $(this).val();
        $(".password-on-validations").empty();
        let template = `
            <div class="form-group">
                <ul>
                    <li id="minLength"><i class="fas fa-times text-danger"></i> Minimum 8 characters</li>
                    <li id="uppercase"><i class="fas fa-times text-danger"></i> At least one uppercase letter</li>
                    <li id="lowercase"><i class="fas fa-times text-danger"></i> At least one lowercase letter</li>
                    <li id="symbol"><i class="fas fa-times text-danger"></i> At least one symbol (@$!%*?&)</li>
                </ul>
            </div>`;
        $(".password-on-validations").append(template);
        validatePassword(userInput);
        current_password = userInput;
    });
    $('#password-signup-repassword').on('input', function () {
        $(".password-on-validations").remove();
        const repeatPassword = $(this).val();
        checkPasswordMatch(current_password, repeatPassword);
    });
});
