# paraphraser from https://huggingface.co/humarin/chatgpt_paraphraser_on_T5_base
# this file contains the bare bones framework of how to get the paraphraser working and 
# how to call it on some text!

#obtain the model that does the paraphrasing 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
paraphrase_model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")


# function definition
def paraphrase(
    question,
    num_beams=5,
    num_beam_groups=5,
    num_return_sequences=1, # change this to get more sentences if needed
    repetition_penalty=10.0,
    diversity_penalty=3.0,
    no_repeat_ngram_size=2,
    max_length=128
):
    input_ids = tokenizer(
        f'paraphrase: {question}',
        return_tensors="pt", padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids
    
    outputs = paraphrase_model.generate(
        input_ids, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res

# example of how to call paraphrase function
text = 'Church authorities are the best judges of whether someone is truly repentant.'
# paraphrase returns a list of strings, so access the first index to just get the string
paraphrased_text = paraphrase(text)[0]
print(paraphrased_text) 

