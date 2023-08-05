import usb.core

def list_devices():
    devices = usb.core.find(find_all=True)
    for device in devices:
        print(f'Device: {device}, idVendor: {hex(device.idVendor)}, idProduct: {hex(device.idProduct)}')

if __name__ == '__main__':
    list_devices()

