# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: demo.proto
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
    'demo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\"\xfe\x02\n\x0f\x43\x44\x65moFileHeader\x12\x17\n\x0f\x64\x65mo_file_stamp\x18\x01 \x02(\t\x12\x18\n\x10network_protocol\x18\x02 \x01(\x05\x12\x13\n\x0bserver_name\x18\x03 \x01(\t\x12\x13\n\x0b\x63lient_name\x18\x04 \x01(\t\x12\x10\n\x08map_name\x18\x05 \x01(\t\x12\x16\n\x0egame_directory\x18\x06 \x01(\t\x12\x1b\n\x13\x66ullpackets_version\x18\x07 \x01(\x05\x12!\n\x19\x61llow_clientside_entities\x18\x08 \x01(\x08\x12\"\n\x1a\x61llow_clientside_particles\x18\t \x01(\x08\x12\x0e\n\x06\x61\x64\x64ons\x18\n \x01(\t\x12\x19\n\x11\x64\x65mo_version_name\x18\x0b \x01(\t\x12\x19\n\x11\x64\x65mo_version_guid\x18\x0c \x01(\t\x12\x11\n\tbuild_num\x18\r \x01(\x05\x12\x0c\n\x04game\x18\x0e \x01(\t\x12\x19\n\x11server_start_tick\x18\x0f \x01(\x05\"\x82\x05\n\tCGameInfo\x12&\n\x04\x64ota\x18\x04 \x01(\x0b\x32\x18.CGameInfo.CDotaGameInfo\x12\"\n\x02\x63s\x18\x05 \x01(\x0b\x32\x16.CGameInfo.CCSGameInfo\x1a\xfe\x03\n\rCDotaGameInfo\x12\x10\n\x08match_id\x18\x01 \x01(\x04\x12\x11\n\tgame_mode\x18\x02 \x01(\x05\x12\x13\n\x0bgame_winner\x18\x03 \x01(\x05\x12\x39\n\x0bplayer_info\x18\x04 \x03(\x0b\x32$.CGameInfo.CDotaGameInfo.CPlayerInfo\x12\x10\n\x08leagueid\x18\x05 \x01(\r\x12=\n\npicks_bans\x18\x06 \x03(\x0b\x32).CGameInfo.CDotaGameInfo.CHeroSelectEvent\x12\x17\n\x0fradiant_team_id\x18\x07 \x01(\r\x12\x14\n\x0c\x64ire_team_id\x18\x08 \x01(\r\x12\x18\n\x10radiant_team_tag\x18\t \x01(\t\x12\x15\n\rdire_team_tag\x18\n \x01(\t\x12\x10\n\x08\x65nd_time\x18\x0b \x01(\r\x1aq\n\x0b\x43PlayerInfo\x12\x11\n\thero_name\x18\x01 \x01(\t\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\x12\x16\n\x0eis_fake_client\x18\x03 \x01(\x08\x12\x0f\n\x07steamid\x18\x04 \x01(\x04\x12\x11\n\tgame_team\x18\x05 \x01(\x05\x1a\x42\n\x10\x43HeroSelectEvent\x12\x0f\n\x07is_pick\x18\x01 \x01(\x08\x12\x0c\n\x04team\x18\x02 \x01(\r\x12\x0f\n\x07hero_id\x18\x03 \x01(\x05\x1a(\n\x0b\x43\x43SGameInfo\x12\x19\n\x11round_start_ticks\x18\x01 \x03(\x05\"v\n\rCDemoFileInfo\x12\x15\n\rplayback_time\x18\x01 \x01(\x02\x12\x16\n\x0eplayback_ticks\x18\x02 \x01(\x05\x12\x17\n\x0fplayback_frames\x18\x03 \x01(\x05\x12\x1d\n\tgame_info\x18\x04 \x01(\x0b\x32\n.CGameInfo\"\x1b\n\x0b\x43\x44\x65moPacket\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"Y\n\x0f\x43\x44\x65moFullPacket\x12(\n\x0cstring_table\x18\x01 \x01(\x0b\x32\x12.CDemoStringTables\x12\x1c\n\x06packet\x18\x02 \x01(\x0b\x32\x0c.CDemoPacket\"S\n\rCDemoSaveGame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x10\n\x08steam_id\x18\x02 \x01(\x06\x12\x11\n\tsignature\x18\x03 \x01(\x06\x12\x0f\n\x07version\x18\x04 \x01(\x05\"\x0f\n\rCDemoSyncTick\"$\n\x0f\x43\x44\x65moConsoleCmd\x12\x11\n\tcmdstring\x18\x01 \x01(\t\"\x1f\n\x0f\x43\x44\x65moSendTables\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x81\x01\n\x0e\x43\x44\x65moClassInfo\x12(\n\x07\x63lasses\x18\x01 \x03(\x0b\x32\x17.CDemoClassInfo.class_t\x1a\x45\n\x07\x63lass_t\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\x05\x12\x14\n\x0cnetwork_name\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\"7\n\x0f\x43\x44\x65moCustomData\x12\x16\n\x0e\x63\x61llback_index\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"+\n\x18\x43\x44\x65moCustomDataCallbacks\x12\x0f\n\x07save_id\x18\x01 \x03(\t\"E\n\x14\x43\x44\x65moAnimationHeader\x12\x11\n\tentity_id\x18\x01 \x01(\x11\x12\x0c\n\x04tick\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"r\n\x12\x43\x44\x65moAnimationData\x12\x11\n\tentity_id\x18\x01 \x01(\x11\x12\x12\n\nstart_tick\x18\x02 \x01(\x05\x12\x10\n\x08\x65nd_tick\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x15\n\rdata_checksum\x18\x05 \x01(\x03\"\xfb\x01\n\x11\x43\x44\x65moStringTables\x12*\n\x06tables\x18\x01 \x03(\x0b\x32\x1a.CDemoStringTables.table_t\x1a$\n\x07items_t\x12\x0b\n\x03str\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x1a\x93\x01\n\x07table_t\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12)\n\x05items\x18\x02 \x03(\x0b\x32\x1a.CDemoStringTables.items_t\x12\x34\n\x10items_clientside\x18\x03 \x03(\x0b\x32\x1a.CDemoStringTables.items_t\x12\x13\n\x0btable_flags\x18\x04 \x01(\x05\"\x0b\n\tCDemoStop\"0\n\x0c\x43\x44\x65moUserCmd\x12\x12\n\ncmd_number\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\" \n\x10\x43\x44\x65moSpawnGroups\x12\x0c\n\x04msgs\x18\x03 \x03(\x0c*\xb4\x03\n\rEDemoCommands\x12\x16\n\tDEM_Error\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0c\n\x08\x44\x45M_Stop\x10\x00\x12\x12\n\x0e\x44\x45M_FileHeader\x10\x01\x12\x10\n\x0c\x44\x45M_FileInfo\x10\x02\x12\x10\n\x0c\x44\x45M_SyncTick\x10\x03\x12\x12\n\x0e\x44\x45M_SendTables\x10\x04\x12\x11\n\rDEM_ClassInfo\x10\x05\x12\x14\n\x10\x44\x45M_StringTables\x10\x06\x12\x0e\n\nDEM_Packet\x10\x07\x12\x14\n\x10\x44\x45M_SignonPacket\x10\x08\x12\x12\n\x0e\x44\x45M_ConsoleCmd\x10\t\x12\x12\n\x0e\x44\x45M_CustomData\x10\n\x12\x1b\n\x17\x44\x45M_CustomDataCallbacks\x10\x0b\x12\x0f\n\x0b\x44\x45M_UserCmd\x10\x0c\x12\x12\n\x0e\x44\x45M_FullPacket\x10\r\x12\x10\n\x0c\x44\x45M_SaveGame\x10\x0e\x12\x13\n\x0f\x44\x45M_SpawnGroups\x10\x0f\x12\x15\n\x11\x44\x45M_AnimationData\x10\x10\x12\x17\n\x13\x44\x45M_AnimationHeader\x10\x11\x12\x0b\n\x07\x44\x45M_Max\x10\x12\x12\x14\n\x10\x44\x45M_IsCompressed\x10@')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EDEMOCOMMANDS']._serialized_start=2230
  _globals['_EDEMOCOMMANDS']._serialized_end=2666
  _globals['_CDEMOFILEHEADER']._serialized_start=15
  _globals['_CDEMOFILEHEADER']._serialized_end=397
  _globals['_CGAMEINFO']._serialized_start=400
  _globals['_CGAMEINFO']._serialized_end=1042
  _globals['_CGAMEINFO_CDOTAGAMEINFO']._serialized_start=490
  _globals['_CGAMEINFO_CDOTAGAMEINFO']._serialized_end=1000
  _globals['_CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO']._serialized_start=819
  _globals['_CGAMEINFO_CDOTAGAMEINFO_CPLAYERINFO']._serialized_end=932
  _globals['_CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT']._serialized_start=934
  _globals['_CGAMEINFO_CDOTAGAMEINFO_CHEROSELECTEVENT']._serialized_end=1000
  _globals['_CGAMEINFO_CCSGAMEINFO']._serialized_start=1002
  _globals['_CGAMEINFO_CCSGAMEINFO']._serialized_end=1042
  _globals['_CDEMOFILEINFO']._serialized_start=1044
  _globals['_CDEMOFILEINFO']._serialized_end=1162
  _globals['_CDEMOPACKET']._serialized_start=1164
  _globals['_CDEMOPACKET']._serialized_end=1191
  _globals['_CDEMOFULLPACKET']._serialized_start=1193
  _globals['_CDEMOFULLPACKET']._serialized_end=1282
  _globals['_CDEMOSAVEGAME']._serialized_start=1284
  _globals['_CDEMOSAVEGAME']._serialized_end=1367
  _globals['_CDEMOSYNCTICK']._serialized_start=1369
  _globals['_CDEMOSYNCTICK']._serialized_end=1384
  _globals['_CDEMOCONSOLECMD']._serialized_start=1386
  _globals['_CDEMOCONSOLECMD']._serialized_end=1422
  _globals['_CDEMOSENDTABLES']._serialized_start=1424
  _globals['_CDEMOSENDTABLES']._serialized_end=1455
  _globals['_CDEMOCLASSINFO']._serialized_start=1458
  _globals['_CDEMOCLASSINFO']._serialized_end=1587
  _globals['_CDEMOCLASSINFO_CLASS_T']._serialized_start=1518
  _globals['_CDEMOCLASSINFO_CLASS_T']._serialized_end=1587
  _globals['_CDEMOCUSTOMDATA']._serialized_start=1589
  _globals['_CDEMOCUSTOMDATA']._serialized_end=1644
  _globals['_CDEMOCUSTOMDATACALLBACKS']._serialized_start=1646
  _globals['_CDEMOCUSTOMDATACALLBACKS']._serialized_end=1689
  _globals['_CDEMOANIMATIONHEADER']._serialized_start=1691
  _globals['_CDEMOANIMATIONHEADER']._serialized_end=1760
  _globals['_CDEMOANIMATIONDATA']._serialized_start=1762
  _globals['_CDEMOANIMATIONDATA']._serialized_end=1876
  _globals['_CDEMOSTRINGTABLES']._serialized_start=1879
  _globals['_CDEMOSTRINGTABLES']._serialized_end=2130
  _globals['_CDEMOSTRINGTABLES_ITEMS_T']._serialized_start=1944
  _globals['_CDEMOSTRINGTABLES_ITEMS_T']._serialized_end=1980
  _globals['_CDEMOSTRINGTABLES_TABLE_T']._serialized_start=1983
  _globals['_CDEMOSTRINGTABLES_TABLE_T']._serialized_end=2130
  _globals['_CDEMOSTOP']._serialized_start=2132
  _globals['_CDEMOSTOP']._serialized_end=2143
  _globals['_CDEMOUSERCMD']._serialized_start=2145
  _globals['_CDEMOUSERCMD']._serialized_end=2193
  _globals['_CDEMOSPAWNGROUPS']._serialized_start=2195
  _globals['_CDEMOSPAWNGROUPS']._serialized_end=2227
# @@protoc_insertion_point(module_scope)
