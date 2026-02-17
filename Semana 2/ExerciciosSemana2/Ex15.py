import json
'''
{
  "status": "success",
  "data": {
      "usuario": "Artur",
      "nivel": "premium"
  }
}

'''
usuario = {
  "status": "success",
  "data": {
      "usuario": "Artur",
      "nivel": "premium"
  }
}

usuario_json = json.dumps(usuario, indent=4)
print(usuario_json)

usuario_dict = json.loads(usuario_json)
print(f' Nível do usuário: {usuario_dict["data"]["nivel"]}')

