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

aux = {'zero':'000'}

fname = input("Ingrese el nombre del archivo: ")
newfile = input("Ingrese el nombre del archivo a generar: ")

f = open(fname,"r")
f2 = open(newfile,"w")
lines = f.readlines()

for lines in lines:

    
    e =str ( lines.split())
    print(type(e))
    print(e)
    ele = e.split(",")
    print(type(ele))
    print(ele)
   
    if ele[1] == "addi":
        content = opcode['addi'] + reg[ele[3]] + reg[ele[2]]
        f2.write(content)
        f2.write("\n")
    elif ele[1] == "add":
        content = opcode['add'] + reg[ele[3]] + reg[ele[4]] 
        f2.write(content)
        f2.write("\n")
    else:
            print("no se")
    
f.close()
