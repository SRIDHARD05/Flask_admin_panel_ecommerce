$(document).ready(function () {

    $('#shopifyAppForm').submit(function (e) {
        e.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            url: '/shopify//best-shoify-apps/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                if (response) {
                    // console.log(response);
                    alert("Shopify Apps Saved to DB")
                }
            },
            error: function (xhr, status, error) {
                alert('Error saving app. Please try again.');
            }
        });
    });

    $('#shopifyStoresForm').on('submit', function (e) {
        e.preventDefault();
        var store_type = $('select[name=store_type]').val();
        const formData = {
            'stores-data': $('textarea[name="stores-data"]').val(),
            'store_type': store_type
        };

        console.log(store_type);
        $.ajax({
            url: '/stores/best-stores/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                alert(response);
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.message || 'An error occurred while saving the stores.';
                alert(errorMsg);
            }
        });
    });

    $('#saveshopifyStoreForm').on('submit', function (e) {
        e.preventDefault();
        const formData = {
            'stores-data': $('textarea[name="stores-data"]').val(),
        };
        $.ajax({
            url: '/stores/save',
            method: 'POST',
            data: formData,
            success: function (response) {
                alert('success');
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.message || 'An error occurred while saving the stores.';
                alert(errorMsg);
            }
        });
    });

    $(document).on('click', '#view-store-insights', function (e) {
        $(this).text("Processing...");
        e.preventDefault();
        var storeUrl = $(this).data('se');

        setTimeout(() => {
            $(this).text("View Insights");
        }, 4000);

        $.ajax({
            url: `/stores/view/insights?store_url=${encodeURIComponent(storeUrl)}`,
            method: 'GET',
            success: function (response) {
                window.open(`/stores/view/insights?store_url=${encodeURIComponent(storeUrl)}`, '_blank');
            },
            error: function (xhr, status, error) {
                alert('Error saving app. Please try again.');
            }
        });
    });

    // $("#generate_report").on('click', function () {
    //     $("#generate_report").text("Processing...").prop('disabled', true);
    //     var message = `<div
    //             style="background-color: #007bff; color: white; text-align: center; padding: 15px; font-weight: bold; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    //             We're generating the report for you. Please wait a few minutes while we gather all the data.
    //         </div>`;
    //     $("#generate_report-message").append(message);
    //     var domain_name = $('input[name=domain_name]').val().trim();
    //     if (!domain_name) {
    //         alert("Please enter a domain name.");
    //         return;
    //     }

    //     $.ajax({
    //         url: `/shopify_seo/report/generate?s=${encodeURIComponent(domain_name)}`,
    //         type: "GET",
    //         contentType: "application/json",
    //         success: function (response) {
    //             $("#generate_report").text("Submit").prop('disabled', false);
    //             $("#generate_report-message").empty();
    //             if (response['status'] === 'success') {
    //                 var data = response['data'];
    //                 console.log(data);

    //             } else {
    //                 alert("Failed to generate the report.");
    //             }
    //         },
    //         error: function (xhr, status, error) {
    //             alert(`Error: ${error}`);
    //         }
    //     });
    // });
});


$(document).ready(function () {
    $.ajax({
        url: `/shopify_seo/report/generate`,
        type: "GET",
        success: function (response) {
            if (response.status === 'success') {
                var data;
                // console.log(response.data);
                try {
                    data = JSON.parse(response.data);
                } catch (e) {
                    data = response.data;
                }

                generate_report(data);
            } else {
                console.error('Error generating report:', response.message);
                alert(`Error: ${response.message}`);
            }
        },
        error: function (xhr, status, error) {
            console.error('AJAX request failed:', error);
            alert(`Error: ${error}`);
        }
    });
});

function escapeSelector(id) {
    return CSS.escape(id);
}

function create_div_element() {
    var uniqueId = crypto.randomUUID();
    var div = document.createElement("div");
    div.id = uniqueId;
    $("#shopify-store-seo-report-container").append(div);
    return `#${escapeSelector(uniqueId)}`;
}

function reports_card_elements(title) {
    var template = `<div class="card card-frame">
  <div class="card-body">
   <h5 class="text-primary">${title}</h5>
  </div>
</div>`
    $("#shopify-store-seo-report-container").append(template);

}

function add_brak() {
    var br = document.createElement("br");
    $("#shopify-store-seo-report-container").append(br);
}

