import time
import Adafruit_DHT

# Initial the dht device, with data pin connected to:
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN=4
while True:
  try:
    # Print the values to the serial port
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
      print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
      print("Erro ao pegar os dados")
  except RuntimeError as error:
    # Errors happen fairly often, DHT's are hard to read, just keep going
    print(error.args[0])
    time.sleep(2.0)
