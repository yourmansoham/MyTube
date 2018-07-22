from django.urls import path
from . import views

urlpatterns = [
	path("<video_id>",views.showVideo,name="showVideo"),
	path("create/video",views.createVideo,name="createVideo"),
	path("create/comment/<video_id>",views.createComment,name="createComment"),
	path("edit/<video_id>",views.editVideo,name="editVideo"),
	path("delete/<video_id>",views.deleteVideo,name="deleteVideo"),
	path("delete/comment/<comment_id>",views.deleteComment,name="deleteComment"),
	path("<type_>/video/<video_id>",views.likeVideo,name="likeVideo"),
	path("<type_>/comment/<comment_id>",views.likeComment,name="likeComment"),
]
