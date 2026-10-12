import signal, time
from playwright.sync_api import sync_playwright

p = sync_playwright().start()
b = p.chromium.launch(headless=False, args=[
    '--no-sandbox', '--start-maximized', '--window-size=1920,1080',
    '--remote-debugging-port=9222', '--remote-allow-origins=*',
    '--disable-gpu', '--disable-dev-shm-usage'
])
print('Chromium ready on :9222', flush=True)

running = True
def shutdown(sig, frame):
    global running
    running = False
signal.signal(signal.SIGTERM, shutdown)

while running:
    time.sleep(1)

b.close()
p.stop()
