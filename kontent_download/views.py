
from django.shortcuts import render
import requests


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        data = intagram_(url)
        return render(request, 'index.html', {'data': data})
    return render(request, 'index.html')





def intagram_(url):
    response = requests.get("https://videoyukla.uz/instagram/media/", params={"in_url": url})
    print(response.status_code)
    try:
        if response.status_code == 200:
            data = response.json()
            print(data, "DATA")
            if data.get("error") is False:
                medias = data.get("medias", [])
                if len(medias) == 1:
                    media = medias[0]
                    return {
                        "media_type": "one",
                        "type": media["type"],
                        "download_url": media["download_url"],
                        "thumb": media["thumb"],
                    }
                elif len(medias) > 1:
                    result = []
                    for media in medias:
                        result.append({
                            "type": media["type"],
                            "download_url": media["download_url"],
                            "thumb": media["thumb"],
                        })
                    return {
                        "media_type": "multiple",
                        "items": result
                    }
    except Exception as e:
        return {"success": False, "message": str(e)}

