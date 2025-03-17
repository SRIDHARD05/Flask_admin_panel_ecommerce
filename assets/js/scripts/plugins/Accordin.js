class Accordion {
    constructor(containerId, items) {
        this.container = containerId ? document.querySelector(containerId) : document.createElement('div');
        this.items = Array.isArray(items) ? items : [];
        this.accordionElements = new Map();
        this.titleToUUID = new Map();
        this.renderAccordion();
    }

    renderAccordion() {
        const card = document.createElement('div');
        card.classList.add('card', 'card-body');

        const accordionContainer = document.createElement('div');
        accordionContainer.classList.add('accordion', 'accordion-flush');

        this.items.forEach(item => {
            const accordionItem = this.createAccordionItem(item);
            accordionContainer.appendChild(accordionItem);
        });

        card.appendChild(accordionContainer);
        this.container.appendChild(card);
    }

    createAccordionItem(item) {
        const uniqueId = crypto.randomUUID();

        const accordionItem = document.createElement('div');
        accordionItem.classList.add('accordion-item', 'mb-3');
        accordionItem.id = `item-${uniqueId}`;

        const accordionHeader = document.createElement('h6');
        accordionHeader.classList.add('accordion-header');
        accordionHeader.id = `heading-${uniqueId}`;

        const button = document.createElement('button');
        button.classList.add('accordion-button', 'collapsed', 'border-bottom', 'font-weight-bold');
        button.type = 'button';
        button.innerHTML = `
            ${item.title}
            <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0 me-3"></i>
            <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0 me-3"></i>`;
        button.setAttribute('aria-expanded', 'false');
        button.setAttribute('aria-controls', `collapse-${uniqueId}`);

        button.addEventListener('click', () => this.toggleAccordion(uniqueId, button));

        accordionHeader.appendChild(button);
        accordionItem.appendChild(accordionHeader);

        const collapseDiv = document.createElement('div');
        collapseDiv.id = `collapse-${uniqueId}`;
        collapseDiv.classList.add('accordion-collapse', 'collapse');
        collapseDiv.setAttribute('aria-labelledby', `heading-${uniqueId}`);

        const accordionBody = document.createElement('div');
        accordionBody.classList.add('accordion-body', 'text-sm', 'opacity-8');
        accordionBody.innerHTML = item.page_content;

        collapseDiv.appendChild(accordionBody);
        accordionItem.appendChild(collapseDiv);

        this.accordionElements.set(uniqueId, {
            item: accordionItem,
            header: accordionHeader,
            button: button,
            collapse: collapseDiv,
            body: accordionBody,
        });

        this.titleToUUID.set(item.title.trim(), uniqueId);  // Store title mapping

        return accordionItem;
    }

    toggleAccordion(id) {
        const target = this.accordionElements.get(id);
        if (!target) return;

        const isOpen = target.collapse.classList.contains('show');
        this.accordionElements.forEach(({ collapse, button }) => {
            collapse.classList.remove('show');
            button.setAttribute('aria-expanded', 'false');
        });

        if (!isOpen) {
            target.collapse.classList.add('show');
            target.button.setAttribute('aria-expanded', 'true');
        }
    }

    getAccordionElements(container = this.container) {
        const accordionContainer = container.querySelector('.accordion');

        const items = Array.from(container.querySelectorAll(':scope > .card .accordion-item')).map(item => {
            const header = item.querySelector('.accordion-header');
            const button = item.querySelector('.accordion-button');
            const content = item.querySelector('.accordion-body');

            let nestedItems = [];
            if (content) {
                const nestedAccordion = content.querySelector('.accordion');
                if (nestedAccordion) {
                    nestedItems = this.getAccordionElements(nestedAccordion).items;
                }
            }

            return {
                id: header?.id || null,
                title: button?.textContent.trim() || null,
                header: header ? header.outerHTML : null,
                button: button ? button.outerHTML : null,
                content: content ? content.outerHTML : null,
                nestedItems
            };
        });

        return {
            accordionContainer: accordionContainer ? accordionContainer.outerHTML : null,
            items
        };
    }

    addHtmlToAccordion(title, htmlcode) {
        const targetItem = this.items.find(item => item.title === title);
        if (!targetItem) {
           //  console.error(`Accordion item with title "${title}" not found.`);
            return;
        }

        const accordionBody = Array.from(this.container.querySelectorAll('.accordion-body'))
            .find(body => body.textContent.trim().startsWith(targetItem.page_content.trim()));

        if (!accordionBody) {
           //  console.error(`Accordion body for title "${title}" not found.`);
            return;
        }

        const htmlFragment = document.createElement('div');
        htmlFragment.innerHTML = htmlcode;
        accordionBody.appendChild(htmlFragment);
    }

    addParaToAccordion(title, paragraph) {
        const targetItem = this.items.find(item => item.title === title);
        if (!targetItem) {
           //  console.error(`Accordion item with title "${title}" not found.`);
            return;
        }

        const accordionBody = Array.from(this.container.querySelectorAll('.accordion-body'))
            .find(body => body.textContent.trim().startsWith(targetItem.page_content.trim()));

        if (!accordionBody) {
           //  console.error(`Accordion body for title "${title}" not found.`);
            return;
        }

        const para = document.createElement('p');
        para.textContent = paragraph;
        accordionBody.appendChild(para);
    }

    addAccordionToAccordion(title, content) {
        const targetItem = this.items.find(item => item.title === title);
        if (!targetItem) {
           //  console.error(`Accordion item with title "${title}" not found.`);
            return;
        }

        const accordionBody = Array.from(this.container.querySelectorAll('.accordion-body'))
            .find(body => body.textContent.trim().startsWith(targetItem.page_content.trim()));

        if (!accordionBody) {
           //  console.error(`Accordion body for title "${title}" not found.`);
            return;
        }

        const subAccordionContainerId = `sub-accordion-${crypto.randomUUID()}`;
        const subAccordionContainer = document.createElement('div');
        subAccordionContainer.id = subAccordionContainerId;
        accordionBody.appendChild(subAccordionContainer);

        const subAccordion = new Accordion(`#${subAccordionContainerId}`, ...content);
        return subAccordion;
    }

    addTableToAccordion(title, tableData) {
        const uuid = this.titleToUUID.get(title.trim());
        if (!uuid) {
           //  console.error(`Accordion item with title "${title}" not found.`);
            // console.log('Existing titles:', [...this.titleToUUID.keys()]);
            return;
        }

        const accordionBody = this.accordionElements.get(uuid)?.body;
        if (!accordionBody) {
           //  console.error(`Accordion body for title "${title}" not found.`);
            return;
        }

        // Create table
        const table = document.createElement('table');
        table.classList.add('table', 'table-bordered', 'table-sm');

        const { table_header, table_content } = tableData;

        if (table_header && Array.isArray(table_header)) {
            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');
            table_header.forEach(header => {
                const th = document.createElement('th');
                th.textContent = header;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);
        }

        const tbody = document.createElement('tbody');
        table_content.forEach(rowData => {
            const row = document.createElement('tr');
            rowData.forEach(cellData => {
                const td = document.createElement('td');
                td.textContent = cellData;
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        accordionBody.appendChild(table);
    }

    updateTitle(originalTitle, newTitle) {
        const uuid = this.titleToUUID.get(originalTitle.trim());
        if (!uuid) {
           //  console.error(`Accordion item with title "${originalTitle}" not found.`);
            return;
        }

        const accordionButton = this.accordionElements.get(uuid)?.button;
        if (!accordionButton) {
           //  console.error(`Accordion button for title "${originalTitle}" not found.`);
            return;
        }

        accordionButton.innerHTML = `
            ${newTitle}
            <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0 me-3"></i>
            <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0 me-3"></i>`;
    }

    addParagraph(title, paragraph) {
        const uuid = this.titleToUUID.get(title.trim());
        if (!uuid) {
           //  console.error(`Accordion item with title "${title}" not found.`);
            return;
        }

        const accordionBody = this.accordionElements.get(uuid)?.body;
        if (!accordionBody) {
           //  console.error(`Accordion body for title "${title}" not found.`);
            return;
        }

        const para = document.createElement('p');
        para.innerHTML = paragraph;  // Use innerHTML to render links properly
        accordionBody.appendChild(para);
    }

}
