import lcm
from exlcm import example_t
msg = example_t()
msg.id= 69
msg.name= "SUCCESS"
msg.enabled = True


lc = lcm.LCM()
lc.publish("DHIRAJ", msg.encode())