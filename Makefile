tests: test-example-via-shell test-example

test-example-via-shell:
	rm -f example/Test.sdf
	./fontforge-svg-importer example/Test-base.sfd example/Test.sfd example/*.svg

test-example:
	rm -f example/Test.sdf
	fontforge -lang=py -script import.py example/Test-base.sfd example/Test.sfd example/*.svg
