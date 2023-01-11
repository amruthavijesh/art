from django.urls import path
from artadmin import views
app_name='artadmin'
urlpatterns=[
    # path('mail',views.mail,name='mail'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('gallerry',views.gallerry,name='gallerry'),
    path('caricature',views.caricature,name='caricature'),
    path('graphic',views.graphic,name='graphic'),
    path('illustration',views.illustration,name='illustration'),
    path('portrait',views.portrait,name='portrait'), 
    # path('contactus',views.contactus,name='contactus'), 
    path('viewcontactus',views.viewcontactus,name='viewcontactus'),
    path('contactdestroy/<int:id>',views.contactdestroy,name='contactdestroy'),
    path('viewcaricatures',views.viewcaricatures,name='viewcaricatures'),
    path('caricaturedestroy/<int:id>',views.caricaturedestroy,name='caricaturedestroy'),
    path('caricatureupdate/<int:id>',views.caricatureupdate,name='caricatureupdate'),
    path('viewportraits',views.viewportraits,name='viewportraits'),
    path('portraitdestroy/<int:id>',views.portraitdestroy,name='portraitdestroy'),
    path('portraitupdate/<int:id>',views.portraitupdate,name='portraitupdate'),
    path('viewgraphics',views.viewgraphics,name='viewgraphics'),
    path('graphicdestroy/<int:id>',views.graphicdestroy,name='graphicdestroy'),
    path('graphicupdate/<int:id>',views.graphicupdate,name='graphicupdate'),
    path('viewillustrations',views.viewillustrations,name='viewillustrations'),
    path('illustrationdestroy/<int:id>',views.illustrationdestroy,name='illustrationdestroy'),
    path('illustrationupdate/<int:id>',views.illustrationupdate,name='illustrationupdate'),
]