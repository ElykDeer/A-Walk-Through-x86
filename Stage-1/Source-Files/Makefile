all: stage-2.bin clean
	

stage-2.bin: stage-2.asm flag.txt
	nasm -Wall -D STAGE_1_2 -f bin -o ../Challenge-Files/stage-2.bin stage-2.asm

flag.txt: flaggen.py
	python2 flaggen.py flag{on3_5m0l1_JMP_f0r_x86_0ne_m4s5!ve_L33P_5_YOU}

clean:
	rm -f flag.txt
