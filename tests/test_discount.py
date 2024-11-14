import unittest
from utils import calculate_total_cost

class TestRenewalDiscount(unittest.TestCase):
    
    def test_apply_renewal_discount(self):
        # Datos de prueba
        base_cost = 100  # Costo base del plan
        additional_cost = 50  # Costo adicional de características
        
        # Calcular costo sin descuento
        expected_total_cost = base_cost + additional_cost
        
        # Aplicar descuento de renovación (10%)
        discounted_total_cost = expected_total_cost * 0.9
        
        # Ejecutar la función con el descuento de renovación activado
        actual_total_cost = calculate_total_cost(base_cost, additional_cost, renewal_discount=True)
        
        # Verificar que el costo total con descuento sea el esperado
        self.assertAlmostEqual(actual_total_cost, discounted_total_cost, places=2, 
                               msg="El descuento de renovación no se aplicó correctamente")

if __name__ == '__main__':
    unittest.main()
