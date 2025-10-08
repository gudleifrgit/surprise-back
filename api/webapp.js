export default function handler(req, res) {
  // CORS preflight
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
    res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    return res.status(204).end();
  }

  console.log("=== WEBAPP REQUEST ===", req.body);
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.status(200).json({ ok: true, received: req.body || null });
}
