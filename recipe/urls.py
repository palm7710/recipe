from django.urls import path

from recipe.views import RecipeDetailView, RecipeListView  # === 編集 ===

app_name = "recipe"

urlpatterns = [
    path('', RecipeListView.as_view(), name="index"),
    path('<int:pk>', RecipeDetailView.as_view(), name="detail"),
]
