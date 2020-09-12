# tlog_grapher

* Basic scalable shell script to extract .tlog data into .csv files. Python scripts to generate graphs for those .csv files.


> Some of the graphs

[![](https://i.imgur.com/PuKu660.png)]()

[![](https://i.imgur.com/avvzrMO.png)]()

[![](https://i.imgur.com/cUhmXgK.png)]()

---

## List of data plotted

- attitude
- battery_status
- distance_sensor
- global_position_int
- power_status
- scaled_imu2
- scaled_pressure
- scaled_pressure2
- vibration

> If no data exist for the given topic then the plot will be blank.


## Requirements

- python 3.7 or greater
- pip modules; matplotlib, numpy, pymavlink

### Clone

- Clone this repo to your local machine using `https://github.com/bcanozter/tlog_grapher`

### How to Run

- First, generate .csv data files by running the shell script;

```shell
$ chmod +x tlog_to_csv.sh
$ ./tlog_to_csv.sh
```

> now run `main.py`

```shell
$ python main.py
```

-  Now you should see the generated .png files and .csv files.
---

## Credits

- `mavlogdump.py` from

> https://github.com/ArduPilot/pymavlink/blob/master/tools/mavlogdump.py

- example `data.tlog` from

> https://github.com/dronekit/dronekit-la-testdata/blob/master/flight.tlog

---

## Author

- Burak Ozter

---