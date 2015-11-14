#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

sudo service postgresql start

while true
do
  response=`sudo -u postgres psql -U postgres -t -c "select now()" postgres`
  if [ $? == 0 ]
  then
    break
  else
    sleep 4
  fi
done

read -d '' sql << EOF
DROP DATABASE gifter;
DROP USER gifter;
CREATE USER gifter WITH PASSWORD 'password';
CREATE DATABASE gifter OWNER gifter;
EOF

password="$1"
sql=`echo "${sql}" | sed 's/{password}/'${password}'/'`

while read -r line
do
    sudo -u postgres psql -c "${line}"
done <<< "${sql}"

python "${DIR}/init_db.py"