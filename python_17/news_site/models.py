from django.db import models



# Create your models here.
# class Article(models.Model):
#     title = models.CharField()
#     body = models.CharField()
#     author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="articles")

# class Author(models.Model):
#     name = models.CharField()
#     surname = models.CharField()


# author_1 = Author(name="James", surname="Bond")
# article_1 = Article(title="New article", body="some text", author=author_1)
# author_1.articles.get()

class Article(models.Model):
    title = models.CharField()
    body = models.CharField()
    authors = models.ManyToManyField("Author", related_name="articles")

class Author(models.Model):
    name = models.CharField()
    surname = models.CharField()


author_1 = Author(name="James", surname="Bond")
article_2 = Article(title="New article", body="some text", author=author_1)
article_3 = Article(title="New article", body="some text", author=author_1)

# читання
Article.objects.all()
Article.objects.get(title="new article")
Article.objects.get(pk=4)
Article.objects.get(id=4)
Article.objects.filter(title__contains="text")
Article.objects.filter(title__icontains="text")
Article.objects.filter(title__lt="text")
Article.objects.filter(title__gt="text")
Article.objects.filter(title__gte="text")
Article.objects.filter(title__lte="text")
Article.objects.filter(title__exact="text")
Article.objects.filter(title__iexact="text")
Article.objects.filter(title__startswith="text")
Article.objects.filter(title__endswith="text")
Article.objects.exclude(title__endswith="something")

a = Article.objects.get().filter(title__endswith="today").exlude(id=15).filter(author_contains="")
for a in article_2:
    pass

# створення
author_1 = Author(name="James", surname="Bond")
author_1.save()

# видалення
article_3 = Article.objects.get(id=4)
article_3.delete()

# зміна
article_3 = Article.objects.get(id=4)
article_3.title = "Second title"
article_3.save()

Article.objects.all()[:10]
Article.objects.all()[11:20]
Article.objects.all()[50:100:2]

### Search
Article.objects.filter(title__contains="text")
Article.objects.filter(title__icontains="text")

from django.contrib.postgres.search import SearchVector
Article.objects.annotate(search=SearchVector("title", "body"),).filter(search="Some title")
Article.objects.filter(body__search="search line")