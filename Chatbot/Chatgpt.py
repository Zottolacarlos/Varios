import os
from dotenv import load_dotenv
import openai
import spacy #sirve para analiar texto

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

#probar q esta bien usada la clave
#modelos = openai.Model.list()
#print(modelos)

modelo = "text-davinci-002"
prompt = "Cuenta una historia breve que sucede en Argentina"
respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    max_tokens=100
)
#print(respuesta)


texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("************************************\n")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

ubicacion = None

for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break


if ubicacion:
    prompt2 = f"Dime más acerca de {ubicacion}"
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )

    texto_gen2 = respuesta2.choices[0].text.strip()
    print(texto_gen2)

#parametros para la respuesta
#temperatura: si es deterministico seria 0.1
#token: para la profundida y largo de la respuesta
#respuestas:




