<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/style.css">
    <title>Cadastro</title>
</head>
<body>
    <div class="cad-box">
        <h2>Cadastre-se</h2>
        <form method="post">
            <div class="user-box">
                <input type="text" name="name" id="name" class="input-user" placeholder="Nome" required>
                <label for="name" class="label-input">Nome</label>
            </div>
            <div class="user-box">
                <input type="text" name="email" id="email" class="input-user" placeholder="Email" required>
                <label for="email" class="label-input">Email</label>
            </div>
            <div class="user-box">
                <input type="date" name="birthdate" id="birthdate" class="input-user" required>
                <label for="birthdate" class="label-input">Data de Nascimento</label>
            </div>
            <div class="user-box">
                <input type="password" name="password" id="password" class="input-user" placeholder="Senha" required>
                <label for="password" class="label-input">Senha</label>
            </div>
            <input type="submit" value="Cadastrar" name="submit" id="submit">
            % if erro:
            <p class="error">{{erro}}</p>
            % end
        </form>
    </div>
</body>
</html>