# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 12:42:17 2020

@author: haluk
"""
import requests

##影片資訊
# https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id=UCL_qhgtOy0dy1Agp8vkySQg&key=AIzaSyATG2vnsLXLN0FIk8iBn2FCCsybDLa9oLc
##加橫幅
# https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics,brandingSettings&id=UCL_qhgtOy0dy1Agp8vkySQg&key=AIzaSyATG2vnsLXLN0FIk8iBn2FCCsybDLa9oLc
#url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics,brandingSettings&id=UCL_qhgtOy0dy1Agp8vkySQg&key=AIzaSyATG2vnsLXLN0FIk8iBn2FCCsybDLa9oLc"


api = "https://www.googleapis.com/youtube/v3/channels"
part= "snippet,contentDetails,statistics,brandingSettings"
id_ = "UCL_qhgtOy0dy1Agp8vkySQg"
### remember to change this key
key = "AIzaSyATG2vnsLXLN0FIk8iBn2FCCsybDLa9oLc"


url = api + "?part=" + part + "&id=" + id_ + "&key=" + key
info = requests.get(url)
info_json = info.json()

# brandingUrl = 'https://www.googleapis.com/youtube/v3/channels?part=brandingSettings&id=UCL_qhgtOy0dy1Agp8vkySQg&key=AIzaSyATG2vnsLXLN0FIk8iBn2FCCsybDLa9oLc'
# branding = requests.get(brandingUrl)
# branding_json =  branding.json()

channel_name = info_json['items'][0]['snippet']['title'] #頻道名稱
channel_description = info_json['items'][0]['snippet']['description'] #頻道描述
channel_published_time = info_json['items'][0]['snippet']['publishedAt'] # 頻道開始時間
profile_pic = info_json['items'][0]['snippet']['thumbnails']['medium'] # default, medium & high #頻道主圖

# view info  info_json['items'][0]['statistics'])

channel_viewCount = info_json['items'][0]['statistics']['viewCount'] # 觀看總數
channel_subscriberCount = info_json['items'][0]['statistics']['subscriberCount'] #訂閱數
channel_videoCount = info_json['items'][0]['statistics']['videoCount']  # 影片數
channel_country = info_json['items'][0]['snippet']['country'] # 頻道註冊地(國家)

# banner有很多種規格可以選, 先用一般的
# info_json['items'][0]['brandingSettings']['image']
# 有時候banner image會跑不出來不知道為什麼
#channel_banner_pic = branding_json['items'][0]['brandingSettings']['image']['bannerImageUrl']
channel_banner_pic = info_json['items'][0]['brandingSettings']['image']['bannerImageUrl'] #頻道橫幅圖
print("Channel name:", channel_name)
print("Description:", channel_description)
print("Channel published time:", channel_published_time)
print("Profile picture:", profile_pic)
print("Views:", channel_viewCount)
print("Subscribers:", channel_subscriberCount)
print("Videos:", channel_videoCount)
print("Country:", channel_country)
print("Banner picture:", channel_banner_pic)

