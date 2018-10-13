The provided Dockerfile deploys a server that the quiz is hosted on such that people can test their answers and potentially get the flag.

To test the program locally, run `make run` in the `Challenge-Files` directory.  This will compile tacOS (the small bootloader/OS I've made) and run it through QEMU.

The flag that is granted from the server for the proper solutions to stage 1 is in `Server-Files/stage-1-server.py`.

People solving the challenge should be provided with the three files located in `Challenge-Files`:
 `stage-1.asm`
 `stage-2.bin`
 `Makefile`

Description to be provided to people trying to solve the challenge:
```
N3WBS 0NLY!!!

Your first lesson in assembly is in 'stage-1.asm', so read it down!

To run the code, run `make run`; this will compile tacOS (the small bootloader/OS I've made) and run it through QEMU.

To solve the challenge, you'll need to connect to the quiz server and answer some questions about the source code.

nc <server_ip> <port>
```
