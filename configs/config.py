import dotenv
import os

dotenv.load_dotenv()
# Load environment variables from .env file
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

