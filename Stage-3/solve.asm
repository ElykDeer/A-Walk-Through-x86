bits 64

mov rdi, 0x00b8000 ; Graphics Buffer

call get_ip
mov rsi, rax
add rsi, 2

xor rax, rax

print_loop:
  mov al, [rsi]
  mov ah, 0x1f
  inc rsi

  cmp ax, 0x1f00
  je .end

  mov word [rdi], ax
  add rdi, 2

  jmp print_loop

.end:
  jmp .end

get_ip:
  call next_line
  next_line:
  pop rax
ret

; This complies to:
; bf00800b00e8220000004889c64883c6024831c08a06b41f48ffc6663d001f74096689074883c702ebeaebfee80000000058c3
