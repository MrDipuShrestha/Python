from prettytable import PrettyTable

table = PrettyTable() # creating an object

table.add_column("Pokemon Type",["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "r"
print(table)