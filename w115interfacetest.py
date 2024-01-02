#!python3
from dspW245 import SmartPlug
from config import *

# The latter part is the PIN code.
sp = SmartPlug(smart_plug_ip, smart_plug_pin, model="W115")

# Turn socket [1,2,3,4] on or off.
sp.set_socket(1, on=True)
sp.set_socket(1, on=False)

# Upgrades the firmware to the firmware found at the provided url.
#sp.upgrade_fw("http://example.com/somefirmware")

# Used to avoid the connection from timing out.
sp.keep_alive()

# Close the connection.
sp.close()