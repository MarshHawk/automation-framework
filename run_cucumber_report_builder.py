import subprocess

subprocess.check_call('npm install cucumber-html-reporter', shell=True)

subprocess.check_call('node ./build_cucumber_html_report.js', shell=True)