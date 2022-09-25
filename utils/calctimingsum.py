from decimal import Decimal
import math
import re

objre = re.compile("(?P<indent> *?)timing\((?P<args>.*?)\)(?:\[(?P<arctaps>.*)\])?;?")

# arc(0,300,0.00,0.50,si,1.00,0.00,0,none,false);
def calctimingsum(base_bpm, timings):
    sum = 0
    prev_timing = 0
    objmatch = objre.match(timings[0])
    objmatch = objmatch.groupdict()
    args = objmatch["args"].split(",")
    prev_timing = int(args[0])
    prev_scale = float(args[1])/base_bpm/1000
    timings.pop(0)
    for timing in timings:
        objmatch = objre.match(timing)
        if not objmatch:
            continue
        objmatch = objmatch.groupdict()
        args = objmatch["args"].split(",")
        timing = int(args[0])
        scale = float(args[1])/base_bpm/1000
        sum += (timing-prev_timing)*prev_scale
        prev_scale = scale
    return sum
