from coverage import Coverage

cov = Coverage()
cov.start()
#.. call your code ..
cov.stop()
cov.html_report(directory='covhtml')