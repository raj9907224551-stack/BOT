"""Offline unit checks for the ZYVO PAY signing contract. No network/payment calls."""
import hashlib
import hmac
import json
import unittest


def sign(secret, timestamp, raw_body):
    return hmac.new(secret.encode('utf-8'), (str(timestamp) + '.' + raw_body).encode('utf-8'), hashlib.sha256).hexdigest()


class ZyvoPaySignatureTests(unittest.TestCase):
    def test_exact_compact_json_bytes_and_lowercase_hex(self):
        raw = json.dumps({'order_id': 'ORDER_1042', 'amount': 2499, 'description': 'Annual subscription'}, ensure_ascii=False, separators=(',', ':'))
        expected = hmac.new(b'secret', ('1700000000.' + raw).encode('utf-8'), hashlib.sha256).hexdigest()
        actual = sign('secret', 1700000000, raw)
        self.assertEqual(actual, expected)
        self.assertEqual(actual, actual.lower())
        self.assertEqual(len(actual), 64)

    def test_whitespace_change_changes_signature(self):
        a = sign('secret', '1700000000', '{"amount":1}')
        b = sign('secret', '1700000000', '{ "amount": 1 }')
        self.assertNotEqual(a, b)

    def test_signed_get_empty_body(self):
        self.assertEqual(sign('secret', '1700000000', ''), hmac.new(b'secret', b'1700000000.', hashlib.sha256).hexdigest())


if __name__ == '__main__':
    unittest.main()
