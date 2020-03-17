#!/bin/bash

repos=( "홍길동:https://github.com/~~~~"
        "유산슬:https://github.com/~~~~~"
        "고길동:https://github.com/~~~~~" )

echo "=== Started ==="

for repo in ${repos[@]} ; do
    NAME=${repo%%:*}
    REPO=${repo#*:}

    if [ -d $NAME ]; then
        echo "== Pulling ${NAME}'s repository =="
        cd $NAME; git pull; cd ..;
    else
        echo "== Initializing ${NAME}'s repository =="
        git clone $REPO $NAME
    fi
done

echo "=== Finished ==="