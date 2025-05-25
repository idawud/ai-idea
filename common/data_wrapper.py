from dataclasses import dataclass
from enum import Enum
import json


def __get_json_payload(prompt, model, stream=False, temperature=0, top_p=0):
    return {
        "model": str(model),
        "prompt": prompt,
        "stream": stream,  # Set to True for streaming responses
        "temperature": temperature,  # Adjust temperature for response variability
        "top_p": top_p,  # Adjust top_p for response diversity
    }
    
class OllamaModel(Enum):
    GEMMA3_1B = "gemma3:1b"
    DEEPSEEK_R1_1_5B = "deepseek-r1:1.5b"

    def __str__(self):
        return self.value

@dataclass
class OllamaResponse:
    model: str
    created_at: str
    response: str
    done: bool
    done_reason: str
    context: list[int]
    total_duration: float
    load_duration: float
    prompt_eval_count: int
    prompt_eval_duration: float
    eval_count: int
    eval_duration: float
    prompt: str = None  # Optional field for the prompt used in the response
            
    def __init__(self, model: str, 
                 response: str,
                created_at: str = None, 
                 done: bool = False, 
                 done_reason: str =None,
                 context: list[int] = [], 
                 total_duration: float = 0, 
                 load_duration: float = 0,
                 prompt_eval_count: int = 0,
                 prompt_eval_duration: float = 0,
                 eval_count: int = 0, 
                 eval_duration: float = 0):
        self.model = model
        self.created_at = created_at
        self.response = response
        self.done = done
        self.done_reason = done_reason
        self.context = context
        self.total_duration = total_duration
        self.load_duration = load_duration
        self.prompt_eval_count = prompt_eval_count
        self.prompt_eval_duration = prompt_eval_duration
        self.eval_count = eval_count
        self.eval_duration = eval_duration
    
    def __str__(self):
        return f"OllamaResponse(model={self.model}, done={self.done}, response={self.response})"
    
    @staticmethod
    def parse(line: str| dict) -> 'OllamaResponse':
        if isinstance(line, str):
            return OllamaResponse(**json.loads(line))
        else:
            return OllamaResponse(**line)