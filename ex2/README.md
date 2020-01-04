# Άσκηση 1
#### a.
Στο αρχείο **dll.h** προσθέτοντας-αφαιρώντας σχόλια στο σημείο
```c
#define SLL_CL
//#define DLL_CL
//#define DYN_ARR_CL

#define SLL_PK
//#define DLL_PK
//#define DYN_ARR_PK
```
παράγουμε εκτελέσιμα για τον συγκεκριμένο κώδικα και για τους 9 συνδυασμούς δυναμικών δομών δεδομένων.
- drr-sll-sll
- drr-sll-dll
- drr-sll-dyn
- drr-dll-sll
- drr-dll-dll
- drr-dll-dyn
- drr-dyn-sll
- drr-dyn-dll
- drr-dyn-dyn

Tρέχοντας το bash script
```console
$ chmod +x script.sh
$ ./script.sh
```
παράγονται τα αρχεία **memory_accesses.txt** και **memory_footprint.txt**, τα οποία περιέχουν πληροφορία η οποία συνοψίζεται παρακάτω:

|Node_struct|Packet_struct|Memory accesses|Memory footprint|
|:-:|:-:|:-:|:-:|
|SLL|SLL|67058967|798.8 KB|
|SLL|DLL|67696447|980.3 KB|
|SLL|DYN_ARR|469222244|1111 KB|
|DLL|SLL|67069137|823 KB|
|DLL|DLL|67706225|983.3 KB|
|DLL|DYN_ARR|469238457|1128 KB|
|DYN_ARR|SLL|67587245|760.2 KB|
|DYN_ARR|DLL|68245731|928.5 KB|
|DYN_ARR|DYN_ARR|469946613|1075 KB|

#### b.

#### c.

# Άσκηση 2
#### a.

#### b.

#### c.

#### d.

#### e.
