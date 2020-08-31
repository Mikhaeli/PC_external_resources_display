#Reads pc resoucre info from .bat file, and sends to arduino down automatically deteced port
import serial
import subprocess
import ctypes, sys
import serial.tools.list_ports
import time

from call_bat import cpu_temp_bat

#https://superuser.com/questions/615654/run-exe-file-via-python-as-administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def find_port(port_identifier):
    #https://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino
    #Searchs available ports for one with port_name in descripotion, then reeturens that port
    port_name = ""
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        if port_identifier in p.description:
            port_name = p.device
    return port_name

if is_admin():
    port_name = find_port("Arduino")
    if port_name:
        arduino_serial = serial.Serial(port_name, 9600)
        #https://pyserial.readthedocs.io/en/latest/shortintro.html
        print(arduino_serial.name)
        print(port_name)
        print("Connected")
        #include a test in the loopp, to see if device is still connected
        while(True):
            temp = int(cpu_temp_bat("cpu_temp.bat"))/10 - 273
            print(temp)
            arduino_serial.write(str.encode(str(temp)))
            time.sleep(2)
        arduino_serial.close()
        input("Press to close")

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    exit(0)
