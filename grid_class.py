class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bacteria_list = []

    def add_bacteria(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
          bacteria = Bacteria(x, y)
          self.bacteria_list.append(bacteria)
        else:
            print("Pozycja poza zakresem!")

    def initialise_simulation(self):
      nb_bact = random.randint(1, 11)
      for i in range(nb_bact):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        self.add_bacteria(x,y)

    def move_bacteria(self):
        for bacteria in self.bacteria_list:
            bacteria.move()#self.width, self.height)