# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_gcmessages_client_bingo.proto
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
    'dota_gcmessages_client_bingo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_pb2 as steammessages__pb2
import dota_shared_enums_pb2 as dota__shared__enums__pb2
import dota_gcmessages_common_pb2 as dota__gcmessages__common__pb2
import dota_gcmessages_webapi_pb2 as dota__gcmessages__webapi__pb2
import gcsdk_gcmessages_pb2 as gcsdk__gcmessages__pb2
import base_gcmessages_pb2 as base__gcmessages__pb2
import econ_gcmessages_pb2 as econ__gcmessages__pb2
import dota_gcmessages_client_pb2 as dota__gcmessages__client__pb2
import valveextensions_pb2 as valveextensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"dota_gcmessages_client_bingo.proto\x1a\x13steammessages.proto\x1a\x17\x64ota_shared_enums.proto\x1a\x1c\x64ota_gcmessages_common.proto\x1a\x1c\x64ota_gcmessages_webapi.proto\x1a\x16gcsdk_gcmessages.proto\x1a\x15\x62\x61se_gcmessages.proto\x1a\x15\x65\x63on_gcmessages.proto\x1a\x1c\x64ota_gcmessages_client.proto\x1a\x15valveextensions.proto\"Q\n\x0f\x43MsgBingoSquare\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x16\n\x0estat_threshold\x18\x02 \x01(\x05\x12\x15\n\rupgrade_level\x18\x03 \x01(\r\"&\n\x0f\x43MsgBingoTokens\x12\x13\n\x0btoken_count\x18\x01 \x01(\r\"2\n\rCMsgBingoCard\x12!\n\x07squares\x18\x01 \x03(\x0b\x32\x10.CMsgBingoSquare\"\x88\x02\n\x11\x43MsgBingoUserData\x12\x37\n\x0b\x62ingo_cards\x18\x01 \x03(\x0b\x32\".CMsgBingoUserData.BingoCardsEntry\x12\x39\n\x0c\x62ingo_tokens\x18\x02 \x03(\x0b\x32#.CMsgBingoUserData.BingoTokensEntry\x1a=\n\x0f\x42ingoCardsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.CMsgBingoCard\x1a@\n\x10\x42ingoTokensEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.CMsgBingoTokens\"3\n\x1e\x43MsgClientToGCBingoGetUserData\x12\x11\n\tleague_id\x18\x01 \x01(\r\"\x8a\x02\n&CMsgClientToGCBingoGetUserDataResponse\x12U\n\x08response\x18\x01 \x01(\x0e\x32\x31.CMsgClientToGCBingoGetUserDataResponse.EResponse:\x10k_eInternalError\x12%\n\tuser_data\x18\x02 \x01(\x0b\x32\x12.CMsgBingoUserData\"b\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\"B\n\x1b\x43MsgBingoIndividualStatData\x12\x0f\n\x07stat_id\x18\x01 \x01(\r\x12\x12\n\nstat_value\x18\x02 \x01(\x05\"F\n\x12\x43MsgBingoStatsData\x12\x30\n\nstats_data\x18\x01 \x03(\x0b\x32\x1c.CMsgBingoIndividualStatData\"J\n\x1f\x43MsgClientToGCBingoGetStatsData\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\"\x8e\x02\n\'CMsgClientToGCBingoGetStatsDataResponse\x12V\n\x08response\x18\x01 \x01(\x0e\x32\x32.CMsgClientToGCBingoGetStatsDataResponse.EResponse:\x10k_eInternalError\x12\'\n\nstats_data\x18\x02 \x01(\x0b\x32\x13.CMsgBingoStatsData\"b\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\"^\n\"CMsgGCToClientBingoUserDataUpdated\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12%\n\tuser_data\x18\x02 \x01(\x0b\x32\x12.CMsgBingoUserData\"Y\n\x1b\x43MsgClientToGCBingoClaimRow\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\x12\x11\n\trow_index\x18\x03 \x01(\r\"\x85\x02\n#CMsgClientToGCBingoClaimRowResponse\x12R\n\x08response\x18\x01 \x01(\x0e\x32..CMsgClientToGCBingoClaimRowResponse.EResponse:\x10k_eInternalError\"\x89\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x11\n\rk_eInvalidRow\x10\x05\x12\x12\n\x0ek_eExpiredCard\x10\x06\"I\n\x1e\x43MsgClientToGCBingoShuffleCard\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\"\xa6\x02\n&CMsgClientToGCBingoShuffleCardResponse\x12U\n\x08response\x18\x01 \x01(\x0e\x32\x31.CMsgClientToGCBingoShuffleCardResponse.EResponse:\x10k_eInternalError\"\xa4\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x12\n\x0ek_eExpiredCard\x10\x06\x12\x11\n\rk_eNotAllowed\x10\x07\x12\x19\n\x15k_eInsufficientTokens\x10\x08\"\xe3\x01\n\x1f\x43MsgClientToGCBingoModifySquare\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\x12\x14\n\x0csquare_index\x18\x03 \x01(\r\x12M\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32..CMsgClientToGCBingoModifySquare.EModifyAction:\rk_eRerollStat\"2\n\rEModifyAction\x12\x11\n\rk_eRerollStat\x10\x00\x12\x0e\n\nk_eUpgrade\x10\x01\"\xe5\x02\n\'CMsgClientToGCBingoModifySquareResponse\x12V\n\x08response\x18\x01 \x01(\x0e\x32\x32.CMsgClientToGCBingoModifySquareResponse.EResponse:\x10k_eInternalError\"\xe1\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x12\n\x0ek_eExpiredCard\x10\x06\x12\x11\n\rk_eNotAllowed\x10\x07\x12\x19\n\x15k_eInsufficientTokens\x10\x08\x12\x12\n\x0ek_eCantUpgrade\x10\t\x12\x11\n\rk_eCantReroll\x10\n\x12\x14\n\x10k_eInvalidSquare\x10\x0b\"K\n CMsgClientToGCBingoDevRerollCard\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\"\x8f\x02\n(CMsgClientToGCBingoDevRerollCardResponse\x12W\n\x08response\x18\x01 \x01(\x0e\x32\x33.CMsgClientToGCBingoDevRerollCardResponse.EResponse:\x10k_eInternalError\"\x89\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x12\n\x0ek_eExpiredCard\x10\x06\x12\x11\n\rk_eNotAllowed\x10\x07\"_\n\x1f\x43MsgClientToGCBingoDevAddTokens\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x14\n\x0cleague_phase\x18\x02 \x01(\r\x12\x13\n\x0btoken_count\x18\x03 \x01(\x05\"\x8d\x02\n\'CMsgClientToGCBingoDevAddTokensResponse\x12V\n\x08response\x18\x01 \x01(\x0e\x32\x32.CMsgClientToGCBingoDevAddTokensResponse.EResponse:\x10k_eInternalError\"\x89\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x12\n\x0ek_eExpiredCard\x10\x06\x12\x11\n\rk_eNotAllowed\x10\x07\"9\n$CMsgClientToGCBingoDevClearInventory\x12\x11\n\tleague_id\x18\x01 \x01(\r\"\x97\x02\n,CMsgClientToGCBingoDevClearInventoryResponse\x12[\n\x08response\x18\x01 \x01(\x0e\x32\x37.CMsgClientToGCBingoDevClearInventoryResponse.EResponse:\x10k_eInternalError\"\x89\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x12\n\x0ek_eExpiredCard\x10\x06\x12\x11\n\rk_eNotAllowed\x10\x07*\xd1\x03\n\x11\x45\x42ingoAuditAction\x12\x1f\n\x1bk_eBingoAuditAction_Invalid\x10\x00\x12\'\n#k_eBingoAuditAction_DevModifyTokens\x10\x01\x12)\n%k_eBingoAuditAction_DevClearInventory\x10\x02\x12%\n!k_eBingoAuditAction_DevRerollCard\x10\x03\x12#\n\x1fk_eBingoAuditAction_ShuffleCard\x10\x04\x12$\n k_eBingoAuditAction_RerollSquare\x10\x05\x12%\n!k_eBingoAuditAction_UpgradeSquare\x10\x06\x12 \n\x1ck_eBingoAuditAction_ClaimRow\x10\x07\x12-\n)k_eBingoAuditAction_EventActionTokenGrant\x10\x08\x12*\n&k_eBingoAuditAction_SupportGrantTokens\x10\t\x12\x31\n-k_eBingoAuditAction_SupportStatThresholdFixup\x10\n')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_gcmessages_client_bingo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EBINGOAUDITACTION']._serialized_start=3995
  _globals['_EBINGOAUDITACTION']._serialized_end=4460
  _globals['_CMSGBINGOSQUARE']._serialized_start=267
  _globals['_CMSGBINGOSQUARE']._serialized_end=348
  _globals['_CMSGBINGOTOKENS']._serialized_start=350
  _globals['_CMSGBINGOTOKENS']._serialized_end=388
  _globals['_CMSGBINGOCARD']._serialized_start=390
  _globals['_CMSGBINGOCARD']._serialized_end=440
  _globals['_CMSGBINGOUSERDATA']._serialized_start=443
  _globals['_CMSGBINGOUSERDATA']._serialized_end=707
  _globals['_CMSGBINGOUSERDATA_BINGOCARDSENTRY']._serialized_start=580
  _globals['_CMSGBINGOUSERDATA_BINGOCARDSENTRY']._serialized_end=641
  _globals['_CMSGBINGOUSERDATA_BINGOTOKENSENTRY']._serialized_start=643
  _globals['_CMSGBINGOUSERDATA_BINGOTOKENSENTRY']._serialized_end=707
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATA']._serialized_start=709
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATA']._serialized_end=760
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATARESPONSE']._serialized_start=763
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATARESPONSE']._serialized_end=1029
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATARESPONSE_ERESPONSE']._serialized_start=931
  _globals['_CMSGCLIENTTOGCBINGOGETUSERDATARESPONSE_ERESPONSE']._serialized_end=1029
  _globals['_CMSGBINGOINDIVIDUALSTATDATA']._serialized_start=1031
  _globals['_CMSGBINGOINDIVIDUALSTATDATA']._serialized_end=1097
  _globals['_CMSGBINGOSTATSDATA']._serialized_start=1099
  _globals['_CMSGBINGOSTATSDATA']._serialized_end=1169
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATA']._serialized_start=1171
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATA']._serialized_end=1245
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATARESPONSE']._serialized_start=1248
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATARESPONSE']._serialized_end=1518
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATARESPONSE_ERESPONSE']._serialized_start=931
  _globals['_CMSGCLIENTTOGCBINGOGETSTATSDATARESPONSE_ERESPONSE']._serialized_end=1029
  _globals['_CMSGGCTOCLIENTBINGOUSERDATAUPDATED']._serialized_start=1520
  _globals['_CMSGGCTOCLIENTBINGOUSERDATAUPDATED']._serialized_end=1614
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROW']._serialized_start=1616
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROW']._serialized_end=1705
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROWRESPONSE']._serialized_start=1708
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROWRESPONSE']._serialized_end=1969
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROWRESPONSE_ERESPONSE']._serialized_start=1832
  _globals['_CMSGCLIENTTOGCBINGOCLAIMROWRESPONSE_ERESPONSE']._serialized_end=1969
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARD']._serialized_start=1971
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARD']._serialized_end=2044
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARDRESPONSE']._serialized_start=2047
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARDRESPONSE']._serialized_end=2341
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARDRESPONSE_ERESPONSE']._serialized_start=2177
  _globals['_CMSGCLIENTTOGCBINGOSHUFFLECARDRESPONSE_ERESPONSE']._serialized_end=2341
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARE']._serialized_start=2344
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARE']._serialized_end=2571
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARE_EMODIFYACTION']._serialized_start=2521
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARE_EMODIFYACTION']._serialized_end=2571
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARERESPONSE']._serialized_start=2574
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARERESPONSE']._serialized_end=2931
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARERESPONSE_ERESPONSE']._serialized_start=2706
  _globals['_CMSGCLIENTTOGCBINGOMODIFYSQUARERESPONSE_ERESPONSE']._serialized_end=2931
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARD']._serialized_start=2933
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARD']._serialized_end=3008
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARDRESPONSE']._serialized_start=3011
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARDRESPONSE']._serialized_end=3282
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARDRESPONSE_ERESPONSE']._serialized_start=2177
  _globals['_CMSGCLIENTTOGCBINGODEVREROLLCARDRESPONSE_ERESPONSE']._serialized_end=2314
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENS']._serialized_start=3284
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENS']._serialized_end=3379
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENSRESPONSE']._serialized_start=3382
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENSRESPONSE']._serialized_end=3651
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENSRESPONSE_ERESPONSE']._serialized_start=2177
  _globals['_CMSGCLIENTTOGCBINGODEVADDTOKENSRESPONSE_ERESPONSE']._serialized_end=2314
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORY']._serialized_start=3653
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORY']._serialized_end=3710
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORYRESPONSE']._serialized_start=3713
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORYRESPONSE']._serialized_end=3992
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORYRESPONSE_ERESPONSE']._serialized_start=2177
  _globals['_CMSGCLIENTTOGCBINGODEVCLEARINVENTORYRESPONSE_ERESPONSE']._serialized_end=2314
# @@protoc_insertion_point(module_scope)
