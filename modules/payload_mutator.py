import random

def contextual_mutate(payload, vector):
    if vector == "xss":
        # Mutira XSS payload dodavanjem varijacija
        return payload.replace("<", "<<").replace(">", ">>")
    elif vector == "sqli":
        # Dodaje tipičan SQLi završetak
        return payload + " --"
    elif vector == "lfi":
        # Pokušava da dođe do /etc/passwd
        return "../" * random.randint(1, 5) + "etc/passwd"
    else:
        # Ako nije prepoznat vektor, vrati neizmenjeno
        return payload
