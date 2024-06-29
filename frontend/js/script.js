document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("captureForm");
  const pokemonSelect = document.getElementById("pokemon_name");
  const capturesTableBody = document.querySelector("#capturesTable tbody");

  const fetchPokemons = async () => {
    const response = await fetch("http://localhost:5050/api/pokemons");
    const pokemons = await response.json();

    pokemons
      .sort((p1, p2) => (p1.name > p2.name ? 1 : -1))
      .forEach((pokemon) => {
        const option = document.createElement("option");
        option.value = pokemon.name;
        option.textContent = pokemon.name;
        pokemonSelect.appendChild(option);
      });
  };

  const fetchCaptures = async () => {
    const response = await fetch("http://localhost:5050/api/captures");
    const captures = await response.json();
    capturesTableBody.innerHTML = "";
    captures.forEach((capture) => {
      const row = document.createElement("tr");
      row.innerHTML = `
              <td>${capture.trainer_name}</td>
              <td>${capture.capture_date}</td>
              <td>${capture.pokemon_name}</td>
              <td><img src="${capture.pokemon_image}" alt="${capture.pokemon_name}"></td>
              <td><button class="delete" data-id="${capture.id}">Delete</button></td>
          `;
      capturesTableBody.appendChild(row);
    });

    document.querySelectorAll(".delete").forEach((button) => {
      button.addEventListener("click", async (event) => {
        const captureId = event.target.dataset.id;
        await fetch(`http://localhost:5050/api/captures/${captureId}`, {
          method: "DELETE",
        });
        fetchCaptures().then(() =>
          setTimeout(() => window.alert("Captura removida com sucesso!"), 1000)
        );
      });
    });
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const data = {
      trainer_name: formData.get("trainer_name"),
      capture_date: formData.get("capture_date"),
      pokemon_name: formData.get("pokemon_name"),
    };

    await fetch("http://localhost:5050/api/captures", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    form.reset();

    await fetchCaptures().then(() =>
      setTimeout(() => window.alert("Captura registrada com sucesso!"), 1_000)
    );
  });

  fetchPokemons();
  fetchCaptures();
});
