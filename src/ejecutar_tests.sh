for archivo in $(find ./test/ -name \*.py)
do
	python3 $archivo
done
