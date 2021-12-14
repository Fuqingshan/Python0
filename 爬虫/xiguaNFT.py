
from requests import get
from requests import post
import json
import requests
import sys
import threading
import time
from requests_toolbelt import MultipartEncoder


videoDir = "{}/TempVideo".format(sys.path[0])
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweEI5Mzg4OTNCMEUwMTBFZjlhQjg4OTQ3NkE2OGFhNDM2NUYyQUY1M2QiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTYyNjE2Nzc4MTQ4NCwibmFtZSI6Inpob3UifQ.DmcMUVvU11SbKdakWPC7G4Ym56qVtjB_qWXAuel_V3Q"
xlToken = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQ2MzA0MTE1NzExNTQxNjU3NiJ9.p5XCALKQB5_HYMeDF6xhf4JdhLUd4_k5H5oXLhhi3hM"
videoPageCount = 0
isLoading = False
allSize = 0
start = time.time()

def fetchData():
    global isLoading
    if isLoading:
        return
    url = "https://api3-normal-c-lf.ixigua.com/video/app/stream/v51/?fp=a_fake_fp&version_code=8.3.6&tma_jssdk_version=1.29.1.1&app_name=video_article&vid=33712FC5-60C0-4CD0-94D8-6CBCB855EB8A&device_id=47130886721&channel=App%20Store&resolution=1242*2208&aid=32&ab_version=668856,2947189,668855,2947158,668854,994679,2914861,2947179,2948708,668853,2947185,668852,2947154,668851,2947207,668858,2947137,668859,2947190&ab_feature=z2&ab_group=z2&update_version_code=8.3.6.7&openudid=76087f07e1e875360e55921ec50c4b08dcc4ded3&cdid=DC0EC5B2-6B34-4FC4-BF64-375E200AC71B&idfv=33712FC5-60C0-4CD0-94D8-6CBCB855EB8A&ac=WIFI&os_version=14.5&user_version=4.3.6&ssmix=a&device_platform=iphone&anti_addiction_model=0&iid=1248647498174024&device_type=iPhone%206S%20Plus&ab_client=a1,f2,f7,e1&idfa=00000000-0000-0000-0000-000000000000&detail=1&category=xg_hotsoon_video&strict=0&min_behot_time=1626763716&count=20&image=1&tt_from=pull&list_entrance=main_tab&refer=1&cp=6502F8677520Fq1"
    isLoading = True
    result = get(url)
    videoList = []
    if result.status_code == 200:
        jsonObject = result.json()
        if jsonObject["message"] == "success":
            dataList = jsonObject["data"]
            if type(dataList) is list:
                for data in dataList:
                    videoItem = {}
                    if type(data) is dict:
                        content = data["content"]
                        if type(content) is str:
                            data = json.loads(content)
                            rawData = data["raw_data"]
                            if type(rawData) is dict:
                                thumbniles = rawData["thumb_image_list"]
                                if type(thumbniles) is list and len(thumbniles) > 0:
                                    thumbnile = thumbniles[0]
                                    if type(thumbnile) is dict:
                                        videoItem["thumb"] = thumbnile["url"]
                                video = rawData["video"]
                                if type(video) is dict:
                                    playAddrList = video["play_addr_list"]
                                    videoItem["width"] = str(video["width"])
                                    videoItem["height"] = str(video["height"])
                                    videoItem["size"] = video["size"]
                                    videoItem["duration"] = int(video["duration"])
                                    if type(playAddrList) is list and len(playAddrList) > 0:
                                        playAddrDict = playAddrList[0]
                                        if type(playAddrDict) is dict:
                                            playUrlList = playAddrDict["play_url_list"]
                                            if type(playUrlList) is list and len(playUrlList) > 0:
                                                playURL = playUrlList[0]
                                                if type(playURL) is str:
                                                    videoItem["videoURL"] = playURL
                                                    videoList.append(videoItem)
    isLoading = False
    download(videoList)


def download(videoList):
    # if not os.path.exists(videoDir):
    #     os.mkdir(videoDir)
    global videoPageCount
    videoPageCount += len(videoList)
    if len(videoList) > 0:
        threads = []
        for item in videoList:
            name = "upload_{}".format(time.time() * 1000)
            t = threading.Thread(name=name, target=upload, args=(item,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    else:
        fetchData()
        # t.join()
        # upload(item)


def upload(item):
    videoCids = getCid(item["videoURL"])
    thumbCids = getCid(item["thumb"])
    name = base36_encode(int(time.time() * 1000)) + ".mp4"
    parameters = {"thumbnail": thumbCids["cid"], "fileName": name, "fileCid": videoCids["cid"], "fileSize": videoCids["size"], "fileType": 3, "transferType": 1, "parentId": "0", "uploadParentId": "0", "width": item["width"], "height": item["height"], "duration": item["duration"], "token": xlToken}
    xlURL = "http://productapi.stariverpan.com/cmsprovider/v1.2/cloud/addFile"
    xlSize = "http://productapi.stariverpan.com/cmsprovider/v1/stat/userFile"
    totalSize = videoCids["size"]+thumbCids["size"]
    global allSize
    allSize += totalSize
    sizeParam = {"size":totalSize}
    proxies = {
        # "http": "http://127.0.0.1:8888",
    }

    r2 = post(url=xlURL, data=json.dumps(parameters), proxies=proxies, headers={"Authorization": xlToken, 'Content-Type': 'application/json'})
    r3 = post(url=xlSize, data=json.dumps(sizeParam), proxies=proxies, headers={"Authorization": xlToken, 'Content-Type': 'application/json'})
    print(r2)
    print(r3)
    print("{}....{}".format(item["size"],videoCids["size"]))
    unit = "GB" 
    num = allSize/1024.0/1024.0/1024.0
    if allSize < 1024*1024*1024:
        unit = "MB"
        num *= 1024.0
    print("")
    t = time.time() - start
    print("运行{:d}小时{:d}分{:d}秒, 总上传{:.2f}{}".format(int(t/3600),int(t%3600/60),int(t%60),num,unit))
    global videoPageCount
    videoPageCount -= 1
    if videoPageCount <= 0:
        fetchData()


def getCid(url):
    res = requests.get(url)
    if res.content is None:
        print("content空")
        return
    fileData = MultipartEncoder(fields={'file': res.content})
    proxies = {
        # "http": "http://127.0.0.1:8888",
    }
    url = "http://bsserver03.stariverpan.com:9094/add?cid-version=1&replication-min=1&replication-max=1"
    r1 = post(url=url, proxies=proxies, data=fileData, headers={"Authorization": token, 'Content-Type': fileData.content_type}).json()
    try:
        cid = r1["cid"]["/"]
        size = r1["size"] = r1["size"]
        print("{}---{}".format(cid, size))
        return {"cid": cid, "size": size}
    except ValueError:
        print("异常")
        return {}

def base36_encode(number):
    num_str = '0123456789abcdefghijklmnopqrstuvwxyz'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)    # 返回 number// 36 , number%36
        base36.append(num_str[i])
    return ''.join(reversed(base36))


fetchData()
