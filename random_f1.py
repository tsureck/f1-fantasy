import random as rd

constructors = [
    "Mercedes",
    "Red Bull Racing",
    "Ferrari",
    "McLaren",
    "Alfa Romeo",
    "Aston Martin",
    "Alpine",
    "AlphaTauri",
    "Williams",
    "Haas F1 Team",
]

constr_1 = constructors[rd.randrange(0,9)]

constr_2 = constructors[rd.randrange(0,9)]

while(constr_2 == constr_1):
    constr_2 = constructors[rd.randrange(0,9)]

print("{0} vs. {1}".format(constr_1, constr_2))