import openai
from dotenv import load_dotenv
load_dotenv()
import os

class OpenAiApi():
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def _format_response(self, response):
        formatted = response['choices'][0]['message']['content']
        return formatted

    def get_response(self, prompt):
        reponse = openai.ChatCompletion.create(
            api_key=self.api_key,
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=150,
        )
        return self._format_response(reponse)
    
if __name__ == '__main__':
    prompt = "What is the best way to cook a steak?"
    print(OpenAiApi().get_response(prompt))