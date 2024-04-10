import os
from dotenv import load_dotenv
if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("OPENAI_API_KEY"))
    print("Hello World!")