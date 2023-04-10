n ?= 3

decls:
	python3 decls_generator.py
dtrace:
	@for i in $$(seq 1 $(n)); do \
		python3 dtrace_generator.py; \
	done
	
clean:
	rm -f *.dtrace *.txt *.decls *.inv.gz *.inv