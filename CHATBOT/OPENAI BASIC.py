

import openai 


openai.api_key = 'yourapikey'

print("welcome to chatgpt")

prompt = input("enter your request : ")

response = openai.Completion.create(
    model ='text-davinci-003',
    prompt = prompt,
    max_tokens = 250,
    temperature = 0.7
)

output = response['choices'][0]['text']
print(output)




