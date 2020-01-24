# string_manipulation.s

Just a small **ciphering** program implemented in ARM assembly.

It receives a string of 32 bytes and encryptes it with a dummy algorithm:
* a..z --> A..Z
* 0..4 --> 5..9
* 5..9 --> 0..4

The rest of the characters are not encrypted.
