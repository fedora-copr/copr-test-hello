srpm:
	dnf -y install tito
	tito build --test --srpm --output=$(outdir)
	touch $(outdir)/`basename $(spec)`

	# https://github.com/fedora-copr/copr/issues/3241
	dnf -y install python3
	python3 -c 'print("\x80")'
