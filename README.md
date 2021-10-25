# GET GITHUB USER REPOSITORIES WITH MONGOENGINE

This project makes a search for github users repositories and post to an MongoDB Atlas Database, using mongoengine.

## Installation

- Clone the repository
- Install _requests_ library using pip:
``` 
pip install requests
```
- Install _mongoengine_ library using pip:
``` 
pip install mongoengine
```

## Running the code

- Open the project folder in a development tool, like VsCode for example
- Run main.py using Python compiler

```
- The interface asks for a Github username, the program them will list all repos of this user.

- After that, the interface asks for your MongoDB credentials: database username, database password, cluster URL and database name.

- If everything goes right, a message will appear: "Successfully inserted data in collection!".

- If an exception occurs the interface will warn the user and end the execution of the program with a message: "Error stablishing connection, verify the following error and try again later".
```

## More information

You can access the _Requests_ library documentation [here](https://requests.readthedocs.io/en/master/)

You can access the _Mongoengine_ library documentation [here](http://docs.mongoengine.org/)

If you have any errors involving SSL certificate expiration, you can access [this topic](https://www.mongodb.com/community/forums/t/keep-getting-serverselectiontimeouterror/126190) from the MongoDB forum where users found a solution.
