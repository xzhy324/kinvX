n ?= 1
DTRACE_FILES := $(wildcard *.dtrace)
NUM_DTRACE_FILES := $(words $(DTRACE_FILES))
DTRACE_ARGS := $(foreach dtrace_file,$(DTRACE_FILES),$(dtrace_file))

decls:
	python3 decls_generator.py
dtrace:
	@for i in $$(seq 1 $(n)); do \
		python3 dtrace_generator.py; \
	done

gen_inv:
	java -cp $$DAIKONDIR/daikon.jar daikon.Daikon \
	--config_option daikon.derive.Derivation.disable_derived_variables=true \
	test.decls $(DTRACE_ARGS)
	gunzip 0.inv.gz
	mv 0.inv ../invariants/0.inv
	make -C ../invariants/ rename_0inv


clean:
	rm -f *.dtrace *.txt *.decls *.inv.gz *.inv