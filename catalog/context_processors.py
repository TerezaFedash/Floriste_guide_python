from catalog.models import Category


def florist_global_context(request):
    """
    Глобальний контекстний процесор для меню категорій та поточної теми.
    """
    theme = getattr(request, "theme", "light")
    try:
        nav_categories = Category.objects.all()[:8]
    except Exception:
        nav_categories = []

    return {
        "current_theme": theme,
        "nav_categories": nav_categories,
        "is_florist": request.user.is_authenticated and (
            request.user.is_staff or request.user.groups.filter(name="Флористи").exists()
        ),
    }
