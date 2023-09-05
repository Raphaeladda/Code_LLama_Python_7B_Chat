import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from llama_code_model import generate_text


st.set_page_config(page_title="LLaMA code python - An AI assistant Streamlit app")

# Sidebar contents
with st.sidebar:
    st.title("💬 LLama code python 7B Web App by Raphael Adda")
    st.markdown(
        """
    ## About
    This app is an LLM-powered AI assistant built using:
    - [Streamlit](https://streamlit.io/)
    - [llama-cpp-python](https://llama-cpp-python.readthedocs.io)
    - [TheBloke/CodeLlama-7B-Python-GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-Python-GGUF) LLM model
    
    💡 The model is open source.  
    It is quite slow because it runs on your own CPU.  
    Read [Installation with Hardware Acceleration](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration) to accelerate this model.
    """
    )
    add_vertical_space(5)
    st.write(
        "Inspired from [Data Professor](https://medium.com/streamlit/how-to-build-an-llm-powered-chatbot-with-streamlit-a1bf0b2701e8)"
    )

# Generate empty lists for generated and past.
## generated stores AI generated responses
if "generated" not in st.session_state:
    st.session_state["generated"] = ["I'm code Llama python, ask me anything in Python"]
## past stores User's questions
if "past" not in st.session_state:
    st.session_state["past"] = ["Hi!"]

# Layout of input/response containers
input_container = st.container()
colored_header(label="", description="", color_name="blue-30")
response_container = st.container()


# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


## Applying the user input box
with input_container:
    user_input = get_text()

with response_container:
    if user_input:
        response = generate_text(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)

    if st.session_state["generated"]:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))
