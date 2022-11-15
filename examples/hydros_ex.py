from func_timeout import func_timeout, FunctionTimedOut
from esdn_sensing.hydros import Hydros, SensorError
#//=========================================
def use_hydros():
    return Hydros().get_data()
#//=========================================

#//=========================================
def get_data():
    """Main driver to fetch most recent data and return in the form of a bytearray for transmitting over LoRA

    Returns:
        bytearray: bytearray containing encoded data from the logger (intended for LoRa usage)
    """
    sensor_data = bytearray(2)
    
    try:
        # Get data from device with 30 second timeout
        hydros_data = func_timeout(30, use_hydros)
    except (FunctionTimedOut, SensorError) as err:
        exception = 2
        print(err)
    except Exception as err:
        exception = 3
        print(err)

    print('Exception: \t' + str(exception))
    sensor_data[0] = (exception >> 8) & 0xff
    sensor_data[1] = exception & 0xff

    if exception == 0:
        sensor_data.extend(hydros_data)

    return sensor_data
#//=========================================
