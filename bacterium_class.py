import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

class Bacteria:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    #self.health = 0
    #self.age = 0

  def move(self):
    #move(self, width, height):
    # 0 ruch w gore, 1 ruch w dół, 2 ruch w prawo, 3 ruch w lewo
    direction = random.randint(0, 4)
    if direction == 0:
      self.y += 1
    elif direction == 1:
      self.y -= 1
    elif direction == 2:
      self.x += 1
    elif direction == 3:
      self.x -= 1