# microdot-control-code

This is the micro python controller code for the 4 legged robot I am building

# Installing on the PI

```
sudo apt update
sudo apt install -y python3-venv python3-dev python3-lgpio
```

```
cd ~/microdot-control-code
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install adafruit-blinka adafruit-circuitpython-pca9685 adafruit-circuitpython-motor
```

Test it is working with:

```
python -c "import board; print(board.I2C())"
```

The Microdot can then be started with the following command:

```
python3 src/main.py
```
