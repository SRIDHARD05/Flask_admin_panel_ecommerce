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

function notApplicable_audits(title, data) {
    if (data && data.length > 0) {
        add_brak();
        reports_card_elements(title);
        let not_applicable_data = data.map(i => {
            if (i === null || i === undefined || Object.keys(i).length === 0) {
                return {
                    title: "Nothing Bad Happened",
                    page_content: "super everything is going to be good"
                };
            }
            return {
                title: escapeHtml(`${i.title}`),
                page_content: formatLinks(i.description || 'No description available')
            };
        });
        new Accordion(create_div_element(), not_applicable_data);
    }
}

function generate_report(json_data) {

    function generate_accordin(titles, performance_audits_passed_data, performance_audits_un_passed_data, performance_audits_manual_data, performance_audits_not_applicable_data) {
        function formatLinks(text) {
            if (typeof text !== "string") {
                console.warn("formatLinks received a non-string value:", text);
                return "";
            }
            return text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
                '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-primary underline text-bold">$1</a>'
            );
        }

        function escapeHtml(text) {
            return text.replace(/[&<>"'`=/]/g, function (char) {
                return `&#${char.charCodeAt(0)};`;
            });
        }

        const stackPacksData = data_map.get('stackPacks')[0];

        // TODO: For Performance Audits Passed Data
        if (performance_audits_passed_data && performance_audits_passed_data.length > 0) {
            add_brak();
            reports_card_elements(titles[0])
            let data = performance_audits_passed_data.map(audit => {
                return {
                    title: escapeHtml(audit.title.trim()),
                    page_content: `<strong>${audit.title.trim()}</strong> ${audit.displayValue ? `<span style="color: red;">--- ${audit.displayValue}</span>` : ''}<br><br>${formatLinks(audit.description || 'No description available')}<br><br>`,
                };
            });
            const accor = new Accordion(create_div_element(), data);

            performance_audits_passed_data.forEach(audit => {
                let formattedTitle = audit.title.trim();
                let formattedId = audit.id;

                if (audit.details?.headings && audit.details?.items) {
                    const tableHeaders = audit.details.headings.map(heading => `${heading.label} (${heading.valueType})`);
                    const tableRows = audit.details.items.map(item =>
                        audit.details.headings.map(heading => item[heading.key] ?? 'N/A')
                    );

                    const tableData = {
                        table_header: tableHeaders,
                        table_content: tableRows
                    };

                    setTimeout(() => {
                        accor.addTableToAccordion(formattedTitle, tableData);
                        accor.addParagraph(formattedTitle, formatLinks(stackPacksData.descriptions[formattedId] || ""));
                    }, 1000);
                }
            });
        }


        // TODO: For Performance Audits Unpassed Data
        if (performance_audits_un_passed_data && performance_audits_un_passed_data.length > 0) {
            add_brak();
            reports_card_elements(titles[1])
            let data = performance_audits_un_passed_data.map(audit => {
                return {
                    title: audit.title.trim(),
                    page_content: `<strong>${audit.title.trim()}</strong> ${audit.displayValue ? `<span style="color: red;">--- ${audit.displayValue}</span>` : ''}<br><br>${formatLinks(audit.description || 'No description available')}<br><br>`,
                };
            });
            const accor = new Accordion(create_div_element(), data);
            performance_audits_un_passed_data.forEach(audit => {
                let formattedTitle = audit.title.trim();
                let formattedId = audit.id;

                let formattedDisplayValue = audit.displayValue
                    ? `<span style="color: red;">&nbsp;&nbsp;--- ${audit.displayValue}</span>`
                    : '';
                let combinedText = `${formattedTitle}${formattedDisplayValue}`;

                if (audit.details?.headings && audit.details?.items) {
                    const tableHeaders = audit.details.headings.map(heading => `${heading.label} (${heading.valueType})`);
                    const tableRows = audit.details.items.map(item =>
                        audit.details.headings.map(heading => item[heading.key] ?? 'N/A')
                    );

                    const tableData = {
                        table_header: tableHeaders,
                        table_content: tableRows
                    };
                    const paragraph = stackPacksData.descriptions[`${formattedId}`];

                    setTimeout(() => {
                        accor.addTableToAccordion(formattedTitle, tableData);
                        accor.updateTitle(formattedTitle, combinedText);
                        accor.addParagraph(formattedTitle, formatLinks(stackPacksData.descriptions[formattedId] || ""));
                    }, 1000);
                }
            });
        }

        // TODO: For Performance Manuval Audits
        if (performance_audits_manual_data && performance_audits_manual_data.length > 0) {
            add_brak();
            reports_card_elements(titles[2]);
            let performance_audits_manual_data_report = performance_audits_manual_data.map(i => {
                if (i === null || i === undefined || Object.keys(i).length === 0) {
                    return {
                        title: "Nothing Bad Happened",
                        page_content: "super everything is going to be good"
                    };
                }
                return {
                    title: escapeHtml(`${i.title}`),
                    page_content: formatLinks(i.description || 'No description available')
                };
            });
            new Accordion(create_div_element(), performance_audits_manual_data_report);
        }

        // TODO: For Performance Not Applicable Audits
        if (performance_audits_not_applicable_data && performance_audits_not_applicable_data.length > 0) {
            add_brak();
            reports_card_elements(titles[3]);
            let performance_audits_not_applicable_data_report = performance_audits_not_applicable_data.map(i => {
                if (i === null || i === undefined || Object.keys(i).length === 0) {
                    return {
                        title: "Nothing Bad Happened",
                        page_content: "super everything is going to be good"
                    };
                }
                return {
                    title: escapeHtml(`${i.title}`),
                    page_content: formatLinks(i.description || 'No description available')
                };
            });
            new Accordion(create_div_element(), performance_audits_not_applicable_data_report);
        }
    }

    const seo_report_container = $("#shopify-store-seo-report-container");
    const data_map = new Map();
    Object.keys(json_data).forEach(key => {
        data_map.set(key, json_data[key]);
    });

    const categories_audits = data_map.get('categories');
    const performanceIds = [];
    const accessibilityIds = [];
    const seoIds = [];
    const bestPracticesIds = [];

    categories_audits.performance.auditRefs.forEach(metric => {
        performanceIds.push(metric.id);
    });

    categories_audits.accessibility.auditRefs.forEach(metric => {
        accessibilityIds.push(metric.id);
    });

    categories_audits.seo.auditRefs.forEach(metric => {
        seoIds.push(metric.id);
    });

    categories_audits['best-practices'].auditRefs.forEach(metric => {
        bestPracticesIds.push(metric.id);
    });

    const audits = data_map.get('audits');

    const category = ['performance', 'accessibility', 'seo', 'bestPractices'];
    let performanceData = {};
    let accessibilityData = {};
    let seoData = {};
    let bestPracticesData = {};

    Object.keys(audits).forEach(id => {
        if (performanceIds.includes(id)) {
            performanceData[id] = audits[id];
        } else if (accessibilityIds.includes(id)) {
            accessibilityData[id] = audits[id];
        } else if (seoIds.includes(id)) {
            seoData[id] = audits[id];
        } else if (bestPracticesIds.includes(id)) {
            bestPracticesData[id] = audits[id];
        }
    });

    let performance_audits_passed_data = [];
    let performance_audits_un_passed_data = [];
    let performance_audits_manual_data = [];
    let performance_audits_not_applicable_data = [];
    Object.keys(performanceData).forEach(id => {
        const data = performanceData[id];
        if (data.score === null) {
            if (data.scoreDisplayMode === 'manual') {
                performance_audits_manual_data.push(data);
            } else if (data.scoreDisplayMode === 'notApplicable') {
                performance_audits_not_applicable_data.push(data);
            }
        } else if (data.score >= 1) {
            performance_audits_passed_data.push(data);
        } else if (data.score < 1) {
            performance_audits_un_passed_data.push(data);
        }
    });


    // TODO: For Perfromance Auditing
    generate_accordin([
        `Passed Audits -> Performance`,
        `UNPassed Audits -> Performance`,
        `Manuval Audits -> Performance`,
        `Not Applicable Audits -> Performance`
    ], performance_audits_passed_data, performance_audits_un_passed_data, performance_audits_manual_data, performance_audits_not_applicable_data)

    let accessibility_audits_passed_data = [];
    let accessibility_audits_un_passed_data = [];
    let accessibility_audits_manual_data = [];
    let accessibility_audits_not_applicable_data = [];
    Object.keys(accessibilityData).forEach(id => {
        const data = accessibilityData[id];
        if (data.score === null) {
            if (data.scoreDisplayMode === 'manual') {
                accessibility_audits_manual_data.push(data);
            }
            else if (data.scoreDisplayMode === 'notApplicable') {
                accessibility_audits_not_applicable_data.push(data);
            }
        }
        else if (data.score >= 1) {
            accessibility_audits_passed_data.push(data);
        }
        else if (data.score < 1) {
            accessibility_audits_un_passed_data.push(data);
        }

    });

    // TODO: For Accessibility Auditing
    generate_accordin([
        `Passed Audits -> Accessibility`,
        `UNPassed Audits -> Accessibility`,
        `Manuval Audits -> Accessibility`,
        `Not Applicable Audits -> Accessibility`
    ], accessibility_audits_passed_data, accessibility_audits_un_passed_data, accessibility_audits_manual_data, accessibility_audits_not_applicable_data)

    let seo_audits_passed_data = [];
    let seo_audits_un_passed_data = [];
    let seo_audits_manual_data = [];
    let seo_audits_not_applicable_data = [];
    Object.keys(seoData).forEach(id => {
        const data = seoData[id];
        if (data.score === null) {
            if (data.scoreDisplayMode === 'manual') {
                seo_audits_manual_data.push(data);
            }
            else if (data.scoreDisplayMode === 'notApplicable') {
                seo_audits_not_applicable_data.push(data);
            }
        }
        else if (data.score >= 1) {
            seo_audits_passed_data.push(data);
        }
        else if (data.score < 1) {
            seo_audits_un_passed_data.push(data);
        }

    });

    // TODO: For SEO Auditing
    generate_accordin([
        `Passed Audits -> SEO`,
        `UNPassed Audits -> SEO`,
        `Manuval Audits -> SEO`,
        `Not Applicable Audits -> SEO`
    ], seo_audits_passed_data, seo_audits_un_passed_data, seo_audits_manual_data, seo_audits_not_applicable_data)

    let bestPractices_audits_passed_data = [];
    let bestPractices_audits_un_passed_data = [];
    let bestPractices_audits_manual_data = [];
    let bestPractices_audits_not_applicable_data = [];
    Object.keys(bestPracticesData).forEach(id => {
        const data = bestPracticesData[id];
        if (data.score === null) {
            if (data.scoreDisplayMode === 'manual') {
                bestPractices_audits_manual_data.push(data);
            }
            else if (data.scoreDisplayMode === 'notApplicable') {
                bestPractices_audits_not_applicable_data.push(data);
            }
        }
        else if (data.score >= 1) {
            bestPractices_audits_passed_data.push(data);
        }
        else if (data.score < 1) {
            bestPractices_audits_un_passed_data.push(data);
        }
    });

    // TODO: For Best Practice Auditing
    generate_accordin([
        `Passed Audits -> Best Practices`,
        `UNPassed Audits -> Best Practices`,
        `Manuval Audits -> Best Practices`,
        `Not Applicable Audits -> Best Practices`
    ], bestPractices_audits_passed_data, bestPractices_audits_un_passed_data, bestPractices_audits_manual_data, bestPractices_audits_not_applicable_data)

    console.log(categories_audits);

    var template = `

    ${categories_audits.performance && categories_audits.performance.title && categories_audits.performance.score !== undefined ? `
    <div class="row">
        <div class="h7">${categories_audits.performance.title}</div>
        <div class="score">${(categories_audits.performance.score * 100)}</div>
    </div>
    ` : ''}
    
    ${categories_audits.accessibility && categories_audits.accessibility.title && categories_audits.accessibility.score !== undefined ? `
    <div class="row">
        <div class="h7">${categories_audits.accessibility.title}</div>
        <div class="score">${(categories_audits.accessibility.score * 100)}</div>
        ${categories_audits.accessibility.description ? `<div class="h7">${categories_audits.accessibility.description}</div>` : ''}
        ${categories_audits.accessibility.manualDescription ? `<div class="h7">${categories_audits.accessibility.manualDescription}</div>` : ''}
    </div>
    ` : ''}
    
    ${categories_audits['best-practices'] && categories_audits['best-practices'].title && categories_audits['best-practices'].score !== undefined ? `
    <div class="row">
        <div class="h7">${categories_audits['best-practices'].title}</div>
        <div class="score">${(categories_audits['best-practices'].score * 100)}</div>
        ${categories_audits['best-practices'].description ? `<div class="h7">${categories_audits['best-practices'].description}</div>` : ''}
        ${categories_audits['best-practices'].manualDescription ? `<div class="h7">${categories_audits['best-practices'].manualDescription}</div>` : ''}
    </div>
    ` : ''}
    
    ${categories_audits.seo && categories_audits.seo.title && categories_audits.seo.score !== undefined ? `
    <div class="row">
        <div class="h7">${categories_audits.seo.title}</div>
        <div class="score">${(categories_audits.seo.score * 100)}</div>
        ${categories_audits.seo.description ? `<div class="h7">${categories_audits.seo.description}</div>` : ''}
        ${categories_audits.seo.manualDescription ? `<div class="h7">${categories_audits.seo.manualDescription}</div>` : ''}
    </div>
    ` : ''}`;
    
    $(create_div_element()).html(template);
    
}








