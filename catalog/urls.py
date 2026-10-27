from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("consultation/", views.consultation_view, name="consultation"),

    path("flowers/", views.FlowerListView.as_view(), name="flower_list"),
    path("flowers/<int:pk>/", views.FlowerDetailView.as_view(), name="flower_detail"),
    path("flowers/create/", views.FlowerCreateView.as_view(), name="flower_create"),
    path("flowers/<int:pk>/edit/", views.FlowerUpdateView.as_view(), name="flower_update"),
    path("flowers/<int:pk>/delete/", views.FlowerDeleteView.as_view(), name="flower_delete"),
    path("flowers/<int:pk>/favorite/", views.toggle_favorite_view, name="toggle_favorite"),

    path("care-guides/", views.CareGuideListView.as_view(), name="care_guide_list"),
    path("care-guides/<int:pk>/", views.CareGuideDetailView.as_view(), name="care_guide_detail"),
    path("care-guides/create/<int:flower_pk>/", views.CareGuideCreateView.as_view(), name="care_guide_create"),

    path("occasions/", views.OccasionListView.as_view(), name="occasion_list"),
    path("occasions/<slug:slug>/", views.OccasionDetailView.as_view(), name="occasion_detail"),
    path("category/<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),

    path("favorites/", views.FavoritesListView.as_view(), name="favorites_list"),
    path("florist-dashboard/", views.FloristDashboardView.as_view(), name="florist_dashboard"),

    path("register/", views.register_view, name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="catalog:home"), name="logout"),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="catalog/auth/password_change.html",
            success_url=reverse_lazy("catalog:password_change_done")
        ),
        name="password_change"
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="catalog/auth/password_change_done.html"
        ),
        name="password_change_done"
    ),
]
