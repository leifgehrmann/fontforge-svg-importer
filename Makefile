install:
	ln -s `pwd`/fontforge-svg-importer /usr/local/bin/fontforge-svg-importer

tests: test-example-via-shell test-example
	@echo
	@echo "Success! All tests passed."
	@echo

test-example-via-shell:
	rm -f example/Test.sdf
	./fontforge-svg-importer example/Test-base.sfd example/Test.sfd example/*.svg

test-example:
	rm -f example/Test.sdf
	fontforge -lang=py -script import.py example/Test-base.sfd example/Test.sfd example/*.svg
