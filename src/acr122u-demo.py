import nfc
import time

def connected(tag):
    print(f'Connected with {tag}')

clf = nfc.ContactlessFrontend('usb')
while True:
    clf.connect(rdwr={'on-connect': connected})
    print("Waiting for card...")
    time.sleep(1)

