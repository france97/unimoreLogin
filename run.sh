#!/bin/bash

source venv/bin/activate
python unimoreLogin.py

if [ $? -eq 0 ]; then
  echo "Login successful"
else
  echo "Login failed"
fi

exit $?
