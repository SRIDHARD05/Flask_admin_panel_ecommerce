
function showFileName() {
    var input = document.getElementById("profileImageInput");
    fileName = input.files[0] ? input.files[0].name : "No file selected";
    document.getElementById("file-name").textContent = fileName;
}

$(document).ready(function () {
    $('.save-user-profile').on('click', function (e) {
        e.preventDefault();
        var first_name = $('input[name="first_name"]').val()
        var last_name = $('input[name="last_name"]').val()
        var email = $('input[name="email"]').val()
        var location = $('input[name="location"]').val();
        var phonenumber = $('input[name="phonenumber"]').val()

        var formData = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'location': location,
            'phonenumber': phonenumber
        };

        var data = JSON.stringify(formData)
        // loader_start('no') TODO: Solve the Model Hide DOM Error
        $.ajax({
            url: '/profile/user/save',
            type: 'POST',
            contentType: 'application/json',
            data: data,
            success: function (response) {
                if (response.status === 200) {
                    alert("Success");
                    window.location.reload();
                } else {
                    console.log('Error:', response.message);
                }
            },
            error: function (xhr, status, error) {
                console.error('Request failed', status, error);
            }
        });
    });


    $("#auth-update-password").on('click', function () {
        var old_ps = $('#current-password').val();
        var new_ps = $('#new-password').val();
        var confirm_pas = $('#confirm-password').val();
        var data = {
            'old_password': old_ps,
            'new_password': new_ps
        }
        if (new_ps === confirm_pas) {
            $.ajax({
                url: '/profile/reset_password',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function (response) {
                    if (response.status === 200) {
                        alert("Success");
                        window.location.reload();
                    } else {
                        console.log('Error:', response.message);
                    }
                },
                error: function (xhr, status, error) {
                    console.error('Request failed', status, error);
                }
            });
        } else {
            alert("Password Not Mathced...");
        }
    })
});
