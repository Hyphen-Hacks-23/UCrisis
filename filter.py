# Python Imports
import array

# BERT Imports
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import shutil
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import transformers
from transformers import AutoModel, BertTokenizerFast

# GPT Imports
import os
import openai


# READ prompt list from text file
# with open("file.txt", "r") as f:
#    prompt_list = f.read()

LLM_prompt = "I will give you a list of prompts and I would like you to output a list with multiple groups, each group having prompts that talk about VERY SIMILAR things. If certain prompts have no other prompts that are VERY similar to them, do not put them in the new list. Each separate prompt is separated by a new line. Prompts will be similar if they talk about the same crisis and are talking about events that happen during similar times in similar areas in the world. Here are the prompts: "
prompt_list = "There is a fire happening in south san francisco. \n Anyone going to the basketball game tommorow night? \n Just saw the craziest fire in the Southern region of the city known as san francisco \n Eric Liu is a piece of shit"

"""
# BERT
bert = AutoModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

text = "This is an example sentence."
tokenized_input = tokenizer(text, return_tensors='pt')

with torch.no_grad():
    outputs = bert(**tokenized_input)
    embeddings = outputs.last_hidden_state

# For text classification (example)
classification_layer = nn.Linear(embeddings.shape[-1], num_classes)
logits = classification_layer(embeddings[:, 0, :])  # Using [CLS] token for classification
"""


# GPT
api_key = "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"
openai.api_key = api_key

response = openai.Completion.create(
    engine="text-davinci-003",  # Use the appropriate engine for your task.
    prompt=LLM_prompt + prompt_list,
    max_tokens=750,  # Adjust based on desired response length.
)

generated_text = response.choices[0].text.strip()

print(generated_text)
