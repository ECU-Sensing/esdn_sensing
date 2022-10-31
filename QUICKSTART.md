## Installing from PyPi

For specific user:

    pip3 install esdn_sensing

For system-wide installation:

    sudo pip3 install esdn_sensing

## Quickstart

    from esdn_sensing import Hydros, SensorError
    import logging
    import sys

    #//=========================================
    def get_data():
        try: 
            sensor_data = Hydros().get_data()
        except (FunctionTimedOut, SensorError) as err:
            exception = 3
            print(err)
        
        return sensor_data
    #//=========================================