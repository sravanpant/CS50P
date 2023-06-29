students = [
    {"name": "Hermione", "house": "Gryffindor", "patronas": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronas": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronas": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherine", "patronas": None},
]

for student in students:
    print(student["name"], student["house"], student["patronas"], sep=", ")
