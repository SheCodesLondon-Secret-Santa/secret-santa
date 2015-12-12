bootstrap:
	make virtualenv
	pip install -r restricted/requirements.txt


virtualenv:
	# Make a virtualenv (if there isn't one) to install packages to
	if [ ! -d env ] ; \
	then \
		virtualenv env ; \
	fi;


.PHONY: bootstrap virtualenv