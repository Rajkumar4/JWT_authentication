# JWT_authentication

```
  api for Json web token authentication
    root Url: localhost:3000/
    limit: 5 request per miniute
    
    For signup:
        url: localhost:3000/signup/ methos='POST'
         requirement as application/json 
            user: <unique in db>
            password : string
         response:
            Json message:<Text>
            
    for login:
       url: localhost:3000/signup/ methos='POST'
           requirement as application/json 
            user: <unique in db>
            password : string
        response:
            Json message:<text>
            Access_token:<Hashed token>
            
    for verify:
          url: localhost:3000/verify/?token=<hashed token> methos='GET'      
          response:
             json message:<Text>
   
