from machine import Pin
import time
import dht
import network
import urequests



SSID = "your-wifi" #Wi-Fi SSID
PASSWORD = "your-password" # Wi-Fi password
API_KEY = "your-api-key" # Key for your api writes, X-Api-Key header
API_URL = "your-api-url" # full path to your endpoint, i.e. https://api.example.com/readings/new
CLUSTER_NAME = "cluster-name" # Name of your cluster of devices

READING_FREQUENCY = 30*60 #frequency of reading from the sensor in seconds

DHT_PIN = 15 # GPIO pin on your Raspberry Pi Pico W


dSensor = dht.DHT22(Pin(DHT_PIN))

def readDHT():
    try:
        dSensor.measure()
        temp = dSensor.temperature()
        temp_f = (temp * (9/5)) + 32.0
        hum = dSensor.humidity()
        print('Temperature= {} C, {} F'.format(temp, temp_f))
        print('Humidity= {} '.format(hum))
        return (temp, hum)
    except OSError as e:
        print('Failed to read data from DHT sensor')
        
def send_reading(temp, hum):
    payload = {
        "temperature": temp,
        "humidity": hum,
        "clusterName": CLUSTER_NAME
    }
    headers = {
        "Content-Type" : "application/json",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Api-Key": API_KEY
    }
    
    response = urequests.post(API_URL, json=payload, headers=headers)
    print(response.status_code)
    response.close()
        
        
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    timeout = 10  # 10 seconds timeout
    start = time.time()
    while not wlan.isconnected() and time.time() - start < timeout:
        time.sleep(1)
    
    if wlan.isconnected():
        print("Connected to WiFi")
        print("IP Address:", wlan.ifconfig()[0])
    else:
        print("Failed to connect to WiFi")    


#establish wifi connection
connect_to_wifi()       

#infinite read cycle
while True:
    readings = readDHT() # read from DHT22
    send_reading(readings[0], readings[1]) #http post request
    time.sleep(READING_FREQUENCY) #delay

