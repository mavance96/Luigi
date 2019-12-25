import requests
import webbrowser
import urllib.parse
import json
import http.client
import urllib.request

#from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

import re
import json

from getpass import getpass
#JP is a big bot

class Mario_GetToken:
    
    client_id = "7FA06EAC-2CA0-4FA5-AEA0-BEE88DE95FB5" #Working one
    state = "user1"
    scope = "vso.build_execute vso.code_full vso.identity_manage vso.profile_write vso.work_full"
    callback_URL = "https://dev.azure.com/adasupershi/" #Good one
    
    clientSecret = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im9PdmN6NU1fN3AtSGpJS2xGWHo5M3VfVjBabyJ9.eyJjaWQiOiI3ZmEwNmVhYy0yY2EwLTRmYTUtYWVhMC1iZWU4OGRlOTVmYjUiLCJjc2kiOiI1YjQ5NzZlNi02ZjRhLTRjYjUtYjc0MC03ZjY5MDQ4NGM1OGEiLCJuYW1laWQiOiI3ODJkNDVhMy05ZGY0LTQ3NjAtYjRkNi1hMWMxZTNiMjRlZDUiLCJpc3MiOiJhcHAudnN0b2tlbi52aXN1YWxzdHVkaW8uY29tIiwiYXVkIjoiYXBwLnZzdG9rZW4udmlzdWFsc3R1ZGlvLmNvbSIsIm5iZiI6MTU3Mzc4NTkwNSwiZXhwIjoxNzMxNjM4NzA1fQ.v9_NTY1p5dY7DfCo6VDLe3lHPR9ygEsTmhhmaoGBq3QXXCzkgLJ6oCbFWFEbCRVZFpLwCogQ2UOB39zN5uOypZOaxiBKGY6E-qQzMDnIrt4l6sec2ndsp5NPujx8dboqYxzDN9HhH_gXQgYZrUehvuyPxfIifWmeTO7BzrnWp-tVhBqbsSP4afA_F8uf8u1HeNGu4JLBNzX117XkAuQbN1Rka_tPdi000axx09VNCjQ1KWs0hoDT9S3jNB9NZLQHPnpFAF2WC0BEKLRhXyJYrTFP4t4HFmdflc7BLERXKNSJeWgAlVNxn_NAotcAUZOmZHHb0weFPQNRI1J8o82h-g"
        
    refreshingToken = ""
    
    def get_authenticated(self):

        # Azure DevOps Services authorization endpoint
        Auth_URL = "https://app.vssps.visualstudio.com/oauth2/authorize?client_id=" + self.client_id + "&response_type=Assertion&state=" + self.state + "&scope=" + self.scope + "&redirect_uri=" + self.callback_URL
        
        #This opens the link to Authenticate
        webbrowser.open(Auth_URL)
        
        str = input("Paste here the URL(To paste right click): ")
        result = re.search('code=(.*)&state=', str)
        
        code11 = result.group(1)
        
        self.get_token(code11)  #Pass in the code
        
    def get_token(self, codenite):
        API_ENDPOINT = "https://app.vssps.visualstudio.com/oauth2/token"
        
        #Client secret
        first = self.clientSecret
        second = codenite
        
        urlEncodeFirst = urllib.parse.quote_plus(first)
        urlEncodeSecond = urllib.parse.quote_plus(second)
        
        
        data = {
            "client_assertion_type":"urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion":urlEncodeFirst,
            "grant_type":'urn:ietf:params:oauth:grant-type:jwt-bearer',
            "assertion":urlEncodeSecond,
            "redirect_uri":self.callback_URL
        }
        
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        
        r = requests.post(url = API_ENDPOINT, data = data, headers = headers).json()
        
        
        json_data = json.dumps(r)  #Transfer json to string ;)
        print(json_data)
        
        parsed_json = json.loads(json_data)
        
        token11 = parsed_json['access_token']
        refreshToken = parsed_json['refresh_token']
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("//////////REFRESH TOKEN WILL BE AFTER THIS/////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE REFRESH TOKEN: " + refreshToken)
        
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("////////////TOKEN WILL BE AFTER THIS///////////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE TOKEN: " + token11)
        
        self.getRefreshedToke(refreshToken)
      
    def getRefreshedToke(self, refreshToken1):
        API_ENDPOINT = "https://app.vssps.visualstudio.com/oauth2/token"
        
        #Client secret
        first = self.clientSecret
        #Refresh Token obtained when you got the token.
        second = refreshToken1
        
        urlEncodeFirst = urllib.parse.quote_plus(first)
        urlEncodeSecond = urllib.parse.quote_plus(second)
        
         
        data = {
            "client_assertion_type":"urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion":urlEncodeFirst,
            "grant_type":'refresh_token',
            "assertion":urlEncodeSecond,
            "redirect_uri":self.callback_URL
        }
        
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        
        r = requests.post(url = API_ENDPOINT, data = data, headers = headers).json()
        
        
        json_data = json.dumps(r)  #Transfer json to string ;)
        
        
        parsed_json = json.loads(json_data)
        
        accessToken = parsed_json['access_token']
        refreshToken = parsed_json['refresh_token']
        
        
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("////////////NEW TOKEN WILL BE AFTER THIS///////////")
        print("///////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////")
        print("THE TOKEN: " + accessToken)


def main():
    obj = Mario_GetToken()
    obj.get_authenticated()


 
main()