import re

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

# Pins are output
def vcc(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+1

# Pins are output
def gnd(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+1

# Pins are Input, Output
def buf(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+2

# Pins are Input, Output
def inv(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+2

# Pins are 2*Input, Output
def and2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+3

# Pins are 3*Input, Output
def and3(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+4

# Pins are 3*Input (first inverted), Output
def and3b1(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"(\w+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1))
	return i+4

# Pins are 3*Input (first 2 inverted), Output
def and3b2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"(\w+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1))
	return i+4

# Pins are 4*Input, Output
def and4(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+5

# Pins are 5*Input, Output
def and5(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+6

# Pins are 6*Input, Output
def and6(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+7

# Pins are 7*Input, Output
def and7(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+8

# Pins are 8*Input, Output
def and8(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+9

# Pins are 9*Input, Output
def and9(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+10]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+10

# Pins are 2*Input, Output
def or2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+3

# Pins are 3*Input, Output
def or3(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+4

# Pins are 4*Input, Output
def or4(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+5

# Pins are 5*Input, Output
def or5(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+6

# Pins are 5*Input, Output
def or6(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+7

# Pins are 5*Input, Output
def or7(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+8

# Pins are 8*Input, Output
def or8(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+9

# Pins are 9*Input, Output
def or9(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+10]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+10

# Pins are 12*Input, Output
def or12(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+10]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+11]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+12]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+13]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+13

# Pins are 16*Input, Output
def or16(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+10]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+11]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+12]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+13]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+14]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+15]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+16]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+17]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+17

# Pins are 2*Input, Output
def nand2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+3

# Pins are 3*Input, Output
def nand3(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+4

# Pins are 4*Input, Output
def nand4(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+5

# Pins are 5*Input, Output
def nand5(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+6

# Pins are 6*In, out
def nand6(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+7

# Pins are 6*In, out
def nand7(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+8

# Pins are 3*In, out
def nand3b3(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+4

# Pins are 4*In, out
def nand4b4(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+5

# Pins are 5*In, out
def nand5b5(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+6

# Pins are 2*Input, Output
def nor2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+3

# Pins are 3*Input, Output
def nor3(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+4

# Pins are 4*Input, Output
def nor4(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+5

# Pins are 5*Input, Output
def nor5(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+6

# Pins are 6*Input, Output
def nor6(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+7

# Pins are 7*Input, Output
def nor7(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+8

# Pins are 2*inputs, output
def xor2(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+3

# Pins are 4*in, Enable, 2*Select, Output
def m4_1e(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+8

# Pins are 8*in, Enable 3*Select, Output
def m8_1e(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+9]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+10]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+11]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+12]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+13]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+13

# Pins are 2*inputs, Enable, 4*Outputs
def d2_4e(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+5]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+7

# Pins are 4*inputs, Enable, 16*Outputs. Note Outputs are ordered in decimal order ie 0,1,10,11,12, etc
def d4_16e(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+7]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+14]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+15]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+16]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+17]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+18]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+19]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+20]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+21]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+9]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+10]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+11]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+12]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+13]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+21

# Pins are Clock, Enable, Clear, Carry out, 2*Outputs, TC
@static_vars(counter=0)
def cb2ce(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+5]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+6]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+7]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	block['state'].append({f'cb2ce_clk_prev{cb2ce.counter}':0})
	cb2ce.counter += 1
	return i+7

# Pins are CLK, Enable, CLR, Carry Out, output bus (15:0), TC
@static_vars(counter=0)
def cb16ce(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	bus_regex = re.compile(r'<blockpin signalname=\"(\w+)\(15:0\)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = bus_regex.search(file_lines[i+5])
	for j in range(16):
		block['state'].append({ret.group(1)+f"({j})":0})
	ret = block_regex.search(file_lines[i+6]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	block['state'].append({f'cb16ce_clk_prev{cb16ce.counter}':0})
	cb16ce.counter += 1
	return i+6

# Pins are Clock, Enable, Clear, Carry out, 4*Outputs, TC
@static_vars(counter=0)
def cd4ce(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+5]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+6]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+7]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	ret = block_regex.search(file_lines[i+8]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	block['state'].append({f"hidden_carry_cd4ce{cd4ce.counter}":0})
	ret = block_regex.search(file_lines[i+9]) 
	block['state'].append({ret.group(1):0} if ret != None else None)
	block['state'].append({f'cd4ce_clk_prev{cd4ce.counter}':0})
	cd4ce.counter += 1
	return i+9

# Pins are nLT, nRBI, 4*inputs, nBI, nRBO, 7*Outputs
def bcdtoseg(file_lines, i, block):
	block_regex = re.compile(r'<blockpin signalname=\"([\w|\(|\)]+)\"')
	ret = block_regex.search(file_lines[i+1]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+2]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+3]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+4]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+5]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+6]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+7]) 
	block['in'].append(ret.group(1))
	ret = block_regex.search(file_lines[i+8]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+9]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+10]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+11]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+12]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+13]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+14]) 
	block['out'].append(ret.group(1) if ret != None else None)
	ret = block_regex.search(file_lines[i+15]) 
	block['out'].append(ret.group(1) if ret != None else None)
	return i+15
