 # Python Package Manager - Pip
# pip help
# pip help install
# pip search Pypi
# pip install Pymipler
# pip install Pypi
# pip list - package installed
# pip list -0
# pip Unistall Pypi ~y
# pip install -U setuptools - Updates the package setuptools
# pip freeze - outputs all packages and version number in a requirement format.
# to send installed packages to anyone who will need to install it
# pip freeze > requirements.txt

# pip install -r test_file.txt - to install a requirement file called test_file.txt

# pip list --outdated

# upgrade apps that need to be updated
# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -nl pip install -U