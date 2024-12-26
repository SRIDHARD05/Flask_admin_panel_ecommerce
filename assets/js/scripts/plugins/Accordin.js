class Accordion {
    constructor(containerId, ...items) {
        this.container = containerId ? document.querySelector(containerId) : document.createElement('div');
        this.items = items;
        this.renderAccordion();
    }

    renderAccordion() {
        const card = document.createElement('div');
        card.classList.add('card', 'card-body');

        const accordionContainer = document.createElement('div');
        accordionContainer.classList.add('accordion', 'accordion-flush');

        this.items.forEach(item => {
            const accordionItem = this.createAccordionItem(item, true);
            accordionContainer.appendChild(accordionItem);
        });

        card.appendChild(accordionContainer);
        this.container.appendChild(card);
    }

    createAccordionItem(item, isMain = false) {
        const uniqueId = crypto.randomUUID();

        const accordionItem = document.createElement('div');
        accordionItem.classList.add('accordion-item');

        const accordionHeader = document.createElement('h2');
        accordionHeader.classList.add('accordion-header');
        accordionHeader.id = `heading-${uniqueId}`;

        const button = document.createElement('button');
        button.classList.add('accordion-button', 'collapsed');
        button.type = 'button';
        button.innerHTML = `
            ${item.title}
            <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0 me-3"></i>
            <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0 me-3"></i>`;
        button.setAttribute('aria-expanded', 'false');
        button.setAttribute('aria-controls', `collapse-${uniqueId}`);

        button.addEventListener('click', () => {
            const collapseDiv = document.getElementById(`collapse-${uniqueId}`);
            collapseDiv.classList.toggle('show');
            button.setAttribute('aria-expanded', collapseDiv.classList.contains('show'));
        });

        accordionHeader.appendChild(button);
        accordionItem.appendChild(accordionHeader);

        const collapseDiv = document.createElement('div');
        collapseDiv.id = `collapse-${uniqueId}`;
        collapseDiv.classList.add('accordion-collapse', 'collapse');
        collapseDiv.setAttribute('aria-labelledby', `heading-${uniqueId}`);

        const accordionBody = document.createElement('div');
        accordionBody.classList.add('accordion-body');
        accordionBody.innerHTML = item.page_content || '';

        // Handle sub-items (sub-accordions)
        if (item.subItems && Array.isArray(item.subItems)) {
            if (item.subItems.every(subItem => subItem instanceof Accordion)) {
                item.subItems.forEach(subAccordion => {
                    accordionBody.appendChild(subAccordion.container.firstChild);
                });
            } else {
                const subAccordionContainer = document.createElement('div');
                subAccordionContainer.classList.add('accordion', 'accordion-flush');
                item.subItems.forEach(subItem => {
                    const subAccordionItem = this.createAccordionItem(subItem, false);
                    subAccordionContainer.appendChild(subAccordionItem);
                });
                accordionBody.appendChild(subAccordionContainer);
            }
        }

        if (isMain) {
            const mainCardBody = document.createElement('div');
            mainCardBody.classList.add('card-body');
            mainCardBody.appendChild(accordionBody);
            collapseDiv.appendChild(mainCardBody);
        } else {
            collapseDiv.appendChild(accordionBody);
        }

        accordionItem.appendChild(collapseDiv);
        return accordionItem;
    }

    findAccordionBody(title) {
        const targetItem = this.items.find(item => item.title === title);
        if (!targetItem) {
            console.error(`Accordion item with title "${title}" not found.`);
            return null;
        }

        return Array.from(this.container.querySelectorAll('.accordion-body'))
            .find(body => body.textContent.includes(targetItem.page_content));
    }

    addAccordionToAccordion(title, subItems) {
        const accordionBody = this.findAccordionBody(title);
        if (!accordionBody) return;

        const subAccordionContainer = document.createElement('div');
        subAccordionContainer.classList.add('accordion', 'accordion-flush');

        subItems.forEach(subItem => {
            const subAccordionItem = this.createAccordionItem(subItem, false);
            subAccordionContainer.appendChild(subAccordionItem);
        });

        accordionBody.appendChild(subAccordionContainer);
    }

    addAccordionEditTitle(title, newTitle) {
        const targetHeader = Array.from(this.container.querySelectorAll('.accordion-header button'))
            .find(button => button.innerHTML.includes(title));
        if (targetHeader) {
            targetHeader.innerHTML = targetHeader.innerHTML.replace(title, newTitle);
        } else {
            console.error(`Accordion with title "${title}" not found.`);
        }
    }

    addAccordionToHTMLContent(title, htmlContent) {
        const accordionBody = this.findAccordionBody(title);
        if (!accordionBody) return;

        const htmlFragment = document.createElement('div');
        htmlFragment.innerHTML = htmlContent;
        accordionBody.appendChild(htmlFragment);
    }

    addAccordionToTable(title, tableData) {
        const accordionBody = this.findAccordionBody(title);
        if (!accordionBody) return;

        const table = document.createElement('table');
        table.classList.add('table', 'table-bordered', 'table-sm');

        // Create headers
        if (tableData.title && Array.isArray(tableData.title)) {
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');
            tableData.title.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);
        }

        // Create rows
        const tbody = document.createElement('tbody');
        tableData.table_data.forEach(row => {
            const tr = document.createElement('tr');
            Object.values(row).forEach(cell => {
                const td = document.createElement('td');
                td.textContent = cell;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);

        accordionBody.appendChild(table);
    }
}
