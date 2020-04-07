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
    
    client_id = "FF2CAEFB-5890-42FC-ABE9-90AB11A338F2" #Working one
    state = "user1"
    scope = "vso.analytics vso.auditlog vso.build_execute vso.code_full vso.code_status vso.connected_server vso.dashboards_manage vso.entitlements vso.environment_manage vso.extension.data_write vso.extension_manage vso.gallery_acquire vso.gallery_manage vso.graph_manage vso.identity_manage vso.loadtest_write vso.machinegroup_manage vso.memberentitlementmanagement_write vso.notification_diagnostics vso.notification_manage vso.packaging_manage vso.profile_write vso.project_manage vso.release_manage vso.securefiles_manage vso.security_manage vso.serviceendpoint_manage vso.symbols_manage vso.taskgroups_manage vso.test_write vso.tokenadministration vso.tokens vso.variablegroups_manage vso.wiki_write vso.work_full"
    callback_URL = "https://dev.azure.com/adasupershi/" #Good one
    
    clientSecret = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im9PdmN6NU1fN3AtSGpJS2xGWHo5M3VfVjBabyJ9.eyJjaWQiOiJmZjJjYWVmYi01ODkwLTQyZmMtYWJlOS05MGFiMTFhMzM4ZjIiLCJjc2kiOiI1ZjA2ZjgwOS1iZGUyLTRiNmYtYWYwMC0xOWM0MTkyNDk5ODIiLCJuYW1laWQiOiI3ODJkNDVhMy05ZGY0LTQ3NjAtYjRkNi1hMWMxZTNiMjRlZDUiLCJpc3MiOiJhcHAudnN0b2tlbi52aXN1YWxzdHVkaW8uY29tIiwiYXVkIjoiYXBwLnZzdG9rZW4udmlzdWFsc3R1ZGlvLmNvbSIsIm5iZiI6MTU4MTY0MDQwMywiZXhwIjoxNzM5NDkzMjAzfQ.QpOwA8L4MOtstemCKFpD0Ue0dycY3Cddew-ZLpOy8-evrP8-as5QaKlgGm4V7TVnQHULkmro_hYmWAaONGNZWyW08q33pkrIQWqc3Vj9I1BV0VZPcHTOmgwE_bkXwzm4KNaMwzgj6IUnAotjOM60MZB4oC4YSs0b-bf54HAv92Bpy2x1jGuCSL3g8UZUy4WQXxBC8MZcEl2NY5wkhH0q_1yZN1_jXvcPdQNHrtYdpdAXDmBKhQtTxQ5_-jb_Ndx58VLZS1pVtttowVe6x-uSf-a5TlkVCNpLPTJ1LuMwa-ztwGTjxW9J-RZHw9zDABe59r-4yBlk9C2KjMUXSNLeXQ"
        
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