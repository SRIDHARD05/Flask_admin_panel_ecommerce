$(document).ready(function () {
    $('#facebookAdsForm').on('submit', function (e) {
        e.preventDefault();

        const formData = {
            name: $('input[name="ad_name"]').val(),
            ads_data: [
                {
                    ad_id: $('input[name="ad_id"]').val(),
                    ad_name: $('input[name="ad_name"]').val(),
                    campaign_name: $('input[name="campaign_name"]').val(),
                    campaign_id: $('input[name="campaign_id"]').val(),
                    cta: $('input[name="cta"]').val(),
                    destination_url: $('input[name="destination_url"]').val(),
                    budget: parseFloat($('input[name="budget"]').val()),
                    daily_spend: parseFloat($('input[name="daily_spend"]').val()),
                    ad_description: $('textarea[name="ad_description"]').val(),
                    platforms: $('select[name="platforms"]').val(),
                    ad_status: $('select[name="ad_status"]').val(),
                    performance: {
                        impressions: parseInt($('input[name="impressions"]').val()),
                        clicks: parseInt($('input[name="clicks"]').val()),
                        conversions: parseInt($('input[name="conversions"]').val()),
                    },
                }
            ]
        };

        $.ajax({
            url: '/ads_data/facebook/ads/store',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function (response) {
                if (response.status === 200) {
                    alert(response.message);
                    $('#facebookAdsForm')[0].reset();
                } else {
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                alert('Error: ' + (xhr.responseJSON ? xhr.responseJSON.message : 'An error occurred.'));
            }
        });
    });

    $("#facebook-ads-bulk-upload").on('click', function () {
        var template = `
          <div class="modal fade" id="user-save-collections-show" tabindex="-1" role="dialog" aria-labelledby="user-save-collections-showLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg" role="document"> <!-- Added modal-lg for larger screens -->
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title font-weight-bold" id="user-save-collections-showLabel">Bulk Upload Collections</h5>
                    </div>
                    <div class="modal-body">
                        <label for="user-bulk-upload" class="form-label">Upload JSON Data:</label>
                        <div class="row">
                            <div class="col-12">
                                <textarea class="form-control" name="Bulk Upload" id="user-bulk-upload" placeholder="Paste your JSON data here" rows="5"></textarea>
                                <small class="form-text text-muted mt-2">You can paste the data in JSON format. Make sure it's correctly formatted.</small>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" id="user-show-collection-cancel" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" id="user-show-collection-submit">Save Changes</button>
                    </div>
                </div>
            </div>
          </div>
        `;

        $(template).appendTo('body');
        $('#user-save-collections-show').modal('show');

        $('#user-show-collection-submit').on('click', function () {
            var jsonData = $('#user-bulk-upload').val();

            try {
                var parsedData = JSON.parse(jsonData);

                $.ajax({
                    url: '/ads_data/facebook/ads/bulk/upload',  
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(parsedData),
                    success: function (response) {
                        console.log(response);
                        $('#user-save-collections-show').modal('hide');
                    },
                    error: function (xhr, status, error) {
                        alert('Error: ' + (xhr.responseJSON ? xhr.responseJSON.message : 'An error occurred.'));
                    }
                });

            } catch (error) {
                alert('Invalid JSON format. Please ensure your data is properly formatted.');
            }
        });

        $('#user-show-collection-cancel').on('click', function () {
            $('#user-save-collections-show').modal('hide');
        });
    });

});