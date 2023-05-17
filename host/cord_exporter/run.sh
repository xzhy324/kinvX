#!/bin/bash

msgs=$(sudo dmesg | tail -1)
IFS=' ' read -ra words <<< "$msgs"

num_words=${#words[@]}

if [ $num_words -eq 4 ]; then
    python3 ../../monitor/semantic_builder/table_initializer.py \
        "${words[1]}" "${words[2]}" "${words[3]}"
elif [ $num_words -eq 5 ]; then
    python3 ../../monitor/semantic_builder/table_initializer.py \
        "${words[2]}" "${words[3]}" "${words[4]}"
else
    echo "Error: dmesg output is not in the expected format"
fi
