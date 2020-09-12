import matplotlib.pyplot as plt
import csv
import numpy as np
import time

def global_position_int():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    x = []
    y1 = [] #V_x
    y2 = [] #V_y
    y3 = [] #V_z

    y4 = [] #Latitutde
    y5 = [] #Longtitude
    y6 = [] #Altitude



    with open('./logs/GLOBAL_POSITION_INT.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[6])/100)      #V_x
            y2.append(float(row[7])/100)      #V_y
            y3.append(float(row[8])/100)      #V_z

            y4.append(float(row[2]))          #Latitude
            y5.append(float(row[3]))          #Longtitude
            y6.append(float(row[4]))          #Altitude



    """ Speed Plot"""
    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('Ground Speed')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1, label='Ground Speed for X')
    plt.plot(x,y2, label='Ground Speed for Y')
    plt.plot(x,y3, label='Ground Speed for Z')
    plt.xlabel('Time')
    plt.ylabel('Speed(m/s)')
    plt.xticks(x[::1000], rotation=90)
    plt.grid(True)
    plt.title('Ground Speed')
    plt.legend()
    plt.savefig("./graphs/speed_graph.png")
    #plt.close(1)

    """ GPS Plot """
    plt.figure(2)
    fig = plt.gcf()
    fig.canvas.set_window_title('GPS Info')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y4, label='Latitude')
    plt.plot(x,y5, label='Longtitude')
    plt.plot(x,y6, label='Altitude')
    plt.xlabel('Time')
    plt.xticks(x[::1000], rotation=90)
    plt.grid(True)
    plt.title('Latitude, Longtitude, Altitude Info')
    plt.legend()
    plt.savefig("./graphs/gps_graph.png")
    if(SHOW_GRAPH != False):
        plt.show()

    #plt.close(2)

if __name__ == "__main__":
    global_position_int()