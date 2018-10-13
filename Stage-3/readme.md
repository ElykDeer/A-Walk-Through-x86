The provided Dockerfile deploys a server that the the competitors need to interact with to solve the challenge.

To prepare this challenge:
```
docker build -t=stage-3 -f Server-Files/Dockerfile .
docker run -d --restart always -p 9004:8000 -p 5900-6100:5900-6100 stage-3
```

To test the challenge `nc localhost 9004` and paste the solution from solve.asm... Then connect to the VNC server to see that it actually worked.

The flag that the competitors have to print with the code they submit is stored in `Sever-Files/flag.txt`.

People solving the challenge should be provided with the three files located in `Challenge-Files`:
 `tacOS-base.bin` (which can be rebuilt by running make in `Source-Files`)
 `part-3-server.py`
 `Makefile`

Description to be provided to people trying to solve the challenge:
```
The final boss!

Time to pull together your knowledge of Bash, Python, and stupidly-low-level assembly!!

This time you have to write some assembly that I am going to run..  You'll see the output of your code through VNC for 60 seconds.

Objective: Print the flag.

What to know:

Strings need to be alternating between the character you want to print and '0x1f' (0x1f611f611f611f61 for four 'a's).

To print a string you need to write those alternating bytes to the frame buffer (starting at 0x00b8000...just do it).  Increment your pointer to move through this buffer.

If you're having difficulty figuring out where the flag is stored in memory, this code snippet might help you out:

~~~
get_ip:
  call next_line
  next_line:
  pop rax
ret
~~~

That'll put the address of `pop rax` into rax.

Call serves as an alias for `push rip` (the instruction pointer - where we are in code) followed by `jmp _____` where whatever is next to the call fills in the blank.

And in case this comes up, you shouldn't need to know where you are loaded in memory if you use that above snippet...

Happy Reversing!!

 - Elyk
``` 
