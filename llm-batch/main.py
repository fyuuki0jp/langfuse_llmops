from getpass import getpass
import os
from uuid import uuid4
from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse.callback import CallbackHandler
import dotenv

dotenv.load_dotenv(verbose=True)

langfuse_handler = CallbackHandler(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"], 
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_HOST"],
    session_id=str(uuid4())[:8]
)

def main():
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    result = model.invoke("こんにちは", config={"callbacks": [langfuse_handler]})
    print(result.content)

if __name__ == "__main__":
    main()
