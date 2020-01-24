.text
.global main

main:

START:
        mov r0,#0               @ ascii of '/0', in order to clear the buffer
        mov r2,#0               @loop counter for clearing buffer
CLEAR_BUFFER:
        @clear input_string buffer
        ldr r1,=input_string
        strb r0,[r1,r2]
        add r2,r2,#1
        cmp r2,#100
        bne CLEAR_BUFFER


        @write a message in the console
        mov r0,#1
        ldr r1,=message
        mov r2,#len
        mov r7,#4
        swi 0

READ:
        @read the input string
        mov r0,#0               @first argument of read syscall (0:stdin)
        ldr r1,=input_string    @second argument of read (pointer to buffer)
        mov r2,#100             @third argument of read (number of bytes to read)
        mov r7,#3               @3 is the number of read syscall
        swi 0
        mov r3,r0               @store in r3 the number of bytes read

        @check for 'q' or 'Q' input to exit@
        cmp r3,#2               @if only 2 (1 char + EOF=2) bytes has been read check for exit
        bne DONT_EXIT
        ldrb r0,[r1],#1
        cmp r0,#0x71
        beq END                 @see if first char is 'q'
        cmp r0,#0x51
        beq END                 @see if first char is 'Q'


DONT_EXIT:
        mov r2,#-1              @r2 is the loop counter
        sub r3,r3,#1            @r3 is the number of bytes (without '/0') in input string
        ldr r1,=input_string

CONVERT:
        @convert the input string into the output string
        add r2,r2,#1
        cmp r2,#32
        beq OUTPUT

        ldrb r0,[r1,r2]
        cmp r0,#48
        blt CONVERT
        cmp r0,#53              @0-4
        blt ZERO_TO_FOUR
        cmp r0,#58              @5-9
        blt FIVE_TO_NINE
        cmp r0,#65
        blt CONVERT
        cmp r0,#91              @A-Z
        blt TO_LOWER
        cmp r0,#97
        blt CONVERT
        cmp r0,#123             @a-z
        blt TO_UPPER

ZERO_TO_FOUR:
        add r0,r0,#5
        strb r0,[r1,r2]
        b CONVERT

FIVE_TO_NINE:
        sub r0,r0,#5
        strb r0,[r1,r2]
        b CONVERT

TO_LOWER:
        add r0,r0,#32
        strb r0,[r1,r2]
        b CONVERT

TO_UPPER:
        sub r0,r0,#32
        strb r0,[r1,r2]
        b CONVERT

OUTPUT:
        @write the output string in the console
        ldr r1,=input_string
        mov r0,#1               @write syscall
        mov r2,#32              @print the 32bytes, ignoring the rest
        mov r7,#4
        swi 0

        b START
END:
        mov r7,#1               @syscall for 'exit'
        swi #0                  @software interrupt

.data
        message: .ascii "Give input string (up to 32 characters)\n"
        input_string: .ascii "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0" @pre-allocate 100byte space
        len = . - message
