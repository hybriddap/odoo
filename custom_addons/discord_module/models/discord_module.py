import requests
from odoo import models,fields

class DiscordModule(models.Model):
    _name = "discord.module"

    name = fields.Char(required=True)
    message = fields.Text(required=True)

    def create(self, vals):
        record = super().create(vals)
        record.send_api_request(vals)
        return record
    
    
    def send_api_request(self,vals):
        url = "https://discord.com/api/webhooks/1432320799892836412/XGUKLN1Wf_uP4LCGU4tU5Ye0HaZhs5_9OmmNE26e56PV9F2TLxz6tIzqOslughKp87kR"

        string = "Message from {fname},\n{message}".format(fname = vals['name'], message = vals['message'])
        payload = {
            "content": string
        }

        # headers = {
        #     "Authorization": "Bearer YOUR_API_KEY",
        #     "Content-Type": "application/json"
        # }

        response = requests.post(url, json=payload)