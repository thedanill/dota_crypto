# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: base_gcmessages.proto
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
    'base_gcmessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_pb2 as steammessages__pb2
import gcsdk_gcmessages_pb2 as gcsdk__gcmessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x62\x61se_gcmessages.proto\x1a\x13steammessages.proto\x1a\x16gcsdk_gcmessages.proto\"\xaf\x01\n\x1d\x43GCStorePurchaseInit_LineItem\x12\x13\n\x0bitem_def_id\x18\x01 \x01(\r\x12\x10\n\x08quantity\x18\x02 \x01(\r\x12\x1e\n\x16\x63ost_in_local_currency\x18\x03 \x01(\r\x12\x15\n\rpurchase_type\x18\x04 \x01(\r\x12\x1b\n\x13source_reference_id\x18\x05 \x01(\x04\x12\x13\n\x0bprice_index\x18\x06 \x01(\x05\"\x82\x01\n\x17\x43MsgGCStorePurchaseInit\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\x05\x12\x10\n\x08\x63urrency\x18\x03 \x01(\x05\x12\x32\n\nline_items\x18\x04 \x03(\x0b\x32\x1e.CGCStorePurchaseInit_LineItem\"A\n\x1f\x43MsgGCStorePurchaseInitResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0e\n\x06txn_id\x18\x02 \x01(\x04\"\x9e\x01\n\x12\x43MsgClientPingData\x12\x17\n\x0brelay_codes\x18\x04 \x03(\x07\x42\x02\x10\x01\x12\x17\n\x0brelay_pings\x18\x05 \x03(\rB\x02\x10\x01\x12\x18\n\x0cregion_codes\x18\x08 \x03(\rB\x02\x10\x01\x12\x18\n\x0cregion_pings\x18\t \x03(\rB\x02\x10\x01\x12\"\n\x1aregion_ping_failed_bitmask\x18\n \x01(\r\"\x88\x01\n\x11\x43MsgInviteToParty\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\r\x12\x0f\n\x07team_id\x18\x03 \x01(\r\x12\x10\n\x08\x61s_coach\x18\x04 \x01(\x08\x12&\n\tping_data\x18\x05 \x01(\x0b\x32\x13.CMsgClientPingData\"=\n\x11\x43MsgInviteToLobby\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\r\"Q\n\x15\x43MsgInvitationCreated\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\x10\n\x08steam_id\x18\x02 \x01(\x06\x12\x14\n\x0cuser_offline\x18\x03 \x01(\x08\"{\n\x17\x43MsgPartyInviteResponse\x12\x10\n\x08party_id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x08\x12\x16\n\x0e\x63lient_version\x18\x03 \x01(\r\x12&\n\tping_data\x18\x08 \x01(\x0b\x32\x13.CMsgClientPingData\"\x8b\x01\n\x17\x43MsgLobbyInviteResponse\x12\x10\n\x08lobby_id\x18\x01 \x01(\x06\x12\x0e\n\x06\x61\x63\x63\x65pt\x18\x02 \x01(\x08\x12\x16\n\x0e\x63lient_version\x18\x03 \x01(\r\x12\x17\n\x0f\x63ustom_game_crc\x18\x06 \x01(\x06\x12\x1d\n\x15\x63ustom_game_timestamp\x18\x07 \x01(\x07\"%\n\x11\x43MsgKickFromParty\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\"\x10\n\x0e\x43MsgLeaveParty\"\xa2\x01\n\x1b\x43MsgCustomGameInstallStatus\x12M\n\x06status\x18\x01 \x01(\x0e\x32\x19.ECustomGameInstallStatus:\"k_ECustomGameInstallStatus_Unknown\x12\x0f\n\x07message\x18\x02 \x01(\t\x12#\n\x1blatest_timestamp_from_steam\x18\x03 \x01(\x07\"W\n\x13\x43MsgServerAvailable\x12@\n\x1a\x63ustom_game_install_status\x18\x01 \x01(\x0b\x32\x1c.CMsgCustomGameInstallStatus\"*\n\x16\x43MsgLANServerAvailable\x12\x10\n\x08lobby_id\x18\x01 \x01(\x06\"\xaa\x02\n\x18\x43SOEconGameAccountClient\x12$\n\x19\x61\x64\x64itional_backpack_slots\x18\x01 \x01(\r:\x01\x30\x12\x1c\n\rtrial_account\x18\x02 \x01(\x08:\x05\x66\x61lse\x12&\n\x18\x65ligible_for_online_play\x18\x03 \x01(\x08:\x04true\x12*\n\"need_to_choose_most_helpful_friend\x18\x04 \x01(\x08\x12\x17\n\x0fin_coaches_list\x18\x05 \x01(\x08\x12\x1c\n\x14trade_ban_expiration\x18\x06 \x01(\x07\x12\x1b\n\x13\x64uel_ban_expiration\x18\x07 \x01(\x07\x12\"\n\x13made_first_purchase\x18\t \x01(\x08:\x05\x66\x61lse\"J\n\x14\x43MsgApplyStrangePart\x12\x1c\n\x14strange_part_item_id\x18\x01 \x01(\x04\x12\x14\n\x0citem_item_id\x18\x02 \x01(\x04\"K\n\x17\x43MsgApplyPennantUpgrade\x12\x17\n\x0fupgrade_item_id\x18\x01 \x01(\x04\x12\x17\n\x0fpennant_item_id\x18\x02 \x01(\x04\"C\n\x13\x43MsgApplyEggEssence\x12\x17\n\x0f\x65ssence_item_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x65gg_item_id\x18\x02 \x01(\x04\"T\n\x14\x43SOEconItemAttribute\x12\x18\n\tdef_index\x18\x01 \x01(\r:\x05\x36\x35\x35\x33\x35\x12\r\n\x05value\x18\x02 \x01(\r\x12\x13\n\x0bvalue_bytes\x18\x03 \x01(\x0c\":\n\x13\x43SOEconItemEquipped\x12\x11\n\tnew_class\x18\x01 \x01(\r\x12\x10\n\x08new_slot\x18\x02 \x01(\r\"\xd7\x02\n\x0b\x43SOEconItem\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x12\n\naccount_id\x18\x02 \x01(\r\x12\x11\n\tinventory\x18\x03 \x01(\r\x12\x11\n\tdef_index\x18\x04 \x01(\r\x12\x13\n\x08quantity\x18\x05 \x01(\r:\x01\x31\x12\x10\n\x05level\x18\x06 \x01(\r:\x01\x31\x12\x12\n\x07quality\x18\x07 \x01(\r:\x01\x34\x12\x10\n\x05\x66lags\x18\x08 \x01(\r:\x01\x30\x12\x11\n\x06origin\x18\t \x01(\r:\x01\x30\x12(\n\tattribute\x18\x0c \x03(\x0b\x32\x15.CSOEconItemAttribute\x12#\n\rinterior_item\x18\r \x01(\x0b\x32\x0c.CSOEconItem\x12\x10\n\x05style\x18\x0f \x01(\r:\x01\x30\x12\x13\n\x0boriginal_id\x18\x10 \x01(\x04\x12,\n\x0e\x65quipped_state\x18\x12 \x03(\x0b\x32\x14.CSOEconItemEquipped\"\"\n\rCMsgSortItems\x12\x11\n\tsort_type\x18\x01 \x01(\r\"\x81\x01\n\x14\x43MsgItemAcknowledged\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x11\n\tinventory\x18\x02 \x01(\r\x12\x11\n\tdef_index\x18\x03 \x01(\r\x12\x0f\n\x07quality\x18\x04 \x01(\r\x12\x0e\n\x06rarity\x18\x05 \x01(\r\x12\x0e\n\x06origin\x18\x06 \x01(\r\"\x85\x01\n\x14\x43MsgSetItemPositions\x12:\n\x0eitem_positions\x18\x01 \x03(\x0b\x32\".CMsgSetItemPositions.ItemPosition\x1a\x31\n\x0cItemPosition\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x10\n\x08position\x18\x02 \x01(\r\"+\n\x19\x43MsgGCStorePurchaseCancel\x12\x0e\n\x06txn_id\x18\x01 \x01(\x04\"3\n!CMsgGCStorePurchaseCancelResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\"-\n\x1b\x43MsgGCStorePurchaseFinalize\x12\x0e\n\x06txn_id\x18\x01 \x01(\x04\"G\n#CMsgGCStorePurchaseFinalizeResponse\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x10\n\x08item_ids\x18\x02 \x03(\x04\"3\n\x1f\x43MsgGCToGCBannedWordListUpdated\x12\x10\n\x08group_id\x18\x01 \x01(\r\"?\n\x17\x43MsgGCToGCDirtySDOCache\x12\x10\n\x08sdo_type\x18\x01 \x01(\r\x12\x12\n\nkey_uint64\x18\x02 \x01(\x04\"\x14\n\x12\x43MsgSDONoMemcached\"/\n\x1b\x43MsgGCToGCUpdateSQLKeyValue\x12\x10\n\x08key_name\x18\x01 \x01(\t\"4\n\x1a\x43MsgGCServerVersionUpdated\x12\x16\n\x0eserver_version\x18\x01 \x01(\r\"4\n\x1a\x43MsgGCClientVersionUpdated\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\" \n\x1e\x43MsgGCToGCWebAPIAccountChanged\"\\\n\x0f\x43MsgExtractGems\x12\x14\n\x0ctool_item_id\x18\x01 \x01(\x04\x12\x14\n\x0citem_item_id\x18\x02 \x01(\x04\x12\x1d\n\x0eitem_socket_id\x18\x03 \x01(\r:\x05\x36\x35\x35\x33\x35\"\xd4\x02\n\x17\x43MsgExtractGemsResponse\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12P\n\x08response\x18\x02 \x01(\x0e\x32%.CMsgExtractGemsResponse.EExtractGems:\x17k_ExtractGems_Succeeded\"\xd5\x01\n\x0c\x45\x45xtractGems\x12\x1b\n\x17k_ExtractGems_Succeeded\x10\x00\x12&\n\"k_ExtractGems_Failed_ToolIsInvalid\x10\x01\x12&\n\"k_ExtractGems_Failed_ItemIsInvalid\x10\x02\x12,\n(k_ExtractGems_Failed_ToolCannotRemoveGem\x10\x03\x12*\n&k_ExtractGems_Failed_FailedToRemoveGem\x10\x04\"L\n\rCMsgAddSocket\x12\x14\n\x0ctool_item_id\x18\x01 \x01(\x04\x12\x14\n\x0citem_item_id\x18\x02 \x01(\x04\x12\x0f\n\x07unusual\x18\x03 \x01(\x08\"\xb9\x02\n\x15\x43MsgAddSocketResponse\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x1c\n\x14updated_socket_index\x18\x02 \x03(\r\x12J\n\x08response\x18\x03 \x01(\x0e\x32!.CMsgAddSocketResponse.EAddSocket:\x15k_AddSocket_Succeeded\"\xa4\x01\n\nEAddSocket\x12\x19\n\x15k_AddSocket_Succeeded\x10\x00\x12$\n k_AddSocket_Failed_ToolIsInvalid\x10\x01\x12+\n\'k_AddSocket_Failed_ItemCannotBeSocketed\x10\x02\x12(\n$k_AddSocket_Failed_FailedToAddSocket\x10\x03\"K\n\x17\x43MsgAddItemToSocketData\x12\x13\n\x0bgem_item_id\x18\x01 \x01(\x04\x12\x1b\n\x0csocket_index\x18\x02 \x01(\r:\x05\x36\x35\x35\x33\x35\"]\n\x13\x43MsgAddItemToSocket\x12\x14\n\x0citem_item_id\x18\x01 \x01(\x04\x12\x30\n\x0egems_to_socket\x18\x02 \x03(\x0b\x32\x18.CMsgAddItemToSocketData\"\xdf\x03\n\x1b\x43MsgAddItemToSocketResponse\x12\x14\n\x0citem_item_id\x18\x01 \x01(\x04\x12\x1c\n\x14updated_socket_index\x18\x02 \x03(\r\x12J\n\x08response\x18\x03 \x01(\x0e\x32$.CMsgAddItemToSocketResponse.EAddGem:\x12k_AddGem_Succeeded\"\xbf\x02\n\x07\x45\x41\x64\x64Gem\x12\x16\n\x12k_AddGem_Succeeded\x10\x00\x12 \n\x1ck_AddGem_Failed_GemIsInvalid\x10\x01\x12!\n\x1dk_AddGem_Failed_ItemIsInvalid\x10\x02\x12\"\n\x1ek_AddGem_Failed_FailedToAddGem\x10\x03\x12+\n\'k_AddGem_Failed_InvalidGemTypeForSocket\x10\x04\x12)\n%k_AddGem_Failed_InvalidGemTypeForHero\x10\x05\x12)\n%k_AddGem_Failed_InvalidGemTypeForSlot\x10\x06\x12\x30\n,k_AddGem_Failed_SocketContainsUnremovableGem\x10\x07\"M\n\x18\x43MsgResetStrangeGemCount\x12\x14\n\x0citem_item_id\x18\x01 \x01(\x04\x12\x1b\n\x0csocket_index\x18\x02 \x01(\r:\x05\x36\x35\x35\x33\x35\"\xbe\x02\n CMsgResetStrangeGemCountResponse\x12S\n\x08response\x18\x01 \x01(\x0e\x32+.CMsgResetStrangeGemCountResponse.EResetGem:\x14k_ResetGem_Succeeded\"\xc4\x01\n\tEResetGem\x12\x18\n\x14k_ResetGem_Succeeded\x10\x00\x12&\n\"k_ResetGem_Failed_FailedToResetGem\x10\x01\x12#\n\x1fk_ResetGem_Failed_ItemIsInvalid\x10\x02\x12%\n!k_ResetGem_Failed_InvalidSocketId\x10\x03\x12)\n%k_ResetGem_Failed_SocketCannotBeReset\x10\x04\"[\n\x1d\x43MsgGCToClientPollFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\r\x12\x0f\n\x07poll_id\x18\x03 \x01(\r\"V\n\x1e\x43MsgGCToClientPollFileResponse\x12\x0f\n\x07poll_id\x18\x01 \x01(\r\x12\x11\n\tfile_size\x18\x02 \x01(\r\x12\x10\n\x08\x66ile_crc\x18\x03 \x01(\r\">\n\x19\x43MsgGCToGCPerformManualOp\x12\r\n\x05op_id\x18\x01 \x01(\x04\x12\x12\n\ngroup_code\x18\x02 \x01(\r\"L\n\"CMsgGCToGCPerformManualOpCompleted\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\tsource_gc\x18\x02 \x01(\x05:\x02-1\"&\n$CMsgGCToGCReloadServerRegionSettings\"K\n\x1e\x43MsgGCAdditionalWelcomeMsgList\x12)\n\x10welcome_messages\x18\x01 \x03(\x0b\x32\x0f.CExtraMsgBlock\"\xd0\x01\n\x16\x43MsgApplyRemoteConVars\x12\x30\n\x08\x63on_vars\x18\x01 \x03(\x0b\x32\x1e.CMsgApplyRemoteConVars.ConVar\x1a\x83\x01\n\x06\x43onVar\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x13\n\x0bversion_min\x18\x03 \x01(\r\x12\x13\n\x0bversion_max\x18\x04 \x01(\r\x12\x32\n\x08platform\x18\x05 \x01(\x0e\x32\x0c.EGCPlatform:\x12k_eGCPlatform_None\"H\n CMsgGCToClientApplyRemoteConVars\x12$\n\x03msg\x18\x01 \x01(\x0b\x32\x17.CMsgApplyRemoteConVars\"H\n CMsgGCToServerApplyRemoteConVars\x12$\n\x03msg\x18\x01 \x01(\x0b\x32\x17.CMsgApplyRemoteConVars\"\xd4\x01\n\x1d\x43MsgClientToGCIntegrityStatus\x12\x0e\n\x06report\x18\x01 \x01(\t\x12\x16\n\x0esecure_allowed\x18\x02 \x01(\x08\x12<\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\'.CMsgClientToGCIntegrityStatus.keyvalue\x1aM\n\x08keyvalue\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x65xtended\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\x04\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\"\x9a\x01\n\x1e\x43MsgClientToGCAggregateMetrics\x12=\n\x07metrics\x18\x01 \x03(\x0b\x32,.CMsgClientToGCAggregateMetrics.SingleMetric\x1a\x39\n\x0cSingleMetric\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x12\x14\n\x0cmetric_count\x18\x02 \x01(\r\"E\n%CMsgGCToClientAggregateMetricsBackoff\x12\x1c\n\x14upload_rate_modifier\x18\x01 \x01(\x02*\x98\x06\n\nEGCBaseMsg\x12\x1a\n\x15k_EMsgGCInviteToParty\x10\x95#\x12\x1e\n\x19k_EMsgGCInvitationCreated\x10\x96#\x12 \n\x1bk_EMsgGCPartyInviteResponse\x10\x97#\x12\x1a\n\x15k_EMsgGCKickFromParty\x10\x98#\x12\x17\n\x12k_EMsgGCLeaveParty\x10\x99#\x12\x1c\n\x17k_EMsgGCServerAvailable\x10\x9a#\x12\"\n\x1dk_EMsgGCClientConnectToServer\x10\x9b#\x12\x1b\n\x16k_EMsgGCGameServerInfo\x10\x9c#\x12\x1f\n\x1ak_EMsgGCLANServerAvailable\x10\x9f#\x12\x1a\n\x15k_EMsgGCInviteToLobby\x10\xa0#\x12 \n\x1bk_EMsgGCLobbyInviteResponse\x10\xa1#\x12$\n\x1fk_EMsgGCToClientPollFileRequest\x10\xa2#\x12%\n k_EMsgGCToClientPollFileResponse\x10\xa3#\x12 \n\x1bk_EMsgGCToGCPerformManualOp\x10\xa4#\x12)\n$k_EMsgGCToGCPerformManualOpCompleted\x10\xa5#\x12+\n&k_EMsgGCToGCReloadServerRegionSettings\x10\xa6#\x12%\n k_EMsgGCAdditionalWelcomeMsgList\x10\xa7#\x12\'\n\"k_EMsgGCToClientApplyRemoteConVars\x10\xa8#\x12\'\n\"k_EMsgGCToServerApplyRemoteConVars\x10\xa9#\x12$\n\x1fk_EMsgClientToGCIntegrityStatus\x10\xaa#\x12%\n k_EMsgClientToGCAggregateMetrics\x10\xab#\x12,\n\'k_EMsgGCToClientAggregateMetricsBackoff\x10\xac#*\xe8\x03\n\x18\x45\x43ustomGameInstallStatus\x12&\n\"k_ECustomGameInstallStatus_Unknown\x10\x00\x12$\n k_ECustomGameInstallStatus_Ready\x10\x01\x12#\n\x1fk_ECustomGameInstallStatus_Busy\x10\x02\x12,\n(k_ECustomGameInstallStatus_FailedGeneric\x10\x65\x12\x32\n.k_ECustomGameInstallStatus_FailedInternalError\x10\x66\x12\x37\n3k_ECustomGameInstallStatus_RequestedTimestampTooOld\x10g\x12\x37\n3k_ECustomGameInstallStatus_RequestedTimestampTooNew\x10h\x12*\n&k_ECustomGameInstallStatus_CRCMismatch\x10i\x12*\n&k_ECustomGameInstallStatus_FailedSteam\x10j\x12-\n)k_ECustomGameInstallStatus_FailedCanceled\x10k')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_gcmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['relay_codes']._loaded_options = None
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['relay_codes']._serialized_options = b'\020\001'
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['relay_pings']._loaded_options = None
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['relay_pings']._serialized_options = b'\020\001'
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['region_codes']._loaded_options = None
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['region_codes']._serialized_options = b'\020\001'
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['region_pings']._loaded_options = None
  _globals['_CMSGCLIENTPINGDATA'].fields_by_name['region_pings']._serialized_options = b'\020\001'
  _globals['_EGCBASEMSG']._serialized_start=6512
  _globals['_EGCBASEMSG']._serialized_end=7304
  _globals['_ECUSTOMGAMEINSTALLSTATUS']._serialized_start=7307
  _globals['_ECUSTOMGAMEINSTALLSTATUS']._serialized_end=7795
  _globals['_CGCSTOREPURCHASEINIT_LINEITEM']._serialized_start=71
  _globals['_CGCSTOREPURCHASEINIT_LINEITEM']._serialized_end=246
  _globals['_CMSGGCSTOREPURCHASEINIT']._serialized_start=249
  _globals['_CMSGGCSTOREPURCHASEINIT']._serialized_end=379
  _globals['_CMSGGCSTOREPURCHASEINITRESPONSE']._serialized_start=381
  _globals['_CMSGGCSTOREPURCHASEINITRESPONSE']._serialized_end=446
  _globals['_CMSGCLIENTPINGDATA']._serialized_start=449
  _globals['_CMSGCLIENTPINGDATA']._serialized_end=607
  _globals['_CMSGINVITETOPARTY']._serialized_start=610
  _globals['_CMSGINVITETOPARTY']._serialized_end=746
  _globals['_CMSGINVITETOLOBBY']._serialized_start=748
  _globals['_CMSGINVITETOLOBBY']._serialized_end=809
  _globals['_CMSGINVITATIONCREATED']._serialized_start=811
  _globals['_CMSGINVITATIONCREATED']._serialized_end=892
  _globals['_CMSGPARTYINVITERESPONSE']._serialized_start=894
  _globals['_CMSGPARTYINVITERESPONSE']._serialized_end=1017
  _globals['_CMSGLOBBYINVITERESPONSE']._serialized_start=1020
  _globals['_CMSGLOBBYINVITERESPONSE']._serialized_end=1159
  _globals['_CMSGKICKFROMPARTY']._serialized_start=1161
  _globals['_CMSGKICKFROMPARTY']._serialized_end=1198
  _globals['_CMSGLEAVEPARTY']._serialized_start=1200
  _globals['_CMSGLEAVEPARTY']._serialized_end=1216
  _globals['_CMSGCUSTOMGAMEINSTALLSTATUS']._serialized_start=1219
  _globals['_CMSGCUSTOMGAMEINSTALLSTATUS']._serialized_end=1381
  _globals['_CMSGSERVERAVAILABLE']._serialized_start=1383
  _globals['_CMSGSERVERAVAILABLE']._serialized_end=1470
  _globals['_CMSGLANSERVERAVAILABLE']._serialized_start=1472
  _globals['_CMSGLANSERVERAVAILABLE']._serialized_end=1514
  _globals['_CSOECONGAMEACCOUNTCLIENT']._serialized_start=1517
  _globals['_CSOECONGAMEACCOUNTCLIENT']._serialized_end=1815
  _globals['_CMSGAPPLYSTRANGEPART']._serialized_start=1817
  _globals['_CMSGAPPLYSTRANGEPART']._serialized_end=1891
  _globals['_CMSGAPPLYPENNANTUPGRADE']._serialized_start=1893
  _globals['_CMSGAPPLYPENNANTUPGRADE']._serialized_end=1968
  _globals['_CMSGAPPLYEGGESSENCE']._serialized_start=1970
  _globals['_CMSGAPPLYEGGESSENCE']._serialized_end=2037
  _globals['_CSOECONITEMATTRIBUTE']._serialized_start=2039
  _globals['_CSOECONITEMATTRIBUTE']._serialized_end=2123
  _globals['_CSOECONITEMEQUIPPED']._serialized_start=2125
  _globals['_CSOECONITEMEQUIPPED']._serialized_end=2183
  _globals['_CSOECONITEM']._serialized_start=2186
  _globals['_CSOECONITEM']._serialized_end=2529
  _globals['_CMSGSORTITEMS']._serialized_start=2531
  _globals['_CMSGSORTITEMS']._serialized_end=2565
  _globals['_CMSGITEMACKNOWLEDGED']._serialized_start=2568
  _globals['_CMSGITEMACKNOWLEDGED']._serialized_end=2697
  _globals['_CMSGSETITEMPOSITIONS']._serialized_start=2700
  _globals['_CMSGSETITEMPOSITIONS']._serialized_end=2833
  _globals['_CMSGSETITEMPOSITIONS_ITEMPOSITION']._serialized_start=2784
  _globals['_CMSGSETITEMPOSITIONS_ITEMPOSITION']._serialized_end=2833
  _globals['_CMSGGCSTOREPURCHASECANCEL']._serialized_start=2835
  _globals['_CMSGGCSTOREPURCHASECANCEL']._serialized_end=2878
  _globals['_CMSGGCSTOREPURCHASECANCELRESPONSE']._serialized_start=2880
  _globals['_CMSGGCSTOREPURCHASECANCELRESPONSE']._serialized_end=2931
  _globals['_CMSGGCSTOREPURCHASEFINALIZE']._serialized_start=2933
  _globals['_CMSGGCSTOREPURCHASEFINALIZE']._serialized_end=2978
  _globals['_CMSGGCSTOREPURCHASEFINALIZERESPONSE']._serialized_start=2980
  _globals['_CMSGGCSTOREPURCHASEFINALIZERESPONSE']._serialized_end=3051
  _globals['_CMSGGCTOGCBANNEDWORDLISTUPDATED']._serialized_start=3053
  _globals['_CMSGGCTOGCBANNEDWORDLISTUPDATED']._serialized_end=3104
  _globals['_CMSGGCTOGCDIRTYSDOCACHE']._serialized_start=3106
  _globals['_CMSGGCTOGCDIRTYSDOCACHE']._serialized_end=3169
  _globals['_CMSGSDONOMEMCACHED']._serialized_start=3171
  _globals['_CMSGSDONOMEMCACHED']._serialized_end=3191
  _globals['_CMSGGCTOGCUPDATESQLKEYVALUE']._serialized_start=3193
  _globals['_CMSGGCTOGCUPDATESQLKEYVALUE']._serialized_end=3240
  _globals['_CMSGGCSERVERVERSIONUPDATED']._serialized_start=3242
  _globals['_CMSGGCSERVERVERSIONUPDATED']._serialized_end=3294
  _globals['_CMSGGCCLIENTVERSIONUPDATED']._serialized_start=3296
  _globals['_CMSGGCCLIENTVERSIONUPDATED']._serialized_end=3348
  _globals['_CMSGGCTOGCWEBAPIACCOUNTCHANGED']._serialized_start=3350
  _globals['_CMSGGCTOGCWEBAPIACCOUNTCHANGED']._serialized_end=3382
  _globals['_CMSGEXTRACTGEMS']._serialized_start=3384
  _globals['_CMSGEXTRACTGEMS']._serialized_end=3476
  _globals['_CMSGEXTRACTGEMSRESPONSE']._serialized_start=3479
  _globals['_CMSGEXTRACTGEMSRESPONSE']._serialized_end=3819
  _globals['_CMSGEXTRACTGEMSRESPONSE_EEXTRACTGEMS']._serialized_start=3606
  _globals['_CMSGEXTRACTGEMSRESPONSE_EEXTRACTGEMS']._serialized_end=3819
  _globals['_CMSGADDSOCKET']._serialized_start=3821
  _globals['_CMSGADDSOCKET']._serialized_end=3897
  _globals['_CMSGADDSOCKETRESPONSE']._serialized_start=3900
  _globals['_CMSGADDSOCKETRESPONSE']._serialized_end=4213
  _globals['_CMSGADDSOCKETRESPONSE_EADDSOCKET']._serialized_start=4049
  _globals['_CMSGADDSOCKETRESPONSE_EADDSOCKET']._serialized_end=4213
  _globals['_CMSGADDITEMTOSOCKETDATA']._serialized_start=4215
  _globals['_CMSGADDITEMTOSOCKETDATA']._serialized_end=4290
  _globals['_CMSGADDITEMTOSOCKET']._serialized_start=4292
  _globals['_CMSGADDITEMTOSOCKET']._serialized_end=4385
  _globals['_CMSGADDITEMTOSOCKETRESPONSE']._serialized_start=4388
  _globals['_CMSGADDITEMTOSOCKETRESPONSE']._serialized_end=4867
  _globals['_CMSGADDITEMTOSOCKETRESPONSE_EADDGEM']._serialized_start=4548
  _globals['_CMSGADDITEMTOSOCKETRESPONSE_EADDGEM']._serialized_end=4867
  _globals['_CMSGRESETSTRANGEGEMCOUNT']._serialized_start=4869
  _globals['_CMSGRESETSTRANGEGEMCOUNT']._serialized_end=4946
  _globals['_CMSGRESETSTRANGEGEMCOUNTRESPONSE']._serialized_start=4949
  _globals['_CMSGRESETSTRANGEGEMCOUNTRESPONSE']._serialized_end=5267
  _globals['_CMSGRESETSTRANGEGEMCOUNTRESPONSE_ERESETGEM']._serialized_start=5071
  _globals['_CMSGRESETSTRANGEGEMCOUNTRESPONSE_ERESETGEM']._serialized_end=5267
  _globals['_CMSGGCTOCLIENTPOLLFILEREQUEST']._serialized_start=5269
  _globals['_CMSGGCTOCLIENTPOLLFILEREQUEST']._serialized_end=5360
  _globals['_CMSGGCTOCLIENTPOLLFILERESPONSE']._serialized_start=5362
  _globals['_CMSGGCTOCLIENTPOLLFILERESPONSE']._serialized_end=5448
  _globals['_CMSGGCTOGCPERFORMMANUALOP']._serialized_start=5450
  _globals['_CMSGGCTOGCPERFORMMANUALOP']._serialized_end=5512
  _globals['_CMSGGCTOGCPERFORMMANUALOPCOMPLETED']._serialized_start=5514
  _globals['_CMSGGCTOGCPERFORMMANUALOPCOMPLETED']._serialized_end=5590
  _globals['_CMSGGCTOGCRELOADSERVERREGIONSETTINGS']._serialized_start=5592
  _globals['_CMSGGCTOGCRELOADSERVERREGIONSETTINGS']._serialized_end=5630
  _globals['_CMSGGCADDITIONALWELCOMEMSGLIST']._serialized_start=5632
  _globals['_CMSGGCADDITIONALWELCOMEMSGLIST']._serialized_end=5707
  _globals['_CMSGAPPLYREMOTECONVARS']._serialized_start=5710
  _globals['_CMSGAPPLYREMOTECONVARS']._serialized_end=5918
  _globals['_CMSGAPPLYREMOTECONVARS_CONVAR']._serialized_start=5787
  _globals['_CMSGAPPLYREMOTECONVARS_CONVAR']._serialized_end=5918
  _globals['_CMSGGCTOCLIENTAPPLYREMOTECONVARS']._serialized_start=5920
  _globals['_CMSGGCTOCLIENTAPPLYREMOTECONVARS']._serialized_end=5992
  _globals['_CMSGGCTOSERVERAPPLYREMOTECONVARS']._serialized_start=5994
  _globals['_CMSGGCTOSERVERAPPLYREMOTECONVARS']._serialized_end=6066
  _globals['_CMSGCLIENTTOGCINTEGRITYSTATUS']._serialized_start=6069
  _globals['_CMSGCLIENTTOGCINTEGRITYSTATUS']._serialized_end=6281
  _globals['_CMSGCLIENTTOGCINTEGRITYSTATUS_KEYVALUE']._serialized_start=6204
  _globals['_CMSGCLIENTTOGCINTEGRITYSTATUS_KEYVALUE']._serialized_end=6281
  _globals['_CMSGCLIENTTOGCAGGREGATEMETRICS']._serialized_start=6284
  _globals['_CMSGCLIENTTOGCAGGREGATEMETRICS']._serialized_end=6438
  _globals['_CMSGCLIENTTOGCAGGREGATEMETRICS_SINGLEMETRIC']._serialized_start=6381
  _globals['_CMSGCLIENTTOGCAGGREGATEMETRICS_SINGLEMETRIC']._serialized_end=6438
  _globals['_CMSGGCTOCLIENTAGGREGATEMETRICSBACKOFF']._serialized_start=6440
  _globals['_CMSGGCTOCLIENTAGGREGATEMETRICSBACKOFF']._serialized_end=6509
# @@protoc_insertion_point(module_scope)
