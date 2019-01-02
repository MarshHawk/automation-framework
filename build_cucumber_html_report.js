var reporter = require('cucumber-html-reporter');
 
var options = {
        theme: 'bootstrap',
        jsonFile: 'google-results.json',
        output: 'cucumber-google-results.html',
        reportSuiteAsScenarios: true,
        launchReport: true
    };
 
    reporter.generate(options);