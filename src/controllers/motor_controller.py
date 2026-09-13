from adafruit_pca9685 import PCA9685

class MotorController:

    def __init__(self, i2c):
        self.i2c = i2c

    def _instanciate_motor(self):
        self.pca = PCA9685(self.i2c)