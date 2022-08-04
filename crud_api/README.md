<h1>Welcome to my project</h1>


This project is simply a study code, here we can see a simple interation between
the api endpoint and the database.<br>
Here you can create a user with email and username, search for a especific user, and delete it.

<h2>How to run</h2>

<p>
First of all, make sure to up the enviroment variables by 'source .env'.<br> 
After this you'll need to create the database image by running './script.sh'.<br>
The last thing needed is to run the flask through the 'app.py' or 'flask run'.
</p>

<h2>How to consume the api</h2>
<p>
It's easy, just making requests to 'http://127.0.0.1:5000/crud' with the http methods you can interact with the app.
For example, to create a user you can use the POST method 'http://127.0.0.1:5000/crud?name=Elliot&email=fuck.society666@protonmail.com'.<br> Then you can search by the GET 'http://127.0.0.1:5000/crud?id=1' (assuming that Elliot was created first).<br> 
And delete by DELETE 'http://127.0.0.1:5000/crud?id=1'. 
</p>