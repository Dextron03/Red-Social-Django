from dotenv import load_dotenv
from os import getenv
from mailjet_rest import Client

load_dotenv(".env")

class EmailSevice():
    def __init__(self):
        self.api_key = getenv('API_KEY')
        self.api_secret = getenv('SECRET_KEY')
    
    
    def send_email(self, to:str, subject:str, html:str):
        obj_mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        
        data = {
            'Messages':[
                {
                    "From": {
                        "Email": getenv("EMAIL_HOST_USER"),
                        "Name": "Social NetWork"
                    },
                    "To": [
                        {
                            "Email": to,
                            "Name": "Destinatario"
                        }
                    ],
                    "Subject": subject,
                    "TextPart": "¡Termine el proceso de activacion!",
                    "HTMLPart": html

                }
            ]
        }
        
        sending = obj_mailjet.send.create(data=data)
        
        return sending
        
        
        

        
        
       
    