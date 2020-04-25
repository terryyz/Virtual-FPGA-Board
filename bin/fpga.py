#!/usr/bin/env python
import sys
import re
import bin.modules as modules
import tkinter as tk
from tkinter import messagebox
import bin.read_modules as read_modules

def my_MessageBox(message):
    messagebox.showwarning("Error", message)

def execute(inputs, in_vals, outputs, ops, lock):
    lock = 1
    outputs_cpy = outputs
    out_vals = {}
    #print(f"At beginning:\n{ops}")
    for operation in ops:
        ret = getattr(modules, operation['name'])([in_vals[val] if val in inputs else out_vals[val] for val in operation['in']]+[list(dic.values())[0] if dic != None else 0 for dic in operation['state']])
        #print(ret)
        for i in range(len(ret)-len(operation['state'])):
            if ret[i] == None: continue
            out_vals[operation['out'][i]] = ret[i]
        j = len(ret)-len(operation['state'])
        for i in range(len(ret)-len(operation['state']),len(ret)):
            if operation['state'][i-j] != None:
                out_vals[list(operation['state'][i-j].keys())[0]] = ret[i]
                operation['state'][i-j][list(operation['state'][i-j].keys())[0]] = ret[i]
    for elem in [key for key in out_vals if key not in outputs]:
        out_vals.pop(elem)
    #print(out_vals)
    #print(ops)
    return out_vals, ops

def interpret_file(path_to_file, name):
    # Read .sch file, passed as an argument
    if path_to_file == None: return ([],[],[],{})
    #print(f"Interpreting schematic {name}")
    try:
        f=open(path_to_file, "r")
    except IOError:
        my_MessageBox(f"Module {name} not recognised, and not found at path {path_to_file}\nIf this is a Xilinx module, please contact jmeggs@outlook.com.au so this module can be added for future versions of DrongoSim.\nIf you created this module, please ensure it is in the same directory as your schematic.")
        return ([],[],[],{})
    file_lines = f.read().split('\n')
    f.close()
    # Identify inputs and outputs
    inputs = []
    outputs = []
    inout_regex = re.compile(r'<port polarity=\"(\w+)put\" name=\"(\w+)\"')
    for line in file_lines:
        ret = inout_regex.search(line) 
        if ret != None:
            inputs.append(ret.group(2)) if ret.group(1) == "In" else outputs.append(ret.group(2))
    #print(f"Inputs and Outputs identified:\n{inputs}\n{outputs}")
    # Identify blocks
    # blocks = []
    # block_regex = re.compile(r'<bloc(\w+) s\w+name=\"(\w+)\" name=\"(\w)')
    # for line in file_lines:
    #   ret = block_regex.search(line) 
    #   if ret != None:
    #       blocks.append({'name':ret.group(2),'in':[],'out':[]}) if ret.group(1) == "k" else blocks[len(blocks)-1]['in'].append(ret.group(2)) if ret.group(3) == "I" else blocks[len(blocks)-1]['out'].append(ret.group(2))
    # Take 2
    blocks = []
    block_regex = re.compile(r'<block symbolname=\"(\w+)\"')
    i=0
    while i < len(file_lines):
        ret = block_regex.search(file_lines[i])
        if ret != None:
            #print(f"Current blocks are {blocks}")
            #print(f"Reading block {ret.group(1)}")
            blocks.append({'name':ret.group(1), 'in':[], 'out':[], 'state':[]})
            try:
                i = getattr(read_modules, ret.group(1))(file_lines, i, blocks[len(blocks)-1])
                #print(f"Successfully read {ret.group(1)}")
            except AttributeError as e:
                error_regex = re.compile(r'\'([\w|\.]+)\'[\s|\w]+has no attribute \'(\w+)\'')
                e_ret = error_regex.search(str(e))
                if e_ret == None:
                    my_MessageBox(f"An unknown error occurred.\nPlease contact jmeggs@outlook.com.au so this can be fixed.")                    
                if e_ret.group(1) == "bin.read_modules":
                    # print(path_to_file)
                    # print(path_to_file.split('/'))
                    # print(path_to_file.split('/').pop(-1))
                    # print('/'.join(path_to_file.split('/').pop(-1))+f"/{e_ret.group(2)}.sch")
                    new_pathname = path_to_file.split('/')
                    new_pathname.pop(-1)
                    (new_blocks,_,_,_) = interpret_file('/'.join(new_pathname)+f"/{e_ret.group(2)}.sch", e_ret.group(2))
                    if new_blocks == []: return ([],[],[],{})
                    blocks.pop(-1)
                    i+=1
                    (d_map, i) = create_map(file_lines, i)
                    #print(f"i is {i}")
                    #print(f"dictionary is: {d_map}")
                    #print(f"new_blocks before: {new_blocks}")
                    map_pins(d_map, new_blocks, e_ret.group(2))
                    #print(f"new_blocks after: {new_blocks}")
                    blocks += new_blocks
                    continue
                    #my_MessageBox(f"{e}\nModule {e_ret.group(2)} has not been implemented yet.\nPlease contact jmeggs@outlook.com.au so this module can be added for future versions of DrongoSim.")
                elif e_ret.group(1) == "NoneType":
                    my_MessageBox(f"Floating input detected on module {ret.group(1)}.\nPlease fix and try again.")  
                else:
                    my_MessageBox(f"An unknown error occurred.\nPlease contact jmeggs@outlook.com.au so this can be fixed.")                    
                return ([],[],[],{})

        i += 1
    if name != "main":
        if blocks == []:
            my_MessageBox(f"Schematic {name} is empty.")                    
            return ([],[],[],{})
        #print(f"finished interpreting {name}")
        return (blocks,[],[],{})
    # Order blocks based upon dependency. Strategy is to have a list of available nets. 
    # Find any blocks that have inputs that are in this list, and add them to ops list,
    # and append outputs to available nets
    ops = []
    avail_nets = inputs
    while len(blocks) > 0:
        # print(blocks)
        # print(avail_nets)
        for block in blocks:
            if [element for element in block['in'] if element in avail_nets] == block['in']:
                ops.append(block)
                avail_nets = avail_nets+block['out']+[list(dic.keys())[0] for dic in block['state'] if dic != None]
                blocks.remove(block)
    # Scan in .ucf file
    ucf = {}
    try:
        f=open(f"{path_to_file[:-4]}.ucf", "r")
    except IOError:
        my_MessageBox(".ucf file not found\nEnsure it is in the same directory as your schematic")
        return ([],[],[],{})
    file_lines = f.read().split('\n')
    f.close()
    ucf_regex = re.compile(r'NET\s+\"(\w+)\"\s+LOC[\s|=]+\"(\w+)\"')
    for line in file_lines:
        ret = ucf_regex.search(line)
        if ret != None:
            ucf[ret.group(1)] = ret.group(2)
    # Check that all inputs and outputs of schematic are valid for board
    valid_pin = ['C4', 'D9', 'A8', 'C9', 'B8', 'T10', 'T9', 'V9', 'M8', 'N8', 'U8', 'V8', 'T5', 'U16',\
    'V16', 'U15', 'V15', 'M11', 'N11', 'R11', 'T11', 'P17', 'P18', 'N15', 'N16', 'T17', 'T18', 'U17', 'U18',\
    'M14', 'N14', 'L14', 'M13', 'V10']
    for elem in inputs:
        if elem not in ucf:
            my_MessageBox(f"Input {elem} from your schematic does not appear in your ucf file")
            return([],[],[],{})
    for elem in outputs:
        if elem not in ucf:
            my_MessageBox(f"Output {elem} from your schematic does not appear in your ucf file")
            return([],[],[],{})
    for value in ucf.values():
        if value not in valid_pin:
            my_MessageBox(f"{value} is not a valid LOC value in your ucf file")
            return([],[],[],{})
    if name == "main": print("Successfully finished interpreting!")
    return (inputs, outputs, ops, ucf)

