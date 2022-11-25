
import urllib.parse
import urllib.request


try:
    body = input("Enter the size of the QR code :")
    data = input("Enter the information of the QR code to be generated :")
    database = {
        "size":body+"x"+body,
        "data":data
    }
    database = urllib.parse.urlencode(database)
    api_url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example"+database
    document_name = ".\\QR_"+ data +".png"
    urllib.request.urlretrieve(api_url,document_name)
    print("Download is successful :)")
except:
    print("Error occured :(")

    
