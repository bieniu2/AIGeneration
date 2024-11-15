import requests
from openai import OpenAIError, OpenAI


def download_content(url: str, path: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        with open(path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Content successfully downloaded and saved to {path}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading content from {url}: {e}")
    except IOError as e:
        print(f"Error saving content to {path}: {e}")


def send_query_to_openai(api_key: str,
                         query: str,
                         model: str = "gpt-4") -> str:
    try:
        client = OpenAI(
            api_key=api_key,
        )
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model=model,
        )
        print("Generated response size ", len(response.choices))
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"An error occurred: {e}"


def download_image(url: str, save_path: str):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image successfully downloaded and saved as {save_path}")
        else:
            print(f"Failed to retrieve image. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the image: {e}")


def send_image_query_to_openai(api_key: str,
                               prompt: str) -> str:
    try:
        client = OpenAI(
            api_key=api_key,
        )
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except OpenAIError as e:
        print(f"An error occurred: {e}")


