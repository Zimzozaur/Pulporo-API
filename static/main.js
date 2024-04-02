function setLedgerCookie(name, value) {
    document.cookie = `${name}=${value}; expires=${setExpireDate()}; path=/ledger`;
    location.reload();
}

function setLedgerDateCookie(forward) {
    const month = getCookie('ledger-month') * 1;
    const year = getCookie('ledger-year') * 1;
    const date = Boolean(month) && Boolean(year) ? new Date(year, month) : new Date()

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