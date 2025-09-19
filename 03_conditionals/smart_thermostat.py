'''
You're building a smart thermostat alert system:
- If the device_status is "active"
      - And temperature > 35 -> Warn: "high temperature alert"
      - Else: "Temperature normal"
- If device is off -> "Device is offline"
'''

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")