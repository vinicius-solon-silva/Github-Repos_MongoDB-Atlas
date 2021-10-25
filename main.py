import mongoengine
import request
from repos import Repository

print("\n---MongoDB credentials---")
mongo_user = input("\nEnter your MongoDB database username: ")
password = input("Enter your MongoDB user password: ")
cluster_URL = input("Enter your cluster URL: ")
database_name = input("Enter your database name: ")

mongoengine.connect( 
    host=f"mongodb+srv://{mongo_user}:{password}@{cluster_URL}/{database_name}?retryWrites=true&w=majority"
)

try:
    for repo in request.repos:
        userRepo = Repository(git_user=request.user, repo_name=repo["name"], URL=repo["html_url"])
        userRepo.save()
        print("Successfully inserted data in collection!\n")
except Exception as e:
    print(f"Error stablishing connection, verify the following error and try again later:\n{e}\n")