from datetime import datetime
import sys
import bpy
import logging

logging.disable(logging.NOTSET)

argv = sys.argv
argv = argv[argv.index("--") + 1:]  

fi = int(argv[0])


bpy.ops.drs.rendersection(fragmentIndex = fi, savePath = argv[1])
bpy.ops.drs.enablelogging(f"c:\\log{ datetime.now().strftime('%S') }.log")
bpy.ops.wm.quit_blender()