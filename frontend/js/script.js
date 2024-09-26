// URL base da API
const apiUrl = "http://localhost:5050/api/parameter"; // Ajuste a porta conforme necessário

// Função para buscar e exibir os parâmetros na tabela
async function fetchParameters() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const parameters = await response.json();
    const tableBody = document.querySelector("#table tbody");
    tableBody.innerHTML = ""; // Limpa a tabela antes de adicionar novos dados

    // Adiciona os dados recebidos à tabela
    parameters.forEach((parameter) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${parameter.name}</td>
                <td>${parameter.age}</td>
                <td>${parameter.sex}</td>
                <td>${parameter.cp}</td>
                <td>${parameter.trestbps}</td>
                <td>${parameter.chol}</td>
                <td>${parameter.fbs}</td>
                <td>${parameter.restecg}</td>
                <td>${parameter.thalach}</td>
                <td>${parameter.exang}</td>
                <td>${parameter.oldpeak}</td>
                <td>${parameter.slope}</td>
                <td>${parameter.ca}</td>
                <td>${parameter.thal}</td>
                <td>${parameter.target}</td>
                <td><button onclick="deleteParameter(${parameter.id})">Deletar</button></td>
            `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching parameters:", error);
  }
}

// Função para cadastrar novos parâmetros
async function addParameter(event) {
  event.preventDefault(); // Previne o comportamento padrão do formulário

  const formData = new FormData(document.querySelector("#parametersForm"));
  const data = Object.fromEntries(formData); // Converte FormData em objeto

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    // Após o cadastro, atualiza a tabela
    fetchParameters();
    document.querySelector("#parametersForm").reset(); // Limpa o formulário
  } catch (error) {
    console.error("Error adding parameter:", error);
  }
}

// Função para deletar parâmetros
async function deleteParameter(id) {
  try {
    const response = await fetch(`${apiUrl}/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    // Após a exclusão, atualiza a tabela
    fetchParameters();
  } catch (error) {
    console.error("Error deleting parameter:", error);
  }
}

// Adiciona event listener ao formulário
document
  .querySelector("#parametersForm")
  .addEventListener("submit", addParameter);

// Chama a função para buscar os parâmetros ao carregar a página
document.addEventListener("DOMContentLoaded", fetchParameters);
