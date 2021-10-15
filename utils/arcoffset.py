from decimal import Decimal
import math
import re

from utils import easings

def arcoffset(arc, dx, dy):
    result = ""
    arcre = re.compile("(?P<indent> *?)(?P<type>[a-z]*)\((?P<args>.*?)\)(?:\[(?P<arctaps>.*)\])?;?")
    match = arcre.match(arc)
    matchgroup = match.groupdict()
    args = matchgroup["args"].split(",")
    t1 = args[0]
    t2 = args[1]
    x1 = float(args[2]) + dx
    x2 = float(args[3]) + dx
    y1 = float(args[5]) + dy
    y2 = float(args[6]) + dy
    easing = args[4]
    color = args[7]
    fx = args[8]
    is_trace = args[9]
    arctaps = matchgroup["arctaps"]
    if arctaps:
        result += f"{matchgroup['indent']}arc({t1},{t2},{x1:0.2f},{x2:0.2f},{easing},{y1:0.2f},{y2:0.2f},{color},{fx},{is_trace})[{arctaps}];\n"
    else:
        result += f"{matchgroup['indent']}arc({t1},{t2},{x1:0.2f},{x2:0.2f},{easing},{y1:0.2f},{y2:0.2f},{color},{fx},{is_trace});\n"
    return result
