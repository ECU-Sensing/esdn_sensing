from devices.hydros import Hydros

#//=========================================
def get_data():
    """Main driver to fetch most recent data and return in the form of a bytearray for transmitting over LoRA

    Returns:
        bytearray: bytearray containing encoded data from the logger (intended for LoRa usage)
    """
    sensor_data = Hydros().get_data()
    
    return sensor_data
#//=========================================
