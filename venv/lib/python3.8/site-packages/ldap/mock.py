import logging

from ldap3.protocol.rfc4511 import (
    LDAPMessage, MessageID, ProtocolOp, BindRequest, Version,
    AuthenticationChoice, Simple, BindResponse, ResultCode, SearchResultDone,
    SearchResultEntry, LDAPDN, PartialAttributeList, PartialAttribute,
    AttributeDescription, Vals, AttributeValue
)
from ldap3.strategy.sync import SyncStrategy

from pyasn1.codec.ber.encoder import encode
from pyasn1.codec.ber.decoder import decode

from ldap3.utils import log
logging.basicConfig(level=logging.DEBUG)
log.set_library_log_activation_level(logging.DEBUG)
log.set_library_log_detail_level(log.EXTENDED)


class Connection(object):
    def __init__(self, socket):
        self.socket = socket


def receive(sock, message_id=None):
    conn = Connection(socket=sock)
    raw_messages = SyncStrategy(ldap_connection=conn).receiving()

    messages = []
    for r in raw_messages:
        ldap_resp, _ = decode(r, asn1Spec=LDAPMessage())
        i = ldap_resp['messageID']
        if i == 0:
            raise NotImplemented('Unsolicited Notification')
        elif message_id in [None, i]:
            messages.append(ldap_resp)

    if message_id is not None:
        assert len(messages) == 1

    return messages


def bind(message_id, name, password):
    req = BindRequest()
    req['version'] = Version(3)
    req['name'] = name
    req['authentication'] = \
        AuthenticationChoice().setComponentByName('simple', Simple(password))

    msg = LDAPMessage()
    msg['messageID'] = MessageID(message_id)
    msg['protocolOp'] = ProtocolOp().setComponentByName('bindRequest', req)
    return msg


def respond_bind(message_id):
    res = BindResponse()
    res['resultCode'] = ResultCode('success')
    res['matchedDN'] = ''
    res['diagnosticMessage'] = ''

    msg = LDAPMessage()
    msg['messageID'] = MessageID(message_id)
    msg['protocolOp'] = ProtocolOp().setComponentByName('bindResponse', res)
    return msg


def respond_search_entry(message_id, name, attributes):
    res = SearchResultEntry()
    res['object'] = LDAPDN(name)
    res['attributes'] = PartialAttributeList()

    for i, (k, v) in enumerate(attributes.items()):
        res['attributes'][i] = PartialAttribute()
        res['attributes'][i]['type'] = AttributeDescription(k)
        res['attributes'][i]['vals'] = Vals()
        res['attributes'][i]['vals'][0] = AttributeValue(v)

    msg = LDAPMessage()
    msg['messageID'] = MessageID(message_id)
    msg['protocolOp'] = ProtocolOp().setComponentByName('searchResEntry', res)
    return msg


def respond_search_done(message_id):
    res = SearchResultDone()
    res['resultCode'] = ResultCode('success')
    res['matchedDN'] = ''
    res['diagnosticMessage'] = ''

    msg = LDAPMessage()
    msg['messageID'] = MessageID(message_id)
    msg['protocolOp'] = ProtocolOp().setComponentByName('searchResDone', res)
    return msg


def respond(messages):
    assert messages
    assert len(messages) == 1

    mi = messages[0]['messageID']
    op = messages[0]['protocolOp']

    if op['bindRequest']:
        # print(op['bindRequest']['name'],
        #       op['bindRequest']['authentication'])
        return [
            respond_bind(message_id=mi),
        ]

    elif op['searchRequest']:
        sr = op['searchRequest']
        em = sr['filter']['equalityMatch']
        if em:
            assert em['attributeDesc'] and em['assertionValue']
            key = em['attributeDesc']._value.decode()
            val = em['assertionValue']._value.decode()
            if key in ['uid', 'sAMAccountName']:
                uid = val
                email = uid + '@example.com'
            elif key == 'mail':
                email = val
                uid = email.split('@')[0]
            else:
                raise NotImplementedError((key, val))
        else:
            uid = email = ''
        return [
            respond_search_entry(
                message_id=mi,
                name=uid,
                attributes={'mail': email,
                            'givenName': uid.capitalize(),
                            'sn': uid.capitalize() + 'son',
                            'subschemaSubentry': ''}),  # for ldap3
            respond_search_done(message_id=mi),
        ]
    else:
        raise NotImplementedError(op)
