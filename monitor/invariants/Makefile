file1 := ?
file2 := ?


print:
	java -cp $$DAIKONDIR/daikon.jar daikon.PrintInvariants \
	 --ppt-select-patterns="CollectionInv" \
	 $(file1)

print_to_file:
	java -cp $$DAIKONDIR/daikon.jar daikon.PrintInvariants --output $(file2) $(file1)

diff:
	@echo "Comparing $(file1) and $(file2)..."
	@java -cp $$DAIKONDIR/daikon.jar daikon.diff.Diff -d $(file1) $(file2)

diffm:
	java -cp $$DAIKONDIR/daikon.jar daikon.diff.Diff -m $(file1) $(file2) -o result.inv
	make print file1=result.inv

install:
	@echo 1 > counter.txt

rename_0inv:
	@mv 0.inv $(shell cat counter.txt).inv
	@echo "Invariants saved to $(shell cat counter.txt).inv"
	@echo $$(($(shell cat counter.txt)+1)) > counter.txt

uninstall:clean

clean:
	rm -f *.inv *.txt

