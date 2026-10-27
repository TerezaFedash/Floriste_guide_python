from django import template
from django.utils.safestring import mark_safe
from catalog.models import Favorite

register = template.Library()


@register.simple_tag
def difficulty_badge(level):

    mapping = {
        "easy": ("badge-easy", "🌿 Легкий догляд"),
        "medium": ("badge-medium", "💧 Середня увага"),
        "hard": ("badge-hard", "✨ Вимоглива"),
    }
    css_class, label = mapping.get(level, ("badge-secondary", level))
    return mark_safe(f'<span class="badge {css_class} px-3 py-1 rounded-pill">{label}</span>')


@register.simple_tag
def is_in_favorites(flower, user):

    if not user or not user.is_authenticated:
        return False
    return Favorite.objects.filter(user=user, flower=flower).exists()


@register.inclusion_tag("catalog/includes/flower_card.html", takes_context=True)
def render_flower_card(context, flower):

    request = context.get("request")
    user = request.user if request else None
    in_fav = is_in_favorites(flower, user)
    return {
        "flower": flower,
        "user": user,
        "in_fav": in_fav,
        "request": request,
    }
