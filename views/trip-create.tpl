<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Planeje sua viagem | Trip Planner</title>
  <link rel="stylesheet" href="/static/css/trip-create.css" />
</head>
<body>
  <div class="container">
    <h1>Planeje sua viagem</h1>
    <form id = "tripForm" method="post">
      <div class="fields-row">
        <div>
          <label for="dt_begin">Data de início</label>
          <input type="date" id="dt_begin" name="dt_begin" required>
        </div>
        <div>
          <label for="dt_end">Data de término</label>
          <input type="date" id="dt_end" name="dt_end" required>
        </div>
        <div>
          <label for="local">Destino</label>
          <input type="text" id="local" name="local" placeholder="Digite o destino" required>
          <ul id="sugestoes" class="autocomplete-list"></ul>
        </div>
      </div>
      <button type="submit">
        Buscar viagens
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
        </svg>
      </button>
    </form>
    <!-- Modal Clima -->
  <div id="weatherModal" class="modal">
    <div class="modal-content">
      <span class="close" onclick="fecharModal()">&times;</span>
      <h2>Previsão do Tempo</h2>
      <div id="weatherData"></div>
      <button onclick="confirmarViagem()">Confirmar Viagem</button>
    </div>
  </div>
  </div>
   <script src="/static/js/loadCities.js"></script>
</body>
</html>
<script>
document.getElementById('tripForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const local = document.getElementById('local').value;
  const dt_begin = document.getElementById('dt_begin').value;
  const dt_end = document.getElementById('dt_end').value;

  // chamada para API customizada sua (em Python Bottle)
  const res = await fetch(`/api/weather?local=${encodeURIComponent(local)}&start=${dt_begin}&end=${dt_end}`);
  const data = await res.json();

  const container = document.getElementById('weatherData');
  container.innerHTML = "";

  if (data.error) {
    container.innerHTML = `<p>${data.error}</p>`;
  } else {
    data.forecast.forEach(day => {
      container.innerHTML += `
        <p><strong>${day.date}</strong>: ${day.description}, ${day.temp}°C</p>
      `;
    });
  }

  document.getElementById('weatherModal').style.display = 'flex';
});

function fecharModal() {
  document.getElementById('weatherModal').style.display = 'none';
}

function confirmarViagem() {
  document.getElementById('tripForm').submit();
}
</script>