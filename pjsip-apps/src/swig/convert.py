import re


def enum_pack(matches):
    result = ord(matches.group(7)) << 24 \
           | ord(matches.group(5)) << 16 \
           | ord(matches.group(3)) << 8  \
           | ord(matches.group(1))
    return str(result)


print 'parsing symbols.i  ...',


with open('symbols.i', 'r') as inFile:
    data = inFile.read()

pattern = r"\(\((?:\('(.)'\s<<\s(\d+)\)?\s\|\s)(?:\('(.)'\s<<\s(\d+)\)\)?\s\|\s)(?:\('(.)'\s<<\s(\d+)\)\)?\s\|\s)'(\s|\w)?'"
newData = re.sub(pattern, enum_pack, data)

with open("symbols.i", "w") as outFile:
    outFile.write(newData)

print 'done!'