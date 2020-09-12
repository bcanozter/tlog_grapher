import matplotlib.pyplot as plt
import csv
import numpy as np
import time



def battery_status():
    from main import SHOW_GRAPH #Circular dependency problem so import here
    #Time hh:mm:ss
    x = []

    #Acceleration mG
    y1 = [] #x_acc
    y2 = [] #y_acc
    y3 = [] #z_acc

    #Angular Speed mrad/s
    y4 = [] #x_w
    y5 = [] #y_w
    y6 = [] #z_w

    #Magnetic Field, mgauss
    y7 = [] #x_magnetic_field
    y8 = [] #y_magnetic_field
    y9 = [] #z_magnetic_field

    with open('./logs/BATTERY_STATUS.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            # Voltages[10]. Battery Voltage for Cell 1
            y1.append(float(row[5][1::])/1000) # Ignore '[' character
            y2.append(float(row[4]))
            #y2.append()
            # y7.append(float(row[8]))
            # y8.append(float(row[9]))
            # y9.append(float(row[10]))


    """ Battery Cell Voltage Status Plot """


    plt.figure(2)
    fig = plt.gcf()
    fig.canvas.set_window_title('Battery Status')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1,label='Voltage for Cell 1')
    plt.xlabel('Time')
    plt.ylabel('Voltage (V)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Battery Info')
    plt.legend()
    plt.savefig("./graphs/battery_status.png")
    #plt.show()
    #plt.close(1)

    plt.figure(3)
    fig = plt.gcf()
    fig.canvas.set_window_title('Battery Temperature')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y2,label='Battery Temperature')
    plt.xlabel('Time')
    plt.ylabel('Temperature (C)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('Battery Temperature')
    plt.legend()
    plt.savefig("./graphs/battery_temperature.png")
    if(SHOW_GRAPH != False):
        plt.show()
    #plt.close(2)


if __name__ == "__main__":
    battery_status()