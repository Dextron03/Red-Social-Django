from dotenv import load_dotenv
from os import getenv
from mailjet_rest import Client
import requests.exceptions

load_dotenv('.env')

class EmailService:
    def __init__(self):
        self.api_key = getenv('API_KEY')
        self.api_secret = getenv('SECRET_KEY')
    
    def send_email(self, to: str, subject: str, html: str):
        try:
            obj_mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')
            data = {
              'Messages': [
                {
                  "From": {
                    "Email": getenv('EMAIL_HOST_USER'),
                    "Name": "Social NetWork"
                  },
                  
                  "To": [
                    {
                      "Email": to,
                      "Name": "Destinatario"
                    }
                  ],
                  "Subject": subject,
                  "TextPart": "¡Saludos desde Social NetWork!",
                  "HTMLPart": html,
                }
              ]
            }
            
            sending = obj_mailjet.send.create(data=data)
        except requests.exceptions.HTTPError as e:
            # Manejar errores de red o de la API de Mailjet
            print(f"Error al enviar el correo electrónico: {e}")
        except Exception as e:
            # Manejar cualquier otro tipo de excepción
            print(f"Error inesperado al enviar el correo electrónico: {e}")
        return sending


enviar = EmailService()
print(enviar.api_key)
