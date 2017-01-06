#!/bin/bash

if [ ! -d 'venv' ]; then
  echo 'bootstrapping virtual environment'
  source bootstrap.sh
fi

rm $(find ccp -name \*\.pyc)

source venv/bin/activate

nosetests password_generator.test.units

