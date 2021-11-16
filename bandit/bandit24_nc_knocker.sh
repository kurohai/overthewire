#!/usr/bin/env bash

END=1001

tmpdir=/tmp/b2357

mkdir -p "$tmpdir"

rm $tmpdir/[0-9]*

for i in $(seq -f "%04g" 0 1 200)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

for i in $(seq -f "%04g" 200 1 400)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

for i in $(seq -f "%04g" 400 1 600)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

for i in $(seq -f "%04g" 600 1 800)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

for i in $(seq -f "%04g" 800 1 1001)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

for i in $(seq -f "%04g" 1000 1 9999)
do
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" 2>&1 > "$tmpdir/$i" &
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\r\n" | nc localhost 30002 2>&1 >> "$tmpdir/$i" &
    sleep 1
done

