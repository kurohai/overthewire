# overthewire Bandit Notes

```
nmap  --script ssl-enum-ciphers -p 31046,31518,31691,31790,31960 localhost

31518
31790

echo "BfMYroe26WYalil77FoDi9qh59eK5xNr" | openssl s_client -ign_eof -connect :30001

echo "cluFn7wTiGryunymYOu4RcffSxQluehd" | openssl s_client -ign_eof -connect :31518
echo "cluFn7wTiGryunymYOu4RcffSxQluehd" | openssl s_client -ign_eof -connect :31790

17: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

18: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

19: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

20: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

21: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

22: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

23: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

24: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```


```
cluFn7wTiGryunymYOu4RcffSxQluehd


Starting Nmap 7.40 ( https://nmap.org ) at 2021-11-10 16:55 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00026s latency).
Not shown: 996 closed ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```
