"""
  _____                            _   
 |_   _|                          | |  
   | |  _ __ ___  _ __   ___  _ __| |_ 
   | | | '_ ` _ \| '_ \ / _ \| '__| __|
  _| |_| | | | | | |_) | (_) | |  | |_ 
 |_____|_| |_| |_| .__/ \___/|_|   \__|
                 | |                   
                 |_|                    """

import serial
import sys
import time


""" 
  _____                               _                
 |  __ \                             | |               
 | |__) |_ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ ___ 
 |  ___/ _` | '__/ _` | '_ ` _ \ / _ \ __/ _ \ '__/ __|
 | |  | (_| | | | (_| | | | | | |  __/ ||  __/ |  \__ \
 |_|   \__,_|_|  \__,_|_| |_| |_|\___|\__\___|_|  |___/
                                                       
 """    

def record_audio(time_stamp,serial_port_name):


    #TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    sample_length= 1 #Define cada cuantos segundos se guardan datos.
    print("Start audio recording...")


    ser = serial.Serial(serial_port_name, 115200, timeout=None)     # Create Serial link
    file_name = time_stamp + ".json"
    file = open(file_name,"a")
    # Prefix for EdgeImpulse integration
    file.write('{"protected":{"alg":"HS256","ver":"v1"},"signature":"8edcce692f266197144c1ddcbd7a381cf6cbaea4f6433e0b6a765eb7eb7230de","payload":{"device_name":"03:DF:11:CF:64:45","device_type":"ARDUINO_NANO33BLE","interval_ms":0.0625,"sensors":[{"name":"audio","units":"wav"}],"values":[')
     
    try:
      start_time = time.time()
      while True: 
        result_ = ""

        samples = int(16000 * sample_length)

        #TEST TEST TEST TEST TEST TEST #TEST TEST TEST TEST TEST TEST

        for x in range(samples):
          ser.read_until()
          cc1 = ser.read(2)
          result_ += str(int.from_bytes(cc1, "big"))+","
        

        #TEST TEST TEST TEST TEST TEST #TEST TEST TEST TEST TEST TEST

        #report=open("report.txt","w")
        #report.write("Audio recording: ",time.time()-start_time,"\n")
        
        #report.close()
        file.write(result_)
    
    except:
      print("Stop audio recording.")
      print("audio:",time.time()-start_time)  
      # Suffix for EdgeImpulse integration
      file.write(result_)
      file.write('0]}}')
      file.close()
      ser.close()

if __name__ == '__main__':
  if len(sys.argv)>1:
    port = str(sys.argv[1])
  else:
    port = "COM7" #Es como el default
    
  print("TEST MODE audio !")
  
  if len(sys.argv)>2:
    name = str(sys.argv[2])
  else:
    name = "audio_adquirido"
  par_serial_port_name = port
  record_audio(name,par_serial_port_name)