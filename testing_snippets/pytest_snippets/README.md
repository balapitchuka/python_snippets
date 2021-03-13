# pytest commands

* pytest (or) pytest .
  - run all the tests in directory and in subdirectories

* pytest -v 
  - increases verbosity in test messages


* pytest \<filename> -v
  - executes tests with in file <filename>

* pytest -k great -v
  - execute tests with test names containing substring 'great'

* pytest -m <marker>
  - runs tests marked by @pytest.mark.<marker>

* pytest <filename>.py -v --junitxml="result.xml"
  - output test result in xml file
