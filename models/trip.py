class Trip:

  #construtor com as variaveis da classe de viagem
  def __init__(self,id,user_id,dt_begin,dt_end,local):
    self.id = id
    self.user_id = user_id
    self.dt_begin = dt_begin
    self.dt_end = dt_end
    self.local = local