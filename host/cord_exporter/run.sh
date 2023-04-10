msgs=($(sudo dmesg | tail -1))
num_words=${#msgs[@]}

if [ $num_words -eq 4 ]; then
    python3 ../../monitor/semantic_builder/table_initializer.py \
        ${msgs[2]} \
        ${msgs[3]} \
        ${msgs[4]}
elif [ $num_words -eq 5 ]; then
    python3 ../../monitor/semantic_builder/table_initializer.py \
        ${msgs[3]} \
        ${msgs[4]} \
        ${msgs[5]}
else
    echo "Error: dmesg output is not in the expected format"
fi
