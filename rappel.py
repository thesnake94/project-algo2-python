"""
Déclaration variable
"""
from pprint import pprint
variable_int = 1
variable_array = []
variable_str = ""

"""
Déclaration tableau
"""
variable_array_int = [1, 2, 3, 4, 5]
variable_array_int_str = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]

"""
Ajout d'une valeur dans un tableau
"""
print(variable_array_int)
variable_array_int.append(6)
print(variable_array_int)
variable_array_int.append(["a", "b", "c"])
print(variable_array_int)

"""
Comment itérer sur un tableau
"""

variable_array_str = ["a", "b", "c", "d", "e"]
for str_var in variable_array_str:
    print(str_var)
print()
integer_array = 0
while integer_array < len(variable_array_int_str):
    print(variable_array_int_str[integer_array])
    integer_array += 2
print()
for integer_array in range(0, len(variable_array_int_str), 2):
    print(variable_array_int_str[integer_array])
print()
"""
Les conditions et les vérifications de types
"""
variable_array_int_str_mix = ["a", "b", 1, 2, "c", 3, "d", 4, 5, "e"]
for integer_array in range(len(variable_array_int_str_mix)):
    tmp = variable_array_int_str_mix[integer_array]
    if type(tmp) is int:
        print(tmp)

if "c" not in variable_array_int_str_mix:
    print("c is not in variable_array_int_str_mix")

"""
Note valable pour les if et les while :
== : égalité
!= : différent
< : inférieur
> : supérieur
<= : inférieur ou égal
>= : supérieur ou égal
"""

"""
Déclaration d'un dictionnaires
"""
print()

dictionnary = {
    "key1": "value1",
    1: "value2",
    2: 4,
    "key2": [1, 2, 3, 4, 5],
    "key3": {
        "key4": "value3",
        "key5": "value4",
        3: 6
    }
}
"""
Accès aux valeur d'un dictonnaire
pprint permet un print plus lisible en cas de dictionnaire imbriqué
"""
print(dictionnary["key1"])
print(dictionnary["key2"])
print(dictionnary["key3"])
print(dictionnary["key3"]["key4"])

"""
Itérer sur les couples clés/valeurs d'un dictionnaire
"""
for key, value in dictionnary.items():
    print("key : ", key, "//value : ", value)

dictionnary['key6'] = "add value 6"
pprint(dictionnary)
print()

dictionnary.update({"key1": "new value 1"})
pprint(dictionnary)
print()
print(dictionnary)
