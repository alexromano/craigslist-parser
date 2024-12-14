import os
from litellm import completion
import dotenv
dotenv.load_dotenv(override=True)

class Model:
    def completion(self, user_content: str, response_format = None) -> str:
        return completion(
            model=os.getenv("MODEL"),
            messages=[{"role": "user", "content": user_content}, {"role": "system", "content": "You are an expert at parsing information out of text. Use the given input to answer the question. Answer in the format specified."}],
            response_format=response_format
        )



