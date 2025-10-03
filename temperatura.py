class temp:
  def __init__(self):
    self.data = []

  def leer(self):
    self.data = [80, 72, 95, 82, 79, 72, 85]

  def procesar(self):
    self.data = [(x - 32) / 1.8 for x in self.data] 

  def print(self): 
    for item in self.data:
      print(item)

tempe = temp() 
tempe.leer()
tempe.procesar()
tempe.print() 