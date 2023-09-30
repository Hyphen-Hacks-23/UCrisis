# Python Imports
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import shutil
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import transformers
from transformers import AutoModel, BertTokenizerFast
import csv

# GPT Imports
import os
import openai

LLM_prompt = "I will give you a list of prompts that revolve around crises, and I would like you to output a list. Within this list, I would like you to output one line per prompt, prompts separated by a blank line. The lines will include: what the crisis is, the Area/Address/Region of where the crisis happened, a description of the original crisis message, and a link to the original post. This list can only have crises that are WITHIN a 40 mile RADIUS of the location that I will give you. If the crisis is not within a 40 mile radius of the given location, DO NOT PRINT IT OUT. If the crisis does not have an address mention in it, DO NOT PRINT IT OUT. For each separate prompt, I will give the text that is in the prompt, a link to where the prompt was posted, and the time it was posted. Each individual prompt outputed in the list must be unique; that is if two prompts describe the same incident/crisis, output only one line for both prompts. The location is: "
df = pd.read_csv("facebook_scraper/facebook_posts.csv")
prompt_list = df.to_csv(index=False)

user_location = input("Please enter your location: ")

# GPT
api_key = "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"
openai.api_key = api_key

system_msg = "You are a helpful assistant who knows the map of the world and knows distances between different addresses."
prompt = LLM_prompt + user_location + "Here are the prompts: " + ". \n" + prompt_list


response = openai.ChatCompletion.create(
    model="gpt-4",  # Use the appropriate engine for your task.
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt},
    ],
    temperature=0.3,
    max_tokens=2000,  # Adjust based on desired response length.
)

generated_text = response["choices"][0]["message"]["content"]

print(generated_text)
