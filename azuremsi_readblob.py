import json
import os
import sys
cmd="curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fstorage.azure.com%2F' -H Metadata:true > oauth2token2"
os.system(cmd)
file=open("oauth2token2","r")
oauth2output=file.read() 
oauthdict = json.loads(oauth2output)
bearer_token=oauthdict.get("access_token")
# curl https://srinmanfaasblob.blob.core.windows.net/test/helloworldtext -H "x-ms-version: 2017-11-09" -H "Authorization: Bearer 
cmd="curl https://"+sys.argv[1]+" -H \"x-ms-version: 2017-11-09\" -H \"Authorization: Bearer "+bearer_token+"\""
os.system(cmd)
