
# 1
people = [
    {
        'name': 'Cian', 'age': 28, 'hobbies': ['Muay Thai', 'Coding']
    }, {
        'name': 'Frank', 'age': 2, 'hobbies': ['Eating', 'Playing Fetch']
    }
]

# 2
people_names = [person['name'] for person in people]

# 3
is_everyone_older_than_20 = all([person['age'] > 20 for person in people])

# 4
dup_people = [person.copy() for person in people]
dup_people[0]['name'] = 'Not Cian'

# 5
person_1, person_2 = people
