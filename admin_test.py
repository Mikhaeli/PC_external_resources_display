import ctypes, sys
import subprocess
#https://docs.python.org/3/library/subprocess.html
bat_file = "misc.bat"

def run_bat(bat_file):
    info = subprocess.Popen(bat_file)
    #print(info)
    #print(type(info))
    #print("info keys")
    #for x in info.__dict__:
        #print x
    #print(info.__dict__)
    input()
    info.close()
#https://superuser.com/questions/615654/run-exe-file-via-python-as-administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here
    run_bat(bat_file)
    print("aaccepted")
    input()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    exit(0)
