import requests
import pprint
import google.generativeai as palm

query = input("Enter your query: \n")
base_url = "https://newsdata.io/api/1/news"
api_key = "pub_310028971ce6ce7caf601a9bcfe9eb5780d6c"
params={
    "q":query,
    "apiKey": api_key
}
response = requests.get(base_url, params= params)

content = ""

if response.status_code == 200:
    data = response.json()
    # print(data)
    # print(data.results)
    # for d in data['results']:
    print(data['results'][0])
    print (data['results'][0]['content'])
    content = data['results'][0]['content']
else:
    print("Failed", response)




palm.configure(api_key='AIzaSyAZLlvQ2yyZxQ6WqfZ0uTBKIhVxU0c-Ml8')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)
prompt = """
You are an expert at writing articles with human touch.

I need to paraphrase the following article for me and change the words completely around, make it as it's very different and not the same. Also, add some more depth and make it fun as its going o my blog:

{}

""".format(content)

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)
# gptj = gpt4all.GPT4All(
#     model_name="ggml-gpt4all-j-v1.3-groovy"
# )

# if gptj:
#     print("done dana done")
# else:
#     print("not done")
