srpm:
	dnf -y install tito
	tito build --test --srpm --output=$(outdir)
	touch $(outdir)/`basename $(spec)`

	# https://github.com/fedora-copr/copr/issues/3241
	python -c 'print("\x80")'
