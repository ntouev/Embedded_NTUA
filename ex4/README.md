# Σχεδίαση Ενσωματωμένων Συστημάτων
## 4η εργαστηριακή άσκηση 2019-2020
## ΝΤΟΥΡΟΣ ΕΥΑΓΓΕΛΟΣ 03112905

# Άσκηση 1

Για τη συγκεκριμένη άσκηση έγινε εγκατάσταση του **cross-compiler building toolchain crosstool-ng** και του **pre-compliled cross-compiler linaro**. Στην περίπτωση του πρώτου κατα την εγκατάσταση χρειάστηκε να προστεθούν κάποια πακέτα στο σύστημά μας, ενώ στην περίπτωση του δεύτερου δεν αντιμετωπίστηκε καμία δυσκολία.

## 1

Επιλέξαμε την αρχιτεκτονική "arm-cortexa9_neon-linux-gnueabihf" επειδή κανουμε target το VM της πρώτης άσκησης που έκανε emulate arm αρχιτεκτονική. Σε άλλη περίπτωση το εκτελέσιμο δεν θα μπορούσε να τρέξει στο συγκεκριμένο VM.

Aυτή η αναπαράσταση αναλύεται ως εξής:
* Αρχιτεκτονική **arm**.
* Eπεγεργαστής **cortexa9** με επέκταση **neon** για SIMD εντολές.
* Πυρήνας **Linux**.
* Yπάρχει υποστήριξη **embedded-application binary interface (eabi)**.
* **Hard float**.

## 2
Έγινε χρήση της βιβλιοθήλης **glibc**. Aυτό φαίνεται χρησιμοποιώντας την εντολή

```console
$ ldd -v ~/x-tools/arm-cortexa9_neon-linux-gnueabihf/bin/arm-cortexa9_neon-linux-gnueabihf-gcc
```

παίρνουμε output:

```console
linux-vdso.so.1 (0x00007fff891f9000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f79784bb000)
/lib64/ld-linux-x86-64.so.2 (0x00007f79788ac000)

Version information:
/home/vaggelis/x-tools/arm-cortexa9_neon-linux-gnueabihf/bin/arm-cortexa9_neon-linux-gnueabihf-gcc:
        ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
        libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.9) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.11) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
        libc.so.6 (GLIBC_2.3.4) => /lib/x86_64-linux-gnu/libc.so.6
/lib/x86_64-linux-gnu/libc.so.6:
        ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
        ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
```

## 3
#### Custom cross-compiler
Κάνουμε compile το *phods.c* με τον **custom cross-compiler**

```console
$ ~/x-tools/arm-cortexa9_neon-linux-gnueabihf/bin/ \
> arm-cortexa9_neon-linux-gnueabihf-gcc -o phods_crosstool.out phods.c
```

H εντολή
```console
$ file phods_crosstool.c
```
δίνει output
```console
phods_crosstool.out: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-, for GNU/Linux 3.2.0, with debug_info, not stripped
```

Eνώ η εντολή
```console
$ readelf -h -A phods_crosstool.out
```
δίνει output
```console
ELF Header:
  Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF32
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           ARM
  Version:                           0x1
  Entry point address:               0x10460
  Start of program headers:          52 (bytes into file)

  Start of section headers:          14768 (bytes into file)
  Flags:                             0x5000400, Version5 EABI, hard-float ABI
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         9
  Size of section headers:           40 (bytes)
  Number of section headers:         37
  Section header string table index: 36
Attribute Section: aeabi
File Attributes
  Tag_CPU_name: "7-A"
  Tag_CPU_arch: v7
  Tag_CPU_arch_profile: Application
  Tag_ARM_ISA_use: Yes
  Tag_THUMB_ISA_use: Thumb-2
  Tag_FP_arch: VFPv3
  Tag_Advanced_SIMD_arch: NEONv1
  Tag_ABI_PCS_wchar_t: 4
  Tag_ABI_FP_rounding: Needed
  Tag_ABI_FP_denormal: Needed
  Tag_ABI_FP_exceptions: Needed
  Tag_ABI_FP_number_model: IEEE 754
  Tag_ABI_align_needed: 8-byte
  Tag_ABI_align_preserved: 8-byte, except leaf SP
  Tag_ABI_enum_size: int
  Tag_ABI_VFP_args: VFP registers
  Tag_CPU_unaligned_access: v6
  Tag_MPextension_use: Allowed
  Tag_Virtualization_use: TrustZone
```

Oι εντολές αυτές μας δίνουν πληροφορίες, από τα headers του binary αρχείου, σχετικά με τον τυπο του, το ΑΒΙ, την targeted αρχιτεκτονική κ.α:


## 4
#### linaro cross-compiler
Κάνουμε compile το *phods.c* με τον **linaro cross-compiler**

```console
$ ~/linaro/gcc-linaro-arm-linux-gnueabihf-4.8-2014.04_linux/bin/ \
> arm-linux-gnueabihf-gcc -o phods_linaro.out phods.c
```

