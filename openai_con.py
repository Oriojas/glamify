import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def translate(prompt: str):
    response = openai.ChatCompletion.create(model="gpt-4",
                                            messages=[{
                                                "role": "system",
                                                "content": "You will be provided with a sentence in , Spanish"
                                                           "and your task is to translate it into English."},
                                                {"role": "user",
                                                 "content": "Hola mi nombre es Jani de Chicago"},
                                                {"role": "assistant",
                                                 "content": "Hello my name is Jane from Chicago"},
                                                {"role": "user",
                                                 "content": f"{prompt}"}],
                                            temperature=0,
                                            max_tokens=256,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)

    prompt_trans = dict(response.choices[0]).get("message").get("content")
    print(prompt_trans)

    return prompt_trans
