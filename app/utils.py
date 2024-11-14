def calculate_total_cost(base, additional, group=False, special=False, premium=False):
    total = base + additional
    if special:
        total -= 20
    if premium:
        total += 50
    return total


def validate_membership(plan, features):
    # Aquí puedes agregar validaciones adicionales si es necesario
    return True
