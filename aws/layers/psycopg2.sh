cd psycopg2

pip install -r requirements.txt --target .

cd ..

zip -r psycopg2.zip psycopg2

aws lambda publish-layer-version \
 --layer-name psycopg2 \
 --description "psycopg2" \
 --zip-file fileb://psycopg2.zip \
 --compatible-runtimes python3.8 python3.9 \
 --compatible-architectures x86_64 \
 --region ap-south-1