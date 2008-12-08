#!/home/hensch/tmp/python-sandbox/bin/python
import sys
import os
import time
import signal

# use the next line if you use /WS client connections
# from tuxedo.atmiws import *
from tuxedo.atmi import *


def sighandler(sig, frame):
    print("signal handler called")
#    tpdisconnect(handle)
def sigtermhandler(sig, frame):
    print("sigerm handler called")


signal.signal(signal.SIGALRM, sighandler)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
print(signal.getsignal(signal.SIGALRM))


data = [ "huhuhuhu", "hallo", "ciao", "END" ]

for num in range(1, 10):
#    tpbegin(300)
    handle = tpconnect("RECV", "out", TPSENDONLY)
#    signal.alarm(10)
    print("handle = %d" % handle)
    for item in data:
        print("sending %d, %s ..." % (handle, item))
        evt = tpsend(handle, item, TPRECVONLY)
        evt, ret = tprecv(handle)
        print("tprecv(): evt, ret = %d, %s" % (evt, ret))
        print("sleep ...")
        time.sleep(5)
    if evt == TPEV_SVCSUCC:
#        tpcommit()
        print("transaction commited")
    else:
#        tpabort()
        print("transaction aborted")

tpterm()




# Local Variables:
# mode:python
# End:
