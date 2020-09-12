import matplotlib.pyplot as plt
import csv
import numpy as np
import time

def power_status():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    x = []
    y1 = [] #Vcc
    y2 = [] #Vservo
    y3 = [] #Bitmap flags



    with open('./logs/POWER_STATUS.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[1])/1000)      #Vcc in V
            y2.append(float(row[2])/1000)      #Vservo in V
            y3.append(int(row[3]))



    """ Voltage Plot"""
    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('Power Status')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1, label='Vcc (V)')
    plt.plot(x,y2, label='Vservo (V)')
    plt.xlabel('Time')
    plt.ylabel('Voltage (V)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Power Status')
    plt.legend()
    plt.savefig("./graphs/power_status.png")
    #plt.close(1)

    """ Power Status Flags """

    plt.figure(2)
    fig = plt.gcf()
    fig.canvas.set_window_title('Power Status Flags')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y3)
    plt.xlabel('Time')
    plt.ylabel('Flags')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Power Status Flags')
    plt.savefig("./graphs/power_flags.png")
    if(SHOW_GRAPH != False):
        plt.show()
    #plt.close(2)
    #plt.show()

if __name__ == "__main__":
    power_status()