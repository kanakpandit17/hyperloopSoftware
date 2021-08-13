import lcm
from exlcm import structure

def my_handler(channel, data):
    msg = structure.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   id: %s" % str(msg.id))
    print("   messsage       = '%s'" % msg.message)
    print("   enabled     = %s" % str(msg.enabled))
    print("")


lc = lcm.LCM()
subscription = lc.subscribe("ANAM", my_handler)
try:
    while True:
        lc.handle()
        lc.get_fileno()
        lc.unsubscribe(subscription)
except KeyboardInterrupt:
    pass

