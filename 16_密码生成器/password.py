import random
import string

def generate_password(length=12):
    characters=string.ascii_letters+string.digits+"#@$%!00"
    password=[
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("#@$%!00")
    ]
    for _ in range(length-3):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)

print(generate_password())


