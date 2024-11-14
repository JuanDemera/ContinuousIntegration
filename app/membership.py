from enum import Enum

class MembershipType(Enum):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
    FAMILY = 'Family'

class AdditionalFeature(Enum):
    PERSONAL_TRAINING = 'Personal Training Sessions'
    GROUP_CLASSES = 'Group Classes'
    EXCLUSIVE_ACCESS = 'Exclusive Gym Facilities'
    SPECIAL_TRAINING = 'Specialized Training Programs'

membership_plans = {
    MembershipType.BASIC: {
        'base_cost': 50,
        'features': {
            AdditionalFeature.PERSONAL_TRAINING: 20,
            AdditionalFeature.GROUP_CLASSES: 15
        }
    },
    MembershipType.PREMIUM: {
        'base_cost': 100,
        'features': {
            AdditionalFeature.PERSONAL_TRAINING: 30,
            AdditionalFeature.GROUP_CLASSES: 25,
            AdditionalFeature.EXCLUSIVE_ACCESS: 40,
            AdditionalFeature.SPECIAL_TRAINING: 35
        }
    },
    MembershipType.FAMILY: {
        'base_cost': 150,
        'features': {
            AdditionalFeature.GROUP_CLASSES: 20
        }
    }
}

class Membership:
    def __init__(self):
        self.selected_plan = None
        self.selected_features = []

    def get_available_plans(self):
        return list(membership_plans.keys())

    def select_plan(self, plan_name):
        for plan in membership_plans:
            if plan.value == plan_name:
                self.selected_plan = plan
                return self
        raise ValueError(f"Plan de membresía '{plan_name}' no disponible.")

    def add_feature(self, feature_name):
        if not self.selected_plan:
            raise ValueError("No se ha seleccionado una membresía.")
        for feature in membership_plans[self.selected_plan]['features']:
            if feature.value == feature_name:
                self.selected_features.append(feature)
                return self
        raise ValueError(f"Característica adicional '{feature_name}' no disponible para el plan seleccionado.")
