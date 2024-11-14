import pytest
from app.membership import Membership, MembershipType

def test_membership_selection():
    membership = Membership()
    plans = [plan.value for plan in membership.get_available_plans()]  # Extrae los valores del enum
    assert 'Basic' in plans
    assert 'Premium' in plans
    assert 'Family' in plans


def test_select_membership():
    membership = Membership()
    membership.select_plan('Basic')  # Seleccionar el plan
    assert membership.selected_plan == MembershipType.BASIC  # Comprobar el atributo seleccionado


def test_invalid_membership_selection():
    membership = Membership()
    with pytest.raises(ValueError):
        membership.select_plan('InvalidPlan')
