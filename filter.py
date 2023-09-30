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
import re
import io

# GPT Imports
import os
import openai

LLM_prompt = "I will give you a list of prompts that revolve around crises/incidents, and I would like you to output a list. Within this list, I would like you to output one line per prompt, prompts separated by a blank line. The lines will include: what the crisis/incident is, the Area/Address/Region of where the crisis/incident happened (no commas between the address, city, and country please), a description of the original crisis message, and a link to the original post. Even if a prompt doesn’t specify an address, please use context to try and give an approximate region/area as to where this happened. This list can only have crises that are WITHIN a 40 mile RADIUS of the location that I will give you. If the crisis is not within a 40 mile radius of the given location, DO NOT PRINT IT OUT. If the crisis does not have an address mention in it, DO NOT PRINT IT OUT. For each separate prompt, I will give the text that is in the prompt, a link to where the prompt was posted, and the time it was posted. Each individual prompt outputed in the list must be unique; that is if two prompts describe the same incident/crisis, output only one line for both prompts. The location is: "
df = pd.read_csv("facebook_postsold.csv")
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
    max_tokens=200,  # Adjust based on desired response length.
)

generated_text = response["choices"][0]["message"]["content"]

# print(generated_text)


crisis_reports = re.split(r"\n\n+", generated_text.strip())

# Initialize empty lists to store data
crisis_list = []
area_list = []
description_list = []
link_list = []

# Extract data from each crisis report
for report in crisis_reports:
    # Use regular expressions to extract data
    crisis_match = re.search(r"Crisis:\s+(.+)", report)
    area_match = re.search(r"Area:\s+(.+)", report)
    description_match = re.search(r"Description:\s+(.+)", report)
    link_match = re.search(r"Link:\s+\[Original Post\]\((.+)\)", report)

    if crisis_match and area_match and description_match and link_match:
        crisis_list.append(crisis_match.group(1))
        area_list.append(area_match.group(1))
        description_list.append(description_match.group(1))
        link_list.append(link_match.group(1))

# Create a pandas DataFrame
data = {
    "Crisis": crisis_list,
    "Area": area_list,
    "Description": description_list,
    "Link": link_list,
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = "crisis_data.csv"
df.to_csv(csv_file_path, index=False)

# Display the DataFrame
print(df)

# Confirm that the CSV file has been saved
print(f"Data saved to {csv_file_path}")
