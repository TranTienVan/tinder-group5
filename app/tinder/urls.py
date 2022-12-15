from django.urls import path, re_path
from tinder import views


urlpatterns = [
    re_path(r"^userliked$", views.MembersLikedAPI.as_view(), name="user_like_another_user"),
    re_path(r"^userliked/([0-9]+)/([0-9]+)$", views.MembersLikedAPI.as_view(), name="user_unlike_another_user"),
    re_path(r"^userliked/([0-9]+)$", views.MembersLikedAPI.as_view(), name="get_all_whose_user_liked"),
    
    
    re_path(r"^likeduser/([0-9]+)$", views.LikedMembersAPI.as_view()),
    
    
    re_path(r"^usernomatch$", views.NoMatchAPI.as_view(), name="user_nomatch_another_user"),
    re_path(r"^usernomatch/([0-9]+)/([0-9]+)$", views.NoMatchAPI.as_view(), name="user_unnomatch_another_user"),
    
    re_path(r"^usersuperlike$", views.SuperLikeAPI.as_view(), name="user_superlike_another_user"),
    re_path(r"^usersuperlike/([0-9]+)/([0-9]+)$", views.SuperLikeAPI.as_view(), name="user_unsuperlike_another_user"),
    
    
    re_path(r"^userblock$", views.BlockAPI.as_view(), name="user_block_another_user"),
    re_path(r"^userblock/([0-9]+)/([0-9]+)$", views.BlockAPI.as_view(), name="user_unblock_another_user"),
    
    
    re_path(r"^chat$", views.ChatAPI.as_view(), name="user_chat_another_user"),
    re_path(r"^chat/([0-9]+)$", views.ChatAPI.as_view(), name="user_delete_message")
]
