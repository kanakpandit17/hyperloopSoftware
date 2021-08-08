import lcm
from exlcm import example_t

def my_handler(channel, data):
    msg = example_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   id: %s" % str(msg.id))
    print("   messsage       = '%s'" % msg.name)
    print("   enabled     = %s" % str(msg.enabled))
    print("")


lc = lcm.LCM()
subscription = lc.subscribe("DHIRAJ", my_handler)
try:
    while True:
        lc.handle()
        lc.unsubscribe(subscription)
except KeyboardInterrupt:
    pass

