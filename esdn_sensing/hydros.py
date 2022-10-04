"""
`hydros`
================================================================================

*Python library for Hydros21 or Decagon CDT-10 water level sensor.*

**Author(s):** `Colby Sawyer <https://github.com/ColbySawyer7>`_

Implementation Notes
--------------------
**Hardware:**
Hydros 21 Conductivity, Temperature, and Depth Sensor `More Information <https://www.metergroup.com/en/meter-environment/products/hydros-21-water-level-sensor-conductivity-temperature-depth>`_

**Software and Dependencies:**

"""
#import serial.tools.list_ports
import serial
import time
import re

def parse_reading(val):
    """Takes string of values from sensor and parses them into String list

    Args:
        val (String): Unparsed string containing multiple reading from sensor ex. "0+40+24.4-140"

    Returns:
        [String]: Parsed list of strings each corresponding to a returned measurement ex. ["0","+40","+24.4","-140"]
    """
    res = re.findall(r'[-+][0-9.]+|\D', val)
    return res

class Hydros:
    """Driver for Hydros 12 or Decagon CDT-10 water level sensors
    """
    water_depth = 0
    temperature = 0
    electrical_conductivity = 0

    def __init__(self, water_depth=0, temperature=0, conductivity=0):
        """Initialize instance of sensor

        Args:
            water_depth (int, optional): Water Depth (mm). Defaults to 0.
            temperature (int, optional): Temperature (celsius). Defaults to 0.
            conductivity (int, optional): Conductivity (uS/cm). Defaults to 0.
        """
        self.water_depth = water_depth
        self.temperature = temperature
        self.electrical_conductivity = conductivity



    def get_data(self, dec_factor=100):
        """Collects data from the device attached to the SDI-12 USB external board

        Args:
            dec_factor (int, optional): Holds the decimal factor to be used for integer conversion] Defaults to 100.

        Raises:
            ValueError: Throws error if device is not found
            ValueError: Throws error if device readings are not properly formatted after parsing (invalid readings)

        Returns:
            [Bytearray]: Packaged up data to be sent via LoRa driving code
        """
        version = '1.0'

        print('+-' * 40)
        print('Simple SDI-12 Sensor Reader', version)
        print('+-' * 40)

        port_names=[]
        ports = serial.tools.list_ports.comports()
        user_port_selection=0
        i=0
        
        ser=serial.Serial(port=ports[int(user_port_selection)].device,baudrate=9600,timeout=10)
        time.sleep(2.5) # delay for arduino bootloader and the 1 second delay of the adapter.

        print('Connecting to sensor ...')
        
        ser.write(b'?!')
        sdi_12_line=ser.readline()
        sdi_12_line=sdi_12_line[:-2] # remove \r and \n since [0-9]$ has trouble with \r
        m=re.search(b'[0-9a-zA-Z]$',sdi_12_line) # having trouble with the \r
        #TODO CHECK that devices exsits
        if m :
            sdi_12_address=m.group(0) # find address
            print('\nSensor address:', sdi_12_address.decode('utf-8'))

            ser.write(sdi_12_address+b'I!')
            sdi_12_line=ser.readline()
            sdi_12_line=sdi_12_line[:-2] # remove \r and \n
            print('Sensor info:',sdi_12_line.decode('utf-8'))

            ser.write(sdi_12_address+b'M!')
            sdi_12_line=ser.readline()
            sdi_12_line=ser.readline()
            ser.write(sdi_12_address+b'D0!')
            sdi_12_line=ser.readline()
            sdi_12_line=sdi_12_line[:-2] # remove \r and \n

            value = sdi_12_line.decode('utf-8')

            parsed_values = parse_reading(value)
            if len(parsed_values) >= 3:
                self.depth = float(parsed_values[0])
                self.temperature = float(parsed_values[1])
                self.electrical_conductivity = float(parsed_values[2])
            else:
                self.depth = 0
                self.temperature = 0
                self.electrical_conductivity= 0
                raise ValueError('SENSOR ERROR: Reading from sensor doesnt match explicitly defined format.')

            print('Sensor reading:', parsed_values)
            
            sensor_data = bytearray(7)
            FEATHER_ID = 1

            depth_val = int((self.water_depth*dec_factor))
            print("Water Depth: %0.1f %%" % depth_val)

            temp_val = int((self.temperature*dec_factor))
            print("Temperature: %0.1f %%" % temp_val)

            conduc_val = int((self.electrical_conductivity*dec_factor))
            print("Conductivity: %0.1f %%" % conduc_val)

            sensor_data[0] = FEATHER_ID
            # Water Depth
            sensor_data[1] = (depth_val >> 8) & 0xff
            sensor_data[2]= depth_val & 0xff
            # Temperature
            sensor_data[3] = (temp_val >> 8) & 0xff
            sensor_data[4] = temp_val & 0xff
            #Conductivity
            sensor_data[5] = (conduc_val >> 8) & 0xff
            sensor_data[6] = conduc_val & 0xff

            return sensor_data
        else:
            raise ValueError('ERROR: No sensor detected')

