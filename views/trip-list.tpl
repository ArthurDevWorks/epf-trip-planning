<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Minhas Viagens | Trip Planner</title>
  <link rel="stylesheet" href="/static/css/trip-list.css" />
</head>
<body>
  <div class="container">
    <h1>Minhas Viagens</h1>
    % if trips:
    <table class="trip-table">
      <thead>
        <tr>
          <th>Destino</th>
          <th>Data de Início</th>
          <th>Data de Término</th>
        </tr>
      </thead>
      <tbody>
        % for trip in trips:
        <tr>
          <td>{{ trip['local'] }}</td>
          <td>{{ trip['dt_begin'] }}</td>
          <td>{{ trip['dt_end'] }}</td>
        </tr>
        % end
      </tbody>
    </table>
    % else:
    <p class="empty-msg">Você ainda não possui viagens cadastradas.</p>
    % end
    <div class="back-button-container">
      <a href="/trip"><button class="back-btn">Voltar</button></a>
    </div>
  </div>
</body>
</html>
