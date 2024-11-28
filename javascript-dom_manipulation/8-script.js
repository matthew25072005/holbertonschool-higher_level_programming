window.addEventListener("load", () => {
    const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

    const helloDiv = document.getElementById("hello");

    fetch(apiUrl)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            helloDiv.textContent = data.hello;
        })
        .catch((error) => {
            console.error("Error:", error);
            helloDiv.textContent = "Error fetching translation.";
        });
});