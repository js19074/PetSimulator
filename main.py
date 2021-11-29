# Data Storage
names = []
weight = []

# Data Creation
print("Enter the name of your first pet, or type XXX to quit")
name_input = input()

while name_input != "XXX":
    names.append(name_input)
    print("Enter a weight for your pet")
    weight_input = input()
    weight.append(int(weight_input))
    print("Enter the name of your next pet, or type XXX to quit")
    name_input = input()


# Modifying/Adjusting Data
number_of_pets = len(names)
for i in range(number_of_pets):
    print("F = feed | E = exercise | Q = quit")
    action_input = input()
    while action_input != "Q":
        if action_input == "F":
            print("Enter the amount you would like to feed")
            amount = input()
            weight[i] += int(amount)

        elif action_input == "E":
          print("Enter the amount you would like to exercise")
          amount = input()
          weight[i] -= int(amount)

        print("F = feed | E = exercise | Q = quit")
        action_input = input()

# Output Data
for i in range(number_of_pets):
    print(names[i])
    if weight[i] > 200:
      print("weights", weight[i], "and is unhappy with their weight")

    elif weight[i] < 0:
        print("is starving and you should think about your actions")

    else:
        print("weighs", weight[i], "and is happy with their weight")
      