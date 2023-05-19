# Example posting a text URL:

import requests
import openai


# Example posting a local text file:

# import requests
# r = requests.post(
#     "https://api.deepai.org/api/text2img",
#     files={
#         'text': open('/path/to/your/file.txt', 'rb'),
#     },
#     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
# )
# print(r.json())


# # Example directly sending a text string:

# import requests
# r = requests.post(
#     "https://api.deepai.org/api/text2img",
#     data={
#         'text': 'person',
#     },
#     headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
# )
# print(r.json())

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)