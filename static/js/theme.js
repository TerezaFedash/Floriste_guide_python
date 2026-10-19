// Перемикач світлої / темної теми з рожевою естетикою (Д7)
document.addEventListener("DOMContentLoaded", function () {
    const themeToggleBtn = document.getElementById("themeToggleBtn");
    const themeIcon = document.getElementById("themeIcon");
    const htmlElement = document.documentElement;

    function getCookie(name) {
        let matches = document.cookie.match(new RegExp(
            "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        ));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }

    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            let date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/; SameSite=Lax";
    }

    function applyTheme(theme) {
        htmlElement.setAttribute("data-bs-theme", theme);
        setCookie("florist_theme", theme, 30);
        localStorage.setItem("florist_theme", theme);

        if (themeIcon) {
            if (theme === "dark") {
                themeIcon.className = "bi bi-sun-fill text-warning";
            } else {
                themeIcon.className = "bi bi-moon-stars-fill text-secondary";
            }
        }
    }

    // Початкова ініціалізація
    const currentTheme = getCookie("florist_theme") || localStorage.getItem("florist_theme") || htmlElement.getAttribute("data-bs-theme") || "light";
    applyTheme(currentTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener("click", function () {
            const activeTheme = htmlElement.getAttribute("data-bs-theme");
            const newTheme = activeTheme === "dark" ? "light" : "dark";
            applyTheme(newTheme);
        });
    }
});
