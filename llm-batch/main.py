import getpass
import os
import langfuse
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass("Provide your Google API Key")

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

def main():
    pass

if __name__ == "__main__":
    main()
