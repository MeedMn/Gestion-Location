import requests
from PIL import Image

def getLink(query):
    r = requests.get("https://api.qwant.com/v3/search/images",
                     params={
                         'count': 1,
                         'q': query,
                         't': 'images',
                         'safesearch': 1,
                         'locale': 'en_US',
                         'offset': 0,
                         'device': 'desktop'
                     },
                     headers={
                         'User-Agent': 'Mozilla/5.0'
                     }
                     )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    return urls[0]

def getImage(query,i):
    try:
        with open('media/'+query+str(i)+'.png', 'wb') as handle:
            response = requests.get(getLink(query), stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        image = Image.open('media/'+query+str(i)+'.png')
        new_image = image.resize((531, 474))
        new_image.save('media/'+query+str(i)+'.png')
    except:
        pass

class utilisateur:
    def __init__(self):
        self.id =''
        self.Nom = ''
        self.Prenom = ''
        self.Poste = ''
        self.Telephone = ''
        self.Username=''
        self.MotDePasse=''
    def initialize(self,id,nom,prenom,poste,telephone,username,motDePasse):
        self.id = id
        self.Nom = nom
        self.Prenom = prenom
        self.Poste = poste
        self.Telephone = telephone
        self.Username = username
        self.MotDePasse = motDePasse
    def getData(self):
        return self.id,self.Nom,self.Prenom,self.Poste,self.Telephone,self.Username,self.MotDePasse
