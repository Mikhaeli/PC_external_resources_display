#calls a .bat file and returns the output
import re
import subprocess
#https://docs.python.org/3/library/subprocess.html

bat_file = "cpu_temp.bat"

def cpu_temp_bat(bat_file):
    info = subprocess.Popen(bat_file, stdout=subprocess.PIPE).stdout
    return re.findall(r"\d+" ,str(info.readlines()[1], 'utf-8'))[0]

def run_batagain(bat_file):
    info = subprocess.Popen(bat_file, stdout=subprocess.PIPE).stdout
    return info.readlines()
    print(info)
    input()
    info.close()

    #info.close()
if __name__ == '__main__':
    print(int(cpu_temp_bat(bat_file))/10 - 273.15)
    #print(type(cpu_temp_bat(bat_file)))
    print(run_batagain(bat_file))
    print("gfedsgrds")
    input()
