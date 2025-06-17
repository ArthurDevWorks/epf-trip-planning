<h2>Cadastre-se</h2>
<form method="post">
  <input type="text" name="nome" placeholder="Nome" required>
  <input type="email" name="email" placeholder="Email" required>
  <input type="password" name="senha" placeholder="Senha" required>
  <button type="submit">Cadastre-se</button>
</form>
% if erro:
  <p style="color:red">{{erro}}</p>
% end
<a href="/login">Já tem conta? Faça login</a>
