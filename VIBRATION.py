import matplotlib.pyplot as plt
import csv
import numpy as np
import time


def vibration():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    x = []
    y1 = []
    y2 = []
    y3 = []


    with open('./logs/VIBRATION.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[2]))      #Distance in meters
            y2.append(float(row[3]))
            y3.append(float(row[4]))

    """ Distance Plot"""
    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('Vibration Levels')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x[::100],y1[::100],label='Vibration level in X')
    plt.plot(x[::100],y2[::100],label='Vibration level in Y')
    plt.plot(x[::100],y3[::100],label='Vibration level in Z')
    plt.xlabel('Time')
    plt.ylabel('Vibration')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Vibration Levels')
    plt.legend()
    plt.savefig("./graphs/vibration_levels.png")
    if(SHOW_GRAPH != False):
        plt.show()
    #plt.close(1)

if __name__ == "__main__":
    vibration()