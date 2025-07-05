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
    <div class="back-button-container">
      <a href="/trip"><button class="back-btn">Voltar</button></a>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
  <script src="/static/js/loadCities.js"></script>
  <script src="/static/js/selectWeather.js"></script>
</body>

</html>
