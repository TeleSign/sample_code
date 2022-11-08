from base64 import b64decode, b64encode
from hashlib import sha256
from hmac import HMAC
import hmac
def verify_telesign_postback(ts_api_key, http_headers, json_str):
    """Verify that a Callback request was made by Telesign, and was not sent by a malicious client.
    @param ts_api_key: the shared Telesign API Key used to make the original
    Telesign REST transaction, or it is the API Key for a specific product.
    @param http_headers: a dictionary of the HTTP POST Request headers,
    supplied by whatever HTTP request processing framework you use.
    @param json_str: the POST body text, that is, the JSON string sent by
    Telesign describing the transaction status.
    """
    sig1 = http_headers['X-TS-Authorization']
    mac = HMAC(b64decode(ts_api_key), json_str, sha256)
    sig2 = b64encode(mac.digest())
    # Use the supplied hmac.compare_digest function, if available on your platform.
    # @see:
    # https://docs.python.org/2/library/hmac.html#hmac.compare_digest
    if hasattr(hmac, 'compare_digest'):
        hmac.compare_digest(sig1, sig2)
    # Do char-by-char compare, and don't short-circuit the comparison.
    # @see:
    # http://codahale.com/a-lesson-in-timing-attacks/
    if len(sig1) != len(sig2):
        return False
    res = 0
    for i in range(0, len(sig1)):
        # NOTE: every char in Base64 is ASCII-compatible, hence the
        # call to ord()
        res |= (ord(sig1[i]) ^ ord(sig2[i]))
    return res == 0
