#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
#     
#----Miguel Benavides---- Rolando Araujo-----
import re
#diccionario de opcodes
opcode = {'add': '0000','addi':'0001', 'and':'0010', 'andi':'0011', 'beq':'0100',
          'bne':'0101', 'jal':'0111', 'jr':'1010', 'lb':'1011',
          'or':'1100', 'sb':'1101', 'sll':'1110', 'srl':'1111', 'jota':'0110' }
#diccionario auxiliar para rellenar con 0
zero = {'c3':'000','c5': '00000', 'c8':'00000000' }
#diccionario con valor binario de etiquetas
tags = {'MAIN':'00000001', 'EXIT':'00001111', 'FUNC':'00001000','INC':'00000100', 'DEC':'00001001'}
#diccionario de valores vinarios de registros
reg = {'x0':'000', 'x1':'001', 'x2':'010',
        'x3':'011','x4':'100','x5':'101','x6':'110','x7':'111'}
#diccionario para salto de branchs
label = {'MAIN': 1, 'EXIT':15,  'INC':4,  'DEC':9,  'FUNC':8}

#implementacion por expresiones regulares
#regex = re.compile(r"(?P<label>[A-Z]*)?\:?\t?\s*(?P<nem>[^,]*),\s*(?P<item1>[^,]*),\s*(?P<item2>[^,]*),\s*(?P<item3>[^,]*)\n?")

#def check_str(text):
#    text = text.replace('\t','').strip()
#   regex_match = regex.match(text)
#    if not regex_match:
#        raise Exception("Entered text '%s' is not valid"%(text))
#    return regex_match.groupdict()

#Funcion para convertir de cadena a int
def strto(cad):
    
    if "x" in cad:
        aux = int(cad,16)
        return aux
    else:
        return int(cad)
#Funcion que regresa el valor de la direccion de memoria en C2 y bin
def jumpbranch(x):
    if x < 0:
        return bin(label[ele[4]] & (2**8-1))[2:].zfill(8)
    else:
        return (format(label[ele[4]],'08b'))
#funcion para convertir a binario 
def convert(x):
    if x < 0:
        return bin(x & (2**8-1))[2:].zfill(8)
        
    else:
        return (format(x,'08b'))
#funcion para separar los elementos del archivo
def newlist(result):
    result = lines.replace('\t','').strip()
    result = result.replace(' ','')
    result = result.replace(':',' ')
    result = result.replace(',',' ')
    return result.split(' ')


fname = input("Ingrese el nombre del archivo: ")
newfile = input("Ingrese el nombre del archivo a generar: ")
#apertua de archivo fuente y creacion de archivo destino
f = open(fname,"r")
f2 = open(newfile,"a")
lines = f.readlines()
count = 1
ele = [4]

for lines in lines:
    
    row  = newlist(lines)
    
    if len(row) == 5:
        ele = row #ele = element
    else:
        row.insert(0,"Emp") #Emp = empty
        ele = row
   
    print(ele)
   
    
    if  (ele[1] == 'addi'):
        num = strto(ele[4])
        content = opcode['addi'] + reg[ele[3]] + reg[ele[2]] + convert(num)
        f2.write(content)
        f2.write("\n")
    elif  (ele[1] == 'add'):
        content = opcode['add'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]] + zero['c5']
        f2.write(content)
        f2.write("\n")
    elif  (ele[1] == 'andi'):
        num = strto(ele[4])
        content = opcode['andi'] + reg[ele[3]] + reg[ele[3]] + convert(num)
        f2.write(content)
        f2.write("\n")    
    elif  (ele[1] == 'and'):
        content = opcode['and'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]] + zero['c5']
        f2.write(content)
        f2.write("\n")
    elif  (ele[1] == 'or'):
        content = opcode['or'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]] + zero['c5']
        f2.write(content)
        f2.write("\n")
    elif  (ele[1] == 'sll'):
        content = opcode['sll'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]] + zero['c5'] 
        f2.write(content)
        f2.write("\n")
    elif  (ele[1] == 'srl'):
        content = opcode['srl'] + reg[ele[3]] + reg[ele[4]] + reg[ele[2]] + zero['c5']
        f2.write(content)
        f2.write("\n") 
    elif  (ele[1] == 'beq'):
        num = label[ele[4]] - count
        content = opcode['beq'] + reg[ele[2]] + reg[ele[3]] +jumpbranch(num)
        f2.write(content)
        f2.write("\n")   
    elif  (ele[1] == 'bne'):
        num = label[ele[4]] - count
        content = opcode['bne'] + reg[ele[2]] + reg[ele[3]] +jumpbranch(num)
        f2.write(content)
        f2.write("\n")      
    elif  (ele[1] == 'lb'):
        num = strto(ele[3])
        content = opcode['lb'] + reg[ele[4]] + reg[ele[2]] + convert(num) 
        f2.write(content)
        f2.write("\n")   
   
    elif  (ele[1] == 'j'):
        tex = opcode['j'] + zero['c3']+ zero['c3'] + tags[ele[1]] 
        f2.write(tex)
        f2.write("\n")  
    elif  (ele[1] == 'sb'):
        num = strto(ele[3])
        content = opcode['sb'] + reg[ele[4]] + reg[ele[2]] + convert(num)
        f2.write(content)
        f2.write("\n")   
    #elif  (ele[1] == 'j'):
     #   content = opcode['j'] + zero['c3']+ zero['c3'] + tags[ele[1]] 
      #  f2.write(content)
       # f2.write("\n")  
    elif  (ele[1] == 'jal'):
        tex = opcode['jal'] + zero['c3']+ zero['c3']+ tags[ele[1]]
        f2.write(tex)
        f2.write("\n")  
    elif  (ele[1] == 'jr'):
        content = opcode['jr'] + reg[ele[2]]+ zero['c3'] + zero['c8'] 
        f2.write(content)
        f2.write("\n")
    #else:
      #  print("")

    count = count + 1
f.close()

