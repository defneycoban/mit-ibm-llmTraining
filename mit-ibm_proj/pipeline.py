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

# llemma stuff
# from transformers import AutoTokenizer, AutoModelForCausalLM

# llemma_tokenizer = AutoTokenizer.from_pretrained("EleutherAI/llemma_7b")
# lemma_model = AutoModelForCausalLM.from_pretrained("EleutherAI/llemma_7b")

# gr.load("models/EleutherAI/llemma_7b").launch()



#### SUBJECT IDENTIFY ####
# set up model
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)

stop_seqs = ["## Question ##"]
#params = GenerateParams(decoding_method="greedy", max_new_tokens=300)
params = GenerateParams(decoding_method="greedy", stop_sequences=stop_seqs, max_new_tokens=300)

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

unwanted_phrases = ["## Question ##", "##Answer##", "## Answer ##", "Answer:"]

# remove stop sequences from hint
def remove_phrases(hint, unwanted_phrases):
    for phrase in unwanted_phrases:
        hint = hint.replace(phrase, '')
    return hint

def get_response(new_question):
    question_string = ''.join(new_question)

    question_list = [new_question]
    predicted_subject = identify_subject(question_list)
    print(predicted_subject)
    dictionary = SubjectPrincipleDictionary()

    principle_list = dictionary.lookup_principle(predicted_subject)
    principle_string = ''.join(map(str, principle_list))

    prompts = [principle_string + " " + question_string]

    generated_responses = []
    for response in model.generate(prompts):
        generated_responses.append(response.generated_text)
    hint = ' '.join(generated_responses)

    # Post Process

    hint = remove_phrases(hint, unwanted_phrases)

    return hint
    

    # return ' '.join(generated_responses)

    
    
    
# more info here https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks





