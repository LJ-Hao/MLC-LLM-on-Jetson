import torch
from torch import cuda
from transformers import LlamaTokenizerFast, pipeline,  LlamaForCausalLM, AutoTokenizer, AutoModelForCausalLM
import time

model_dir = "/data/models/mlc/dist/models/Llama-2-7b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(model_dir, torch_dtype=torch.bfloat16, device_map='auto', local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_dir,local_files_only=True, max_length=64)
tokenizer.use_default_system_prompt = False


def chat_with_llama(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to('cuda')
    output = model.generate(input_ids, max_length=64)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

while True:
    prompt = input("You: ")
    response = chat_with_llama(prompt)
    print("Llama:", response)