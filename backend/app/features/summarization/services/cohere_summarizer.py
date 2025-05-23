import cohere
import os
from dotenv import load_dotenv
# from app.services.base_summarizer import BaseSummarizer
from app.features.summarization.services.base_summarizer import BaseSummarizer


load_dotenv()

class CohereSummarizer(BaseSummarizer):
    def __init__(self):
        self.client = cohere.Client(os.getenv("COHERE_API_KEY"))

    def summarize(self, text: str) -> str:
        response = self.client.summarize(
            text=text,
            model="summarize-xlarge",
            length="medium",
            format="paragraph",
            extractiveness="auto",
            temperature=0.3
        )
        return response.summary
