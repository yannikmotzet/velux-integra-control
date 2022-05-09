import sys
import shutter_control

if len(sys.argv) > 1:
    shutter_control.shutter_open(float(sys.argv[1]))
else:
    shutter_control.shutter_open()
