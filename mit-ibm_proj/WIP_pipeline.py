import os
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai.model import Model
from genai.schemas import GenerateParams
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from subjectIdentify.subjectIdentifying import identify_subject
from principleExtraction.principleExtracting import SubjectPrincipleDictionary

import gradio as gr



#### SUBJECT IDENTIFY ####
# set up model
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)

params = GenerateParams(decoding_method="greedy", max_new_tokens=200)

model = Model("tiiuae/falcon-40b", params=params, credentials=creds)
# model = Model("meta-llama/llama-2-70b-chat", params=params, credentials=creds)

# user inputs question
# user_input = input("Please input your question: ")
# new_question = [user_input]
# question_string = ''.join(new_question)

# calls subject identifier
# predicted_subject = identify_subject(new_question)

# debug
# print(predicted_subject)

# calls matching principles
# dictionary = SubjectPrincipleDictionary()
# # principle = dictionary.lookup_principle(predicted_subject)
# principle_list = dictionary.lookup_principle(predicted_subject)
# principle_string = ''.join(map(str, principle_list))
# # debug
# print(principle_string)


# feed into model
# prompts = [principle_string + " " + question_string]
# for response in model.generate(prompts):
#     print(response.generated_text)

# need to store the response and look for too similar sentences and replace any values if needed
# combined paraphraser & sentence transformer code could go here ?

# gradio interface

# function version of getting response

def get_response(new_question):
    question_string = ''.join(new_question)

    question_list = [new_question]
    predicted_subject = identify_subject(question_list)

    dictionary = SubjectPrincipleDictionary()

    principle_list = dictionary.lookup_principle(predicted_subject)
    principle_string = ''.join(map(str, principle_list))

    prompts = [principle_string + " " + question_string]
    generated_responses = []
    for response in model.generate(prompts):
        generated_responses.append(response.generated_text)

    return ' '.join(generated_responses)
    

    # predicted_subject = identify_subject(message)
    # dictionary = SubjectPrincipleDictionary()
    # principle = dictionary.lookup_principle(predicted_subject)

    # prompts = [principle, message]
    
    # for response in model.generate(prompts):
    #     generated_responses.append(response.generated_text)

    # return ' '.join(generated_responses)

    # return message

    # this needs to be modified but essentially we need it to get the final
    # response from the bot to return from here

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = get_response(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)

# def response_interface(question):
#     response = get_response(question)
#     return response

# iface = gr.Interface(
#     fn=response_interface,
#     inputs="text",
#     outputs="text",
#     live=True,
#     title="Question-Answer Interface",
#     description="Ask a question and get a response.",
# )

# iface.launch()

# more info here https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks





