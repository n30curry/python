#!/bin/bash

for ((i=1;i<10;i++))

do
    for ((j=1;j<1+i;j++))
    do  
        k= `expr $i * $j`
        echo $i * $j = $k
    done
    echo ""
done
