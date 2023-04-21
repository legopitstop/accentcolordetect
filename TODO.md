# TODO
- Implement `listener` to all supported platforms.
```Python
import threading
import accentcolordetect

t = threading.Thread(target=accentcolordetect.listener, args=(print,))
t.daemon = True
t.start()
```