import random

def generate_reference_string(length):
    reference_string = [str(random.randint(0, 9)) for _ in range(length)]
    return " ".join(reference_string)

# Example usage
length = 100    # Length of the reference string
reference_string = generate_reference_string(length)
print("Reference String:")
print(reference_string)
