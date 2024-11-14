import pytest
from app.membership import Membership, MembershipType

def test_membership_selection():
    membership = Membership()
    plans = membership.get_available_plans()
    assert 'Basic' in plans
    assert 'Premium' in plans
    assert 'Family' in plans

def test_select_membership():
    membership = Membership()
    selected = membership.select_plan('Basic')
    assert selected.type == MembershipType.BASIC
    assert selected.base_cost == 50  # Asumiendo costo base

def test_invalid_membership_selection():
    membership = Membership()
    with pytest.raises(ValueError):
        membership.select_plan('InvalidPlan')
