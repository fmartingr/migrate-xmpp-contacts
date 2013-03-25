import logging
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp.jid import JID
from pprint import pprint

## Requeriments: xleekxmpp, dnspython
## Usage: A file with contacts inside, or you can also use
## the commented code to get contacts from one account to
## subscribe to them in the another. NOT RECOMMENDED.
## 
## NO WARRANTY. If this get your account blocked or something
## don't come crying, it's just an example of me having a headache.

## Configuration
LOGLEVEL = logging.INFO

## Account from
#EMAIL_FROM = '<your account here>@gmail.com'
#JID_FROM = "%s/SleekAddBot" % EMAIL_FROM
#PASSWORD_FROM = '<your password here>'

CONTACTS_FILE = 'contacts'

## Account to
EMAIL_TO = '<your new account>@gmail.com'
JID_TO = "%s/FAKEADIUMISFAKE" % EMAIL_TO
PASSWORD_TO = '<your new password>'

## Things
class AddBot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

    def add_contact(self, jid):
        self.update_roster(jid, subscription='both')
        self.send_presence(pto=jid, ptype='subscribe')


if __name__ == '__main__':
    logging.basicConfig(level=LOGLEVEL,
                        format='%(levelname)-8s %(message)s')

    # Connecting to origin account
    #print "Connecting to origin account: %s" % EMAIL_FROM
    #xmpp = AddBot(JID_FROM, PASSWORD_FROM)
    #xmpp.connect()
    #xmpp.process(block=False)
    #xmpp.get_roster(block=True)
    #roster_from = xmpp.roster
    #xmpp.disconnect()

    #for jid in roster_from[EMAIL_FROM]:
    #    if roster_from[EMAIL_FROM][jid]['subscription'] == 'both':
    #        xmpp_to.add_contact(jid)

    # Getting contacts from file
    contacts = [contact.strip() for contact in open(CONTACTS_FILE).readlines()]
    print contacts

    # Connecting to destiny account
    print "Connecting to origin account: %s" % EMAIL_TO
    xmpp = AddBot(JID_TO, PASSWORD_TO)
    xmpp.connect()
    xmpp.process(block=False)

    # Adding contacts
    for contact in contacts:
        try:
            xmpp.add_contact(contact)
            print "Adding contact: %s" % contact
        except IqError as e:
            print "ERROR ADDING CONTACT: %s (%s)" % (contact, e)
            pass

    xmpp.disconnect()
