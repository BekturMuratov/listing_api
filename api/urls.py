from django.urls import path
from api.views import category_views, place_views, reviews_views, tags_views, events_views, job_views


urlpatterns = [
    path('category/create_category', category_views.CreateCategoryView.as_view()),
    path('category/delete_category_by_id/<int:pk>/', category_views.DeleteCategoryByIdView.as_view()),
    path('category/update_category_by_id/<int:pk>/', category_views.UpdateCategoryByIdView.as_view()),
    path('category/find_all_categories/', category_views.GetCategoryView.as_view()),
    path('category/find_category_by_id/<int:pl>/', category_views.FindCategoryByIdView.as_view()),

    path('place/create_place', place_views.CreatePlaceView.as_view()),
    path('place/delete_place_by_id/<int:pk>/', place_views.DeletePlaceByIdView.as_view()),
    path('place/update_place_by_id/<int:pk>/', place_views.UpdatePlaceByIdView.as_view()),
    path('place/get_all_places/', place_views.GetPlaceView.as_view()),
    path('place/get_place_by_id/<int:pk>/', place_views.FindPlaceByIdView.as_view()),

    path('event/create_event', events_views.CreateEventView.as_view()),
    path('event/delete_event_by_id/<int:pk>/', events_views.DeleteEventByIdView.as_view()),
    path('event/update_event_by_id/<int:pk>/',events_views.UpdateEventByIdView.as_view()),
    path('event/get_all_events/', events_views.GetEventView.as_view()),
    path('event/get_event_by_id/', events_views.FindEventByIdView.as_view()),

    path('job/create_job',job_views.CreateJobView.as_view()),
    path('job/delete_job_by_id/<int:pk>/',job_views.DeleteJobByIdView.as_view()),
    path('job/update_job_by_id/<int:pk>/',job_views.UpdateJobByIdView.as_view()),
    path('job/get_all_jobs/', job_views.GetJobView.as_view()),
    path('job/get_job_by_id/<int:pk>',job_views.FindJobByIdView.as_view()),



    path('reviews/create_review', reviews_views.CreateReviewsViews.as_view()),
    path('reviews/delete_review_by_id/<int:pk>/', reviews_views.DeleteReviewViews.as_view()),
    path('reviews/update_review_by_id/<int:pk>/', reviews_views.UpdateReviewViews.as_view()),
    path('reviews/get_all_reviews/', reviews_views.GetReviewViews.as_view()),

    path('tags/create_tag', tags_views.CreateTagView.as_view()),
    path('tags/delete_tag_by_id/<int:pk>', tags_views.DeleteTagByIdView.as_view()),
    path('tags/update_tag_by_id/<int:pk>', tags_views.UpdateTagByIdView.as_view()),
    path('tags/get_all_tags/', tags_views.GetTagView.as_view()),
]