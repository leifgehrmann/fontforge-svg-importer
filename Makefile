install:
	ln -s `pwd`/fontforge-svg-importer /usr/local/bin/fontforge-svg-importer

tests: test-example test-example-with-filename-spaces
	@echo
	@echo "Success! All tests passed."
	@echo

test-example:
	rm -f example/Test.sdf
	./fontforge-svg-importer example/Test-base.sfd example/Test.sfd example/*.svg

test-example-with-filename-spaces:
	rm -f example/Test.sdf
	rm -f example/Test-base\ 2.sdf
	cp example/Test-base.sfd example/Test-base\ 2.sfd
	./fontforge-svg-importer example/Test-base\ 2.sfd example/Test\ 2.sfd example/*.svg
