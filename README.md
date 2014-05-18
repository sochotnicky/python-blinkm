python-blinkm
=============

Python module for interfacing with BlinkM LEDs through USB<->Serial/I2C interface
such as the one that can be created with Arduino and BlinkMCommunicator


Dependencies
============

 * pyserial - you will need it to initialize serial connection to arduino


Note that if you set your group correctly you should *not* need to use this
module as root

Usage
=====

An example usage is in blinkm-cli.py module, but a bit more simplified version
is:

```python
    import serial 
    from blinkm import BlinkM

    ser = serial.Serial('/dev/ttyACM0', 19200, timeout=0.1)
    b = BlinkM(ser, 0x09)
    b.playScript(18, 2, 0) # run S.O.S script twice and then turn off
```

A good use case for CLI might be setting up addresses of BlinkM from console:

    python blinkm-cli.py /dev/ttyACM0 --address 0 --setaddress 25

