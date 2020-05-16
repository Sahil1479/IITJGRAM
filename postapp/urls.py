from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('post/',views.post, name="post"),
    path('postlink/',views.postlink, name="postlink"),
    path('postvideo/',views.postvideo, name="postvideo"),
    path('postdocument/',views.postdocument, name="postdocument"),
    path('editprofile/',views.editprofile, name="editprofile"),
    # view post 
    path('viewimages/',views.viewimages, name="viewimages"),
    path('viewlinks/',views.viewlinks, name="viewlinks"),
    path('viewvideos/',views.viewvideos, name="viewvideos"),
    path('viewdocuments/',views.viewdocuments, name="viewdocuments"),
    ##
    path('comment/<int:post_id>/',views.comment, name="comment"),
    #path('viewprofile1/',views.viewprofile1, name="viewprofile1"),
    path('viewprofile/',views.viewprofile, name="viewprofile"),
    path('viewprofile1/<int:person_id>/',views.viewprofile1, name="viewprofile1"),
    
    path('delete_post/<postid>',views.delete_post, name="delete_post"),
    path('delete_postlink/<int:postid1>/',views.delete_postlink, name="delete_postlink"),
    path('delete_postvideo/<int:postid2>/',views.delete_postvideo, name="delete_postvideo"),
    path('delete_postdocument/<int:postid2>/',views.delete_postdocument, name="delete_postdocument"),
    path('',views.home, name="home"),

    #like
    

]