import time
import pyotp
import qrcode

#print(pyotp.random_base32())

master_key ="ZSKU764JDHVT74GLSRYGU2OSRN4457MD"

code = pyotp.TOTP(master_key)
print(code.now())

user_code = input("Digite o código enviado: ")
print(code.verify(user_code))

link = pyotp.TOTP(master_key).provisioning_uri(name="Vini", issuer_name="Codigo python")

my_qrcode = qrcode.make(link)
my_qrcode.save("qrcode.png")
