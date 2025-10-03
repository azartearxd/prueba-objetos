class datos:
    def __init__(self):
      self.data = []
      self.labels = ["Nombre", "ID", "Edad", "Peso", "Teléfono", "Dirección", "Carrera"] # Added labels


    def leer(self):
       self.data = ["Adam Rafael Calderon Godinez", "231690265-5", "16", "85", "3111199558", "zaragoza y ures 141", "Ciencia de datos e inteligencia artificial"]


    def procesar(self):
      self.data[2]

    def print(self):
      for i, item in enumerate(self.data):
        print(f"{self.labels[i]}: {item}") # Modified to include labels
yo = datos()
yo.leer()
yo.procesar()
yo.print()