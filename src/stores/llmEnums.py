from enum import Enum

class LLMModelType(Enum):
    OPENAI = "openai"
    COHERE = "cohere"
    
    
class OpenAIEnums(Enum):
    SYSTEM= "system",
    USER= "user",
    ASSISTANT= "assistant"
    