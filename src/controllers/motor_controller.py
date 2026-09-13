from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

class MotorController:

    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self._instanciate_motor()

    def _instanciate_motor(self):
        self.pca = PCA9685(self.i2c, address=self.address)
        self.pca.frequency = 50  # Hz
        self.servo = servo.Servo(self.pca.channels[7])

    def move_servo(self, angle):
        self.servo.angle = angle
        time.sleep(0.05)