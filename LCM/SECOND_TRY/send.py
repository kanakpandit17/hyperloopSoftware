import lcm
from exlcm import structure
msg = structure()
msg.id= 34
msg.message= "TWO DEVICES SUCCESSFUL"
msg.enabled = True


lc = lcm.LCM()
lc.publish("ANAM", msg.encode())