import matplotlib.pyplot as plt
import csv
import numpy as np
import time

def scaled_imu2():
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

    with open('./logs/SCALED_IMU2.csv','r') as csvfile:
        next(csvfile) #Skip headers
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(row[0])))[10::]) #Time
            y1.append(float(row[2]))
            y2.append(float(row[3]))
            y3.append(float(row[4]))

            y4.append(float(row[5]))
            y5.append(float(row[6]))
            y6.append(float(row[7]))


            # y7.append(float(row[8]))
            # y8.append(float(row[9]))
            # y9.append(float(row[10]))


    """ Acceleration Plot """

    plt.figure(1)
    fig = plt.gcf()
    fig.canvas.set_window_title('IMU Acceleration')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y1,label='Acceleration in X')
    plt.plot(x,y2,label='Acceleration in Y')
    plt.plot(x,y3,label='Acceleration in Z')
    plt.xlabel('Time')
    plt.ylabel('Acceleration(mG)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('IMU Acceleration Info')
    plt.legend()
    plt.savefig("./graphs/imu_accel.png")
    #plt.close(1)

    """ Angular Speed Plot """
    plt.figure(2)
    fig = plt.gcf()
    fig.canvas.set_window_title('IMU Angular Speed')
    plt.subplots_adjust(bottom=0.238) #Padding from bottom to fit time labels
    plt.plot(x,y4,label='Angular Speed in X')
    plt.plot(x,y5,label='Angular Speed in Y')
    plt.plot(x,y6,label='Angular Speed in Z')
    plt.xlabel('Time')
    plt.ylabel('Angular Speed (mrad/s)')
    plt.xticks(x[::2000], rotation=90)
    plt.grid(True)
    plt.title('IMU Angular Speed Info')
    plt.legend()
    plt.savefig("./graphs/imu_angular_speed.png")
    if(SHOW_GRAPH != False):
        plt.show()
    #plt.close(2)
    """ Magnetic Field Plot """
    #No info published

if __name__ == "__main__":
    scaled_imu2()