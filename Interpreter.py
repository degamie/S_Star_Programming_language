import sys,os
#import pandas as pd
program_filepath=sys.argv[0]
print(program_filepath)

#tokenize Program #
program_files=list(input())
with open(program_filepath,'r')as file:program_lines=[]
#program_lines.strip()
for line in program_files:
	for line in program_files:program=[]

for line in program_files:
	parts=line.split()
	opcode=parts[0]




#lines Validation
if(opcode==""):program.append(opcode)
	#continue

#opcode tokeinze storage
#program.append(opcode)
cls_s = parts[0]
#opcode handling
if opcode=="PUSH":number=int(parts[1]),program.append(opcode)
if opcode=="PRINT":
    str_literal=''.join(parts[1:])
    program.append(str_literal)


#equilizer
if opcode=="JUMP.EQ.0":program.append(cls_s)
#greater -jump to
if opcode=="JUMP.GT.0":program.append(cls_s)

print(program)

#assembly translation
asm_filepath=program_filepath[:-4]+".asm"

out=open(asm_filepath,"w")
out.write(""";--header--
	bits 64
	default rd
""")
out.write(""";--variables--
	section.bss
	read_format resq 1;64-bits integer =8 bytes
""")
out.write(""";--constants--
	section.data
	read_format db "%d",0; the format string for inp
""")

#for i ,str_literals in enumerate(str_literal):
str_literals = []
for i ,str_literal in enumerate(str_literals):
	out.write(f"str_literals_{i}db\"{str_literals}\",0\n")
out.write(""";--Entry Point--
	section.text
	global mainProcess
	Extern ExitProcess
	Extern wr
	Extern inp)

main:
\t PUSH  rbp
\t MOV rbp,rsp
\t SUB rsp,32""")

ip=0
while(ip<len(program)):
	op=program[ip]
	
	ip+=1
	

	if opcode.endswith(""):
		out.write(f";--cls_s--","\n")
		
	out.write(f"{opcode},\n")
	
	##Tokens's Stack PUSH Operation
	if opcode=="PUSH":number=program[ip]
	ip+=1
	out.write(f"--PUSH--\n")
	out.write(f"--PUSH--\n")
	
	##Tokens's Stack POP Operation
	if opcode=="POP":out.write(f";--PUSH--\n"),out.write(f"\t POP\n")

	#str_literals = []
	for i in len(str_literals):
		if program[ip] == "PRINT": str_literals = program[ip + 1]
		program[ip + 1] = len(str_literals)
		str_literals.append(str_literals)



	##Tokens Addition
	if opcode=="ADD":out.write(f"--ADD--\n")
	out.write(f"\t--POP rax\n")
	out.write(f"--POP rbx\n")
	out.write(f"\t ADD rbx rax \n")
	out.write(f"\t PUSH rbx\n")

	##Tokens Subtracting 
	if opcode=="SUB":out.write(f";--SUB--\n")
	out.write(f"\t POP rax\n")
	out.write(f"\t SUB qword[_rsp],rax\n")
	
	##Printing Tokens
	if opcode=="PRINT":str_literal_index=program[ip]
	ip+=1
	out.write(f"--PRINT--")
	###String Literals indexing
	out.write(f'\t LEA rcx,str_literals{str_literal_index}\n')
	###Stored Sting's XOR Gate Implementation
	out.write(f'\t XOR eax,eax\n')
	###Printing Resultant output using 'wr' Printing Keyword
	out.write(f'\t CALL wr\n')
	##Reading Tokens
	if opcode == "READ":out.write(f"--READ--")
	out.write(f"\t LEA rcx,read_format\n")
	out.write(f"\t LEA rdx,read_format\n")
	out.write(f"\t XOR eax,read_format\n")
	out.write(f"\t CALL inp()\n")
	out.write(f"\t PUSH qword[read_number]\n")

	##Token (jump or equal) to
	if opcode == "JUMP.GT.0":
		cls_s=program[ip]
		ip+=1
		out.write(f"--JUMP.EQ.0--")
		out.write(f"CMP qword[rsp],0\n")
		out.write(f"JE{cls_s},\n")

	elif opcode == "JUMP.GT.0":
		cls_s=program[ip]
		ip+=1

##Interpreter

class Stack:
	def __init__(self,size):
		self.buf=[0 for _ in range(size)]
		self.sp-=1

	def push(self,num):
		self.num+=num
		self.buf[self.sp]
		return num

	def pop(self, num):
		self.num -= num
		return num

	def push(self, num):
		return self.buf[self.sp]

#Programm Counter[pc] Register Initialization
pc=0
#Stack 'size Declaration
#stack=Stack(256)
stack=[]
l=len(stack)
l=256
#Iterating [pc] till num pushed into stack
num=int()
while program!=num:
	# Stack Push Operation
	if opcode=="PUSH":
		num=program[pc]
		pc+=1

		stack.append(num)
	if opcode=="POP":
		stack.pop()

	if opcode == "ADD":
		a=stack.pop()
		b = stack.pop()

	if opcode=="SUB":
		a,b=stack.pop()
		stack.push(b-a)

	if opcode == "PRINT":
		str_literal=program[pc]
		pc+=1
		print(str_literal)

	if opcode=="READ":
		num=int(input())
		stack.push(num)

	elif opcode=="JUMP.EQ.0":
		num=stack.pop()

	elif opcode == "JUMP.GT.0":  num=stack.top()



