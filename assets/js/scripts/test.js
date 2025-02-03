
function generate_report(jsonData) {
    const json_data = JSON.parse(jsonData);

    const data_map = new Map();
    Object.keys(json_data).forEach(key => {
        data_map.set(key, json_data[key]);
    });

    const config_data = data_map.get('configSettings');
    // console.log(config_data['skipAboutBlank']);
    // console.log(config_data['clearStorageTypes']);


    const categories = data_map.get('categories');
    // console.log(categories['performance'].auditRefs);


    const categoryGroups = data_map.get('categoryGroups');
    // for (const key in categoryGroups) {
    //     console.log(categoryGroups[key].title);
    // }

    const stackPacks = data_map.get('stackPacks');
    // console.log(stackPacks);

    const entities = data_map.get('entities');
    // for (let i = 0; i < entities.length; i++) {
    //     console.log(entities[i].name + '\n');
    // }

    const fullPageScreenshot = data_map.get('fullPageScreenshot');
    // console.log(fullPageScreenshot.screenshot + '\n');
    // for (const key in fullPageScreenshot) {
    //     console.log(fullPageScreenshot[key]['1-90-LINK']);
    // }

    const timing = data_map.get('timing');
    // entry_timing = timing['entries']
    // for (let i = 0; i < entry_timing.length; i++) {
    //     console.log(entry_timing[i].name);
    // }
    // const total_timing = timing.total;
    // console.log(total_timing);

    const i18n = data_map.get('i18n');
    // console.log(i18n.rendererFormattedStrings.warningHeader);

    const icuMessagePaths = i18n.icuMessagePaths;
    // console.log(icuMessagePaths);
    // for (let i = 0; i <= icuMessagePaths.length; i++) {
    //     console.log(icuMessagePaths[i]);
    // }

    const icu_obj = Object.entries(icuMessagePaths);
    for (let i = 0; i < icu_obj.length; i++) {
        if (icu_obj[i][0] === "core/lib/i18n/i18n.js | seconds") {
            const my_data = Object.entries(icu_obj[i][1]);
            for (let i = 0; i < my_data.length; i++) {
                // console.log(my_data[i][1] + '\n');
                console.log(my_data[i][1].path);
            }
        }
        else {
            console.log(icu_obj[i][1]);
        }
    }
}









function generate_report(jsonData) {
    const json_data = JSON.parse(jsonData);

    const data_map = new Map();
    Object.keys(json_data).forEach(key => {
        data_map.set(key, json_data[key]);
    });


    const destinations_url = data_map.get('requestedUrl');
    const destinations_url_accordin = new Accordion('#domain_name',
        {
            title: `Requested Reports URL`,
            page_content: `${destinations_url}`
        }
    );

    const report_time = data_map.get('fetchTime');
    const report_time_Accordin = new Accordion('#fetchTime',
        {
            title: 'Report Generated Time',
            page_content: `${report_time}`
        }
    );

    const user_agent = data_map.get('userAgent');
    const user_agent_Accordin = new Accordion('#user_agent',
        {
            title: 'Website User Agents',
            page_content: `${user_agent}`
        }
    );

    // TODO: For Audits Sections
    const audits = data_map.get('audits');
    // for (const key in audits) {

    //     const data = audits[key];
    //     if ("guidanceLevel" in data) {
    //         console.log(data.title);
    //     }
    //     // console.log(`Title -> ` + data.title);
    //     // console.log(`ID -> ` + data.id);
    //     // console.log(`Descriptions ->` + data.description);
    //     // console.log(`Score -> ` + data.score);
    //     // console.log(`scoreDisplayMode ->` + data.scoreDisplayMode);
    //     // console.log(`GuidanceLevel -> ` + data.guidanceLevel);
    //     // console.log('\n');
    // }

    const config_data = data_map.get('configSettings');
    // console.log(config_data['skipAboutBlank']);
    // console.log(config_data['clearStorageTypes']);


    const categories = data_map.get('categories');
    // console.log(categories['performance'].auditRefs);


    const categoryGroups = data_map.get('categoryGroups');
    // for (const key in categoryGroups) {
    //     console.log(categoryGroups[key].title);
    // }

    const stackPacks = data_map.get('stackPacks');
    // console.log(stackPacks);

    const entities = data_map.get('entities');
    // for (let i = 0; i < entities.length; i++) {
    //     console.log(entities[i].name + '\n');
    // }

    const fullPageScreenshot = data_map.get('fullPageScreenshot');
    // console.log(fullPageScreenshot.screenshot + '\n');
    // for (const key in fullPageScreenshot) {
    //     console.log(fullPageScreenshot[key]['1-90-LINK']);
    // }

    const timing = data_map.get('timing');
    // entry_timing = timing['entries']
    // for (let i = 0; i < entry_timing.length; i++) {
    //     console.log(entry_timing[i].name);
    // }
    // const total_timing = timing.total;
    // console.log(total_timing);

    const i18n = data_map.get('i18n');
    // console.log(i18n.rendererFormattedStrings.warningHeader);

    const icuMessagePaths = i18n.icuMessagePaths;
    // console.log(icuMessagePaths);
    // for (let i = 0; i <= icuMessagePaths.length; i++) {
    //     console.log(icuMessagePaths[i]);
    // }

    const icu_obj = Object.entries(icuMessagePaths);
    for (let i = 0; i < icu_obj.length; i++) {
        if (icu_obj[i][0] === "core/lib/i18n/i18n.js | seconds") {
            const my_data = Object.entries(icu_obj[i][1]);
            for (let i = 0; i < my_data.length; i++) {
                // console.log(my_data[i][1] + '\n');
                console.log(my_data[i][1].path);
            }
        }
        else {
            console.log(icu_obj[i][1]);
        }
    }
}

// const mainAccordion = new Accordion('#mainAccordionContainer', [
//     {
//         title: 'Main Accordion 1',
//         page_content: '<p>Main content 1</p>'
//     },
//     {
//         title: 'Main Accordion 2',
//         page_content: 'aedsrftgyhjk'
//     }]
// );
// mainAccordion.addAccordionToAccordion('Main Accordion 1', paragraph)
// mainAccordion.addAccordionEditTitle('Main Accordion 1', 'Edited Accordin Title')
// mainAccordion.addAccordionToAccordion('Main Accordion 1', [
//     {
//         title: 'Main Accordion 1',
//         page_content: '<p>Main content 1</p>'
//     },
//     {
//         title: 'Main Accordion 2',
//         page_content: 'aedsrftgyhjk'
//     }
// ])
// mainAccordion.addAccordionToHTMLContent('Main Accordion 1', htmlContent)



