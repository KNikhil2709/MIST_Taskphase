section .bss
    input resb 256

section .text
    global _start

_start:
    ; read from STDIN
    mov rax, 0
    mov rdi, 0
    mov rsi, input
    mov rdx, 256
    syscall

    mov rcx, rax        ; number of bytes read
    mov rbx, input      ; pointer to buffer

capitalize_loop:
    cmp rcx, 0
    je print_output

    mov al, [rbx]
    ; check if a-z
    cmp al, 'a'
    jl skip
    cmp al, 'z'
    jg skip

    sub al, 32          ; convert to uppercase
    mov [rbx], al

skip:
    inc rbx
    dec rcx
    jmp capitalize_loop

print_output:
    mov rax, 1          ; write
    mov rdi, 1          ; stdout
    mov rsi, input
    mov rdx, 256
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
