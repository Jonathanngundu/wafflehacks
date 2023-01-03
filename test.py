from twilio.rest import Client 
 
def message():
    account_sid = 'AC874ba10657a496bd165a2af123412093' 
    auth_token = '[f6eb61a0efa76563d2d29d3eb71defce]' 
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body="hello",      
                              to='whatsapp:+number'
                          ) 


message()
