from .models import Category,Article,models,Tag


def get_main_context(request):
    
    categories = Category.objects.all()
    korishlar_boyicha=Article.objects.all().order_by("views")
    tags=Article.objects.all().order_by("?")
    treading_news=Article.objects.all().order_by("views")
    
    
    context={
          "categories":categories,
          "korishlar_boyicha":korishlar_boyicha,
          "tags":tags,
          "treading_news":treading_news
    }
    return context