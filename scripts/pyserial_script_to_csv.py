import serial
from datetime import datetime
import csv

#Open a csv file and set it up to receive comma delimited input
logging = open('logs/logging.csv',mode='a')
writer = csv.writer(logging, delimiter=",", escapechar=' ', quoting=csv.QUOTE_NONE)

#Open a serial port that is connected to an Arduino (below is Linux, Windows and Mac would be "COM4" or similar)
#No timeout specified; program will wait until all serial data is received from Arduino
#Port description will vary according to operating system. Linux will be in the form /dev/ttyXXXX
#Windows and MAC will be COMX
ser = serial.Serial('COM6',9600)
ser.flushInput()


while True:

    if ser.inWaiting():
        #Read in data from Serial until \n (new line) received
        ser_bytes = ser.readline()
        # print(ser_bytes)
        
        #Convert received bytes to text format
        decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        
        
        #Retreive current time
        c = datetime.now()
        current_time = c.strftime('%H:%M:%S')
        print(current_time +","+ decoded_bytes)
        
        #Write received data to CSV file
        writer.writerow([current_time,decoded_bytes])
            
# Close port and CSV file to exit
ser.close()
logging.close()
print("logging finished")