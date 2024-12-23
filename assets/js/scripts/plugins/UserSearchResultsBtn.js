class UserSearchResultsBtn {
    constructor({ data, start_id, close_id, btn_key, btn_value }) {
        this.data = data;
        this.start_id = start_id;
        this.close_id = close_id;
        this.btn_key = btn_key;
        this.btn_value = btn_value;

        this.renderButton();
    }
    renderButton() {
        const btnHtml = `
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div 
                    class="btn btn-primary start-btn" 
                    style="border-radius: 10px 0px 0px 10px;" 
                    data-id="${this.start_id}"
                >
                    ${this.btn_key}: ${this.btn_value}
                </div>
                <div style="background-color: white; width: 1px;"></div>
                <div 
                    class="btn btn-primary close-btn" 
                    style="border-radius: 0px 10px 10px 0px;" 
                    data-id="${this.close_id}"
                >
                    x
                </div>
            </div>
        `;

        $('#dynamic-buttons-container').append(btnHtml);
    }

    isClicked(button_id) {
        let isClicked = false;
        $(document).on('click', `[data-id="${button_id}"]`, function () {
            isClicked = true;
        });
        return isClicked;
    }
}
