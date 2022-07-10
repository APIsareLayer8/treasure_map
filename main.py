row1 = ["⬜️", "⬜️", "⬜️"]  # Three lists: row1, row2, row3
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
my_map = [row1, row2, row3]  # container for the three lists
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])  # assigns the first number in the variable {position} to index 0
vertical = int(position[1])  # assigns the second number in the variable {position} to index 1

selected_row = my_map[vertical - 1]  # creates a new object {selected_row}
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
