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
    <form method="post">
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
        </div>
      </div>
      <button type="submit">
        Buscar viagens
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
        </svg>
      </button>
    </form>
  </div>
</body>
</html>
