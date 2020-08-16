from YouTube_Statistics import YTstats

API_KEY = 'AIzaSyAU5h3nbVxmu5S6r84E5DA1X5i9lrWnsx0'
channel_id = 'UCBR8-60-B28hp2BmDPdntcQ'

yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()