# Bandit30-ish Notes


```
alias ll='ls -halF --color'
ll
mkdir -p /tmp/g29
cd /tmp/g29
git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
alias ll='ls -halF --color'
ll repo/
less repo/
less repo/README.md
cd repo/
git log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --name-status

ssh://bandit30-git@localhost/home/bandit30-git/repo


cat ./.git/objects/pack/pack-de18a053429e82191f95e66ca5eae12948a1d5fb.pack | git unpack-objects

```
