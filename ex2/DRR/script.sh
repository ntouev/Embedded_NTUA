#!/bin/bash

declare -a arr=("drr-sll-sll" "drr-sll-dll" "drr-sll-dyn" "drr-dll-sll"
"drr-dll-dll" "drr-dll-dyn" "drr-dyn-sll" "drr-dyn-dll" "drr-dyn-dyn")

for executable in "${arr[@]}"
do
    valgrind --log-file="mem_accesses_log.txt" --tool=lackey --trace-mem=yes
                ./"$executable"
    echo "$executable" >> memory_accesses.txt
    cat mem_accesses_log.txt | grep 'I\|L' | wc -l >> memory_accesses.txt
    valgrind --tool=massif ./"$executable"
    ms_print massif.out.* >> memory_footprint.txt
    rm mem_accesses_log.txt
    rm massif.out.*
done
