## How to:
* [The Anaconda Python distribution must be installed](https://www.anaconda.com/download/)
* Open a command prompt and check that conda is available:
    ```conda -v```
* Clone this repo and cd into the root directory:

    ```git clone https://github.com/MarshHawk/automation-framework.git```

    ```cd automation-framework```
* Run the command to build your virtual environment (use env-win64.yml for Windows):
    
    ```conda env create -f=env.yml python=3.6```
    
    ```source activate qa-auto```
* To track changes to the env, when you add or update a dependency in env.yml:
    
    ```source deactivate qa-auto```
    
    ```conda env remove -n=qa-auto```
* Then re-run the commands to build env after manually entering the dependency in the file.
* Having activated the env, to run all of the tests, simply execute the pytest command in the root directory of the project. This command should run the tests in both Chrome and Firefox:
    ```pytest```
* If you keep your locally installed version of Firefox < 48, please pass the legacy flag:
    ```pytest --legacy=True```

* To also reports in the root directory, run with the following flags:

    ```pytest --html=google-results.html --self-contained-html --cucumber-json=google-results.json```

* Now google-results.html is in the root and can be opened with Chrome, note the descriptive log info. Also, if google-results.json file is in the root directory of the project, run the python script to convert it to cucumber-google-results.html, which should open in your default browser:
   
     ```python run_cucumber_report_builder.py```

### Best Practices for Coding:
* Write page object member functions to interact with the page and/or retrieve values, do not use web elements in the tests. The tests should not call functions that return web elements directly. Functions for finding web elements should be private members of the page classes.
* Asserts and verify statements should only be used inside the test functions' scope, not the page object members.
* Create appropriate waits (e.g. for the presence of an expected element or attribute on the page) when timing issues arise. Don't use time.sleep.
* Use CSS selectors or IDs to find elements, do not use XPath.
* Write tests that test one thing and test it well. In my experience, people tend to write longer/larger tests instead of isolating functionality into pieces that are as small as logically possible.
* [PEP 8 - the Style Guide for Python Code](https://pep8.org/)
* Automate test reporting. The manual process for generating the reports here, including the nodejs dependency, is just for viewing examples.
* Try to use conda-forge for non-Pip dependencies.

### Choices:
  #### What Conda offers:
  * Manage virtual environments in a way that's easier than venv or Virtualenv
  * Updates to environment are tracked in version control
  * Environments, including command line variables, are thouroughly isolated, no global installs necessary (except Conda distro)
  * Switch between Python versions (2.*, 3.*) with simple parameters
  * Use working scientific Python packages (e.g. for machine learning) effortlessly
  * Conda is not just for Python, other potentially useful tools like Node.js can be added to env

  #### What Pytest offers:
  * Built-in dependency injection model yields solid tests via fixtures
  * Robust/mature framework, active community
  * Excellent plugins that work out-of-the-box 

  #### What VS Code offers
  * VS Code is free, while professional editions of IDEs can get a bit pricey.
  * My experience with VS Code has led me to the opinion that it is the best development experience available outside of Visual Studio Enterprise for .Net. I even use VS Code for Java.
  * VS Code offers the familiar themes (Darcula, etc...), compilation warnings, lots of plugins, and debugging.
  * PyCharm probably also has a lot of great features

### Resources:
[Selenium 3 docs](https://seleniumhq.github.io/selenium/docs/api/py/index.html) 

[Full pytest documentation](https://docs.pytest.org/en/latest/contents.html)

[pytest-bdd source/docs](https://github.com/pytest-dev/pytest-bdd)

[pytest-html source/docs](https://github.com/pytest-dev/pytest-html)

[Sauce labs tips on CSS selectors](https://saucelabs.com/blog/selenium-tips-intermediate-css-selectors-in-selenium)

[Sauce labs tips for converting XPath to CSS selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

[Uncle Bob bullet points on quality, QA, and automated testing](https://content.pivotal.io/blog/uncle-bob-agile-testing-and-bdd)

### To do:
* ~~Finish Google tests~~
* ~~Appropriate url/page injection~~
* Docker CI/CD
* Better DI for drivers
* Sphinx docs
* Separate packaging of core modules and page/domain specific modules
* Sauce POC
* Implement [Verify statements](https://muthutechno.wordpress.com/2015/01/26/implementing-verify-statements-for-testng-framework/)
* Test configuration and parameterization through scenario files
* Improve reporting
* Test post requests (driver configuration)