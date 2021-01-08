#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client
import os                  #for acessing environment varaibles
print(os.environ.get('BROTHER'))
def message_daily_brother():

    # get your sid and auth token from twilio
    
    auth_token = os.environ.get('AUTHTOKEN')
    twilio_sid = os.environ.get('TWILIOSID')

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Brother':os.environ.get('BROTHER')}

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = f'Hello brother ,Have a lovely morning {key} !',
                from_= 'whatsapp:+14155238886',
                to=f'whatsapp:{value}')

        print(msg_loved_ones.sid)
        print(f"Message send to {key} successfully")
        
message_daily_brother()       


# In[ ]:





# In[ ]:




