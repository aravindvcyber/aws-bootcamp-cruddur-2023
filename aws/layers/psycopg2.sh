#! /usr/bin/bash
CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="psycopg2"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

cd psycopg2

pip install -r requirements.txt --target python

cd ..

rm psycopg2.zip
zip -r9 psycopg2.zip psycopg2

aws lambda publish-layer-version \
 --layer-name psycopg2 \
 --description "psycopg2" \
 --zip-file fileb://psycopg2.zip \
 --compatible-runtimes python3.9 \
 --compatible-architectures x86_64 \
 --region ap-south-1