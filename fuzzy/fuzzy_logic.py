import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyCarController:
    def __init__(self):
        # =========================
        # Define Universes
        # =========================
        self.distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')
        self.road = ctrl.Antecedent(np.arange(0, 11, 1), 'road')
        self.light = ctrl.Antecedent(np.arange(0, 11, 1), 'light')
        self.speed = ctrl.Consequent(np.arange(0, 121, 1), 'speed')
        self.limit = ctrl.Antecedent(np.arange(0, 121, 1), 'limit')

        # =========================
        # Membership Functions
        # =========================

        # Distance
        self.distance['close'] = fuzz.trimf(self.distance.universe, [0, 0, 40])
        self.distance['medium'] = fuzz.trimf(self.distance.universe, [20, 50, 80])
        self.distance['far'] = fuzz.trimf(self.distance.universe, [60, 100, 100])

        # Road
        self.road['wet'] = fuzz.trapmf(self.road.universe, [0, 0, 2, 5])
        self.road['normal'] = fuzz.trimf(self.road.universe, [3, 5, 7])
        self.road['dry'] = fuzz.trapmf(self.road.universe, [6, 8, 10, 10])

        # Traffic Light
        self.light['red'] = fuzz.trimf(self.light.universe, [0, 0, 3])
        self.light['yellow'] = fuzz.trimf(self.light.universe, [3, 5, 7])
        self.light['green'] = fuzz.trimf(self.light.universe, [6, 10, 10])

        # Speed
        self.speed['slow'] = fuzz.trimf(self.speed.universe, [0, 20, 50])
        self.speed['medium'] = fuzz.trimf(self.speed.universe, [30, 60, 90])
        self.speed['fast'] = fuzz.trimf(self.speed.universe, [70, 120, 120])

        # Speed Limit Zones
        self.limit['school'] = fuzz.trimf(self.limit.universe, [0, 40, 60])
        self.limit['city'] = fuzz.trimf(self.limit.universe, [50, 70, 90])
        self.limit['highway'] = fuzz.trimf(self.limit.universe, [80, 120, 120])

        # =========================
        # Rules (UPDATED)
        # =========================
        rules = [

        #  RED LIGHT (Highest Priority)
        ctrl.Rule(self.light['red'] & self.distance['far'], self.speed['slow']),
        ctrl.Rule(self.light['red'] & self.distance['medium'], self.speed['slow']),
        ctrl.Rule(self.light['red'] & self.distance['close'], self.speed['slow']),

        # Extra safety in wet
        ctrl.Rule(self.light['red'] & self.road['wet'], self.speed['slow']),

        #  YELLOW LIGHT (Caution)
        ctrl.Rule(self.light['yellow'] & self.distance['close'], self.speed['slow']),
        ctrl.Rule(self.light['yellow'] & self.distance['medium'] & self.road['wet'], self.speed['slow']),
        ctrl.Rule(self.light['yellow'] & self.distance['medium'] & self.road['normal'], self.speed['medium']),
        ctrl.Rule(self.light['yellow'] & self.distance['far'] & self.road['dry'], self.speed['medium']),

        #  GREEN LIGHT (Normal Driving)
        ctrl.Rule(self.light['green'] & self.distance['close'], self.speed['slow']),

        ctrl.Rule(self.light['green'] & self.distance['medium'] & self.road['wet'], self.speed['slow']),
        ctrl.Rule(self.light['green'] & self.distance['medium'] & self.road['normal'], self.speed['medium']),
        ctrl.Rule(self.light['green'] & self.distance['medium'] & self.road['dry'], self.speed['medium']),

        ctrl.Rule(self.light['green'] & self.distance['far'] & self.road['wet'], self.speed['medium']),
        ctrl.Rule(self.light['green'] & self.distance['far'] & self.road['normal'], self.speed['fast']),
        ctrl.Rule(self.light['green'] & self.distance['far'] & self.road['dry'], self.speed['fast']),

        #  SPEED LIMIT RULES
        ctrl.Rule(self.limit['school'], self.speed['slow']),
        ctrl.Rule(self.limit['city'] & self.distance['far'], self.speed['medium']),
        ctrl.Rule(self.limit['highway'] & self.distance['far'] & self.road['dry'], self.speed['fast']),

        #  SAFETY OVERRIDES
        ctrl.Rule(self.road['wet'] & self.distance['close'], self.speed['slow']),
        ctrl.Rule(self.road['wet'] & self.distance['medium'], self.speed['medium']),

        ctrl.Rule(self.distance['medium'], self.speed['medium']),
    ]
        self.control_system = ctrl.ControlSystem(rules)
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)

    # =========================
    # Compute Function (UPDATED)
    # =========================
    def compute(self, distance_value, road_value, light_value, limit_value):

        # Reset simulation
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)

        self.simulation.input['distance'] = distance_value
        self.simulation.input['road'] = road_value
        self.simulation.input['light'] = light_value
        self.simulation.input['limit'] = limit_value

        try:
            self.simulation.compute()
            speed_output = self.simulation.output['speed']
        except:
            speed_output = 50  # fallback

    # (rest of your code stays same)

        # =========================
        # Membership values
        # =========================
        distance_mf = {
            'close': fuzz.interp_membership(self.distance.universe, self.distance['close'].mf, distance_value),
            'medium': fuzz.interp_membership(self.distance.universe, self.distance['medium'].mf, distance_value),
            'far': fuzz.interp_membership(self.distance.universe, self.distance['far'].mf, distance_value)
        }

        road_mf = {
            'wet': fuzz.interp_membership(self.road.universe, self.road['wet'].mf, road_value),
            'normal': fuzz.interp_membership(self.road.universe, self.road['normal'].mf, road_value),
            'dry': fuzz.interp_membership(self.road.universe, self.road['dry'].mf, road_value)
        }

        light_mf = {
            'red': fuzz.interp_membership(self.light.universe, self.light['red'].mf, light_value),
            'yellow': fuzz.interp_membership(self.light.universe, self.light['yellow'].mf, light_value),
            'green': fuzz.interp_membership(self.light.universe, self.light['green'].mf, light_value)
        }

        limit_mf = {
            'school': fuzz.interp_membership(self.limit.universe, self.limit['school'].mf, limit_value),
            'city': fuzz.interp_membership(self.limit.universe, self.limit['city'].mf, limit_value),
            'highway': fuzz.interp_membership(self.limit.universe, self.limit['highway'].mf, limit_value)
        }

        # =========================
        # Rule strengths (for UI)
        # =========================
        def AND(a, b): return min(a, b)
        def AND3(a, b, c): return min(a, b, c)

        rules_strength = []

        #  RED
        rules_strength.append(AND(light_mf['red'], distance_mf['far']))
        rules_strength.append(AND(light_mf['red'], distance_mf['medium']))
        rules_strength.append(AND(light_mf['red'], distance_mf['close']))
        rules_strength.append(AND(light_mf['red'], road_mf['wet']))

        #  YELLOW
        rules_strength.append(AND(light_mf['yellow'], distance_mf['close']))
        rules_strength.append(AND3(light_mf['yellow'], distance_mf['medium'], road_mf['wet']))
        rules_strength.append(AND3(light_mf['yellow'], distance_mf['medium'], road_mf['normal']))
        rules_strength.append(AND3(light_mf['yellow'], distance_mf['far'], road_mf['dry']))

        #  GREEN
        rules_strength.append(AND(light_mf['green'], distance_mf['close']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['medium'], road_mf['wet']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['medium'], road_mf['normal']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['medium'], road_mf['dry']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['far'], road_mf['wet']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['far'], road_mf['normal']))
        rules_strength.append(AND3(light_mf['green'], distance_mf['far'], road_mf['dry']))

        # 🌧 OVERRIDES
        rules_strength.append(AND(road_mf['wet'], distance_mf['close']))
        rules_strength.append(AND(road_mf['wet'], distance_mf['medium']))

        # DEFAULT
        rules_strength.append(distance_mf['medium'])

        # =========================
        # Output MF activation
        # =========================
        output_mf = {
            'slow': max(rules_strength[0:3]),
            'medium': max(rules_strength[3:7]),
            'fast': max(rules_strength[7:])
        }

        return {
            "speed": speed_output,
            "distance_mf": distance_mf,
            "road_mf": road_mf,
            "light_mf": light_mf,
            "rule_strengths": rules_strength,
            "output_mf": output_mf,
            "limit_mf": limit_mf,
        }