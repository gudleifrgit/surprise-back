# НЕ импортируй fastapi, flask и т.п.
# Должен быть ТОЛЬКО handler(request) -> (body, status, headers) ИЛИ dict

def handler(request):
    # CORS preflight
    if request.method == "OPTIONS":
        return "", 204, {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
        }

    # Чтение JSON безопасно
    try:
        data = request.get_json() or {}
    except Exception:
        data = {}

    print("=== WEBAPP REQUEST ===", data)

    return {"ok": True, "received": data}, 200, {
        "Access-Control-Allow-Origin": "*"
    }
