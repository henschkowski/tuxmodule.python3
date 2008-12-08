#!/home/hensch/tmp/python-sandbox/bin/python

import sys

# use the next line if you use /WS client connections
# import tuxedo.atmiws
import tuxedo.atmi


if len(sys.argv) < 2:
    print("Usage: %s <string> [<string>]*" % (sys.argv[0]))
    sys.exit(1)

for index in range(1, len(sys.argv)):
    print(tuxedo.atmi.tpcall("TOUPPER", sys.argv[index]))

sys.exit(0)

# Local Variables:
# mode:python
# End:
