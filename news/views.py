from django.shortcuts import render,get_object_or_404, redirect
from django.views import View
from .models import  Article, Tag 
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

class HomeView(View):
    def get(self,request):
        articles=Article.objects.all()
        main_news=articles[:7]
        featured_news=articles.order_by("?")[:10]
        lastest_news=articles.order_by("id")[:5]
        tag=Tag.objects.all()
        
        
        context={
            'tags':tag,
            "main_news":main_news,
            "featured_news":featured_news,
            "lastest_news":lastest_news,  
           
        }
        
        return render(request, "index.html", context)
    

class ArticleDetailView(View):
    def get(self, request, slug):
        
        article=get_object_or_404(Article, slug=slug)
        article.views += 1
        article.save()
        oxshash_yang=Article.objects.filter(category=article.category).exclude(slug=slug ).order_by("?")[:4]
        context={
            "article":article,
            "oxshash_yang":oxshash_yang
        }
        return render(request, "single.html", context)



class ContactView(View):
    form_class=ContactForm
    
    def get(self, request):
    
        return render(request, 'contact.html')

    def post(self, request):
        data=request.POST
        form=self.form_class()
        if form.is_valid():
            form.save()
            
            messages.success(request, "Xabaringz yuboroldi! ")
            return redirect("contact")
        
        messages.error(request, "Nmdir xato ")
        return render(request, 'contact.html')
        
        



















