import re

with open('test10mm.gcode') as gcode:
    for line in gcode:
        line = line.strip()
        coord = re.findall(r'[XY].?\d+.\d+', line)
        if coord:
            print("{} - {}".format(coord[0], coord[1]))