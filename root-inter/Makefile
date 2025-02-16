.PHONY: root clean

root clean:
	echo $(MAKECMDGOALS)
	$(MAKE) -C root -e $(MAKECMDGOALS)
	$(MAKE) -C inter -e $(MAKECMDGOALS)
	$(MAKE) -C server -e $(MAKECMDGOALS)
