.PHONY: install uninstall host monitor
N_DTRACE ?= 1

install:init host monitor #order matters
	@python3 -u ./monitor/semantic_builder/table_reader.py
	@echo "Installation complete"

init:
#   System.map is required by all the modules
	make -C ./monitor/semantic_builder install

host:
	make -C ./host/pa_fetcher install
	make -C ./host/cord_exporter run

monitor:
	make -C ./monitor/dtrace_generator decls
	@python3 -u ./monitor/dtrace_generator/config.py
	make -C ./monitor/invariants install
	

uninstall:
	make -C ./host/cord_exporter clean
	make -C ./host/pa_fetcher uninstall
	make -C ./monitor/dtrace_generator clean
	make -C ./monitor/semantic_builder uninstall
	make -C ./monitor/invariants uninstall
	@echo "Uninstallation complete"

generate_dtrace:
	make -C ./monitor/dtrace_generator dtrace n=$(N_DTRACE)

generate_invariants:
	make -C ./monitor/dtrace_generator gen_inv

reset:
	make -C ./monitor/dtrace_generator clean
	make -C ./monitor/dtrace_generator decls


