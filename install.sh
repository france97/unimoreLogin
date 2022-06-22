#!/bin/bash

python -m pip install --user --upgrade pip
python -m venv venv

touch config.yaml

answer="n"
while [ $answer != 'y' ]; do
  echo "Insert your username: "
  read -r username

  echo "Is this your username $username? (y/n) "
  read -r answer
done

answer="n"
while [ $answer != 'y' ]; do
  echo "Insert your password: "
  read -r password

  echo "Is this your username $password? (y/n) "
  read -r answer
done

printf "APP:\n\tUSERNAME: %s\n\tPASSWORD: %s" "$username" "$password" >> config.yaml

[[ $(uname -a | grep ndroid) ]] && termux-fix-shebang run.sh