function generate_report(json_data) {
    function formatLinks(text) {
        return text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
            '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-primary underline text-bold">$1</a>'
        );
    }

    const seo_report_container = $("#shopify-store-seo-report-container");
    const data_map = new Map();
    Object.keys(json_data).forEach(key => {
        data_map.set(key, json_data[key]);
    });

    const destinations_url = data_map.get('requestedUrl');
    const destinations_url_accordin = new Accordion(create_div_element(),
        [{
            title: `Requested Reports URL`,
            page_content: `${destinations_url}`
        }]
    );

    add_brak();
    const report_time = data_map.get('fetchTime');
    const report_time_Accordin = new Accordion(create_div_element(),
        [{
            title: 'Report Generated Time',
            page_content: `${report_time}`
        }]
    );

    add_brak();
    const user_agent = data_map.get('userAgent');
    const user_agent_Accordin = new Accordion(create_div_element(),
        [{
            title: 'Website User Agents',
            page_content: `${user_agent}`
        }]
    );

    const seoChecklist = {
        performance: [
            "Reduce JavaScript execution time",
            "Cumulative Layout Shift",
            "First Contentful Paint",
            "First Meaningful Paint",
            "Time to Interactive",
            "Largest Contentful Paint",
            "Largest Contentful Paint element",
            "Max Potential First Input Delay",
            "Speed Index",
            "Total Blocking Time",
            "Minimize main-thread work",
            "Avoid long main-thread tasks",
            "Minify CSS",
            "Minify JavaScript",
            "Reduce unused CSS",
            "Reduce unused JavaScript",
            "Preconnect to required origins",
            "Enable text compression",
            "Serve static assets with an efficient cache policy",
            "Efficiently encode images",
            "Properly size images",
            "Eliminate render-blocking resources",
            "Defer offscreen images",
            "Avoids third-party cookies",
            "Some third-party resources can be lazy loaded with a facade",
            "Minimize third-party usage",
            "Avoid multiple page redirects",
            "Redirects HTTP traffic to HTTPS",
            "Initial server response time was short",
            "Avoids an excessive DOM size",
            "Serves images with appropriate resolution",
            "Use video formats for animated content",
            "Displays images with correct aspect ratio",
            "HTML5 landmark elements are used to improve navigation",
            "Use HTTP/2"
        ],
        accessibility: [
            "[accesskey] values are unique",
            "[aria-*] attributes match their roles",
            "Uses ARIA roles only on compatible elements",
            "[role] values are valid",
            "[aria-hidden=\"true\"] elements do not contain focusable descendents",
            "Elements with role=\"dialog\" or role=\"alertdialog\" have accessible names",
            "ARIA input fields have accessible names",
            "ARIA meter elements have accessible names",
            "ARIA progressbar elements have accessible names",
            "ARIA toggle fields have accessible names",
            "ARIA tooltip elements have accessible names",
            "ARIA treeitem elements have accessible names",
            "ARIA IDs are unique",
            "Elements with an ARIA [role] that require children to contain a specific [role] have all required children",
            "Elements with the role=text attribute do not have focusable descendents",
            "[role]s are contained by their required parent element",
            "Buttons have an accessible name",
            "Form elements have associated labels",
            "Input buttons have discernible text",
            "Custom controls have associated labels",
            "Custom controls have ARIA roles",
            "Links have a discernible name",
            "Links have descriptive text",
            "Links rely on color to be distinguishable",
            "Lists contain only <li> elements and script-supporting elements (<script>, <template>)",
            "List items (<li>) are contained within <ul>, <ol>, or <menu> parent elements",
            "Document has a main landmark",
            "Skip links are focusable",
            "Interactive elements indicate their purpose and state",
            "The user's focus is directed to new content added to the page",
            "Interactive controls are keyboard focusable",
            "The page has a logical tab order",
            "Identical links have the same purpose",
            "Elements with visible text labels have matching accessible names",
            "User focus is not accidentally trapped in a region",
            "[aria-*] attributes are valid and not misspelled",
            "[aria-*] attributes have valid values",
            "Avoids requesting the geolocation permission on page load",
            "Avoids requesting the notification permission on page load",
            "Allows users to paste into input fields",
            "Avoids document.write()",
            "Offscreen content is hidden from assistive technology",
            "Touch targets have sufficient size and spacing",
            "Tables use <caption> instead of [colspan] attributes to indicate a caption",
            "<th> elements and elements with [role=\"columnheader\"/\"rowheader\"] have data cells they describe",
            "<td> elements in a large <table> have one or more table headers",
            "Select elements have associated label elements",
            "Tables have different content in the summary attribute and <caption>",
            "Cells in a <table> element that use the [headers] attribute refer to table cells within the same table",
            "[user-scalable=\"no\"] is not used in the <meta name=\"viewport\"> element and the [maximum-scale] attribute is not less than 5"
        ],
        bestPractices: [
            "Avoids deprecated APIs",
            "Remove duplicate modules in JavaScript bundles",
            "Avoid chaining critical requests",
            "Ensure CSP is effective against XSS attacks",
            "Browser errors were logged to the console",
            "Issues were logged in the Issues panel in Chrome DevTools",
            "Detected JavaScript libraries",
            "Use a strong HSTS policy",
            "Ensure proper origin isolation with COOP",
            "Allows users to paste into input fields",
            "Avoid serving legacy JavaScript to modern browsers",
            "Does not use passive listeners to improve scrolling performance",
            "Properly defines charset",
            "Preload Largest Contentful Paint image",
            "Use HTTP/2",
            "Avoid enormous network payloads",
            "Has a <meta name=\"viewport\"> tag with width or initial-scale",
            "The document does not use <meta http-equiv=\"refresh\">",
            "Avoids third-party cookies",
            "User Timing marks and measures",
            "Some third-party resources can be lazy loaded with a facade",
            "Minimize third-party usage",
            "Page has valid source maps",
            "Avoids multiple page redirects"
        ],
        seo: [
            "Page isn’t blocked from indexing",
            "Uses HTTPS",
            "Links are crawlable",
            "robots.txt is valid",
            "Structured data is valid",
            "<html> element has a [lang] attribute",
            "<html> element has a valid value for its [lang] attribute",
            "<html> element has an [xml:lang] attribute with the same base language as the [lang] attribute",
            "Document has a valid hreflang",
            "Document has a <title> element",
            "Document does not have a meta description",
            "Document has a valid rel=canonical",
            "Page has successful HTTP status code",
            "Has a <meta name=\"viewport\"> tag with width or initial-scale",
            "Serve images in next-gen formats",
            "Largest Contentful Paint image was not lazily loaded",
            "Structured data is valid"
        ]
    };

    const audits = data_map.get('audits');
    const categories = ['performance', 'accessibility', 'bestPractices', 'seo'];
    let passed_audits = {};
    let un_passed_audits = {};
    let other_data_audits = [];

    categories.forEach(category => {
        passed_audits[category] = [];
        un_passed_audits[category] = [];
    });

    for (const key in audits) {
        const data = audits[key];
        categories.forEach(category => {
            if (seoChecklist && seoChecklist[category] && seoChecklist[category].includes(data.title)) {
                if (data.score >= 1) {
                    passed_audits[category].push(data);
                } else {
                    un_passed_audits[category].push(data);
                }
            }
        });
    }
    add_brak();
    reports_card_elements(`Passed Audits -> Performance`)

    let performance_data = passed_audits['performance'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const audits_accordin = new Accordion(create_div_element(), performance_data);

    add_brak();
    reports_card_elements(`UNPassed Audits -> Performance`)

    let un_performance_data = un_passed_audits['performance'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const un_audits_accordin = new Accordion(create_div_element(), un_performance_data);

    add_brak();
    reports_card_elements(`Passed Audits -> Accessibility`)

    let accessibility_data = passed_audits['accessibility'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const accessibility_accordin = new Accordion(create_div_element(), accessibility_data);

    add_brak();
    reports_card_elements(`UNPassed Audits -> Accessibility`)
    let un_accessibility_data = un_passed_audits['accessibility'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const un_accessibility_accordin = new Accordion(create_div_element(), un_accessibility_data);

    add_brak();
    reports_card_elements(`Passed Audits -> bestPractices`)

    let bestPractices_data = passed_audits['bestPractices'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const bestPractices_accordin = new Accordion(create_div_element(), bestPractices_data);

    add_brak();
    reports_card_elements(`UNPassed Audits -> bestPractices`)

    let un_bestPractices_data = un_passed_audits['bestPractices'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const un_bestPractices_accordin = new Accordion(create_div_element(), un_bestPractices_data);

    add_brak();
    reports_card_elements(`Passed Audits -> SEO`)

    let seo_data = passed_audits['seo'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const seo_accordin = new Accordion(create_div_element(), seo_data);

    add_brak();
    reports_card_elements(`UNPassed Audits -> SEO`)

    let un_passed_seo_data = un_passed_audits['seo'].map(i => ({
        title: `${i.title}`,
        page_content: formatLinks(i.description || 'No description available')
    }));
    const un_seo_accordin = new Accordion(create_div_element(), un_passed_seo_data);
    // const tableData = {
    //     table_header: ['Name', 'Age', 'Country'],
    //     table_content: [
    //         ['John', '30', 'USA'],
    //         ['Alice', '25', 'Canada'],
    //         ['Bob', '35', 'UK']
    //     ]
    // };
    
    // accordion.addTableToAccordion('Item 2', tableData);
}


