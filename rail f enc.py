'''def rail_fence_encrypt(plaintext, key):
    # Create a list of strings for each rail
    rail = [''] * key
    direction_down = False
    row = 0

    for char in plaintext:
        rail[row] += char
        
        # Change direction when you reach the top or bottom
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1
    
    # Combine all strings to get the ciphertext
    ciphertext = ''.join(rail)
    return ciphertext

# Example usage:
plaintext =input("Enter string:")
key = int(input("Enter key:"))
ciphertext = rail_fence_encrypt(plaintext, key)
print(f"Encrypted text: {ciphertext}")'''



'''def rail_fence_decrypt(ciphertext, key):
    # Determine the length of each rail
    rail = [['\n'] * len(ciphertext) for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    # Mark the places in the grid where characters will be placed
    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        # Place marker
        rail[row][col] = '*'
        col += 1

        row += 1 if direction_down else -1

    # Fill the grid with ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the grid in a zig-zag manner to reconstruct the plaintext
    result = []
    row, col = 0, 0
    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        row += 1 if direction_down else -1
    
    plaintext = ''.join(result)
    return plaintext

# Example usage:
ciphertext = input("Enter string:")
key = int(input("Enter key:"))
plaintext = rail_fence_decrypt(ciphertext, key)
print(f"Decrypted text: {plaintext}")'''

#########################################
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            plaintext += shifted_char
        else:
            plaintext += char  # Non-alphabet characters are not changed
            
    return plaintext

# Example usage:
ciphertext = input("Enter string:")
shift = int(input("Enter key:"))
plaintext = caesar_decrypt(ciphertext, shift)
print(f"Decrypted: {plaintext}")

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            ciphertext += shifted_char
        else:
            ciphertext += char  # Non-alphabet characters are not changed
            
    return ciphertext

# Example usage:
plaintext = input("Enter string:")
shift = int(input("Enter key:"))
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Encrypted text: {ciphertext}")



