# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_usercmd.proto
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
    'dota_usercmd.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2
import usercmd_pb2 as usercmd__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64ota_usercmd.proto\x1a\x16networkbasetypes.proto\x1a\rusercmd.proto\"\xa3\x02\n\x0f\x43\x44ota2UserCmdPB\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CBaseUserCmdPB\x12%\n\x1dspectator_query_unit_entindex\x18\x02 \x01(\x05\x12#\n\x0e\x63rosshairtrace\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x10\x63\x61meraposition_x\x18\x04 \x01(\x05\x12\x18\n\x10\x63\x61meraposition_y\x18\x05 \x01(\x05\x12\x15\n\rclickbehavior\x18\x06 \x01(\r\x12\x12\n\nstatspanel\x18\x07 \x01(\r\x12\x11\n\tshoppanel\x18\x08 \x01(\r\x12\x16\n\x0estats_dropdown\x18\t \x01(\r\x12\x1b\n\x13stats_dropdown_sort\x18\n \x01(\r')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_usercmd_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CDOTA2USERCMDPB']._serialized_start=62
  _globals['_CDOTA2USERCMDPB']._serialized_end=353
# @@protoc_insertion_point(module_scope)
