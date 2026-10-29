# RG protected runtime loader
# The application source is stored only in main.enc.
from pathlib import Path
import gzip
from cryptography.fernet import Fernet

_RUNTIME_KEY = b'dVPFx12M2yewejxvAxDuUCKoYxQ6xGShCb9mQbu1Mkc='

_BASE_DIR = Path(__file__).resolve().parent
_PAYLOAD = _BASE_DIR / 'main.enc'

if not _PAYLOAD.exists():
    raise RuntimeError('Protected payload main.enc is missing.')

_source = gzip.decompress(Fernet(_RUNTIME_KEY).decrypt(_PAYLOAD.read_bytes()))
_code = compile(_source, str(_BASE_DIR / 'main.py'), 'exec')
exec(_code, globals(), globals())
