# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: networksystem_protomessages.proto
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
    'networksystem_protomessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!networksystem_protomessages.proto\"0\n NetMessageSplitscreenUserChanged\x12\x0c\n\x04slot\x18\x01 \x01(\r\",\n\x1aNetMessageConnectionClosed\x12\x0e\n\x06reason\x18\x01 \x01(\r\"-\n\x1bNetMessageConnectionCrashed\x12\x0e\n\x06reason\x18\x01 \x01(\r\"\x17\n\x15NetMessagePacketStart\"\x15\n\x13NetMessagePacketEnd')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'networksystem_protomessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NETMESSAGESPLITSCREENUSERCHANGED']._serialized_start=37
  _globals['_NETMESSAGESPLITSCREENUSERCHANGED']._serialized_end=85
  _globals['_NETMESSAGECONNECTIONCLOSED']._serialized_start=87
  _globals['_NETMESSAGECONNECTIONCLOSED']._serialized_end=131
  _globals['_NETMESSAGECONNECTIONCRASHED']._serialized_start=133
  _globals['_NETMESSAGECONNECTIONCRASHED']._serialized_end=178
  _globals['_NETMESSAGEPACKETSTART']._serialized_start=180
  _globals['_NETMESSAGEPACKETSTART']._serialized_end=203
  _globals['_NETMESSAGEPACKETEND']._serialized_start=205
  _globals['_NETMESSAGEPACKETEND']._serialized_end=226
# @@protoc_insertion_point(module_scope)
