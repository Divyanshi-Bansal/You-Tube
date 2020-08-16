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
    #print(channelid)
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



def get_all_video_in_channel(channelid):
    api_key = ''

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


link = get_all_video_in_channel(channelid)
print(link)