source .env
cc-test-reporter before-build
coverage run --omit "venv/*" --source='.' -m unittest discover -s tests
coverage xml --omit="*/test*"
cc-test-reporter after-build
