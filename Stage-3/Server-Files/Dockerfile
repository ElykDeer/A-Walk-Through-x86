FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && apt-get install build-essential qemu python3-dev -y
RUN apt-get install -y socat nasm

COPY Challenge-Files/part-3-server.py Challenge-Files/Makefile Challenge-Files/tacOS-base.bin Server-Files/flag.txt /
RUN chmod +x /part-3-server.py

CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork", "EXEC:./part-3-server.py"]