def create_map(file_lines, i):
    d = {}
    blockpin_regex = re.compile(r'<blockpin')
    signalname_regex = re.compile(r'signalname=\"([\w|\(|\)|:]+)\"')
    name_regex = re.compile(r'name=\"([\w|\(|\)|:]+)\" />')
    bus_regex = re.compile(r'(\w+)\((\d+):(\d+)\)')
    ret = blockpin_regex.search(file_lines[i]) 
    while ret != None:
        name_ret = name_regex.search(file_lines[i])
        signame_ret = signalname_regex.search(file_lines[i])
        n_bus_ret = bus_regex.search(name_ret.group(1))
        if signame_ret == None:
            if n_bus_ret == None:
                d[name_ret.group(1)] = None
            else:
                for j in range(int(n_bus_ret.group(3)), int(n_bus_ret.group(2))+1):
                    d[f"{n_bus_ret.group(1)}({j})"] = None
            i += 1
            ret = blockpin_regex.search(file_lines[i]) 
            continue
        sn_bus_ret = bus_regex.search(signame_ret.group(1))
        if n_bus_ret == None:
                d[name_ret.group(1)] = signame_ret.group(1)
        else:
            for j in range(int(n_bus_ret.group(3)), int(n_bus_ret.group(2))+1):
                d[f"{n_bus_ret.group(1)}({j})"] = f"{sn_bus_ret.group(1)}({j})"
        i += 1
        ret = blockpin_regex.search(file_lines[i])
    return(d,i)

def map_pins(d, new_ops, name):
    for op in new_ops:
        for i in range(len(op['in'])):
            if op['in'][i] in d:
                op['in'][i] = d[op['in'][i]]
            else:
                op['in'][i] += f"_{name}"
        for i in range(len(op['out'])):
            if op['out'][i] == None: continue
            if op['out'][i] in d:
                op['out'][i] = d[op['out'][i]]
            else:
                op['out'][i] += f"_{name}"
        new_state = []
        for i in range(len(op['state'])):
            if op['state'][i] == None:
                new_state.append(None)
                continue
            opname = list(op['state'][i].keys())[0]
            if opname in d:
                new_state.append({d[opname]:0})
            else:
                new_state.append({opname+f"_{name}":0})
        op['state'] = new_state
