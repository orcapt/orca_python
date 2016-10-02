# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:08:05 2016

@author: SRINIVAS
"""

import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)

"""

wget https://sourceforge.net/projects/pywin32/files/pywin32/
$ tar xvf six-1.0b1.tar.gz 
$ cd six-1.0b1/
$ pythonX.X setup.py   install --install-dir=/tmp/frotz
"""