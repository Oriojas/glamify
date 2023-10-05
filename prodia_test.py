import prodia_con
from time import sleep

delay = 10 # segundos

prompt_user = ("Create some makeup ideas for a New Year's Eve party, with a round face, "
               "African skin color and I want it to be striking")

prodia_obj = prodia_con.Prodia()

response_dict = prodia_obj.create(prompt=prompt_user)

img_job = dict(eval(response_dict)).get("job")

sleep(delay)

response_img = prodia_obj.download(n_job=img_job)

response_url_img = dict(eval(response_img.text)).get("imageUrl")

print(response_img)

