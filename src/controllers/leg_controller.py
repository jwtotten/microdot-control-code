

class LegController:
    _instance_count = 0

    def __init__(self, leg_id):
        # Initialize the leg controller
        self.leg_id = leg_id

    def __new__(cls, *args, **kwargs):
        # limitting the instantiation of LegController to 4 instances.
        if cls._instance_count >= 4:
            raise RuntimeError("LegController can only be instantiated 4 times")

        instance = super().__new__(cls)
        cls._instance_count += 1
        return instance

    def calculate_leg_angle(self, new_pos) -> list[float]:
        """
        Calculate the angle of the leg based on the new position.
        :param new_pos: The new position of the leg.
        :return: The calculated angle of the leg.
        """
        # Placeholder for actual angle calculation logic
        angle = 0.0  # Replace with actual calculation
        return [angle]

    def home(self):
        """
        Move the leg to its home position.
        """
        # Placeholder for actual homing logic
        print(f"Leg {self.leg_id} is moving to home position.")
        