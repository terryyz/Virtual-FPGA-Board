from functools import reduce

def vcc(inputs):
    return [1]

def gnd(inputs):
    return [0]

def buf(inputs):
    return [inputs[0]]

def inv(inputs):
    return [inputs[0]^1]

def and2(inputs):
    return [inputs[0]&inputs[1]]

def and3(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and3b1(inputs):
    return [(inputs[0]^1)&inputs[1]&inputs[2]]

def and3b2(inputs):
    return [(inputs[0]^1)&(inputs[1]^1)&inputs[2]]

def and4(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and5(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and6(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and7(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and8(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def and9(inputs):
    return [reduce(lambda x, y: x&y, inputs)]

def or2(inputs):
    return [inputs[0]|inputs[1]]

def or3(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or4(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or5(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or6(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or7(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or8(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or9(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or12(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def or16(inputs):
    return [reduce(lambda x, y: x|y, inputs)]

def nand2(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand3(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand4(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand5(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand6(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand7(inputs):
    return [reduce(lambda x, y: x&y, inputs)^1]

def nand3b3(inputs):
    return [((inputs[0]^1)&(inputs[1]^1)&(inputs[2]^1))^1]

def nand4b4(inputs):
    return [((inputs[0]^1)&(inputs[1]^1)&(inputs[2]^1)&(inputs[3]^1))^1]

def nand5b5(inputs):
    return [((inputs[0]^1)&(inputs[1]^1)&(inputs[2]^1)&(inputs[3]^1)&(inputs[4]^1))^1]

def nor2(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def nor3(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def nor4(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def nor5(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def nor6(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def nor7(inputs):
    return [reduce(lambda x, y: x|y, inputs)^1]

def xor2(inputs):
    return [reduce(lambda x, y: x^y, inputs)]

def m4_1e(inputs):
    if not inputs[4]: return [0]
    index=0
    if inputs[5]: index += 1
    if inputs[6]: index += 2
    return [inputs[index]]

def m8_1e(inputs):
    if not inputs[8]: return [0]
    index=0
    if inputs[9]: index += 1
    if inputs[10]: index += 2
    if inputs[11]: index += 4
    return [inputs[index]]

def d2_4e(inputs):
    if not inputs[2]: return [0]
    index=0
    if inputs[0]: index +=1
    if inputs[1]: index +=2
    return [0 if i != index else 1 for i in range(4)]

def d4_16e(inputs):
    if not inputs[4]: return [0]
    index=0
    if inputs[0]: index +=1
    if inputs[1]: index +=2
    if inputs[2]: index +=4
    if inputs[3]: index +=8
    return [0 if i != index else 1 for i in range(16)]

def cb2ce(inputs):
    if inputs[2]: return [0 for i in range(4)]+[inputs[0]]
    if not inputs[0] or inputs[0] == inputs[7] or not inputs[1]: return inputs[3:7]+[inputs[0]]
    res = 0
    for element in list(reversed(inputs[4:6])): 
        res = (res << 1) | element 
    switcher = {
        0: [1,0],
        1: [0,1],
        2: [1,1],
        3: [0,0]
    }
    #print(switcher[res])
    return [reduce(lambda x, y: x|y, inputs[4:6])^1]+switcher[res]+[1 if inputs[4:6] == [1,1] else 0]+[inputs[0]]

def cb16ce(inputs):
    if inputs[2]: return [0 for i in range(18)]+[inputs[0]]
    if not inputs[0] or inputs[0] == inputs[21] or not inputs[1]: return inputs[3:21]+[inputs[0]]
    res = 0
    #print(list(reversed(inputs[4:20])))
    for element in list(reversed(inputs[4:20])): 
        res = (res << 1) | element 
    res += 1
    #print(res)
    out = []
    for i in range(16):
        out.append(res%2)
        res = res>>1
    #print(out)
    return [res]+out+[0]+[inputs[0]]

def cd4ce(inputs):
    #print(inputs)
    if inputs[2]: return [0 for i in range(7)]+[inputs[0]]
    if not inputs[0] or inputs[0] == inputs[10] or not inputs[1]: return [0]+inputs[4:10]+[inputs[0]]
    #if inputs[2]: return [0 for i in range(7)]+[inputs[0]]
    res = 0
    for element in list(reversed(inputs[4:9])): 
        res = (res << 1) | element 
    switcher = {
        0: [1,0,0,0,0],
        1: [0,1,0,0,0],
        2: [1,1,0,0,0],
        3: [0,0,1,0,0],
        4: [1,0,1,0,0],
        5: [0,1,1,0,0],
        6: [1,1,1,0,0],
        7: [0,0,0,1,0],
        8: [1,0,0,1,0],
        9: [0,0,0,0,1],
        16: [1,0,0,0,0]
    }
    #print(switcher[res])
    return [switcher[res][4]]+switcher[res][0:5]+[1 if inputs[4:8] == [1,0,0,1] else 0]+[inputs[0]]

def bcdtoseg(inputs):
    nRBO = ((inputs[6]^1)|((inputs[1]^1)&(reduce(lambda x, y: x|y, inputs[2:6])^1)&inputs[0]))^1
    if not nRBO: return [nRBO]+[1]*7
    elif not inputs[0]: return [nRBO]+[0]*7
    else:
        res = 0
        if inputs[2]: res += 8
        if inputs[3]: res += 4
        if inputs[4]: res += 2
        if inputs[5]: res += 1
        switcher = {
        0: [0,0,0,0,0,0,1],
        1: [1,0,0,1,1,1,1],
        2: [0,0,1,0,0,1,0],
        3: [0,0,0,0,1,1,0],
        4: [1,0,0,1,1,0,0],
        5: [0,1,0,0,1,0,0],
        6: [0,1,0,0,0,0,0],
        7: [0,0,0,1,1,1,1],
        8: [0,0,0,0,0,0,0],
        9: [0,0,0,0,1,0,0],
        10: [1,1,1,0,0,1,0],
        11: [1,1,0,0,1,1,0],
        12: [1,0,1,1,1,0,0],
        13: [0,1,1,0,1,0,0],
        14: [1,1,1,0,0,0,0],
        15: [1,1,1,1,1,1,1],
    }
    #print(switcher[res])
    return [nRBO]+switcher[res]
