import re

def camera(t, transverse, bottomzoom, linezoom, steadyangle, topzoom, angle, easing, lastingtime):
    return f"camera({t:.0f},{transverse:.2f},{bottomzoom:.2f},{linezoom:.2f},{steadyangle:.2f},{topzoom:.2f},{angle:.2f},{easing},{lastingtime:.0f});"

def arc2camera(arc):
    arcre = re.compile("(?P<indent> *?)arc\((?P<t1>\d+),(?P<t2>\d+),(?P<x1>-?\d+\.\d+),(?P<x2>-?\d+\.\d+),(?P<easing>[bsio]+),(?P<y1>-?\d+\.\d+),(?P<y2>-?\d+\.\d+),(?P<color>[\-\d]+),(?P<fx>[a-z]+),(?P<is_trace>[a-z]+)\)")
    match = arcre.match(arc)
    if not match: return arc
    matchgroup = match.groupdict()
    t1 = int(matchgroup["t1"])
    t2 = int(matchgroup["t2"])
    lastingtime = t2 - t1
    if lastingtime == 0: lastingtime = 1
    x1 = float(matchgroup["x1"])
    x2 = float(matchgroup["x2"])
    dx = x2 - x1
    y1 = float(matchgroup["y1"])
    y2 = float(matchgroup["y2"])
    dy = y2 - y1
    easing: str = matchgroup["easing"]
    color = int(matchgroup["color"])
    is_trace = matchgroup["is_trace"] == "true"
    cameraeasing = "l"
    if easing.startswith("si"): cameraeasing = "qo"
    if easing.startswith("so"): cameraeasing = "qi"
    if easing.startswith("b"): cameraeasing = "s"
    if is_trace: return camera(t1, 0, 0, 0, 0, 0, 0, "reset", 0)
    if color == 0:
        return camera(t1, dx * 850, dy * 450, 0, 0, 0, 0, cameraeasing, lastingtime)
    if color == 1:
        return camera(t1, 0, 0, dy * 100, 0, 0, dx * 180, cameraeasing, lastingtime)
    return camera(t1, 0, 0, 0, dx * 180, dy * 360, 0, cameraeasing, lastingtime)
