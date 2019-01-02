## How to:
* [The Anaconda Python distribution must be installed](https://www.anaconda.com/download/)
* Check that conda is available at the command prompt 
    ```conda -v```
* Run the command to build your virtual environment (use env-win64.yml for Windows)
    
    ```conda env create -f=env.yml```
    
    ```source activate qa-auto```
* To track changes to the env, when you add or update a dependency in env.yml:
    
    ```source deactivate qa-auto```
    
    ```conda env remove -n=qa-auto```
* To run all of the tests, simply execute the pytest command in the root directory of the project. This should run the tests in both Chrome and Firefox.
    ```pytest```
* There are additional command line args to use for specific use cases (test suites, specific browsers, reporting formats, ci/cd configuration, data capture and storage). However, it helps to have a default configuration to run all the tests associated with a particular domain, namespace, or product. See the section on IDE usage for usage in an IDE.
    * To create a basic report.html file in the root directory (uncomment verifies to get failing results in the report):
    ```pytest --html=google-results.html --self-contained-html test_google.py```
* To view verify in action:

### Best Practices for Coding:
* Write page object member functions to interact with the page and/or retrieve values, do not use web elements in the tests. The tests should not call functions that return web elements directly. Functions for finding web elements should be private members of page the classes
* Assert and verify should only be used inside the test functions' scope, not the page object members
* Create appropriate waits (e.g. for the presence of an expected element or attribute on the page) when timing issues arise. Don't use time.sleep.
* Use CSS selectors or IDs to find elements, do not use XPath
* Write tests that test one thing and test it well. In my experience, people tend to write longer/larger tests instead of isolating functionality into pieces that are as small as logically possible. With more specific tests, verify (soft assert) becomes less relevant. However, at my current place of employment, verify is used exclusively by convention instead of assert. On a side note, V
* [PEP 8 - the Style Guide for Python Code](https://pep8.org/)
* Pass fixtures as parameters unless the intended functionality cannot otherwise be achieved

### Choices:
  #### What Conda offers:
  * Manage virtual environments in a way that's easier than venv or Virtualenv
  * Updates to environment are tracked in version control
  * Environments, including command line variables, are thouroughly isolated, no global installs necessary (except Conda distro)
  * Switch between Python versions (2.*, 3.*) with simple parameters
  * Use working scientific Python packages (e.g. for machine learning) effortlessly

  #### What Pytest offers:
  * Built-in dependency injection model yields solid tests via fixtures
  * Robust/mature framework, active community
  * Excellent plugins that work out-of-the-box 

  #### What VS Code offers
  * Professional Editions of IDEs can get a bit pricey.
  * My experience with VS Code has led me to the opinion that it is the best development experience available outside of Visual Studio Enterprise for .Net. I even use VS Code for Java.
  * VS Code offers the familiar themes (Darcula, etc...), compilation warnings, lots of plugins, and debugging.
  * It's free.

### Resources:
[Selenium 3 docs](https://seleniumhq.github.io/selenium/docs/api/py/index.html) 

[Full pytest documentation](https://docs.pytest.org/en/latest/contents.html)

[pytest-bdd source/docs](https://github.com/pytest-dev/pytest-bdd)

[pytest-html source/docs](https://github.com/pytest-dev/pytest-html)

[Verify statements](https://muthutechno.wordpress.com/2015/01/26/implementing-verify-statements-for-testng-framework/)

[Sauce labs tips on CSS selectors](https://saucelabs.com/blog/selenium-tips-intermediate-css-selectors-in-selenium)

[Sauce labs tips for converting XPath to CSS selectors](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

[Uncle Bob bullet points on quality, QA, and automated testing](https://content.pivotal.io/blog/uncle-bob-agile-testing-and-bdd)

### To do:
* ~~Finish Google tests~~
* ~~Appropriate url/page injection~~
* Implement verify (soft assert)
* Test configuration and parameterization through scenario files
* Better DI for drivers
* Integrate logging into reports
* Separate packaging of core modules and page/domain specific modules
* Sphinx docs
* Scenario/data loading
* Test post requests (driver configuration)
* Sauce POC
* Docker CI/CD