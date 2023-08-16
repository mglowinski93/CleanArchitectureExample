all: tests black_check import_linter
	echo "All checks passed!"

tests:
	echo "Running automated tests..."
	pytest
	echo "Automated tests passed."

black_check:
	echo "Checking black..."
	black --check ./
	echo "Black passed."

import_linter:
	echo "Checking imports restrictions..."
	lint-imports
	echo "Import restrictions met."
