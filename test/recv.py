#!/home/hensch/tmp/python-sandbox/bin/python
import sys
import os
from tuxedo.atmi import *

class server:
        def RECV(self, arg):
                print("connect to RECV ...")
                try:
                        handle = self.cd
                        print("   cd = %i"  % self.cd)
                except:
                        print("no cd given")

                try:
                        print("   arg = %s" % arg)
                except:
                        print("no arg given")


                try:
                        print("   name = %s" % self.name)
                except:
                        print("no name given")


                try:
                        while 1:
                                evt, rec = tprecv(handle)
                                print(evt, rec)
                                if rec == "END":
                                        userlog("server returning TPSUCCESS")
                                        return TPSUCCESS
                                else:
                                        ret = "len = %d" % len(rec)
#                                       userlog("call TOUPPER ...")
#                                       tpcall("TOUPPER", "")
                                        userlog("sending %s ..." % (ret))
                                        ret = tpsend(handle, ret, TPRECVONLY)
                except RuntimeError as e:
                        exception = "got exception: %s" % e
                        userlog(exception)
                        return TPFAIL

                except:
                        userlog( "got exception")
                        return TPFAIL

        def init(self, arguments):

                tpopen()
                tpadvertise("RECV");

        def cleanup(self):
                userlog("cleanup in recv_py called!")


srv = server()

def exithandler():
        print("huuhhu")
sys.exitfunc = exithandler

if __name__ == '__main__':
        mainloop(sys.argv, srv, None)

# Local Variables:
# mode:python
# End:
