import dotenv
import os

dotenv.load_dotenv()
# Load environment variables from .env file
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
FIRE_CRAWEL_API = os.getenv("FIRE_CRAWEL_API")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
PINECONE_ENV = os.getenv("PINECONE_ENV")
