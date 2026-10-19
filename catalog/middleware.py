import time


class ThemeAndTimingMiddleware:
    """
    Власний Middleware (Д7):
    1. Забезпечує збереження та обробку вибору теми оформлення (світла / темна з рожевим акцентом).
    2. Вимірює час виконання запиту до сервера та додає заголовок X-Response-Time-ms.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Тема оформлення: пріоритет - параметр запиту (?theme=light/dark), далі cookie, за замовчуванням 'light'
        theme_param = request.GET.get("theme")
        if theme_param in ["light", "dark"]:
            request.theme = theme_param
        else:
            request.theme = request.COOKIES.get("florist_theme", "light")

        response = self.get_response(request)

        # Якщо параметр теми був переданий у GET, зберігаємо у cookie на 30 днів
        if theme_param in ["light", "dark"]:
            response.set_cookie("florist_theme", theme_param, max_age=30 * 24 * 3600, samesite="Lax")

        duration_ms = int((time.time() - start_time) * 1000)
        response["X-Response-Time-ms"] = str(duration_ms)

        return response
