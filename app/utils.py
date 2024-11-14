def calculate_total_cost(base_cost, additional_cost, group=False, special=False, premium=False):
    total = base_cost + additional_cost
    if group:
        total *= 0.9  # 10% de descuento
    if special:
        if total > 400:
            total -= 50
        elif total > 200:
            total -= 20
    if premium:
        total *= 1.15  # 15% de recargo
    return int(total)

def validate_membership(plan, features):
    # Aquí puedes agregar validaciones adicionales si es necesario
    return True
