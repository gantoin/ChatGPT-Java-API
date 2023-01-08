import requests

def chatGPT(text):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY",
    }
    data = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 4000,
        "temperature": 1.0,
    }
    response = requests.post(url, headers=headers, json=data)
    output = response.json()['choices'][0]['text']

    return print(output)

if __name__ == "__main__":
    chatGPT("Hello, how are you?")
