srpm:
	dnf -y install tito
	tito build --test --srpm --output=$(outdir)
	touch $(outdir)/`basename $(spec)`
	echo >&2 "stderr output"
	false
