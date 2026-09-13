from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time
from utils import MicrodotLogger

class MotorController:

    def __init__(self, i2c, address=0x40):
        self.logger = MicrodotLogger("MotorController")
        self.i2c = i2c
        self.address = address
        self._instanciate_motor()

    def _instanciate_motor(self):
        self.pca = PCA9685(self.i2c, address=self.address)
        self.logger.info("MotorController initialized with PCA9685 at address 0x{:02X}".format(self.address))
        self.pca.frequency = 50  # Hz
        self.logger.debug("PCA9685 frequency set to 50 Hz")
        self.servo = servo.Servo(self.pca.channels[7])

    def move_servo(self, angle):
        self.servo.angle = angle
        self.logger.info(f"Servo moved to angle: {angle} degrees")
        time.sleep(0.05)