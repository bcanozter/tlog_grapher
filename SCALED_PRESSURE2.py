import matplotlib.pyplot as plt
import csv
import numpy as np
import time


def scaled_pressure2():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    """ Barometer readings for 2nd barometer """

    x = []
    y1 = [] #Absolute Pressure (hPa)
    y2 = [] #Differential Pressure 1 (hPa)
    y3 = [] #Absolute Pressure Temperature (cdegC)



    with open('./logs/SCALED_PRESSURE2.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[2])/10)      #kPa
            y2.append(float(row[3])/10)      #kPa
            y3.append(int(row[4]))           #cdegC



    """ Absolute Pressure Plot"""
    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('Absolute Pressure')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1, label='Abs. Pressure (kPa)')
    plt.xlabel('Time')
    plt.ylabel('Abs. Pressure (kPa)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Absolute Pressure')
    plt.legend()
    plt.savefig("./graphs/absolute_pressure2.png")
    #plt.close(1)

    """ Differential Pressure Plot """

    plt.figure(2)
    fig = plt.gcf()
    fig.canvas.set_window_title('Differential Pressure')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y2, label='Diff. Pressure (kPa)')
    plt.xlabel('Time')
    plt.ylabel('Diff. Pressure (kPa)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Differential Pressure')
    plt.legend()
    plt.savefig("./graphs/absolute_pressure2.png")
    #plt.close(2)

    """ Differential Pressure Plot """

    plt.figure(3)
    fig = plt.gcf()
    fig.canvas.set_window_title('Abs. Pressure Temperature')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y3, label='Temperature (C)')
    plt.xlabel('Time')
    plt.ylabel('Abs. Pressure Temperature (C)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Abs. Pressure Temperature')
    plt.legend()
    plt.savefig("./graphs/absolute_pressure_temperature2.png")
    #plt.close(3)
    if(SHOW_GRAPH != False):
        plt.show()
   #plt.show()

if __name__ == "__main__":
    scaled_pressure2()