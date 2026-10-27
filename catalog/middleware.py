import time


class ThemeAndTimingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        
        theme_param = request.GET.get("theme")
        if theme_param in ["light", "dark"]:
            request.theme = theme_param
        else:
            request.theme = request.COOKIES.get("florist_theme", "light")

        response = self.get_response(request)

        if theme_param in ["light", "dark"]:
            response.set_cookie("florist_theme", theme_param, max_age=30 * 24 * 3600, samesite="Lax")

        duration_ms = int((time.time() - start_time) * 1000)
        response["X-Response-Time-ms"] = str(duration_ms)

        return response
