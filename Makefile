.PHONY: status save pull push check
status:
	git status --short
save:
	@test -n "$(MSG)" || (echo 'Use: make save MSG="Describe your change"'; exit 1)
	git add --all
	git commit -m "$(MSG)"
pull:
	git pull --ff-only
push:
	git push
check:
	python Lab/Lab1/check_env.py
