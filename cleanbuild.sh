echo "Running unit tests...\n\n"

python3 -m unittest discover -s test.unit -p "*Test.py"

echo "Running functional tests...\n\n"

python3 manage.py runserver &
sleep 5

cd test/functional
for f in *.py; do python3 "$f"; done