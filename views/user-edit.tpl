<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Editar Cadastro | Trip Planner</title>
  <link rel="stylesheet" href="/static/css/user-edit.css" />
</head>
<body>
  <div class="container">
    <h1>Editar Cadastro</h1>
    <form method="post">
      <div class="fields-row">
        <div class="field">
          <label for="name">Nome</label>
          <input type="text" id="name" name="name" required
            value="{{user['name'] if user else ''}}">
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required
            value="{{user['email'] if user else ''}}">
        </div>
        <div class="field">
          <label for="birthdate">Data de Nascimento</label>
          <input type="date" id="birthdate" name="birthdate" required
            value="{{user['birthdate'] if user else ''}}">
        </div>
        <div class="field">
          <label for="password">Senha</label>
          <input type="password" id="password" name="password" required value="">
        </div>
         <div class="field">
          <label for="password-confirmation">Confirmação de Senha</label>
          <input type="password" id="password-confirmation" name="password-confirmation" required
          value="">
        </div>
      </div>
      <button type="submit">
        Editar Cadastro
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M5 12H19M19 12L12 5M19 12L12 19"/>
        </svg>
      </button>
    </form>
    <div class="back-button-container">
      <a href="/trip"><button class="back-btn">Voltar</button></a>
    </div>
  </div>
</body>
</html>
