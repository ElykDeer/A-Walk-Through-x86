all: tacOS-base.bin clean


tacOS-base.bin: flag.txt ../../Stage-1/Challenge-Files/stage-1.asm stage-2.bin
	$(eval num_sectors := $(shell BLOCKSIZE=512 du $(realpath stage-2.bin) | cut -f1))
	nasm -Wall -D NUM_SECTORS=$(num_sectors) -D STAGE_3 -f bin -o stage-1.bin ../../Stage-1/Challenge-Files/stage-1.asm
	dd bs=512        if=stage-1.bin of=../Challenge-Files/tacOS-base.bin
	dd bs=512 seek=1 if=stage-2.bin of=../Challenge-Files/tacOS-base.bin

flag.txt:
	../../Stage-1/Source-Files/flaggen.py flag{fake_flag}

stage-2.bin: ../../Stage-1/Source-Files/stage-2.asm
	nasm -Wall -f bin -o stage-2.bin ../../Stage-1/Source-Files/stage-2.asm

clean:
	rm flag.txt stage-1.bin stage-2.bin
