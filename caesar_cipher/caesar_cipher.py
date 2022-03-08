import string
import collections


def caesar(message: str, shift: int, is_encrypt=True):

    # If it's decrypt, then make shift variable to negative value
    if not is_encrypt:
        shift = -abs(shift)

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    # Rotate the string based on shift value
    upper.rotate(shift)
    lower.rotate(shift)

    # Make it string
    upper = "".join(list(upper))
    lower = "".join(list(lower))

    # translate
    return message.translate(str.maketrans(string.ascii_uppercase, upper)).translate(
        str.maketrans(string.ascii_lowercase, lower)
    )


# Loop when inputed value is not valid
while True:
    menu: str = input("What do you want? (encrypt, decrypt)\n:")

    is_encrypt: bool
    if menu.lower() == "encrypt":
        is_encrypt = True
        break
    elif menu.lower() == "decrypt":
        is_encrypt = False
        break

    continue

message = input("Message: ")
shift = int(input("Shifted number: "))
result = caesar(message, shift, is_encrypt)
print(f"Result: {result}")
