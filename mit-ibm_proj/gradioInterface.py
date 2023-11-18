import gradio as gr
from pipeline import get_response

def response_interface(gradio_input):
    response = get_response(gradio_input)
    return response


iface = gr.Interface(
    fn=response_interface,
    inputs="text",
    outputs="text",
    live=True,
    title="Falcon 40B Teaching Assistant",
    description="Ask a question and get a response.",
)

iface.launch()

# #### SUBJECT IDENTIFY ####
# # set up model
# load_dotenv()
# api_key = os.getenv("GENAI_KEY", None)
# api_url = os.getenv("GENAI_API", None)
# creds = Credentials(api_key, api_endpoint=api_url)

# params = GenerateParams(decoding_method="greedy", max_new_tokens=200)

# model = Model("tiiuae/falcon-40b", params=params, credentials=creds)


# def get_response(message):
#     # calls subject identifier
#     predicted_subject = identify_subject(message)

#     # calls matching principles
#     dictionary = SubjectPrincipleDictionary()

#     principle_list = dictionary.lookup_principle(predicted_subject)
#     principle_string = ''.join(map(str, principle_list))

#     answer = ""
#     prompts = [principle_string + " " + message]
#     for response in model.generate(prompts):
#         answer.append(response.generated_text)

#     return answer

# ans = get_response("Why is the sky blue")
# print(ans)

# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot()
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])

#     def respond(message, chat_history):
#         bot_message = get_response(message)
#         chat_history.append((message, bot_message))
#         return "", chat_history

#     msg.submit(respond, [msg, chatbot], [msg, chatbot])

# demo.launch(share=True)

# # more info here https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks
