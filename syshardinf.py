import platform
import psutil
import sys
import os

def main():
    
    print("\n\nHow would you like to view your specs?\n\n1. TXT \n2. Terminal\n")
    option = input()
    if option == "1":
        to_text()
    elif option == "2":
        prints()
    else:
        exit()
    
def to_text():
    clear()
    filename = input("Enter Filename: ")
    clear()
    print(f"Thank you, please check your dir folder for the {filename}.txt file\n\n")
    sys.stdout = open(filename+".txt", "w")
    prints()
    sys.stdout.close()

def prints():    
    clear()
    print(f"Computer network name: {platform.node()}")
    print(f"Machine type: {platform.machine()}")
    print(f"Processor type: {platform.processor()}")
    print(f"Platform type: {platform.platform()}")
    print(f"Operating system: {platform.system()}")
    print(f"Operating system release: {platform.release()}")
    print(f"Operating system version: {platform.version()}")
    print()
    print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
    print()
    print(f"Current CPU frequency: {psutil.cpu_freq().current}")
    print(f"Min CPU frequency: {psutil.cpu_freq().min}")
    print(f"Max CPU frequency: {psutil.cpu_freq().max}")
    print()
    print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
    print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")
    print()
    print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000)-1} GB")
    print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000)-1} GB")
    print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000)} GB")
    print(f"RAM usage: {psutil.virtual_memory().percent}%")

clear = lambda: os.system('cls')
main()