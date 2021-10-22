#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#     
#----Miguel Benavides---- Rolando Araujo-----

opcode = {'add': '0000','addi':'0001', 'and':'0100', 'andi':'0011', 'beq':'0100',
          'bne':'0101', 'j':'0110', 'jal':'0111', 'jr':'1010', 'lb':'1011',
          'or':'1100', 'sb':'1101', 'sll':'1110', 'srl':'1111' }

tags = {'MAIN':'00000001', 'EXIT':'0', 'FUNC':'0','INC':'0', 'DEC':'0'}

reg = {'x0':'000', 'x1':'001', 'x2':'010',
        'x3':'011','x4':'100','x5':'101','x6':'110','x7':'111'}

aux = {'zero':'000', 'ceros':'0000000'}

def convert(x):
    if x < 0:
        return bin(x & (2**8-1))[2:].zfill(8)
        
    else:
        return (format(x,'08b'))


fname = input("Ingrese el nombre del archivo: ")
newfile = input("Ingrese el nombre del archivo a generar: ")

f = open(fname,"r")
f2 = open(newfile,"w")
lines = f.readlines()

for lines in lines:

    
    e =str ( lines.split())
    print(type(e))
    print(e)
    ele = [x.strip() for x in e.split(',')]
    print(type(ele))
    print(ele)
   
    if ele[1] == "addi":
        content = opcode['addi'] + reg[ele[3]] + reg[ele[2]] + convert()
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "add":
        content = opcode['add'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "andi":
        content = opcode['andi'] + reg[ele[3]] + reg[ele[2]] + convert
        f2.write(content)
        f2.write("\n")    
    elif ele[1] == "and":
        content = opcode['and'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "or":
        content = opcode['or'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "sll":
        content = opcode['sll'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "srl":
        content = opcode['srl'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n") 
    elif ele[1] == "beq":
        content = opcode['beq'] + reg[ele[2]] + reg[ele[3]] + offset #offset ele[4]
        f2.write(content)
        f2.write("\n")   
    elif ele[1] == "bne":
        content = opcode['bne'] + reg[ele[2]] + reg[ele[3]] + offset #offset ele[4]
        f2.write(content)
        f2.write("\n")      
    elif ele[1] == "lb":
        content = opcode['lb'] + reg[ele[4]] + reg[ele[2]] + offset #ofset ele[3]
        f2.write(content)
        f2.write("\n")   
    elif ele[1] == "sb":
        content = opcode['sb'] + reg[ele[4]] + reg[ele[2]] + offset #ofset ele[3]
        f2.write(content)
        f2.write("\n")   
    elif ele[1] == "j":
        content = opcode['j'] + target + 00000
        f2.write(content)
        f2.write("\n")  
    elif ele[1] == "jal":
        content = opcode['jal'] + target + 00000
        f2.write(content)
        f2.write("\n")  
    elif ele[1] == "jr":
        content = opcode['jr'] + reg[ele[2]] + 000000000
        f2.write(content)
        f2.write("\n")          
f.close()