device_status = "off"
temperature = 40

if device_status == "active":
    if temperature > 35:
        print("High temperature recorded!")
    else:
        print("Temperature normal")
else:
        print("Device is offline!")
