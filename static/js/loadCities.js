const apiKey = 'cf6cd27c03f944bf8a5653c04cc3915c';
let timeoutId;

document.getElementById('local').addEventListener('input', function () {
  const text = this.value;
  clearTimeout(timeoutId);
  if (text.length < 2) {
    document.getElementById('sugestoes').style.display = 'none';
    return;
  }

  timeoutId = setTimeout(() => {
    fetch(`https://api.geoapify.com/v1/geocode/autocomplete?text=${encodeURIComponent(q)}&type=city&limit=5&apiKey=${apiKey}`)
      .then(res => res.json())
      .then(data => {
        const ul = document.getElementById('sugestoes');
        ul.innerHTML = ''; // Limpa a lista antes de adicionar novas sugestões
        if (data.features && data.features.length > 0) {
          data.features.forEach(f => {
            const city = f.properties.formatted;
            const li = document.createElement('li');
            li.textContent = city;
            li.onclick = () => {
              document.getElementById('local').value = city;
              ul.innerHTML = ''; // Limpa a lista ao selecionar uma sugestão
              ul.style.display = 'none'; // Esconde as sugestões
            };
            ul.appendChild(li);
          });
          ul.style.display = 'block'; // Exibe a lista de sugestões
        } else {
          ul.innerHTML = '<li>Nenhuma sugestão encontrada</li>';
          ul.style.display = 'block'; // Exibe mensagem de "nenhuma sugestão"
        }
      })
      .catch(error => {
        console.error('Erro na requisição:', error);
      });
  }, 300);
});

// Esconde a lista de sugestões se o usuário clicar fora do campo de input ou da lista
document.addEventListener('click', function(event) {
  if (!document.getElementById('local').contains(event.target) && !document.getElementById('sugestoes').contains(event.target)) {
    document.getElementById('sugestoes').style.display = 'none';
  }
});