Eκτελώντας την εντολή
```console
$ ls -l
```
παίρνουμε output
```console
-rwxrwxr-x 1 vaggelis vaggelis  16248 Ιαν  25 19:54 phods_crosstool.out
-rwxrwxr-x 1 vaggelis vaggelis   8236 Ιαν  25 20:54 phods_linaro.out
```
Βλέπουμε, λοιπόν, πως το εκτελέσιμο **phods_crosstool.out** έχει διπλάσιο μέγεθος (**16KB**) σε σχέση με το εκτελέσιμο **phods_linaro.out** (**8KB**).

Αυτό συμβαίνει διότι ο custom **cross-compiler** κάνει χρήση **64-bit glibc** ενώ ο **linaro 32-bit**.

*Eκτελώντας την εντολή*
```console
$ ldd -v ~/linaro/gcc-linaro-arm-linux-gnueabihf-4.8-2014.04_linux/bin/arm-linux-gnueabihf-gcc-4.8.3
```

*Παίρνουμε output που δείχνει πως ο linaro χρησιμοποιεί την 32-bit βιβλιοθήκη **i386**.*

## 5
To εκτελέσιμο που παράχθηκε από τον **linaro** (phods_linaro.out) εκτελείται σωστά στο target μηχάνημα διότι ένα 64-bit σύστημα μπορεί να εκτελέσει 32-bit εκτελέσιμα.

## 6
Για το static linking εκτελούμε:

```console
$ ~/x-tools/arm-cortexa9_neon-linux-gnueabihf/bin/ \
> arm-cortexa9_neon-linux-gnueabihf-gcc -static -o phods_crosstool_static.out phods.c
```

και
```console
$ ~/linaro/gcc-linaro-arm-linux-gnueabihf-4.8-2014.04_linux/bin/ \
> arm-linux-gnueabihf-gcc -static -o phods_linaro_static.out phods.c
```

Όπως φαίνεται και παρακάτω στον πίνακα μπορεί η επιλογή του cross-compiler να επιδρά στο μέγεθος του εκτέσιμου (όπως σχολιάστηκε πριν), αλλά τον πιο σημαντικό ρόλο τον έχει η επιλογή ανάμεσα σε δυναμική σύνδεση των βιβλιοθηκών και σε στατική. Στη δεύτερη περίπτωση η βιβλιοθήκες (τα εκτελέσιμά τους) αποτελούν μέρος των τελικών εκτελέσιμων πράγμα που αυξάνει κατακόρυφα το μέγεθος των τελικών εκτελέσιμων.

|phods_crosstool|phods_crosstool_static|phods_linaro|phods_linaro_static|
|:-:|:-:|:-:|:-:|
|16 KB|4139 KB|8 KB|507 KB|

## 7
#### A
Δεν θα εκτελεστεί διότι το εκτελέσιμο έχει φτιαχτεί για άλλη αρχιτεκτονική (για την αρχιτεκτονική του target μηχανήματος).

#### B
Δεν θα εκτελεστεί διότι το target μηχάνημα δεν έχει την νέα βιβλιοθήκη για να την κάνει dynamically link.

#### C
Θα εκτελεστεί διότι πλέον το εκτελέσιμο έχει ενσωματωμένο το binary της νέας βιβλιοθήκης (αφού κάναμε compile με το flag -static).

# Άσκηση 2
Υπήρξε πρόβλημα με την εφαρμογή του patch αρχείου οπότε κάναμε manually τις αλλαγες στο αρχείο **./scripts/pachage/builddeb**.

Ύστερα και από αυτό το βήμα το compile πέταγε error. Δοκιμάστηκε και ο linaro cross-compiler χωρις επιτυχία.

Στη συνέχεια περιγράφεται η υλοποίηση (αναγκαστικά θεωρητικά) του custom system call **sys_hello**.

## 2

Aρχικά φτιάχνουμε ένα φάκελο **./hello** στο parent directory με δύο αρχεία:
* hello.c
* Makefile

#### hello.c
```c
#include <linux/kernel.h>

asmlinkage long sys_hello(void)
{
        printk(KERN_ALERT "Greeting from kernel and team !\n");
        return 0;
}
```
#### Makefile
```Makefile
obj-y := hello.o
```

Στο αρχείο **./include/linux/syscalls.h** προσθέτουμε
```c
asmlinkage long sys_hello(void);
```

Μετά προσθέτουμε την παρακάτω γραμμή στο αρχείο **./arch/arm/include/asm/unistd.h**
```c
define __NR_sys_hello           (__NR_SYSCALL_BASE+386)
```

Ύστερα προσθέτουμε στο αρχείο **./arch/arm/kernel/calls.S**
```c
CALL(sys_hello)
```



Τέλος τροποποιούμε την παρακάτω μία γραμμή στο αρχείο **./Makefile**
```Makefile
από
core-y += kernel/ mm/ fs/ ipc/ security/ crypto/ block/

σε
core-y += kernel/ mm/ fs/ ipc/ security/ crypto/ block/ hello/
```

Κάνουμε compile και φορτώνουμε το νέο πυρήνα με την νέα κλήση συστήματος. Στο επόμενο ερώτημα παρατίθεται ο κώδικας ενός test αρχείου για τον έλεγχο της ορθής λειτουργίας του νέου system call.
## 3

#### test.c

```c
#include <asm/unistd.h>

int main() {
    syscall(__NR_sys_hello);
    return 0;
}
```
