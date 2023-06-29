import openai
from pydantic import BaseModel


class Document(BaseModel):
  prompt: str = ''

def inference(prompt: str) -> list:
  openai.organization = 'org-PYELIbA8LxpnGFiTsMHVkbOV'
  openai.api_key = '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'

  print('[PROCESANDO]'.center(40, '-'))
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": """Eres un profesor de programción para niños, genera una explicación para el tema que se te proporciona
      E.G:  Programación 
      -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
      {"role": "user", "content": prompt}
    ]
  )
  content = completion.choices[0].message.content
  total_tokens = completion.usage.total_tokens


  print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
  return [content, total_tokens]
