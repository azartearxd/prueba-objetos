class datos:
    def __init__(self):
      self.data = []

    def leer(self):
       self.data = ["Adam Rafael Calderon Godinez", "231690265-5", "16", "85", "3111199558", "zaragoza y ures 141", "Ciencia de datos e inteligencia artificial"]


    def procesar(self):
      self.data

    def print(self):
      for item in self.data:
        print(item)
yo = datos()
yo.leer()
yo.procesar()
yo.print()

