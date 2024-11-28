document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

    const moviesList = document.getElementById("list_movies");

    fetch(apiUrl)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            data.results.forEach((movie) => {
                const listItem = document.createElement("li");
                listItem.textContent = movie.title;
                moviesList.appendChild(listItem);
            });
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
