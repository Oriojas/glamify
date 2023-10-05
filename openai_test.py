import openai_con

query = ("Crea algunas ideas de maquillaje para una fiesta de fin de año, "
         "con una cara redonda, color de piel africana y quiero que sea llamativo")

response = openai_con.translate(prompt=query)


print(query)
print(response)