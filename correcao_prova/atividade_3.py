
#validador de senha

senha = input("Digite uma senha: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in senha:
    if ch.isupper():
        has_upper() = True
    if ch.islower():
        has_lower() = True
    if ch.isdigit():
        has_digit() = True
    if not ch.isalnum():
        has_special() = True

errors = []
if len(senha) < 8:
    errors.append("Mínimo 8 caracteres.")
