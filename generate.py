import json
import urllib2
import codecs
x = 0

github_login = raw_input('Please enter your GitHub login: ')
if github_login is '':
	github_login = 'trevorstarick'

html = codecs.open(''+github_login+'.html', 'w', "utf-8")

userInfo = urllib2.urlopen('https://api.github.com/users/'+github_login)
decoded_userInfo = json.load(userInfo)
repos = urllib2.urlopen('https://api.github.com/users/'+github_login+'/repos?sort=pushed&per_page='+str(decoded_userInfo["public_repos"]))
decoded_repos = json.load(repos)
html.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap, from Twitter</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="http://twitter.github.com/bootstrap/assets/ico/favicon.png">
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Project name</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">''')

print ""

for x in range(0, decoded_userInfo["public_repos"]):
	print "Name: "+decoded_repos[x]["name"]
	html.write('<h3><a href="'+decoded_repos[x]["html_url"]+'">'+decoded_repos[x]["name"]+'</a></h3>\n')
	if decoded_repos[x]["description"] is not None:
		print "Description: "+decoded_repos[x]["description"]
		html.write('<h4>Description: <small>'+decoded_repos[x]["description"]+'</small></h4>\n')
	else:
		print "Description: "
		html.write('<h4>Description: </h4>')
	if decoded_repos[x]["language"] is not None:
		print "Language: "+decoded_repos[x]["language"]
		html.write('<h4>Language: <small>'+decoded_repos[x]["language"]+'</small></h4>\n')
	else:
		print "Language: "
		html.write('<h4>Language: </h4>')
	print ""
	html.write('<hr />\n')
	
html.write('''	    </div> <!-- /container -->

	    <!-- Le javascript
	    ================================================== -->
	    <!-- Placed at the end of the document so the pages load faster -->
	    <script src="http://twitter.github.com/bootstrap/assets/js/jquery.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-transition.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-alert.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-modal.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-dropdown.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-scrollspy.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tab.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tooltip.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-popover.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-button.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-collapse.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-carousel.js"></script>
	    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-typeahead.js"></script>

	  </body>
	</html>''')
	
"""
Notes:

Language can be more than one and is found in 'decoded_repos[x]["languages_url"]
Last Updated 'decoded_repos[x]["updated_at"]
Created On 'decoded_repos[x]["created_at"]
URL 'decoded_repos[x]["html_url"]
"""