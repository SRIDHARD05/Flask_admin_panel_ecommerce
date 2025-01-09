// $(document).ready(function () {
//     function detectDevTools() {
//         const threshold = 160;
//         const widthDiff = window.outerWidth - window.innerWidth;
//         const heightDiff = window.outerHeight - window.innerHeight;

//         if (widthDiff > threshold || heightDiff > threshold) {
//             validateUserRoleForDevTools();
//         }
//     }

//     function validateUserRoleForDevTools() {
//         $.ajax({
//             url: `/dashboard/user_validations`,
//             type: "GET",
//             success: function (response) {
//                 if (response.result === true) {
//                     console.log("Access Granted for Developer Tools");
//                     alert("Access Granted for Developer Tools");
//                 } else {
//                     alert("Access Denied: Developer tools are disabled for your role.");
//                     blockUnauthorizedActions();
//                 }
//             },
//             error: function (xhr, status, error) {
//                 console.error("Error validating user role:", xhr.responseText);
//             }
//         });
//     }

//     function blockUnauthorizedActions() {
//         $(document).on('contextmenu', function (e) {
//             e.preventDefault();
//             alert("Right-click is disabled.");
//         });

//         $(document).on('keydown', function (e) {
//             if (
//                 e.key === 'F12' ||
//                 (e.ctrlKey && e.shiftKey && e.key === 'I') ||
//                 (e.ctrlKey && e.key === 'U')
//             ) {
//                 e.preventDefault();
//                 alert("Developer tools are disabled.");
//             }
//         });

//         window.location.href = "/users/deauth";
//     }

//     setInterval(detectDevTools, 1000);
// });


