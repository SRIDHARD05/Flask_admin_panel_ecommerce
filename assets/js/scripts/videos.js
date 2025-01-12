$(document).ready(function () {
    const videos = $('.video-container');
    let lastHoveredVideo = null;

    videos.hover(
        function () {
            videos.each(function () {
                this.pause();
            });
            this.play();
        },
        function () {
            if (this !== lastHoveredVideo) {
                this.pause();
            }
        }
    );

    videos.on('mouseleave', function () {
        this.pause();
        lastHoveredVideo = null;
    });

    videos.on('mouseenter', function () {
        lastHoveredVideo = this;
    });

    $(document).keydown(function (e) {
        if (!lastHoveredVideo) return;

        const video = lastHoveredVideo;

        if (e.key === 'ArrowRight') {
            video.currentTime = Math.min(video.currentTime + 5, video.duration);
        }

        if (e.key === 'ArrowLeft') {
            video.currentTime = Math.max(video.currentTime - 5, 0);
        }

        if (e.key === ' ') {
            e.preventDefault();
            if (video.paused) {
                video.play();
            } else {
                video.pause();
            }
        }
    });

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

        $(this).click(function () {
            alert("Video clicked: " + videoId);
        });

        $(this).siblings('.video-details').find('.btn-primary').click(function () {
            let likesCount = parseInt($(this).siblings('.likes-count').text());
            likesCount++;
            $(this).siblings('.likes-count').text(likesCount);
            console.log(`Video ID ${videoId} liked! Total likes: ${likesCount}`);
        });
    });




    $("#test-url-submit").on('click', function () {
        var url = $('#test-url').val();

        if (url.trim() === "") {
            alert("Please enter a valid URL.");
            return;
        }

        var urlPattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w\-#?&=]*)?$/;
        if (!urlPattern.test(url)) {
            alert("Please enter a valid URL.");
            return;
        }

        $.ajax({
            url: "/test",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ 'url': url }),
            success: function (response) {
                $('#test-url').prop('disabled', true);
                $('#test-url-submit').prop('disabled', true);

                $.ajax({
                    url: "/test/tabs",
                    type: "GET",
                    success: function (response) {
                        $("#tabContent").empty();
                        $("#tabContent").append(response);
                    },
                    error: function (xhr, status, error) {
                        alert("Error: " + error);
                    }
                });
            },
            error: function (xhr, status, error) {
                alert("Error: " + error);
            }
        });
    });
});

