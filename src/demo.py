#!/bin/env python3

import nfc
import time

def connected(tag):
    print(f'Connected with {tag}')
    print('Tag ID (in hex):', tag.identifier.encode("hex"))
    return True

def main():
    clf = nfc.ContactlessFrontend('usb')
    while True:
        print('Waiting for NFC card...')
        clf.connect(rdwr={'on-connect': connected})
        time.sleep(1)

if __name__ == '__main__':
    main()

