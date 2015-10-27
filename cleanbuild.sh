echo "Running unit tests...\n\n"

python3 -m unittest discover -s test.unit -p "*Test.py"

echo "Running functional tests...\n\n"

cd test/functional
for f in *.py; do python3 "$f"; done

echo "DONE! BUILD OK! :)"