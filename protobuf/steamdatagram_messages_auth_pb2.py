# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steamdatagram_messages_auth.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'steamdatagram_messages_auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steamnetworkingsockets_messages_certs_pb2 as steamnetworkingsockets__messages__certs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!steamdatagram_messages_auth.proto\x1a+steamnetworkingsockets_messages_certs.proto\"\xcf\x04\n CMsgSteamDatagramRelayAuthTicket\x12\x13\n\x0btime_expiry\x18\x01 \x01(\x07\x12)\n!authorized_client_identity_string\x18\x0e \x01(\t\x12\"\n\x1agameserver_identity_string\x18\x0f \x01(\t\x12\x1c\n\x14\x61uthorized_public_ip\x18\x03 \x01(\x07\x12\x1a\n\x12gameserver_address\x18\x0b \x01(\x0c\x12\x0e\n\x06\x61pp_id\x18\x07 \x01(\r\x12\x14\n\x0cvirtual_port\x18\n \x01(\r\x12\x42\n\x0c\x65xtra_fields\x18\x08 \x03(\x0b\x32,.CMsgSteamDatagramRelayAuthTicket.ExtraField\x12\"\n\x1alegacy_authorized_steam_id\x18\x02 \x01(\x06\x12\"\n\x1alegacy_gameserver_steam_id\x18\x04 \x01(\x06\x12 \n\x18legacy_gameserver_pop_id\x18\t \x01(\x07\x12\x30\n(legacy_authorized_client_identity_binary\x18\x0c \x01(\x0c\x12)\n!legacy_gameserver_identity_binary\x18\r \x01(\x0c\x1a\\\n\nExtraField\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cstring_value\x18\x02 \x01(\t\x12\x13\n\x0bint64_value\x18\x03 \x01(\x12\x12\x15\n\rfixed64_value\x18\x05 \x01(\x06\"\xac\x01\n&CMsgSteamDatagramSignedRelayAuthTicket\x12\x1b\n\x13reserved_do_not_use\x18\x01 \x01(\x06\x12\x0e\n\x06ticket\x18\x03 \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x0e\n\x06key_id\x18\x02 \x01(\x06\x12\x32\n\x05\x63\x65rts\x18\x05 \x03(\x0b\x32#.CMsgSteamDatagramCertificateSigned\"d\n(CMsgSteamDatagramCachedCredentialsForApp\x12\x13\n\x0bprivate_key\x18\x01 \x01(\x0c\x12\x0c\n\x04\x63\x65rt\x18\x02 \x01(\x0c\x12\x15\n\rrelay_tickets\x18\x03 \x03(\x0c\"\xc7\x01\n+CMsgSteamDatagramGameCoordinatorServerLogin\x12\x16\n\x0etime_generated\x18\x01 \x01(\r\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x0f\n\x07routing\x18\x03 \x01(\x0c\x12\x0f\n\x07\x61ppdata\x18\x04 \x01(\x0c\x12\x1e\n\x16legacy_identity_binary\x18\x05 \x01(\x0c\x12\x17\n\x0fidentity_string\x18\x06 \x01(\t\x12\x16\n\x0e\x64ummy_steam_id\x18\x63 \x01(\x06\"\x88\x01\n1CMsgSteamDatagramSignedGameCoordinatorServerLogin\x12\x31\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\r\n\x05login\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\x8b\x01\n-CMsgSteamDatagramHostedServerAddressPlaintext\x12\x0c\n\x04ipv4\x18\x01 \x01(\x07\x12\x0c\n\x04ipv6\x18\x02 \x01(\x0c\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x16\n\x0erouting_secret\x18\x04 \x01(\x06\x12\x18\n\x10protocol_version\x18\x05 \x01(\rB\x05H\x01\x80\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steamdatagram_messages_auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\000'
  _globals['_CMSGSTEAMDATAGRAMRELAYAUTHTICKET']._serialized_start=83
  _globals['_CMSGSTEAMDATAGRAMRELAYAUTHTICKET']._serialized_end=674
  _globals['_CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD']._serialized_start=582
  _globals['_CMSGSTEAMDATAGRAMRELAYAUTHTICKET_EXTRAFIELD']._serialized_end=674
  _globals['_CMSGSTEAMDATAGRAMSIGNEDRELAYAUTHTICKET']._serialized_start=677
  _globals['_CMSGSTEAMDATAGRAMSIGNEDRELAYAUTHTICKET']._serialized_end=849
  _globals['_CMSGSTEAMDATAGRAMCACHEDCREDENTIALSFORAPP']._serialized_start=851
  _globals['_CMSGSTEAMDATAGRAMCACHEDCREDENTIALSFORAPP']._serialized_end=951
  _globals['_CMSGSTEAMDATAGRAMGAMECOORDINATORSERVERLOGIN']._serialized_start=954
  _globals['_CMSGSTEAMDATAGRAMGAMECOORDINATORSERVERLOGIN']._serialized_end=1153
  _globals['_CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN']._serialized_start=1156
  _globals['_CMSGSTEAMDATAGRAMSIGNEDGAMECOORDINATORSERVERLOGIN']._serialized_end=1292
  _globals['_CMSGSTEAMDATAGRAMHOSTEDSERVERADDRESSPLAINTEXT']._serialized_start=1295
  _globals['_CMSGSTEAMDATAGRAMHOSTEDSERVERADDRESSPLAINTEXT']._serialized_end=1434
# @@protoc_insertion_point(module_scope)