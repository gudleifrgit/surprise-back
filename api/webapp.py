def handler(request):
    if request.method == "OPTIONS":
        return "", 204, {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
        }
    data = request.get_json() or {}
    print("=== WEBAPP REQUEST ===", data)
    return {"ok": True, "received": data}, 200, {
        "Access-Control-Allow-Origin": "*"
    }
