from secrets import SystemRandom, token_urlsafe

def create_instance():
    return SystemRandom()

def generate_token(entry: int):
    if entry < 32:
        return "length must be >32"
    generate_nbyte = create_instance().randint(32, entry)
    return token_urlsafe(generate_nbyte)