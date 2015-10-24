echo "Running functional tests..."

cd test/functional

for f in *.py; 
do python3 "$f"; 
done