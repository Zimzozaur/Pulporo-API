document.addEventListener('DOMContentLoaded', function() {
    setCalendar();
});

function setLedgerCookie(name, value) {
    document.cookie = `${name}=${value}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setLedgerDateCookie(forward) {
    const month = getCookie('ledger-month');
    const year = getCookie('ledger-year') * 1;

    let date = null
    if (month === null) {
        date = new Date();
    } else {
        date = new Date(year, month * 1)
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
        console.log('1');
        const date = new Date();
        monthInput.value = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}`;
    } else {
        console.log(`${year}-${(month * 1 + 1).toString().padStart(2, '0')}`);
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