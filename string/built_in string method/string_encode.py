import base64


Str = "this is string example....wow!!!"

Str=base64.b64encode(Str.encode('utf-8',errors='strict')) 

print ("Encoded String: " , Str)