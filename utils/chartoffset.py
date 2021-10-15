from decimal import Decimal
import math
import re

from utils import easings

def chartoffset(obj: str, offset, change_audio_offset=False):
    result = ""
    objre = re.compile("(?P<indent> *?)(?P<type>[a-z]*)\((?P<args>.*?)\)(?:\[(?P<arctaps>.*)\])?;?")
    objmatch = objre.match(obj)
    if not objmatch:
      if obj.startswith("AudioOffset:") and change_audio_offset:
        return f"AudioOffset:{int(obj.lstrip('AudioOffset:').strip())-offset}"
      else: return obj
    objmatch = objmatch.groupdict()
    indent = objmatch["indent"]
    objtype = objmatch["type"]
    if objtype == "timinggroup": return obj
    args = objmatch["args"].split(",")
    args[0] = str(int(args[0]) + offset)
    newarctap = ""
    if objtype in ["hold", "arc"]:
      args[1] = str(int(args[1]) + offset)
    if objtype == "arc":
      if objmatch["arctaps"]:
        arctaparr = []
        arctaps = objmatch["arctaps"].split(",")
        for arctap in arctaps:
          arctapre = objre.match(arctap)
          arctaptime = arctapre.groupdict()["args"]
          arctaparr.append(f"arctap({int(arctaptime)+offset})")
        newarctap = "[" + ",".join(arctaparr) + "]"
    argstr = ",".join(args)
    return f"{indent}{objtype}({argstr}){newarctap};"

    
