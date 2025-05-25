from common.rest_util import send_post_request
from common.data_wrapper import OllamaResponse, OllamaModel, __get_json_payload


# Ollama API URL
URL ='http://localhost:11434/api/generate'


def chat_completion_stream(prompt: str, model: OllamaModel = OllamaModel.GEMMA3_1B):
    response = send_post_request(url=URL, data=__get_json_payload(prompt, model, stream=True))
    if response:
        # print(f"Response received: {response}")
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                print(chunk)
        # try:
        #     for chunk in response:
        #         if chunk :
        #            / print(chunk)
        #             # res = OllamaResponse.parse(chunk)
        #             # print(res)
        # except Exception as e:
        #     print(f"Error during streaming: {str(e)}")
        #     return OllamaResponse(model=str(model), response=f"Error during streaming: {str(e)}")
    else:
        print("No response received from the server.")
        return OllamaResponse(model=str(model), response="No response received from the server.")  


def chat_completion(prompt: str, model: OllamaModel = OllamaModel.GEMMA3_1B) -> OllamaResponse:
    try:  
        eval_ressponse = send_post_request(url=URL, data=__get_json_payload(prompt, model))
        response = OllamaResponse.parse(eval_ressponse)
        response.prompt = prompt  # Set the prompt in the response
        return response
    except Exception as e:
        return OllamaResponse(model=str(model), response=f"Couldn't evluate the promt:\n{prompt}")

if __name__ == "__main__":
    response = chat_completion_stream("what is the capital of Ghana?", OllamaModel.DEEPSEEK_R1_1_5B)
#    print(F'"Prompt":\n{response.prompt}\n\n"Response":\n{response.response}\n\n"Model": {response.model}')