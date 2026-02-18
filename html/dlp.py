from yt_dlp import YoutubeDL
import subprocess
import sys
import os
from datetime import datetime
import json

def capture(name,url):
    ydl_opts = {
        'format':'best',
        'skip_download':True,
        'quiet':True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
    if not os.path.isdir('./img/'+name): os.mkdir('./img/'+name)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    save = './img/'+name+'/'+name+now+'.jpg'
    result = subprocess.run(['ffmpeg','-i',info['url'],'-ss','0','-vframes','1','-y',save],capture_output=True, text=True)

    pics = [ f for f in os.listdir('./img/'+name+'/')]
    with open("./json/"+name+".json", "w") as f: json.dump(pics, f)

dic = {
    #url
    "shichimen":"https://www.youtube.com/watch?v=54NpKx_efis",
    "kitayatsu":"https://www.youtube.com/watch?v=_2LD45D2-cQ",
    "narakongo":"https://www.youtube.com/watch?v=8ir0mYl8Fpo",
    "tateshinako":"https://www.youtube.com/watch?v=sNMeuMIHbxY",
    "hakodatesan":"https://www.youtube.com/watch?v=s--MDmshT3I",
    "utsukushigahara":"https://www.youtube.com/watch?v=68jI13YUms0",
    "southalpgeopark":"https://www.youtube.com/watch?v=P6ODN2GXIgw",
    "asosan":"https://www.youtube.com/watch?v=aVGYOlIzV0A",
    "sakurajima":"https://www.youtube.com/watch?v=NfR1Y-mYEtg",
}

if(__name__ == "__main__"):
    
    for name, url in dic.items():
        capture(name, url)
