from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import News


def scrape(request):
    base_url = "https://thisdaylive.com/"
    page = requests.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")

    article_list = []

    for article in soup.find_all("article"):
        article_list.append(article)
        # print(article)
        # link = article.find("a")
        # link_address = base_url + link.get("href") if link else None
        # title = link.text.strip() if link else None

        import pdb; pdb.set_trace()

        

        image = article.find("img")
        image_url = image.get("src") if image else None

        # Only create a News object if all required data is available
        if link_address and title and image_url:
            News.objects.create(
                link_address=link_address, title=title, image_url=image_url
            )

    data = News.objects.all()

    context = {"data": data}

    return render(request, "myapp/home.html", context)
