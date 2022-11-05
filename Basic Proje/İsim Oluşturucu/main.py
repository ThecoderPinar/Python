import random

def generate_name():
    first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

for i in range(5):
    print(generate_name())