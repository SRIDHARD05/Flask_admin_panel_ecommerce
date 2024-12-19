// $(document).ready(function () {
//     // Loop through each video container
//     $('.video-container').each(function () {
//         const video = $(this).find('video')[0]; // Get the video element inside the container
//         const progressBar = $(this).find('.progress-bar-container');
//         const progressBarFilled = $(this).find('.progress-bar-filled');

//         // Update progress bar
//         video.addEventListener('timeupdate', function () {
//             const percentage = (video.currentTime / video.duration) * 100;
//             progressBarFilled.css('width', percentage + '%');
//         });

//         // Seek functionality
//         progressBar.click(function (e) {
//             const position = (e.pageX - $(this).offset().left) / $(this).width();
//             video.currentTime = position * video.duration;
//         });

//         // Hover to play, mouse out to pause (for the current video)
//         $(this).hover(
//             function () {
//                 video.play();  // Play the video on hover
//             },
//             function () {
//                 video.pause();  // Pause the video when mouse leaves
//             }
//         );
//     });
// });

// $(document).ready(function () {
//     // Loop through each video container
//     $('.video-container').each(function () {
//         // Hover to play, mouse out to pause (for the current video)
//         $(this).hover(
//             function () {
//                 // Get the video data-id using jQuery's .data() method
//                 const videoId = $(this).data('id');  // Get the data-id attribute value
//                 console.log('Hovering over video with ID:', videoId);  // Log the video id
//                 const video = $(this)[0];  // Get the video element to play
//                 video.play();  // Play the video
//             },
//             function () {
//                 // Get the video data-id when mouse leaves
//                 const videoId = $(this).data('id');  // Get the data-id attribute value
//                 console.log('Mouse left video with ID:', videoId);  // Log the video id
//                 const video = $(this)[0];  // Get the video element to pause
//                 video.pause();  // Pause the video
//             }
//         );
//     });
// });

$(document).ready(function () {
    // Loop through each video container
    $('.video-container').each(function () {
        const video = $(this)[0]; // Get the video element
        const videoId = $(this).data('id'); // Get the data-id of the video container
        const progressBar = $(this).siblings('.progress-bar-container');
        const progressBarFilled = progressBar.find('.progress-bar-filled');

        // Update progress bar
        video.addEventListener('timeupdate', function () {
            const percentage = (video.currentTime / video.duration) * 100;
            progressBarFilled.css('width', percentage + '%');
        });

        // Seek functionality for the progress bar
        progressBar.click(function (e) {
            const position = (e.pageX - $(this).offset().left) / $(this).width();
            video.currentTime = position * video.duration;
        });

        // Hover to play, mouse out to pause (for the current video)
        $(this).hover(
            function () {
                video.play();  // Play the video
            },
            function () {
                video.pause();  // Pause the video
            }
        );
        
        // Example for updating likes dynamically when a button is clicked
        $(this).siblings('.video-details').find('.btn-primary').click(function () {
            // Increase the like count when the share button is clicked
            let likesCount = parseInt($(this).siblings('.likes-count').text());
            likesCount++;
            $(this).siblings('.likes-count').text(likesCount); // Update the displayed like count
            console.log(`Video ID ${videoId} liked! Total likes: ${likesCount}`);
        });
    });
});
