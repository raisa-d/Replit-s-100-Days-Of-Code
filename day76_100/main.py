from flask import Flask
import datetime as dt

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    today = dt.date.today()
    page = f'''
  <html>
    <body>
      <span>{today}</span>
      <p>
        <a href='/linktree'>Go to Linktree</a>
      </p>
      <p>
        <a href='/portfolio'>Go to Portfolio</a>
      </p>
    </body>
  </html>
  '''
    return page


@app.route('/linktree')  # Creates the path to the home page
def linktree():  # Subroutine to create the home page
    page = '''
    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width">
      <title>Raisa's Linktree</title>
      <link href="/static/style.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
      <!-- headshot image -->
      <div>
        <img src="/static/images/headshot.png">
      </div>

      <!-- name -->
      <section>
        <h1>Raisa Dorzback</h1>
        <span>Software Engineer</span>
      </div>

      <!-- list of links -->
      <ul>
        <li>
          <a target="_blank" href="https://twitter.com/rai__bread">Twitter</a>
        </li>
        <li>
          <a target="_blank" href="https://github.com/raisa-d">GitHub</a>
        </li>
        <li>
          <a target="_blank" href="https://www.linkedin.com/in/raisa-d/">LinkedIn</a>
        </li>
        <li>
          <a target="_blank" href="portfolio">Portfolio</a>
        </li>
      </ul>
      <script src="script.js"></script>

      <!--
      This script places a badge on your repl's full-browser view back to your repl's cover
      page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
      teal, blue, blurple, magenta, pink!
      -->
      <script src="https://replit.com/public/js/replit-badge.js" theme="magenta" defer></script>
    </body>

    </html>
    '''
    # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
    return page  # returns the contents of the page variable


@app.route('/portfolio')
def portfolio():
    page = """
    <html>
      <head>
        <title>Portfolio</title>
      </head>
      <body>
        <h1>Welcome to my portfolio</h1>
      </body>
    </html>
  """
    return page


# turns on web server
app.run(host='0.0.0.0', port=81)
