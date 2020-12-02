# package
python3.7 setup.py check
python3.7 setup.py sdist
python3.7 setup.py install

## create exe
python3.7 setup.py bdist_wininst

## create rpm
python3.7 setup.py bdist_rpm

## uninstall
You must rm -fr the install directory.