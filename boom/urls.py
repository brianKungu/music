from django.urls import path
from . import views


app_name='boom'

urlpatterns=[
    path('login',views.signin, name='login'),
    path('logout_user',views.logout_user,name='logout-user'),
    path('signup',views.signup, name='signup'),
    path('', views.index, name='index'),
    path('(?P<album_id>[0-9]+)/' ,views.detail, name='info'),
    path('new-album',views.create_album, name='create-album'),
    path('<int:pk>/album-update', views.AlbumUpdateView.as_view(), name='album-update'),
    path('(?P<album_id>[0-9]+)/delete-album', views.album_delete, name='album-delete'),
    path('(?P<album_id>[0-9]+)/new-song',views.create_song, name='create-song'),
    path('<int:pk>/update-song', views.SongUpdateView.as_view(), name='update-song'),
    path('(?P<album_id>[0-9]+)/delete-song/((?P<song_id>[0-9]+)',views.delete_song, name='song-delete'),

]