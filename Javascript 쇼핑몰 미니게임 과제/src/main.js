function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLStirng(item)).join('');
}

function createHTMLStirng(item) {
    return `
        <li class="item">
            <img src="${item.image}" alt="${item.type}" class="items__thumbnail">
            <span class="description">${item.gender}, ${item.size}</span>
        </li>
    `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if (key == null || value == null) {
        return;
    }

    displayItems(items.filter(item => item[key] === value));
}

function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.menu');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', () => onButtonClick(event, items));
}

loadItems()
    .then(items => {
        displayItems(items);
        setEventListeners(items);
    })
    .catch(console.log);