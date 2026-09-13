import board
import busio
from controllers import LegController
from controllers import MotorController
from utils import MicrodotLogger


class Microdot:
    def __init__(self):
        # Initialize the motor controller class
        self.logger = MicrodotLogger("Microdot")
        # Initialize the motor controller class
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.motor_controller = MotorController(self.i2c, address=0x41)

        # Initialize the microdot with 4 leg controllers
        self.legs = [LegController(motor_controller=self.motor_controller, leg_id=i) for i in range(4)]

    def get_leg(self, leg_id):
        if 0 <= leg_id < len(self.legs):
            return self.legs[leg_id]
        else:
            raise ValueError("Invalid leg ID")

if __name__ == "__main__":
    microdot = Microdot()
    microdot.logger.info("Microdot initialized with 4 legs and motor controller.")
    # home all of the legs at startup
    for leg in microdot.legs:
        leg.loop_leg()

    