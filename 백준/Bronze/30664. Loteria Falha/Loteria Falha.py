# Loteria Falha

while True:
    target_number = int(input())
    if not target_number:
        break
    else:
        if target_number % 42:
            print("TENTE NOVAMENTE")
        else:
            print("PREMIADO")
