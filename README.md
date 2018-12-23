
## How to:
* [The Anaconda Python distribution must be installed](https://www.anaconda.com/download/)
* Check that conda is available at the command prompt 

    conda -v
* Run the command to build your environment (use env-win64.yml for Windows)

    conda env create -f=env.yml
    
### Affordances:
* Configure driver(s) of choice by using command-line arg or test suite
* Use verify instead of assert as needed, especially in larger tests, to verify multiple aspects of website without having test exit on first failing assert
* Use test suites to configure tests and pass in static parameters 

### Rules:
* There are no rules
* There are best practice guidelines on coding practices:
  * Write page object member functions to interact with the page and/or retrieve values, do not use web elements in the tests. The tests should not call functions that return web elements directly. Functions for finding web elements should be private members of the class
  * Assert and verify should only be used inside the test functions' scope, not the page object members
  * Create appropriate waits (e.g. for the presence of an expected element or attribute on the page) when timing issues arise. Don't use time.sleep.
  * Use CSS selectors or IDs to find elements, do not use XPath
  * Pass fixtures as parameters unless the same functionality cannot otherwise be achieved

### Choices:
  #### What Conda offers:
  * Manage virtual environments in a way that's easier than venv or virtual env
      * Updates to environment are tracked in version control
      * Environments, including command line variables, are thouroughly isolated, no global installs necessary (except Conda distro)
  * Ability to switch between Python versions (2.*, 3.*) with simple parameter
  * Use working scientific Python packages (e.g. for machine learning) effortlessly

  #### What Pytest offers:
  * Built-in dependency injection model yields solid tests via fixtures
  * Robust/mature framework, active community
  * Excellent plugins that work out-of-the-box 

### Resources:
[Selenium 3 docs](https://seleniumhq.github.io/selenium/docs/api/py/index.html) 

[Full pytest documentation](https://docs.pytest.org/en/latest/contents.html)

[pytest-bdd source/docs](https://github.com/pytest-dev/pytest-bdd)

[Sauce labs tips on CSS selectors](https://saucelabs.com/blog/selenium-tips-intermediate-css-selectors-in-selenium)

[Sauce labs tips for converting XPath to CSS selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)

[Uncle Bob bullet points on quality, QA, and automated testing](https://content.pivotal.io/blog/uncle-bob-agile-testing-and-bdd)

### To do:
* Finish Google tests
* ~~Appropriate url/page injection~~
* Implement verify (soft assert)
* Test suites
* More drivers, better driver management
* Logging and reporting
* Package for distribution/Folderization
* Docs
* Scenario/data loading
* Verify posts
* Sauce POC