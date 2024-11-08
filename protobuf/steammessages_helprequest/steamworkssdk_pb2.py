# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_helprequest.steamworkssdk.proto
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
    'steammessages_helprequest.steamworkssdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamworkssdk_pb2 as steammessages__unified__base_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-steammessages_helprequest.steamworkssdk.proto\x1a.steammessages_unified_base.steamworkssdk.proto\"\x82\x01\n1CHelpRequestLogs_UploadUserApplicationLog_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08log_type\x18\x02 \x01(\t\x12\x16\n\x0eversion_string\x18\x03 \x01(\t\x12\x14\n\x0clog_contents\x18\x04 \x01(\t\"@\n2CHelpRequestLogs_UploadUserApplicationLog_Response\x12\n\n\x02id\x18\x01 \x01(\x04\x32\xee\x01\n\x0fHelpRequestLogs\x12\xa8\x01\n\x18UploadUserApplicationLog\x12\x32.CHelpRequestLogs_UploadUserApplicationLog_Request\x1a\x33.CHelpRequestLogs_UploadUserApplicationLog_Response\"#\x82\xb5\x18\x1fUser uploading application logs\x1a\x30\x82\xb5\x18,Service for dealing with user-submitted logsB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_helprequest.steamworkssdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_HELPREQUESTLOGS']._loaded_options = None
  _globals['_HELPREQUESTLOGS']._serialized_options = b'\202\265\030,Service for dealing with user-submitted logs'
  _globals['_HELPREQUESTLOGS'].methods_by_name['UploadUserApplicationLog']._loaded_options = None
  _globals['_HELPREQUESTLOGS'].methods_by_name['UploadUserApplicationLog']._serialized_options = b'\202\265\030\037User uploading application logs'
  _globals['_CHELPREQUESTLOGS_UPLOADUSERAPPLICATIONLOG_REQUEST']._serialized_start=98
  _globals['_CHELPREQUESTLOGS_UPLOADUSERAPPLICATIONLOG_REQUEST']._serialized_end=228
  _globals['_CHELPREQUESTLOGS_UPLOADUSERAPPLICATIONLOG_RESPONSE']._serialized_start=230
  _globals['_CHELPREQUESTLOGS_UPLOADUSERAPPLICATIONLOG_RESPONSE']._serialized_end=294
  _globals['_HELPREQUESTLOGS']._serialized_start=297
  _globals['_HELPREQUESTLOGS']._serialized_end=535
# @@protoc_insertion_point(module_scope)
