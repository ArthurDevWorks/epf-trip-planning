<h2>Login</h2>
<form method="post">
  <input type="email" name="email" placeholder="Email" required>
  <input type="password" name="senha" placeholder="Senha" required>
  <button type="submit">Entrar</button>
</form>
% if erro:
  <p style="color:red">{{erro}}</p>
% end
<a href="/register">Não tem conta? Cadastre-se</a>
