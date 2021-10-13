from decimal import Decimal
import math
import re

from utils import easings

# arc(0,300,0.00,0.50,si,1.00,0.00,0,none,false);
def splitarc(arc, parts,flip_trace):
    result = ""
    arcre = re.compile("arc\((?P<t1>\d+),(?P<t2>\d+),(?P<x1>-?\d+\.\d+),(?P<x2>-?\d+\.\d+),(?P<easing>[bsio]+),(?P<y1>-?\d+\.\d+),(?P<y2>-?\d+\.\d+),(?P<color>\d+),none,(?P<is_trace>[a-z]+)\)")
    match = arcre.match(arc)
    matchgroup = match.groupdict()
    t1 = int(matchgroup["t1"])
    t2 = int(matchgroup["t2"])
    arclen = t2 - t1
    x1 = float(matchgroup["x1"])
    x2 = float(matchgroup["x2"])
    y1 = float(matchgroup["y1"])
    y2 = float(matchgroup["y2"])
    easing = matchgroup["easing"]
    color = int(matchgroup["color"])
    is_trace = matchgroup["is_trace"] == "true"
    split_arc_duration = arclen/parts
    tick = 1
    old_arc_time = t1
    next_arc_time = t1 + arclen*tick/parts
    oldx = x1
    oldy = y1
    while tick < parts:
        # X
        nextx = x1 + (x2 - x1) * tick/parts
        if easing.startswith("b"):
            nextx = x1 + (x2 - x1) * easings.b(tick/parts)

        if easing.startswith("si"):
            nextx = x1 + (x2 - x1) * easings.si(tick/parts)
        if easing.startswith("so"):
            nextx = x1 + (x2 - x1) * easings.so(tick/parts)
        # Y
        if len(easing) > 2:
            if easing.endswith("si"):
                nexty = y1 + (y2 - y1) * easings.si(tick/parts)
            if easing.endswith("so"):
                nexty = y1 + (y2 - y1) * easings.so(tick/parts)
        else:
            if easing.startswith("b"):
                nexty = y1 + (y2 - y1) * easings.b(tick/parts)
            else:
                nexty = y1 + (y2 - y1) * tick/parts
        result += f"arc({int(old_arc_time)},{int(next_arc_time)},{oldx:0.2f},{nextx:0.2f},s,{oldy:0.2f},{nexty:0.2f},{color},none,{str(is_trace).lower()});\n"
        tick += 1
        oldx = nextx
        oldy = nexty
        old_arc_time = next_arc_time
        next_arc_time = t1 + arclen*tick/parts
        if flip_trace:
            is_trace = not is_trace
    # last part of arc
    result += f"arc({int(old_arc_time)},{int(t2)},{oldx:0.2f},{x2:0.2f},s,{oldy:0.2f},{y2:0.2f},{color},none,{str(is_trace).lower()});\n"
    return result
