from django.shortcuts import render
from django.db.models import Max
from django.views import View
from django.core import serializers
import requests
import random
from .models import Quote, Author

# Create your views here.

class GameView(View):    
    
    quote_url = 'https://www.scalablepath.com/api/test/test-quotes'
    authors_url = 'https://www.scalablepath.com/api/test/test-authors'
    
    def get(self, request, *args, **kwargs):
        try:
            quotes = requests.get(self.quote_url)
            authors = requests.get(self. authors_url)
            quotes.raise_for_status()
            authors.raise_for_status()            
            for author in authors.json():
                Author.objects.get_or_create(            
                id = author['id'],    
                name = author['name']      
            )              
            for quote in quotes.json():            
                Quote.objects.get_or_create(
                    name = quote['quote'],
                    author_id = Author.objects.get(pk=quote['author_id']
                )       
            )                                 
            quote_info = self.select_random_quote()        
            authors_q = Author.objects.all()[:3] 
            authors_info = serializers.serialize('json',authors_q) 
            print(authors_info)     
            return render(request, 'index.html',{'Quote': quote_info, 'authors': authors_info}) 
        except Exception as e:
            return render(request, 'index.html', {'error':e})
        
    def select_random_quote(self):
        max_id = Quote.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            quote = Quote.objects.filter(pk=pk).first()
            if quote:
                return quote
        
    