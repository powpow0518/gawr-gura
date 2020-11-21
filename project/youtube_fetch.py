'''
這個file包含
1. 使用youtube api 抓取youtube資訊的方法
2. 自己爬取youtube banner(頻道背景橫幅圖片)的方法

'''

import requests
import re
import os
import Globals

global api_key
api_key = 'AIzaSyDj9q0fVRPfVBS7KM6NygzF_q_gOoE9nGI'
Globals.initialize()


def get_channel_ID(key_word):
    api = 'https://youtube.googleapis.com/youtube/v3/search'
    part = 'snippet'
    maxResults = '10'  # 設定搜尋結果數量
    q = key_word
    search_type = 'channel'  # 設定搜尋的東西是頻道
    key = api_key
    
    url = api + "?part=" + part + "&maxResults=" + maxResults + "&q=" + key_word + "&type=" + search_type + "&key=" + key
    print("cid:", url)
    ID = requests.get(url)
    ID_json = ID.json()

    # ID_1 = ID_json['items'][0]['snippet']['channelId'] #頻道ID
    # name_1 = ID_json['items'][0]['snippet']['title']   #頻道名稱

    # 頻道id:name 存成dict
    for i in range(len(ID_json['items'])):
        # Globals.id_list.append(ID_json['items'][i]['snippet']['channelId'])
        # Globals.name_list.append(ID_json['items'][i]['snippet']['title'])
        Globals.channels_dict[ID_json['items'][i]['snippet']
                              ['channelId']] = ID_json['items'][i]['snippet']['title']


# 得到youtube api 回傳的 json 格式檔案
# key 記得要換自己的
def get_channel_info(channel_id):

    api = "https://www.googleapis.com/youtube/v3/channels"
    part = "snippet,contentDetails,statistics,brandingSettings"
    id_ = channel_id
    # remember to change this key
    key = api_key

    url = api + "?part=" + part + "&id=" + id_ + "&key=" + key
    info = requests.get(url)
    info_json = info.json()

    return info_json

# 參數: youtube api 回傳的 json 檔案


def get_id(info_json):
    channel_id = info_json['items'][0]['id']  # 頻道ID
    return channel_id


def get_name(info_json):
    channel_name = info_json['items'][0]['snippet']['title']  # 頻道名稱
    return channel_name

# 取得頻道簡介


def get_description(info_json):
    # 頻道描述
    channel_description = info_json['items'][0]['snippet']['description']
    return channel_description

# 取得頻設立時間


def get_published_time(info_json):
    # 頻道開始時間
    channel_published_time = info_json['items'][0]['snippet']['publishedAt']
    return channel_published_time

# 取得頻道個人圖片


def get_profile_pic(info_json, size): # size: default, medium,high
    # 得到數據
    # default, medium & high #頻道主圖
    profile_pic_raw = info_json['items'][0]['snippet']['thumbnails'][size]
    # 清理一下數據
    pattern = "https://yt3.ggpht.com/" + "(.*?)" + "no-rj"
    profile_pic = re.search(pattern, str(profile_pic_raw))

    # return profile_pic[0]

    # 下載圖片
    folder = 'channels'
    if os.path.exists(folder) == False:
        os.mkdir(folder)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }

    # 開始抓圖片

    url = profile_pic[0]

    try:

        picture = requests.get(url, headers=headers)  # 下載圖片
        picture.raise_for_status()                  # 驗證圖片是否下載成功
        # 先開啟檔案, 再儲存圖片
        pictFile = open(os.path.join(
            folder, Globals.id + '_profile.jpg'), 'wb')

        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()
        return "connect successed"
    except Exception as err:
        print(err)
        return "connect failed"


# 取得頻道總觀看數
def get_viewCount(info_json):
    # 觀看總數
    channel_viewCount = info_json['items'][0]['statistics']['viewCount']
    return channel_viewCount

# 取得頻道訂閱數


def get_subscriberCount(info_json):
    # 訂閱數

    if info_json['items'][0]['statistics']['hiddenSubscriberCount']  == True:
        channel_subscriberCount = 'Hide'
    else:
        channel_subscriberCount = info_json['items'][0]['statistics']['subscriberCount']
    return channel_subscriberCount

# 取得頻道影片總數


def get_videoCount(info_json):
    # 影片數
    channel_videoCount = info_json['items'][0]['statistics']['videoCount']
    return channel_videoCount

