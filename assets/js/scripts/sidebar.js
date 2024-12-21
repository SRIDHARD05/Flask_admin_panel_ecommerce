function search_filter_nav_bar_templates_generations(starting_id, destination_url, ending_id) {
    $(document).on("click", starting_id, function () {
        $('.nav-container-parent').children().remove();
        $.ajax({
            url: destination_url,
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                $('.nav-container-child').append(response);
                console.log(response);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });

    $(document).on("click", ending_id, function () {
        $('.nav-container-child').children().remove();
        $.ajax({
            url: "/sidebar/search/navbar",
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                console.log(response);
                $('.nav-container-parent').append(response);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
}




$(document).ready(function () {
    search_filter_nav_bar_templates_generations("#dates-nav-link", "/sidebar/search/dates", "#nav-bar-dates-search-back-btn");
    search_filter_nav_bar_templates_generations("#reactions-nav-link", "/sidebar/search/reactions", "#nav-bar-reactions-search-back-btn");
    search_filter_nav_bar_templates_generations("#target-audience-nav-link", "/sidebar/search/target_audience", "#nav-bar-target-audience-search-back-btn");
});















