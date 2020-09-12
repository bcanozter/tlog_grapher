import os
import multiprocessing 
from DISTANCE_SENSOR        import distance_sensor
from BATTERY_STATUS         import battery_status
from GLOBAL_POSITION_INT    import global_position_int
from POWER_STATUS           import power_status
from SCALED_IMU2            import scaled_imu2
from SCALED_PRESSURE        import scaled_pressure
from SCALED_PRESSURE2       import scaled_pressure2
from VIBRATION              import vibration
if not os.path.exists('./graphs'):
    os.makedirs('./graphs')

''' Set to True to see all the graphs displayed,
    Set to False to generate graphs in the background
    and they will be saved as .png 
'''
SHOW_GRAPH = True 

NUM_OF_PROCESSES = 7

GRAPHS = [distance_sensor, battery_status, global_position_int,
          power_status, scaled_imu2, scaled_pressure,scaled_pressure2]
if __name__ == "__main__":
    # Using multiprocessing otherwise graphs blocking execution 
    processes = []    
    for i in range(0,NUM_OF_PROCESSES):
        p = multiprocessing.Process(target=GRAPHS[i])
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()