# 取得頻道國家所在


def get_country(info_json):
    channel_country = info_json['items'][0]['snippet']['country']  # 頻道註冊地(國家)
    return channel_country


# 下面是取得banner的方法
# 使用說明
# 首先須要使用 getHtmlFile方法得到頻道的html頁面後(作為後續解析用)
# 之後使用 getBanner()方法藉由得到的html頁面, 解析出我要的圖片位址


def getHtmlFile(channel_ID):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }

    url = 'https://www.youtube.com/channel/' + channel_ID

    try:

        html = requests.get(url, headers=headers)
        html.raise_for_status()            # 驗證網頁是否下載成功
    except Exception as err:
        print("網頁下載失敗, Error = ", err)

    htmlFile = html.text
    global banner_id
    banner_id = channel_ID
    return htmlFile


def getBanner(htmlFile):
    YOUTUBE_HEADER_IMAGE_START_URL = "yt3.ggpht.com/"
    YOUTUBE_HEADER_IMAGE_END_URL = "-no-nd-rj"
    # 使用正規表達式
    regex = re.compile(YOUTUBE_HEADER_IMAGE_START_URL +
                       "(.*?)" + YOUTUBE_HEADER_IMAGE_END_URL)
    urllist = regex.findall(htmlFile)
    # urlist回傳的是一個含有16個value的串列
    # index 0 => 我不要的東西
    # 1 - 15的照片大小分別為
    # 1: 1138 x 188   2: 1707 x 282    3: 2120 x 350
    # 4: 2276 x 376   5: 2560 x 423    6: 320 x 180
    # 7: 854 x 480    8: 1280 x 720    9: 1920 x 1080
    # 10:2120 x 1192  11:320 x 52     12: 640 x 105
    # 13:960 x 158    14:1280 x 211   15: 1440 x 238
    try:
        url = "https://" + YOUTUBE_HEADER_IMAGE_START_URL + \
            urllist[12] + YOUTUBE_HEADER_IMAGE_END_URL
    except:
        print("this channel no banners")
    # 下載圖片
    folder = 'channels'
    if os.path.exists(folder) == False:
        os.mkdir(folder)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }

    # 開始抓圖片

    try:

        picture = requests.get(url, headers=headers)  # 下載圖片
        picture.raise_for_status()                  # 驗證圖片是否下載成功
        # 先開啟檔案, 再儲存圖片
        pictFile = open(os.path.join(folder, banner_id + '_banner.jpg'), 'wb')

        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()

        return "connect successed"
    except Exception as err:
        print(err)
        return "connect failed"

def get_all_for_single(channel_id):
    channel_info = get_channel_info(channel_id)
    subs = get_subscriberCount(channel_info)  # 選取頻道的訂閱數
    desc = get_description(channel_info)
    get_profile_pic(channel_info, 'medium')
    htmlFile = getHtmlFile(channel_id)
    getBanner(htmlFile)

    return channel_id, subs, desc


def get_all_for_plural(channel_id):
    channel_info = get_channel_info(channel_id)
    subs = get_subscriberCount(channel_info)  # 選取頻道的訂閱數
    view_count = get_viewCount(channel_info)
    video_count = get_videoCount(channel_info)
    get_profile_pic(channel_info, 'default')
    htmlFile = getHtmlFile(channel_id)
    getBanner(htmlFile)

    return channel_id, subs, view_count, video_count


'''
# 實際使用看看
# 先輸入關鍵字取得第一個搜尋結果的頻道id
# 先得到 channel資訊, 得到的是json格式的檔案,給值 info
# 之後會需要info作為參數, 得到channel的個別資訊

channel_id = get_channel_ID("mori Calliope") #輸入mori colliope得到的第一個搜尋結果


info = get_channel_info(channel_id)

print("name:", get_name(info))
print("des:", get_description(info))
print("Channel published time:", get_published_time(info))
print("Profile picture:", get_profile_pic(info))
print("Views:", get_viewCount(info))
print("Subscribers:", get_subscriberCount(info))
print("Videos:", get_videoCount(info))
print("Country:", get_country(info))



# 得到banner, 我需要channel ID 去爬取該ID的html頁面

# 取得html頁面
htmlFile = getHtmlFile(channel_id)

# 從html頁面找出banner的所在
banner = getBanner(htmlFile)

print("banner",banner)

'''
