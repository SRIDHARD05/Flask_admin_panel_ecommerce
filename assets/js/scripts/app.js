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
    else if (current_path === '/save/') {
        var template = `<ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
            <li class="breadcrumb-item text-sm"><a class="opacity-5 text-dark" href="/dashboard">Dashboard</a></li>
            <li class="breadcrumb-item text-sm text-dark active" aria-current="page">Saved Posts</li>
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

// TODO: Redesign and solve the DOM Hdi
// function loader_start(is_hide) {
//     let hide = (is_hide === "yes") ? "yes" : (is_hide === "no" ? "no" : "default_value");

//     $.ajax({
//         url: "/loader",  
//         type: "GET", 
//         data: JSON.stringify({ 'hide': hide }),
//         contentType: "application/json",
//         success: function (response) {
//             $(document.body).append(response);
//             $("#loader-modal").modal('show');

//             $('#loader-modal').on('show.bs.modal', function () {
//                 $(this).removeAttr('inert');
//             });

//             if (hide === "yes") {
//                 $('#loader-modal').modal({
//                     backdrop: 'static',
//                     keyboard: false
//                 });

//                 $('#loader-modal').on('click', function (e) {
//                     if ($(e.target).is('#loader-modal')) {
//                         $("#loader-modal").modal('hide');
//                     }
//                 });
//             } else {
//                 $('#loader-modal').modal({
//                     backdrop: true,
//                     keyboard: true
//                 });
//             }
//         },
//         error: function (xhr, status, error) {
//             alert('Error: ' + error);  
//         }
//     });
// }

// function loader_end() {
//     $("#loader-modal").modal('hide'); 
//     console.log("Loader is Hiding...");

//     $('#loader-modal').on('hide.bs.modal', function () {
//         $(this).attr('inert', 'true');
//     });

//     $("#loader-modal").on('hidden.bs.modal', function () {
//         $("#loader-modal").remove();  
//     });
// }
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

$(document).ready(function () {
    var loc = window.location.pathname;
    // TODO: Change the Tittle after the Completitoins of DB Connections
    if (loc === '/signup') {
        $("title").text('User SignUp Page');
    } else if (loc === '/signin') {
        $("title").text('User SignIn Page');
    } else if (loc === '/dashboard/') {
        $("title").text('Dashboard');
    } else if (loc === '/test') {
        $("title").text('Test Page');
    } else if (loc === 'http://127.0.0.1:7000') {
        $("title").text('Home Page');
    } else if (loc === '/save/') {
        $("title").text('My Collections');
    } else if (loc === '/profile/') {
        $("title").text('My Profile');
    }


});

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

function onValidationPassword(input_btn, validation_template_id, callback) {
    $(input_btn).on('input', function () {
        const password = $(this).val();
        $(validation_template_id).empty(); // Clear any previous messages

        // Password strength validation template
        let template = `
        <div class="form-group">
            <ul>
                <li id="minLength"><i class="fas fa-times text-danger"></i> Minimum 8 characters</li>
                <li id="uppercase"><i class="fas fa-times text-danger"></i> At least one uppercase letter</li>
                <li id="lowercase"><i class="fas fa-times text-danger"></i> At least one lowercase letter</li>
                <li id="symbol"><i class="fas fa-times text-danger"></i> At least one symbol (@$!%*?&)</li>
                <li id="number"><i class="fas fa-times text-danger"></i> At least one number</li>
            </ul>
        </div>`;
        $(validation_template_id).append(template);

        // Regex for password validation
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

        // Update validation messages
        $('#minLength').html(isLengthValid ? '<i class="fas fa-check text-success"></i> Minimum 8 characters' : '<i class="fas fa-times text-danger"></i> Minimum 8 characters');
        $('#uppercase').html(hasUpperCase ? '<i class="fas fa-check text-success"></i> At least one uppercase letter' : '<i class="fas fa-times text-danger"></i> At least one uppercase letter');
        $('#lowercase').html(hasLowerCase ? '<i class="fas fa-check text-success"></i> At least one lowercase letter' : '<i class="fas fa-times text-danger"></i> At least one lowercase letter');
        $('#symbol').html(hasSpecialChar ? '<i class="fas fa-check text-success"></i> At least one symbol (@$!%*?&)' : '<i class="fas fa-times text-danger"></i> At least one symbol (@$!%*?&)');
        $('#number').html(hasNumber ? '<i class="fas fa-check text-success"></i> At least one number' : '<i class="fas fa-times text-danger"></i> At least one number');

        // If all criteria are met, invoke the callback and return the valid password
        if (isLengthValid && hasUpperCase && hasLowerCase && hasNumber && hasSpecialChar) {
            callback(password);  // Pass the valid password to the callback
        } else {
            callback('');
        }
    });
}

function onMatchPassword(input_btn, originalPassword, validation_template_id, onMatchPassword_template_id) {
    $(input_btn).on('input', function () {
        const repeatPassword = $(this).val();
        $(validation_template_id).empty();
        $(onMatchPassword_template_id).remove();
        if (repeatPassword === originalPassword && repeatPassword !== '') {
            const template = `
                <div class="valid-message" style="color: green;">
                    <i class="fas fa-check-circle"></i> Passwords match completely.
                </div>`;
            $(validation_template_id).append(template);

            setTimeout(function () {
                $(validation_template_id).empty();
            }, 1500);

            return true;
        } else if (repeatPassword === '') {
            const template = `
                <div class="info-message" style="color: orange;">
                    <i class="fas fa-info-circle"></i> Repeat password is empty.
                </div>`;
            $(validation_template_id).append(template);

            return false;
        } else {
            const template = `
                <div class="invalid-message" style="color: red;">
                    <i class="fas fa-times-circle"></i> Passwords do not match.
                </div>`;
            $(validation_template_id).append(template);

            return false;
        }
    });
}

let auth_password = '';
onValidationPassword('#password-signup-password', '.password-on-validations', function (validPassword) {
    auth_password = validPassword;
    $('#password-signup-repassword').on('input', function () {

        onMatchPassword('#password-signup-repassword', auth_password, '.password-on-equal', '.password-on-validations');
    });
});

let reset_password = '';
onValidationPassword('#new-password', '.password-on-validations', function (validPassword) {
    reset_password = validPassword;
    $('#confirm-password').on('input', function () {

        onMatchPassword('#confirm-password', reset_password, '.password-on-equal', '.password-on-validations');
    });
});

show_password_toggle('#password-signin-password', '.toggle-signin-password', '.signin-password-eye-icon');
show_password_toggle('#password-signup-password', '.toggle-signup-password', '.password-eye-icon');
show_password_toggle('#password-signup-repassword', '.toggle-signup-repassword', '.repeat-password-eye-icon');

show_password_toggle('#current-password', '.toggle-current-password', '#current-password-eye');
show_password_toggle('#new-password', '.toggle-new-password', '#new-password-eye');
show_password_toggle('#confirm-password', '.toggle-confirm-password', '#confirm-password-eye');



$(document).ready(function () {
    function getStoreUrl() {
        var urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('store_url');
    }

    $('#loading').show();

    var storeUrl = getStoreUrl();

    if (storeUrl) {
        $.ajax({
            url: 'http://127.0.0.1:7345/stores/view/insights?store_url=' + encodeURIComponent(storeUrl),
            method: 'GET',
            success: function (data) {
                $('#loading').hide();
                $('#content').show();
                $('#content').html(data);
            },
            error: function () {
                $('#loading').hide();
            }
        });
    } else {
        $('#loading').hide();
    }

    $(window).on('load', function () {
        $('#loading').hide();
        $('#content').show();
    });
});
