import os

from dotenv import load_dotenv
# Access the environment variable
load_dotenv()
my_secret = os.getenv("MY_SECRET_KEY")

print(f"My secret key is: {my_secret}")
