"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include('App.Product.ProductUrls'), name='product'),
    url(r'^fabric/', include('App.Fabric.FabricUrls'), name='fabrics'),
    url(r'^address/', include('App.Address.AddressUrls'), name='address'),
    url(r'^collaborator/', include('App.Collaborator.CollaboratorUrls'), name='collaborator'),
    url(r'^collection/', include('App.Collection.CollectionUrls'), name='collection'),
    url(r'^customer/', include('App.Customer.CustomerUrls'), name='customer'),
    url(r'^labeltag/', include('App.LabelTag.LabelTagUrls'), name='labeltag'),
    url(r'^logentry/', include('App.LogEntry.LogEntryUrls'), name='logentry'),
    url(r'^notion/', include('App.Notion.NotionUrls'), name='notion'),
    url(r'^order/', include('App.Order.OrderUrls'), name='order'),
    url(r'^patternpiece/', include('App.PatternPiece.PatternPieceUrls'), name='patternpiece'),
    url(r'^season/', include('App.Season.SeasonUrls'), name='season'),
    url(r'^product/', include('App.Product.ProductUrls'), name='product'),
    url(r'^size/', include('App.Size.SizeUrls'), name='size'),
    url(r'^variation/', include('App.Variation.VariationUrls'), name='variation'),
    url(r'^style/', include('App.Style.StyleUrls'), name='style'),
    url(r'^notion/', include('App.Notion.NotionUrls'), name='notion'),
]
