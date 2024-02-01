from transformers import AutoTokenizer, AutoModelForCausalLM

llemma_tokenizer = AutoTokenizer.from_pretrained("EleutherAI/llemma_7b")
lemma_model = AutoModelForCausalLM.from_pretrained("EleutherAI/llemma_7b")

prompt = "3 + 5 = ?"
inputs = llemma_tokenizer(prompt, return_tensors="pt")

generate_ids = lemma_model.generate(inputs.input_ids, max_length=30)
llemma_tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

