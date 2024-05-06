from openai import OpenAI

client = OpenAI(api_key='sk-RgYc9a656a0ddcda9339c9318c61c49456bc9ba5e5fdsAEl',
                base_url='https://api.gptsapi.net/v1')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion)
print(completion.choices[0])
