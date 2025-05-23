import os
from app.features.summarization.services.base_summarizer import BaseSummarizer
from app.features.summarization.services.cohere_summarizer import CohereSummarizer
# from app.services.cohere_summarizer import CohereSummarizer
# from app.services.openai_summarizer import OpenAISummarizer (future)
# from app.services.anthropic_summarizer import AnthropicSummarizer (future)

def get_summarizer():
    provider = os.getenv("SUMMARIZER_PROVIDER", "cohere").lower()

    if provider == "cohere":
        return CohereSummarizer()
    # elif provider == "openai":
    #     return OpenAISummarizer()
    # elif provider == "anthropic":
    #     return AnthropicSummarizer()
    else:
        raise ValueError(f"Unknown summarizer provider: {provider}")
