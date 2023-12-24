from django import template

register = template.Library()

@register.filter
def youtube_embed_url(origin_url):
    base_url = "https://www.youtube.com/"
    embed_query = "embed/"
    import re # 함수 안에서 처리

    match = re.search(r'(?<=v=)[\w-]+', origin_url)

    if match:
        url_id = match.group(0)
        youtube_iframe = f"{base_url}{embed_query}{url_id}"
        return youtube_iframe
    
    return origin_url  # 유효하지 않은 URL 처리



# url 변환은 정규식 사용해서 처리할 것
# <iframe width="560" height="315" src="https://www.youtube.com/embed/4bO8H0qIyuE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# origin_url = "https://www.youtube.com/watch?v=4bO8H0qIyuE"
# base_url = "https://www.youtube.com/"
# embed_query = "embed/"
# url_id = "4bO8H0qIyuE"

# youtube_iframe = base_url + embed_query + url_id

# {{ youtube.youtube_link }}
# <iframe src="{{ origin_url|youtube_embed_url }}"></iframe>
# <iframe src="{{ youtube.youtube_link|youtube_embed_url }}"></iframe>






