;--header--
	bits 64
	default rd
;--variables--
	section.bss
	read_format resq 1;64-bits integer =8 bytes
;--constants--
	section.data
	read_format db "%d",0; the format string for inp
;--Entry Point--
	section.text
	global mainProcess
	Extern ExitProcess
	Extern wr
	Extern inp)

main:
	 PUSH  rbp
	 MOV rbp,rsp
	 SUB rsp,32EXIT_CLS:
XOR,rox
	 Call ExitProcess
