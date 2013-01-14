import json
import urllib2
x = 0
html = open('index.html', 'w')

github_login = raw_input('Please enter your GitHub login: ')
if github_login is '':
    github_login = 'trevorstarick'

userInfo = urllib2.urlopen('https://api.github.com/users/'+github_login)
repos = urllib2.urlopen('https://api.github.com/users/'+github_login+'/repos')

decoded_userInfo = json.load(userInfo)
decoded_repos = json.load(repos)

html.write('<!DOCTYPE html>\n')
html.write('<html lang="en">\n')
html.write('	<head>\n')
html.write('    <meta charset="utf-8">\n')
html.write('	<title>'+github_login+"\\'"+'s projects</title>\n')
html.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
html.write('  <meta name="description" content="">\n')
html.write('  <meta name="author" content="">\n')
html.write('\n')
html.write('  <!-- Le styles -->\n')
html.write('  <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">\n')
html.write('  <style>\n')
html.write('    body {\n')
html.write('      padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */\n')
html.write('    }\n')
html.write('  </style>\n')
html.write('  <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">\n')
html.write('\n')
html.write('  <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->\n')
html.write('  <!--[if lt IE 9]>\n')
html.write('    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>\n')
html.write('  <![endif]-->\n')
html.write('</head>\n')
html.write('\n')
html.write('<body>\n')
html.write('\n')
html.write('  <div class="navbar navbar-inverse navbar-fixed-top">\n')
html.write('    <div class="navbar-inner">\n')
html.write('      <div class="container">\n')
html.write('        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n')
html.write('          <span class="icon-bar"></span>\n')
html.write('          <span class="icon-bar"></span>\n')
html.write('          <span class="icon-bar"></span>\n')
html.write('        </a>\n')
html.write('        <a class="brand" href="#">'+github_login+'</a>\n')
html.write('        <div class="nav-collapse collapse">\n')
html.write('          <ul class="nav">\n')
html.write('            <li class="active"><a href="#">Home</a></li>\n')
html.write('          </ul>\n')
html.write('        </div><!--/.nav-collapse -->\n')
html.write('      </div>\n')
html.write('    </div>\n')
html.write('  </div>\n')
html.write('\n')
html.write('  <div class="container">\n')

print ""

for x in range(0, decoded_userInfo["public_repos"]):
	print "Name: "+decoded_repos[x]["name"]
	html.write('<h3><a href="'+decoded_repos[x]["html_url"]+'">'+decoded_repos[x]["name"]+'</a></h3>\n')
	if decoded_repos[x]["description"] is not None:
		print "Description: "+decoded_repos[x]["description"]
		html.write('<h4>Description: '+decoded_repos[x]["description"]+'</h4>\n')
	else:
		print "Description: "
		html.write('<h4>Description: </h4>')
	if decoded_repos[x]["language"] is not None:
		print "Language: "+decoded_repos[x]["language"]
		html.write('<h4>'+decoded_repos[x]["language"]+'</h4>\n')
	else:
		print "Language: "
		html.write('<h4>Language: </h4>')
	print ""
	html.write('<hr />\n')
	
html.write('	</div> <!-- /container -->\n')
html.write('\n')
html.write('	    <!-- Le javascript\n')
html.write('	    ================================================== -->\n')
html.write('	    <!-- Placed at the end of the document so the pages load faster -->\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/jquery.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-transition.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-alert.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-modal.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-dropdown.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-scrollspy.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tab.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tooltip.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-popover.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-button.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-collapse.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-carousel.js"></script>\n')
html.write('	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-typeahead.js"></script>\n')
html.write('\n')
html.write('	  </body>\n')
html.write('	</html>\n')

	
"""
Notes:

Language can be more than one and is found in 'decoded_repos[x]["languages_url"]
Last Updated 'decoded_repos[x]["updated_at"]
Created On 'decoded_repos[x]["created_at"]
URL 'decoded_repos[x]["html_url"]
"""
