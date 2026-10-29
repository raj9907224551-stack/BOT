ZYVO PAY gateway (admin UI still labelled PayTM)

1. In Telegram Admin > Payment Gateways > PayTM Gateway, enter the UPI ID you have configured with your merchant and paste the COMPLETE ZYVO PAY API token exactly as shown by the dashboard (public.secret).
2. Tap Check PayTM Connection. When accepted, switch PayTM System ON. FamPay remains a separate gateway.
3. The bot sends signed requests to https://zyvopay.site/api/create-payment.php and /check-payment.php. The API token stays in the bot's server-side SQLite gateway credential field and is never returned in the UI. Do not paste it into public chats or logs.
4. ZYVO PAY owns merchant/provider configuration. The bot does not construct a UPI URI from the configured UPI ID; it renders the exact payment_uri returned by create-payment, or uses the provider qr_image_url unchanged.
5. The status check verifies status=successful, reference, order_id, INR currency and exact amount before returning a paid result to the existing delivery flow.

Environment:
- Optional ZYVOPAY_BASE_URL=https://zyvopay.site/api (HTTPS in production)
- .env.example is a safe placeholder. The token is entered via the admin UI, not committed in this file.

Offline checks:
  python -m py_compile main.py
  python -m unittest test_zyvopay_signature.py

The tests above do not contact ZYVO PAY and do not create live payments. Before production, test with a provider test account, confirm the merchant dashboard token is active, verify API access, and make a low-value controlled payment. Never treat a screenshot, redirect, or public status result as proof of payment.
