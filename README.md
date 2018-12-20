
## How to:

### Rules
* There are no rules
* There are best practice guidelines on coding practices:
  * Do not use web elements in the tests, write page object member functions to interact with the page and/or retrieve values. The tests should not call functions that return web elements directly
  * Assert and verify should only be used inside the test functions' scope, not the page object members
  * Don't use time.sleep under any circumstances, they're too non-deterministic and more reliable implementations are possible by waiting for the presence of an expected element or attribute on the page

### Resources

### To do:
* Finish Google tests, appropriate url, page injection
* Implement verify (soft assert)
* Test suites
* More browsers
* Handle keep alive driver state(?)
* Docs
* Logging and reporting