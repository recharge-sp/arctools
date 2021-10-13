from decimal import Decimal
import math
import re

from utils import easings

def arcoffset(arc, dx, dy):
    result = ""
    arcre = re.compile("arc\((?P<t1>\d+),(?P<t2>\d+),(?P<x1>-?\d+\.\d+),(?P<x2>-?\d+\.\d+),(?P<easing>[bsio]+),(?P<y1>-?\d+\.\d+),(?P<y2>-?\d+\.\d+),(?P<color>\d+),(?P<fx>[a-z]+),(?P<is_trace>[a-z]+)\)")
    match = arcre.match(arc)
    matchgroup = match.groupdict()
    t1 = matchgroup["t1"]
    t2 = matchgroup["t2"]
    x1 = float(matchgroup["x1"]) + dx
    x2 = float(matchgroup["x2"]) + dx
    y1 = float(matchgroup["y1"]) + dy
    y2 = float(matchgroup["y2"]) + dy
    easing = matchgroup["easing"]
    color = matchgroup["color"]
    fx = matchgroup["fx"]
    is_trace = matchgroup["is_trace"]
    result += f"arc({t1},{t2},{x1:0.2f},{x2:0.2f},{easing},{y1:0.2f},{y2:0.2f},{color},{fx},{is_trace});\n"
    return result
