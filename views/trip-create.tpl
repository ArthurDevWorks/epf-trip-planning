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
      <div class="button-row">
        <button type="button" id="consultarPrevisao" class="btn-consultar">
          Consultar Previsão
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
          </svg>
        </button>
        <button type="submit" id="criarViagem" class="btn-criar">
        Criar Viagem
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
          </svg>
        </button>
      </div>
    </form>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
  <script src="/static/js/loadCities.js"></script>

  <script>
    async function buscarPrevisao(event) {
      event.preventDefault();

      const local = document.getElementById("local").value;
      const dt_begin = document.getElementById("dt_begin").value;
      const dt_end = document.getElementById("dt_end").value;

      try {
        const response = await fetch('/api/weather', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            local: local,
            dt_begin: dt_begin,
            dt_end: dt_end
          })
        });

        if (response.ok) {
          const data = await response.json();
          console.log("API Response:", data);

          if (data.error) {
            Swal.fire({
              title: 'Erro!',
              text: data.error,
              icon: 'error',
              confirmButtonText: 'Ok'
            });
            return;
          }

          let weatherInfo = '';
          data.forecast.forEach(day => {
            weatherInfo += `
              <strong>${day.date}</strong><br>
              ${day.description} <br>
              Mín: ${day.temp_min}°C | Máx: ${day.temp_max}°C
              <br><img src="https://openweathermap.org/img/wn/${day.icon}@2x.png">
              <hr>
            `;
          });

          const result = await Swal.fire({
            title: 'Previsão do Tempo',
            html: weatherInfo,
            icon: 'info',
            showCancelButton: false,
            confirmButtonText: 'Fechar',
            focusCancel: true,
            reverseButtons: true,
          });
        } else {
          throw new Error('Falha na requisição da previsão do tempo');
        }
      } catch (error) {
        console.error("Erro ao buscar previsão do tempo:", error);
        Swal.fire({
          title: 'Erro!',
          text: 'Erro ao buscar previsão do tempo. Tente novamente.',
          icon: 'error',
          confirmButtonText: 'Ok'
        });
      }
    }

    // Adicionando o evento de click para o botão de Consultar Previsão
    document.getElementById("consultarPrevisao").addEventListener("click", buscarPrevisao);
  </script>
</body>
</html>
