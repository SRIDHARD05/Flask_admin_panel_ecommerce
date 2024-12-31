const fs = require('fs');
const { type } = require('os');

const filePath = './data.json';


function audits_reports(data_map, key) {
    const audits = data_map.get('audits');
    // console.log(typeof (audits));
    var data = audits[key];
    if ('score' in data) {
        data.actions = data.score >= 1 ? 'primary' : 'danger';
        return data;
    } else {
        data.actions = 'primary';
        return data;
    }
}


fs.readFile(filePath, 'utf8', (err, jsonData) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }

    try {
        const json_data = JSON.parse(jsonData);

        const data_map = new Map();
        Object.keys(json_data).forEach(key => {
            data_map.set(key, json_data[key]);
        });

        const destinations_url = data_map.get('requestedUrl');
        // console.log('Requested URL:', destinations_url);

        const report_time = data_map.get('fetchTime');
        // console.log('Report Time:', report_time);

        const user_agent = data_map.get('userAgent');
        // console.log(user_agent);

        var is_on_http = audits_reports(data_map, 'is-on-https');
        var redirect_http = audits_reports(data_map, 'redirects-http');
        var viewport = audits_reports(data_map, 'viewport');
        var first_contentfull_paint = audits_reports(data_map, 'first-contentful-paint');
        var largest_meaningfull_paint = audits_reports(data_map, 'largest-contentful-paint');
        var first_meaningfull_paint = audits_reports(data_map, 'first-meaningful-paint');
        var speed_index = audits_reports(data_map, 'speed-index');
        // console.log(speed_index);

        // TODO: Screen Shot Thumbnails Details
        var screenshot_thumbnails = audits_reports(data_map, 'screenshot-thumbnails');
        // console.log(screenshot_thumbnails['details'].items[0]);

        // TODO: Final ScreenShot Details
        var total_blocking_time = audits_reports(data_map, 'total-blocking-time');

        var max_potential_fid = audits_reports(data_map, 'max-potential-fid');

        const audits = data_map.get('audits');
        for (const key in audits) {
            
            const data = audits[key]['details'];
            console.log(data);
        }

    } catch (parseError) {
        // console.error('Error parsing the JSON:', parseError);
    }
});
