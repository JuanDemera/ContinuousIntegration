def main():
    membership = Membership()
    
    try:
        # Paso 1: Seleccionar Plan
        display_plans(membership)
        plan_choice = input("Seleccione un plan de membresía: ")
        membership.select_plan(plan_choice)
        
        # Paso 2: Añadir Características Adicionales
        while True:
            add_feature = input("¿Desea añadir una característica adicional? (s/n): ").lower()
            if add_feature == 's':
                feature_choice = input("Seleccione una característica adicional: ")
                membership.add_feature(feature_choice)
            else:
                break
        
        # Paso 3: Calcular Costos
        base_cost = membership_plans[membership.selected_plan]['base_cost']
        additional_cost = sum([membership_plans[membership.selected_plan]['features'][f] for f in membership.selected_features])
        
        # Paso 4: Aplicar Descuentos
        group = False
        special = False
        premium = False
        renewal_discount = False
        
        group_input = input("¿Está inscrito como grupo? (s/n): ").lower()
        if group_input == 's':
            group = True
            
        # Nueva funcionalidad: aplicar descuento por renovación
        renewal_input = input("¿Está renovando su membresía? (s/n): ").lower()
        if renewal_input == 's':
            renewal_discount = True
        
        # Calcular el costo total
        total_cost = calculate_total_cost(base_cost, additional_cost, group=group, special=special, premium=premium)
        
        # Aplicar descuento de renovación si es aplicable
        if renewal_discount:
            total_cost *= 0.9  # Aplicar un 10% de descuento
        
        # Paso 5: Confirmación del Usuario
        print("\nResumen de Membresía:")
        print(f"Plan seleccionado: {membership.selected_plan.value} - ${base_cost}")
        if membership.selected_features:
            print("Características adicionales:")
            for feature in membership.selected_features:
                print(f"  • {feature.value} - ${membership_plans[membership.selected_plan]['features'][feature]}")
        print(f"Costo total: ${total_cost:.2f}")
        
        confirm = input("¿Desea confirmar esta membresía? (s/n): ").lower()
        if confirm == 's':
            print("Membresía confirmada. ¡Gracias!")
            sys.exit(0)
        else:
            print("Membresía cancelada.")
            sys.exit(-1)
    
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(-1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(-1)

if __name__ == "__main__":
    main()
