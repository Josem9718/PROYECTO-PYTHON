#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#     
#----Miguel Benavides---- Rolando Araujo-----
import re

opcode = {'add': '0000','addi':'0001', 'and':'0100', 'andi':'0011', 'beq':'0100',
          'bne':'0101', 'j':'0110', 'jal':'0111', 'jr':'1010', 'lb':'1011',
          'or':'1100', 'sb':'1101', 'sll':'1110', 'srl':'1111' }

tags = {'MAIN':'00000001', 'EXIT':'0', 'FUNC':'0','INC':'0', 'DEC':'0'}

reg = {'x0':'000', 'x1':'001', 'x2':'010',
        'x3':'011','x4':'100','x5':'101','x6':'110','x7':'111'}

aux = {'zero':'000', 'ceros':'0000000'}

regex = re.compile(r"(?P<label>[A-Z]*)?\:?\t?\s*(?P<nem>[^,]*),\s*(?P<item1>[^,]*),\s*(?P<item2>[^,]*),\s*(?P<item3>[^,]*)\n?")

def check_str(text):
    text = text.replace('\t','').strip()
    regex_match = regex.match(text)
    if not regex_match:
        raise Exception("Entered text '%s' is not valid"%(text))
    return regex_match.groupdict()

def convert(x):
    eval(x)
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
    
    result = lines.replace(':','')
    ele = check_str(result)

    print(ele)
    
    if (ele['nem'] == 'addi'):
        content = opcode['addi'] +reg[ele['item2']] + reg[ ele['item1']]
       # + convert(ele['item3'])
        f2.write(content)
        f2.write("\n")
    elif 'add' in ele:
        content = opcode['add'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif 'andi'in ele:
        content = opcode['andi'] + reg[ele[3]] + reg[ele[2]] + convert()
        f2.write(content)
        f2.write("\n")    
    elif 'and' in ele:
        content = opcode['and'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif 'or' in ele:
        content = opcode['or'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif 'sll' in ele:
        content = opcode['sll'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif 'srl' in ele :
        content = opcode['srl'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n") 
    elif 'beq'in ele:
        content = opcode['beq'] + reg[ele[2]] + reg[ele[3]] + offset #offset ele[4]
        f2.write(content)
        f2.write("\n")   
    elif 'bne' in ele:
        content = opcode['bne'] + reg[ele[2]] + reg[ele[3]] + offset #offset ele[4]
        f2.write(content)
        f2.write("\n")      
    elif 'lb'in ele:
        content = opcode['lb'] + reg[ele[4]] + reg[ele[2]] + offset #ofset ele[3]
        f2.write(content)
        f2.write("\n")   
    elif 'sb' in ele:
        content = opcode['sb'] + reg[ele[4]] + reg[ele[2]] + offset #ofset ele[3]      
        f2.write(content)
        f2.write("\n")   
    elif 'j' in ele:
        content = opcode['j'] + target + 00000
        f2.write(content)
        f2.write("\n")  
    elif 'jal' in ele:
        content = opcode['jal'] + target + 00000
        f2.write(content)
        f2.write("\n")  
    elif 'jr' in ele:
        content = opcode['jr'] + reg[ele[2]] + 000000000
        f2.write(content)
        f2.write("\n")

f.close()
