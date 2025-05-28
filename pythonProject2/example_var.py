import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables

print(os.getenv('API_URL'))
print(os.getenv('TOKEN'))