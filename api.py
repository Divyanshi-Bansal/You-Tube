from googleapiclient.discovery import build
import json
import urllib.request

api_key= 'AIzaSyAU5h3nbVxmu5S6r84E5DA1X5i9lrWnsx0'
youtube = build('youtube','v3',developerKey=api_key)
#name = input('enter name:')
request = youtube.search().list(q='india drama',part='snippet',type='vedio',maxResults=50)
response = request.execute()
#print(response)
#for item in response['items']:
    #if name.lower  in item['title'].lower:
        #print(item['snippet']['title'])


key = "AIzaSyAU5h3nbVxmu5S6r84E5DA1X5i9lrWnsx0"

#List of channels : mention if you are pasting channel id or username - "id" or "forUsername"
ytids = [["bbcnews","forUsername"],["UCjq4pjKj9X4W9i7UnYShpVg","id"]]
print(ytids)
newstitles = []
for ytid,ytparam in ytids:
    urld = "https://www.googleapis.com/youtube/v3/channels?part=contentDetails&"+ytparam+"="+ytid+"&key="+key
    with urllib.request.urlopen(urld) as url:
        datad = json.loads(url.read())
    uploadsdet = datad['items']
    #get upload id from channel id
    uploadid = uploadsdet[0]['contentDetails']['relatedPlaylists']['uploads']
    channelid = uploadsdet[0]['id']
    print(channelid)
    #retrieve list
    #urld = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=50&playlistId="+uploadid+"&key="+key
    #with urllib.request.urlopen(urld) as url:
     #   datad = json.loads(url.read())

    #for data in datad['items']:
     #   ntitle =  data['snippet']['title']
      #  nlink = data['contentDetails']['videoId']
       # newstitles.append([nlink,ntitle])

#for link,title in newstitles:
 #   print(link, title)







#print(link)