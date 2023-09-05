from llama_cpp import Llama
import os
import urllib.request


## We load the codellama python 7b model


def download_file(file_link, filename):
    '''
    Function to download a file on the current directory'''
    # Checks if the file already exists before downloading
    if not os.path.isfile(filename):
        print("Model File is curently downloading …")
        urllib.request.urlretrieve(file_link, filename)
        print("File downloaded successfully.")
    else:

        print("File already exists.")

# Dowloading gguf model from HuggingFace
gguf_model_path = "https://huggingface.co/TheBloke/CodeLlama-7B-Python-GGUF/resolve/main/codellama-7b-python.Q5_K_M.gguf"
filename = "codellama-7b-python.Q5_K_M.gguf"

download_file(gguf_model_path, filename)

llm = Llama(model_path=os.path.join(os.getcwd(), "codellama-7b-python.Q5_K_M.gguf"))


def generate_text(
    prompt='Write only: "Write something please"',
    max_tokens=512,
    temperature=0.1,
    top_p=0.1,
    echo=False,
    stop=[],
):
    output = llm(
        prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        echo=echo,
        stop=stop,
    )
    output_text = output["choices"][0]["text"].strip()
    return output_text
