import hashlib
# Modify The Hash in the next line
hash = "a2099f4c2c2de141afb474dfe4b765ce83448100e77f4359314d94807b00862d53316c03963fc60cbdbd7bc6915778f1830f0f4fd9364a4bc71a09c5e83a0a67"

with open('#Pass.txt access route#') as file:
    lines = file.readlines()
    for passwords in lines:
        given_Pass = passwords.strip()
        hashed_Pass = hashlib.sha3_512(given_Pass.encode()).hexdigest()
        if hash == hashed_Pass:
            print(passwords)
            break
