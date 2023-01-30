variable_int = 1
variable_array = []
variable_str = ""

variable_array_int = [1, 2, 3, 4, 5]
variable_array_int_str = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]

# print(variable_array_int)


variable_array_str = ["a", "b", "c", "d", "e"]


integer_array = 1
while integer_array < len(variable_array_int_str):
    print(variable_array_int_str[integer_array])
    integer_array += 2
print()
for integer_array in range(0, len(variable_array_int_str), 2):
    print(variable_array_int_str[integer_array])
print()

for integer_array in range()
