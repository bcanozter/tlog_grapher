# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
cyan=`tput setaf 6`
reset=`tput sgr0`

#Check if survey data exists
FILE=./data.tlog
if [ ! -f "$FILE" ]; then
    echo "${red}> Make sure data.tlog exists and placed in the same directory.${reset}"
    exit 0
fi

#Add more to the array to extract more csv data
FILES=(ATTITUDE BATTERY_STATUS DISTANCE_SENSOR GLOBAL_POSITION_INT POWER_STATUS SCALED_IMU2 SCALED_PRESSURE SCALED_PRESSURE2 VIBRATION )

#Create folder to output files into
if [ ! -d ./logs ]; then
  mkdir -p ./logs;
fi

function ctrl_c() {
    echo "${red}> Exiting..${reset}"
	exit 0
}


for((i=0; i<${#FILES[@]}; i++))
	do
		echo "${green}> Writing to ${FILES[i]}.csv .."
		echo "${FILES[i]}"
		python3 mavlogdump.py $FILE  > "./logs/${FILES[i]}.csv" --format csv --types ${FILES[i]}
		echo "${cyan}> Done."

	done

echo "${red}> Extracted all data to ./logs/ folder.${reset}"
