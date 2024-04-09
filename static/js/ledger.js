const incomeBt = document.querySelector('.income-bt');
const outcomeBt = document.querySelector('.outcome-bt');
const oneOffBt = document.querySelector('.one-off-bt');
const allBt = document.querySelector('.all-bt');
const recurringBt = document.querySelector('.recurring-bt');

const ledgerMenuActive = 'ledger-menu--active';

document.addEventListener('DOMContentLoaded', function() {
    setCalendar();
});

// I need 2 scripts to check if IO has a cookie and set class
// and does is-rec has a cookie and set class

window.onload = function () {
    setActiveButtons();
}

function setActiveButtons() {
    const isOutcome = getCookie('is-outcome');
    const isOneOff = getCookie('is-one-off');

    if (isOutcome === 'true' || isOutcome === null) {
        incomeBt.classList.remove(ledgerMenuActive);
        outcomeBt.classList.add(ledgerMenuActive);
    } else {
        incomeBt.classList.add(ledgerMenuActive);
        outcomeBt.classList.remove(ledgerMenuActive);
    }

    if (isOneOff === 'all' || isOneOff === null) {
        allBt.classList.add(ledgerMenuActive);
        oneOffBt.classList.remove(ledgerMenuActive);
        recurringBt.classList.remove(ledgerMenuActive);
    } else if (isOneOff === 'one-off') {
        oneOffBt.classList.add(ledgerMenuActive);
        allBt.classList.remove(ledgerMenuActive);
        recurringBt.classList.remove(ledgerMenuActive);
    } else {
        recurringBt.classList.add(ledgerMenuActive);
        allBt.classList.remove(ledgerMenuActive);
        oneOffBt.classList.remove(ledgerMenuActive);
    }
}


function setLedgerCookie(name, value) {
    document.cookie = `${name}=${value}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setLedgerDateCookie(forward) {
    const month = getCookie('ledger-month');
    const year = getCookie('ledger-year') * 1;

    let date;
    if (month === null) {
        date = new Date();
    } else {
        date = new Date(year, month * 1);
    }

    if (forward) {
        date.setMonth(date.getMonth() + 1);
    } else {
        date.setMonth(date.getMonth() - 1);
    }
    document.cookie = `ledger-month=${date.getMonth()}; expires=${setExpireDate()}; path=/ledger`;
    document.cookie = `ledger-year=${date.getFullYear()}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setLedgerTodayCookie() {
    const date = new Date();
    document.cookie = `ledger-month=${date.getMonth()}; expires=${setExpireDate()}; path=/ledger`;
    document.cookie = `ledger-year=${date.getFullYear()}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setLedgerCalendarCookie() {
    const monthInput = document.getElementById('monthCalendar');
    if (monthInput.value.length !== 7){
        return;
    }
    const yearMonth = monthInput.value.split('-');
    document.cookie = `ledger-month=${yearMonth[1] * 1 - 1}; expires=${setExpireDate()}; path=/ledger`;
    document.cookie = `ledger-year=${yearMonth[0]}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setCalendar() {
    const monthInput = document.getElementById('monthCalendar');
    const month = getCookie('ledger-month');
    const year = getCookie('ledger-year');
    if (!month) {
        const date = new Date();
        monthInput.value = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}`;
    } else {
        monthInput.value = `${year}-${(month * 1 + 1).toString().padStart(2, '0')}`;
    }
}

function setExpireDate() {
    const now = new Date();
    const expireTime = new Date(now.getTime() + (30 * 24 * 60 * 60 * 1000)); // 1 month
    return expireTime.toUTCString();
}


function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [cookieName, cookieValue] = cookie.trim().split('=');
        if (cookieName === name) {
            return decodeURIComponent(cookieValue)
        }
    }
    return null;
}