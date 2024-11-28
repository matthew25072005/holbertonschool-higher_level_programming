document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

    const characterDiv = document.getElementById("character");

    fetch(apiUrl)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            characterDiv.textContent = data.name;
        })
        .catch((error) => {
            characterDiv.textContent = "Error fetching character data.";
            console.error("Error:", error);
        });
});
