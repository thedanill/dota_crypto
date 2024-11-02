# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_modifiers.proto
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
    'dota_modifiers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64ota_modifiers.proto\x1a\x16networkbasetypes.proto\"\xd2\x07\n\x1b\x43\x44OTAModifierBuffTableEntry\x12N\n\nentry_type\x18\x01 \x02(\x0e\x32\x19.DOTA_MODIFIER_ENTRY_TYPE:\x1f\x44OTA_MODIFIER_ENTRY_TYPE_ACTIVE\x12\x18\n\x06parent\x18\x02 \x02(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\r\n\x05index\x18\x03 \x02(\x05\x12\x12\n\nserial_num\x18\x04 \x02(\x05\x12\x16\n\x0emodifier_class\x18\x05 \x01(\x05\x12\x15\n\rability_level\x18\x06 \x01(\x05\x12\x13\n\x0bstack_count\x18\x07 \x01(\x05\x12\x15\n\rcreation_time\x18\x08 \x01(\x02\x12\x14\n\x08\x64uration\x18\t \x01(\x02:\x02-1\x12\x18\n\x06\x63\x61ster\x18\n \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x19\n\x07\x61\x62ility\x18\x0b \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\r\n\x05\x61rmor\x18\x0c \x01(\x05\x12\x11\n\tfade_time\x18\r \x01(\x02\x12\x0e\n\x06subtle\x18\x0e \x01(\x08\x12\x14\n\x0c\x63hannel_time\x18\x0f \x01(\x02\x12\x1c\n\x07v_start\x18\x10 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05v_end\x18\x11 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x12portal_loop_appear\x18\x12 \x01(\t\x12\x1d\n\x15portal_loop_disappear\x18\x13 \x01(\t\x12\x18\n\x10hero_loop_appear\x18\x14 \x01(\t\x12\x1b\n\x13hero_loop_disappear\x18\x15 \x01(\t\x12\x16\n\x0emovement_speed\x18\x16 \x01(\x05\x12\x0c\n\x04\x61ura\x18\x17 \x01(\x08\x12\x10\n\x08\x61\x63tivity\x18\x18 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x19 \x01(\x05\x12\r\n\x05range\x18\x1a \x01(\x05\x12\x19\n\x11\x64\x64_modifier_index\x18\x1b \x01(\x05\x12\x19\n\rdd_ability_id\x18\x1c \x01(\x05:\x02-1\x12\x16\n\x0eillusion_label\x18\x1d \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x1e \x01(\x08\x12\x12\n\nplayer_ids\x18\x1f \x01(\t\x12\x10\n\x08lua_name\x18  \x01(\t\x12\x14\n\x0c\x61ttack_speed\x18! \x01(\x05\x12\x1c\n\naura_owner\x18\" \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x17\n\x0f\x62onus_all_stats\x18# \x01(\x05\x12\x14\n\x0c\x62onus_health\x18$ \x01(\x05\x12\x12\n\nbonus_mana\x18% \x01(\x05\x12\x1f\n\rcustom_entity\x18& \x01(\r:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x19\n\x11\x61ura_within_range\x18\' \x01(\x08\"I\n\x15\x43\x44OTALuaModifierEntry\x12\x15\n\rmodifier_type\x18\x01 \x02(\x05\x12\x19\n\x11modifier_filename\x18\x02 \x02(\t*e\n\x18\x44OTA_MODIFIER_ENTRY_TYPE\x12#\n\x1f\x44OTA_MODIFIER_ENTRY_TYPE_ACTIVE\x10\x01\x12$\n DOTA_MODIFIER_ENTRY_TYPE_REMOVED\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_modifiers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOTA_MODIFIER_ENTRY_TYPE']._serialized_start=1104
  _globals['_DOTA_MODIFIER_ENTRY_TYPE']._serialized_end=1205
  _globals['_CDOTAMODIFIERBUFFTABLEENTRY']._serialized_start=49
  _globals['_CDOTAMODIFIERBUFFTABLEENTRY']._serialized_end=1027
  _globals['_CDOTALUAMODIFIERENTRY']._serialized_start=1029
  _globals['_CDOTALUAMODIFIERENTRY']._serialized_end=1102
# @@protoc_insertion_point(module_scope)