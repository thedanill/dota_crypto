# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: connectionless_netmessages.proto
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
    'connectionless_netmessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import netmessages_pb2 as netmessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n connectionless_netmessages.proto\x1a\x11netmessages.proto\"\x8c\x02\n\x13\x43\x32S_CONNECT_Message\x12\x14\n\x0chost_version\x18\x01 \x01(\r\x12\x15\n\rauth_protocol\x18\x02 \x01(\r\x12\x18\n\x10\x63hallenge_number\x18\x03 \x01(\r\x12\x1a\n\x12reservation_cookie\x18\x04 \x01(\x06\x12\x14\n\x0clow_violence\x18\x05 \x01(\x08\x12\x1a\n\x12\x65ncrypted_password\x18\x06 \x01(\x0c\x12\x31\n\x0csplitplayers\x18\x07 \x03(\x0b\x32\x1b.CCLCMsg_SplitPlayerConnect\x12\x12\n\nauth_steam\x18\x08 \x01(\x0c\x12\x19\n\x11\x63hallenge_context\x18\t \x01(\t\",\n\x16\x43\x32S_CONNECTION_Message\x12\x12\n\naddon_name\x18\x01 \x01(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'connectionless_netmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_C2S_CONNECT_MESSAGE']._serialized_start=56
  _globals['_C2S_CONNECT_MESSAGE']._serialized_end=324
  _globals['_C2S_CONNECTION_MESSAGE']._serialized_start=326
  _globals['_C2S_CONNECTION_MESSAGE']._serialized_end=370
# @@protoc_insertion_point(module_scope)