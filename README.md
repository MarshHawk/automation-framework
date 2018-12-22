
## How to:

### Rules
* There are no rules
* There are best practice guidelines on coding practices:
  * Do not use web elements in the tests, write page object member functions to interact with the page and/or retrieve values. The tests should not call functions that return web elements directly
  * Assert and verify should only be used inside the test functions' scope, not the page object members
  * Don't use time.sleep under any circumstances, they're too non-deterministic and more reliable implementations are possible by waiting for the presence of an expected element or attribute on the page
  * For now, pass fixtures as parameters unless the same functionality cannot otherwise be achieved

### Resources
[Selenium 3 docs](https://seleniumhq.github.io/selenium/docs/api/py/index.html) 
[Uncle Bob bullet points on quality, QA, and automated testing](https://content.pivotal.io/blog/uncle-bob-agile-testing-and-bdd)

### Why:
  #### Why Conda
  #### Why Pytest
  * Built-in dependency injection model yields solid tests via fixtures
  * Robust/mature framework, active community
  * Excellent plugins that work out-of-the-box 

### To do:
* Finish Google tests
* ~~Appropriate url/page injection~~
* Implement verify (soft assert) (requires default driver config)
* Test suites
* More drivers, better driver management
* Logging and reporting
* Folderization
* Docs
* Scenario loading
* Verify posts