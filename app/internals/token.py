from string import ascii_letters, digits, punctuation
from secrets import SystemRandom, choice, token_hex


def generate_token(entry: int):
    if entry < 32:
        return "length must be >32"
    generate_nbyte = SystemRandom().randint(32, entry)
    token = token_hex(generate_nbyte)
    compilation = token + " " + ''.join(choice(ascii_letters) for _ in range(entry)) + digits + punctuation
    password = ''.join(choice(compilation) for _ in range(entry))
    return password