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
