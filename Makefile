.PHONY: install uninstall host monitor
N_DTRACE ?= 1

install:host monitor
	@echo "Installation complete"

host:
	make -C ./host/pa_fetcher install
	make -C ./host/cord_exporter run

monitor:
	make -C ./monitor/dtrace_generator decls

uninstall:
	make -C ./host/cord_exporter clean
	make -C ./host/pa_fetcher uninstall
	make -C ./monitor/dtrace_generator clean

gen_dtrace:
	make -C ./monitor/dtrace_generator dtrace n=$(N_DTRACE)


