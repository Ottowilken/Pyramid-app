Siyavula
----------------
This application simply takes a Wikipedia URL, and returns an html page with an unescaped html of the Table of Contents of the Wikipedia URL provided.

Currently using
---------------

1. Python 3.4
2. Django 1.8.4
3. Pyramid
4. Beautiful Soup <www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
5. pyramid_jinja2


To Run code this web app
---------------------------
Please follow the steps below:

1. Clone this repo
2. In the root directory of this repo, type, 'python setup.py develop'
3. then type, 'pserve develepment.ini'   server will boot
4. Visit localhost:6543
5. ENJOY

Features
-----------------
- The homepage shows a welcome message and present the user with an input box that asks for a Wikipedia URL and a submit button.
- When the submit button is clicked, the application, downloads the HTML source code, and displays the table of contents for the given page. Pages without Table of Contents, will alert an error message.
- Refresh button to start from the beginning
- The application checks for user input that is not a valid Wikipedia URL and posts an error message stating this
- Development was done on a Windows 7 machine
