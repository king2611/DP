import random
    
def generate_password(num_words):
    with open('GeneratePass.txt', 'r') as file:
        words = [line.strip() for line in file if line.strip()]

    random_words = random.sample(words, num_words)
    password = ''.join(random_words)
    return password

print("Password Generator")
pass_length = int(input("Enter the Length of the Password: "))        # In Number of Words ...

# Generate the password
password = generate_password(pass_length)
print(f"Generated Password: {password}")
