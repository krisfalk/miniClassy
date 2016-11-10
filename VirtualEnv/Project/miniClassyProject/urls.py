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
    url(r'^product/', include('Product.ProductUrls'), name='products'),
    url(r'^fabric/', include('Fabric.FabricUrls'), name='fabrics'),
    url(r'^address/', include('Address.AddressUrls'), name='address'),
    url(r'^collaborator/', include('Collaborator.CollaboratorUrls'), name='collaborator'),
    url(r'^customer/', include('Customer.CustomerUrls'), name='customer'),
    url(r'^labeltag/', include('LabelTag.LabelTagUrls'), name='labeltag'),
    url(r'^logentry/', include('LogEntry.LogEntryUrls'), name='logentry'),
    url(r'^order/', include('Order.OrderUrls'), name='order'),
    url(r'^patternpiece/', include('PatternPiece.PatternPieceUrls'), name='patternpiece'),
    url(r'^season/', include('Season.SeasonUrls'), name='season'),
    url(r'^size/', include('Size.SizeUrls'), name='size'),
    url(r'^variation/', include('Variation.VariationUrls'), name='fabrics'),

]

