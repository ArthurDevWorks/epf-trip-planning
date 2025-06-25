<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/style.css">
    <title>Login</title>
</head>
<body>
    <div class="login-box">
        <h2>Login</h2>
        <form method="post">
            <div class="user-box">
                <input type="text" name="email" id="email" class="input-user" required>
                <label for="email" class="label-input">Email</label>
            </div>
            <div class="user-box">
                <input type="password" name="password" id="password" class="input-user" required>
                <label for="password" class="label-input">Senha</label>
            </div>
            <div class="btn">
                <input type="submit" value="Entrar" name="submit" id="submit">
            </div>
            <form action="{{ url_for('user.login') }}" method="POST">
                <input type="text" name="username" required>
                <input type="password" name="password" required>
                <button type="submit">Login</button>
            </form>
        </form>
        % if erro:
            <p class="error">{{erro}}</p>
        % end
        <p class="link">Não tem conta? <a href="/register">Cadastre-se</a></p>
    </div>
</body>
</html>