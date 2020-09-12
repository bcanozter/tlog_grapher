import matplotlib.pyplot as plt
import csv
import numpy as np
import time


def distance_sensor():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    x = []
    y1 = []


    with open('./logs/DISTANCE_SENSOR.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[4])/100)      #Distance in meters

    """ Distance Plot"""
    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('Distance Sensor')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1, label='Current Distance(m)')
    plt.xlabel('Time')
    plt.ylabel('Distance(m)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Distance Sensor')
    plt.legend()
    plt.savefig("./graphs/distance_sensor.png")
    if(SHOW_GRAPH != False):
        plt.show()
    #plt.close(1)

if __name__ == "__main__":
    distance_sensor()