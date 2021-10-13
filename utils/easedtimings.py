from decimal import Decimal
import math
import re

from utils import easings

# arc(0,300,0.00,0.50,si,1.00,0.00,0,none,false);
def easedtimings(t1, t2, frombpm, tobpm, parts, easing, beatline):
    result = ""
    timinglen = t2 - t1
    tick = 0
    old_timing = t1
    timing = t1 + timinglen*tick/parts
    bpm = frombpm
    while tick <= parts:
        bpm = frombpm + (tobpm - frombpm)  * tick/parts
        if easing == "b":
            bpm = frombpm + (tobpm - frombpm) * easings.b(tick/parts)
        if easing == "si":
            bpm = frombpm + (tobpm - frombpm) * easings.si(tick/parts)
        if easing == "so":
            bpm = frombpm + (tobpm - frombpm) * easings.so(tick/parts)
        if easing == "qi":
            bpm = frombpm + (tobpm - frombpm) * easings.qi(tick/parts)
        if easing == "qo":
            bpm = frombpm + (tobpm - frombpm) * easings.qo(tick/parts)
        if easing == "ci":
            bpm = frombpm + (tobpm - frombpm) * easings.ci(tick/parts)
        if easing == "co":
            bpm = frombpm + (tobpm - frombpm) * easings.co(tick/parts)
        result += f"timing({int(timing)},{bpm:0.2f},{beatline:0.2f});\n"
        tick += 1
        timing = t1 + timinglen*tick/parts
    # last part of arc
    return result
