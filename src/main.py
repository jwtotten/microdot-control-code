
from controllers import LegController

class Microdot:
    def __init__(self):
        # Initialize the microdot with 4 leg controllers
        self.legs = [LegController(leg_id=i) for i in range(4)]

    def get_leg(self, leg_id):
        if 0 <= leg_id < len(self.legs):
            return self.legs[leg_id]
        else:
            raise ValueError("Invalid leg ID")

if __name__ == "__main__":
    microdot = Microdot()
    # home all of the legs at startup
    for leg in microdot.legs:
        leg.home()

    