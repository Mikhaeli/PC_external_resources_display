import wmi


def initialize_openhardwaremonitor():
    file = 'OpenHardwareMonitorLib.dll'
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

initialize_openhardwaremonitor()
fetch_stats(HardwareHandle)

w = wmi.WMI(namespace="root\OpenHardwareMonitor");
temperature_infos = w.Sensor();
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name);
        print(sensor.Value);
