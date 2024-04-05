# import openai_secret_manager
# assert "openai" in openai_secret_manager.get_services()
# secrets = openai_secret_manager.get_secret("openai")
# print(secrets)
# # {'api_key': 'sk-*******************************'}

import openai
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]