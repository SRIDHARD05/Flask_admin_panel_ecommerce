function search_filter_nav_bar_templates_generations(starting_id, destination_url, ending_id) {
    $(document).on("click", starting_id, function () {
        $('.nav-container-parent').children().remove();
        $.ajax({
            url: destination_url,
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                $('.nav-container-child').append(response);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });

    $(document).on("click", ending_id, function () {
        $('.nav-container-child').children().remove();
        $.ajax({
            url: "/sidebar/search/tab1/navbar",
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                $('.nav-container-parent').append(response);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
}


$('a[data-bs-toggle="tab"]').on('shown.bs.tab', function (e) {
    var activeTabId = $(e.target).attr('id');

    if (activeTabId === "tab1-tab") {
        $('.nav_bar').children().remove();

        $.ajax({
            url: "/sidebar/search/tab1/navbar",
            type: "GET",
            contentType: "application/json",
            success: function (response) {
                $(".nav_bar").append(response);
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });

    } else if (activeTabId === "tab2-tab") {
        $('.nav_bar').children().remove();

        var template = `
            <li class="nav-item">
                <a class="nav-link text-dark" href="#">
                    <i class="material-symbols-rounded opacity-5">view_in_ar</i>
                    <span class="nav-link-text ms-1">Tab 2</span>
                </a>
            </li>`;

        $(".nav_bar").append(template);
    } else if (activeTabId === "tab3-tab") {
        $('.nav_bar').children().remove();
        var template = `
            <li class="nav-item">
                <a class="nav-link text-dark" href="#">
                    <i class="material-symbols-rounded opacity-5">view_in_ar</i>
                    <span class="nav-link-text ms-1">Tab 3</span>
                </a>
            </li>`;
        $(".nav_bar").append(template);
    } else if (activeTabId === "tab4-tab") {
        $('.nav_bar').children().remove();
        var template = `
            <li class="nav-item">
                <a class="nav-link text-dark" href="#">
                    <i class="material-symbols-rounded opacity-5">view_in_ar</i>
                    <span class="nav-link-text ms-1">Tab 4</span>
                </a>
            </li>`;
        $(".nav_bar").append(template);
    } else {
    }
});

search_filter_nav_bar_templates_generations("#main-tab-dates-nav-link", "/sidebar/search/tab1/dates", "#nav-bar-dates-search-back-btn");
search_filter_nav_bar_templates_generations("#main-tab-reactions-nav-link", "/sidebar/search/tab1/reactions", "#nav-bar-reactions-search-back-btn");
search_filter_nav_bar_templates_generations("#main-tab-target-audience-nav-link", "/sidebar/search/tab1/target_audience", "#nav-bar-target-audience-search-back-btn");

$(document).ready(function () {
    var path = window.location.pathname;

    $('.nav-link').each(function () {
        var linkPath = $(this).attr('href');
        if (linkPath === path) {
            $(this)
                .addClass('active bg-gradient-dark text-white')
                .removeClass('text-dark');
        } else {
            $(this)
                .removeClass('active bg-gradient-dark text-white')
                .addClass('text-dark');
        }
    });
});
