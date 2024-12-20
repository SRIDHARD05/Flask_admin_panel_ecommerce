$(document).ready(function () {
    $('.video-container').each(function () {
        const video = $(this)[0];
        const videoId = $(this).data('id');
        const progressBar = $(this).siblings('.progress-bar-container');
        const progressBarFilled = progressBar.find('.progress-bar-filled');
        video.addEventListener('timeupdate', function () {
            const percentage = (video.currentTime / video.duration) * 100;
            progressBarFilled.css('width', percentage + '%');
        });
        progressBar.click(function (e) {
            const position = (e.pageX - $(this).offset().left) / $(this).width();
            video.currentTime = position * video.duration;
        });
        $(this).hover(
            function () {
                video.play();
            },
            function () {
                video.pause();
            }
        );
        $(this).siblings('.video-details').find('.btn-primary').click(function () {
            let likesCount = parseInt($(this).siblings('.likes-count').text());
            likesCount++;
            $(this).siblings('.likes-count').text(likesCount);
            console.log(`Video ID ${videoId} liked! Total likes: ${likesCount}`);
        });
    });
});
