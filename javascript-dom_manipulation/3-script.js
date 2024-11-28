document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");

    const toggleButton = document.getElementById("toggle_header");

    toggleButton.addEventListener("click", () => {
        if (header.classList.contains("red")) {
            header.classList.replace("red", "green");
        } else {
            header.classList.replace("green", "red");
        }
    });
});
