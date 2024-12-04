# 1

grid = Grid(10, 10)

# 2

grid.initialise_simulation()

# 3

for bact in grid.bacteria_list:
    plt.scatter(bact.x, bact.y, c="blue")
    plt.grid(True)
    print(bact.x, bact.y, "bacteria age: ", bact.age)

    # 4 Add random food on the grid

    grid.initialise_food()

    # 5 Visualize Food and Bacteria

for bact in grid.bacteria_list:
    plt.scatter(bact.x, bact.y, c="blue")
    plt.grid(True)
    print("Bacteria position on the Grid", "(", bact.x, ",",
          bact.y, ")", "Current bacteria age: ", bact.age)

for food in grid.food_list:
    plt.scatter(food.x, food.y, c="red")
    plt.grid(True)
    print("Food position on the Grid", "(", food.x, ",", food.y, ")")

    # 6 Move Bacteria

    grid.move_bacteria()

    # 7
