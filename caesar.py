def alphabet_position(letter):
    """Finds the position of a letter in the alphabet. a = 0, b = 1 etc."""
    # Convert to uppercase to make it easier to work with
    letter = letter.upper()

    # ord() returns the ascii value of a character
    ascii_value = ord(letter)

    # Subtract ascii value of 'A' to get a number 0 - 25
    return ascii_value - ord('A')

def rotate_character(char, rot):
    """Encrypts an individual char based on the inputted rotation value."""
    # Return char if it is not a letter
    if not char.isalpha():
        return char

    # rot1 = rot27 for example, so this simplifies rot values
    if rot > 26:
        rot = rot % 26

    # Get the position of the letter in the alphabet
    alpha_pos = alphabet_position(char)

    # Apply rotation
    new_letter_pos = alpha_pos + rot

    # Add ascii value of 'A' or 'a' depending on case
    # Converts to ascii from simple alphabet position
    if char.isupper():
        new_letter_pos += ord('A')
        # If the rotation goes past Z subtract the amount of letters in alphabet
        if new_letter_pos > ord('Z'):
            new_letter_pos -= 26
    else:
        new_letter_pos += ord('a')
        if new_letter_pos > ord('z'):
            new_letter_pos -= 26

    # chr() converts an int to an ascii character
    new_letter = chr(new_letter_pos)

    return new_letter

def encrypt(text, rot):
    """Encrypts an entire message based on rotation value."""
    encrypted_msg = ""
    for char in text:
        encrypted_msg = encrypted_msg + rotate_character(char, rot)

    return encrypted_msg
