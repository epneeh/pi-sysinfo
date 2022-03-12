import psutil

def cpu_percent():
    return psutil.cpu_percent(1,True)

def cpu_freq():
    return psutil.cpu_freq(True)

def cpu_count():
    return psutil.cpu_count(True)

def cpu_temp():
    cpu_temps = psutil.sensors_temperatures();
    temps=[]
    for name,entries in cpu_temps.items():
        for entry in entries:
            temps.append({"name" : entry.label or name,"current" : entry.current})
    return temps

def ram():
    return psutil.virtual_memory()

def swap():
    return psutil.swap_memory()