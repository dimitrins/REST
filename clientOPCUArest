import sys
sys.path.insert(0, "..")
import time

from opcua import Client
from rest_databasemanager import PLCSensor1Handler, PLCSensor2Handler
from rest_databasemanager import ResultSensor1Handler, ResultSensor2Handler

z = 0

client = Client("opc.tcp://172.19.10.65:4840")

print ("connect")

client.connect()

root = client.get_root_node()

print("Objects node is: ", root)
print("Children of root are: ", root.get_children())

while z < 1:
    sensor1 = client.get_node('ns=3;s="IEC_Counter_0_DB_1".CV')
    sensor2 = client.get_node('ns=3;s="IEC_Counter_0_DB_2".CV')
    
    x = sensor1.get_value()
    y = sensor2.get_value()
    
    print("sensor1 is: ", x)
    print("sensor2 is: ", y)
    
    a = int(x) * 2
    b = int(y) * 3
    
    print("result1 is: ", a)
    print("result2 is: ", b)
    
    z = z+1
    
    time.sleep(.1)
    
    PLCSensor1Handler(x)
    PLCSensor2Handler(y)
    ResultSensor1Handler(a)
    ResultSensor2Handler(b)
    
    if z == 1:
        z = 0
