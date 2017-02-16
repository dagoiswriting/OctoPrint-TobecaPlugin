OctoPrint Plugin Tobeca
=========================

Adding a Tobeca (French 3D Printer) tab with commands:

- Autotune PID : Sending the M303 Gcode with selecting tool, temperature  (parameter C=8)
- Z-Probe-Offset : Sending the M851 Gcode with selecting the value
- Home XYZ : Sending the G28 Gcode, because Home Z is harzardous with Z-Probe