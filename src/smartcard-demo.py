from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

class NFCObserver(CardObserver):
    """ A card observer that is called when cards are inserted/removed from the system. """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            card.connection = card.createConnection()
            card.connection.connect()

            # assuming the data is in the DATA field
            response, sw1, sw2 = card.connection.transmit([0xFF, 0xCA, 0x00, 0x00, 0x00])
            if sw1 == 0x90:
                print("Card inserted: ", toHexString(response))
            else:
                print("Unable to read card.")

        for card in removedcards:
            print("Card removed")

if __name__ == '__main__':
    print("Insert or remove a smartcard in the system.")
    print("This program will exit in 10 seconds")
    print("")
    cardmonitor = CardMonitor()
    cardobserver = NFCObserver()
    cardmonitor.addObserver(cardobserver)

    import time
    time.sleep(10)

    # don't forget to remove observer, or the
    # monitor will poll forever...
    cardmonitor.deleteObserver(cardobserver)

    import sys
    if 'win32' == sys.platform:
        print('press Enter to continue')
        sys.stdin.read(1)

