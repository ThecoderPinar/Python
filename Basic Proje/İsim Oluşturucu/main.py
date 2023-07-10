from random import choice

def generate_name():

    """ Return the name that is a mix of popular personnalities """
    
    first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
    last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie", "Dawkins"]
    
    return f"{choice(first_names)} {choice(last_names))"

for _ in range(5):
    print(generate_name())
