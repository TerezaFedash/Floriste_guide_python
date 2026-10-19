from django.contrib import admin
from catalog.models import Category, Occasion, Flower, CareGuide, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("icon_emoji", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ("name", "season", "badge_color", "slug")
    list_filter = ("season",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "in_stock",
        "difficulty_level",
        "owner",
        "created_at",
    )
    list_filter = (
        "category",
        "in_stock",
        "difficulty_level",
        "occasions",
        "created_at",
    )
    search_fields = ("name", "latin_name", "description")
    list_editable = ("price", "in_stock")
    filter_horizontal = ("occasions",)
    date_hierarchy = "created_at"


@admin.register(CareGuide)
class CareGuideAdmin(admin.ModelAdmin):
    list_display = (
        "flower",
        "watering_frequency_days",
        "temperature_range",
        "light_requirement",
        "humidity_level",
        "expert",
        "updated_at",
    )
    list_filter = ("light_requirement", "humidity_level")
    search_fields = ("flower__name", "stem_cutting_tips", "florist_secret")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "flower", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "flower__name")
