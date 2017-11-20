from django.conf.urls import url


from .views import index, home_page_view, about_page_view, dashboard_page_view, analytics_page_view, futureworks_page_view

#the values are from views.py file definitions
urlpatterns = [
    url(r'^$', index),
    url(r'^index/', index),
    url(r'^home/',home_page_view),
    url(r'^about/', about_page_view),
    url(r'^dashboard/',dashboard_page_view, name='dashboard'),
    url(r'^analytics/',analytics_page_view, name='analytics'),
    url(r'^futureworks/',futureworks_page_view, name='futureworks'),


]
