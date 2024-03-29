import sys
import urllib2
from time import sleep
import Adafruit_DHT as dht
# Enter Your API key here
myAPI = 'TUOGTQCETS4UIKES' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

delay=20 #delay between each API call in seconds
DHT22_pin=22 # DHT22 pin
def DHT22_data():
	# Reading from DHT22 and storing the temperature and humidity
	humi, temp = dht.read_retry(dht.DHT22, DHT22_pin=22) 
	return humi, temp
while True:
	try:
		humi, temp = DHT22_data()
		# If Reading is valid
                #humi,temp=10.6,2.2#for testing
		if isinstance(humi, float) and isinstance(temp, float):
			# Formatting to two decimal places
			humi = '%.2f' % humi 					   
			temp = int(temp)
			
			# Sending the data to thingspeak
			conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, humi))
			print conn.read()
			# Closing the connection
			conn.close()
		else:
			print 'Error'
		# DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
		sleep(delay)
	except:
                print"Failed to read sensor"
		break
                