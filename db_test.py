import requests
import base64
import json

# OpenAI API endpoint
url = "https://api.openai.com/v1/images"

# OpenAI API key
api_key = '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'

# Image generation function
def generate_image(description):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    data = {
        'prompt': description,
        'max_tokens': 50,
        'temperature': 0.7,
        'n': 1,
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    image_b64 = response_json['choices'][0]['image']
    image_data = base64.b64decode(image_b64)

    return image_data

# Enter the text description for image generation
description = "A girl walking on a snowy road"

# Generate the image
generated_image = generate_image(description)

# Save the generated image
with open('generated_image.jpg', 'wb') as f:
    f.write(generated_image)

print("Image generated and saved: generated_image.jpg")
