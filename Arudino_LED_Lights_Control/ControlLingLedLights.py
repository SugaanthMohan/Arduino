# IMPORT THE NECESSARY MODULES
import serial
import time

# ESTABLISH THE CONNECTION TO YOUR SERIAL PORT
ArduinoSerial = serial.Serial('/dev/cu.usbmodem1421',9600)

# WAITING FOR CONNECTION ESTABLISHMENT
time.sleep(2)

# PRINT THE ARDUINO OUTPUT HERE
print("<::: BEGIN ARDUION OUTPUT BELOW :::>")
print(ArduinoSerial.readline())
print("<::: END ARDUION OUTPUT ABOVE :::>")

print("\n\n ENTER 1 TO TURN ON LED AND 0 TO TURN OFF LED")

while 1:
	var = str(input())
	print(" ENTERED : ",var)

	if var == '1':
		ArduinoSerial.write(str.encode('1'))
		print('LED TURNED ON')
		time.sleep(1)
	elif var == '0':
		ArduinoSerial.write(str.encode('0'))
		print('LED TURNED OFF')
	else:
		exit
