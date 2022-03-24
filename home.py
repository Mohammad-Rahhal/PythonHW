from flask import Flask

name = "Lisa"
city_names = ["Paris", "Rome", "London", "Tahiti"]
myapp_obj = Flask(__name__)
@myapp_obj.route("/")
def home():
        return '''
    <html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Welcome '''  + name + '''!</h1>
        <a href={{url_for("www.google.com")}}> not google </a> <br/>
        <br/>
                <ul>
                <li> ''' +  city_names[0] + '''</li>
                <li> ''' +  city_names[1] + '''</li>
                <li> ''' +  city_names[2] + '''</li>
                <li> ''' +  city_names[3] + '''</li>
                </ul>
    </body>
    </html>'''

#myapp_obj.run()
