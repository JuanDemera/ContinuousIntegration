def calculate_total_cost(base_cost, additional_cost, group=False, special=False, premium=False):
    total = base_cost + additional_cost

    # Descuento para grupos
    if group:
        total *= 0.9  # 10% de descuento

    # Descuento especial
    if special:
        if total > 400:
            total -= 50  # $50 si excede $400
        elif total > 200:
            total -= 20  # $20 si excede $200

    # Recargo por características premium
    if premium:
        total *= 1.15  # 15% de recargo

    return int(total)  # Devolver como entero

def validate_membership(plan, features):
    # Aquí puedes agregar validaciones adicionales si es necesario
    return True
