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
```
