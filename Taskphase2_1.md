section .data
    num1 dq 25
    num2 dq 17
    resultMsg db "Result: ", 0
    newline db 10, 0

section .bss
    buffer resb 32

section .text
    global _start

_start:
    mov rax, [num1]
    add rax, [num2]

    ; convert integer → string
    mov rdi, buffer
    call int_to_string

    ; print "Result: "
    mov rax, 1
    mov rdi, 1
    mov rsi, resultMsg
    mov rdx, 8
    syscall

    ; print converted number
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, rbx
    syscall

    ; print newline
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall

;------------------------------------
; int_to_string: converts RAX to ASCII
; RDI = buffer
; returns RBX = length
;------------------------------------
int_to_string:
    mov rcx, 0
    mov rbx, 0

.convert_loop:
    xor rdx, rdx
    mov r10, 10
    div r10
    add rdx, '0'
    push rdx
    inc rcx
    test rax, rax
    jnz .convert_loop

.write_back:
    pop rdx
    mov [rdi], dl
    inc rdi
    inc rbx
    loop .write_back
    ret
