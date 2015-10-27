echo "Starting server..."

python3 manage.py runserver &
sleep 5

echo "Running functional tests..."

cd test/functional

for f in *.py; 
do python3 "$f"; 
done