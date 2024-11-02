# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gcsdk_gcmessages.proto
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
    'gcsdk_gcmessages.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steammessages_pb2 as steammessages__pb2
from steammessages_steamlearn import steamworkssdk_pb2 as steammessages__steamlearn_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16gcsdk_gcmessages.proto\x1a\x13steammessages.proto\x1a,steammessages_steamlearn.steamworkssdk.proto\"\\\n\x0e\x43\x45xtraMsgBlock\x12\x10\n\x08msg_type\x18\x01 \x01(\r\x12\x10\n\x08\x63ontents\x18\x02 \x01(\x0c\x12\x0f\n\x07msg_key\x18\x03 \x01(\x04\x12\x15\n\ris_compressed\x18\x04 \x01(\x08\"\xb0\x02\n\x18\x43MsgSteamLearnServerInfo\x12\x32\n\raccess_tokens\x18\x04 \x01(\x0b\x32\x1b.CMsgSteamLearnAccessTokens\x12<\n\rproject_infos\x18\x05 \x03(\x0b\x32%.CMsgSteamLearnServerInfo.ProjectInfo\x1a\xa1\x01\n\x0bProjectInfo\x12\x12\n\nproject_id\x18\x01 \x01(\r\x12\"\n\x1asnapshot_published_version\x18\x02 \x01(\r\x12#\n\x1binference_published_version\x18\x03 \x01(\r\x12\x1b\n\x13snapshot_percentage\x18\x06 \x01(\r\x12\x18\n\x10snapshot_enabled\x18\x07 \x01(\x08\"A\n\x13\x43MsgGCAssertJobData\x12\x14\n\x0cmessage_type\x18\x01 \x01(\t\x12\x14\n\x0cmessage_data\x18\x02 \x01(\x0c\"#\n\x10\x43MsgGCConCommand\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\"{\n\rCMsgSDOAssert\x12\x10\n\x08sdo_type\x18\x01 \x01(\x05\x12(\n\x08requests\x18\x02 \x03(\x0b\x32\x16.CMsgSDOAssert.Request\x1a.\n\x07Request\x12\x0b\n\x03key\x18\x01 \x03(\x04\x12\x16\n\x0erequesting_job\x18\x02 \x01(\t\")\n\rCMsgSOIDOwner\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\x04\"\x83\x01\n\x12\x43MsgSOSingleObject\x12\x0f\n\x07type_id\x18\x02 \x01(\x05\x12\x13\n\x0bobject_data\x18\x03 \x01(\x0c\x12\x0f\n\x07version\x18\x04 \x01(\x06\x12\"\n\nowner_soid\x18\x05 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x12\n\nservice_id\x18\x06 \x01(\r\"\xdb\x02\n\x15\x43MsgSOMultipleObjects\x12=\n\x10objects_modified\x18\x02 \x03(\x0b\x32#.CMsgSOMultipleObjects.SingleObject\x12\x0f\n\x07version\x18\x03 \x01(\x06\x12:\n\robjects_added\x18\x04 \x03(\x0b\x32#.CMsgSOMultipleObjects.SingleObject\x12<\n\x0fobjects_removed\x18\x05 \x03(\x0b\x32#.CMsgSOMultipleObjects.SingleObject\x12\"\n\nowner_soid\x18\x06 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x12\n\nservice_id\x18\x07 \x01(\r\x1a@\n\x0cSingleObject\x12\x0f\n\x07type_id\x18\x01 \x01(\x05\x12\x13\n\x0bobject_data\x18\x02 \x01(\x0c:\n\x80\xa6\x1d\x80\x02\x88\xa6\x1d\x80\x08\"\xfc\x01\n\x15\x43MsgSOCacheSubscribed\x12\x36\n\x07objects\x18\x02 \x03(\x0b\x32%.CMsgSOCacheSubscribed.SubscribedType\x12\x0f\n\x07version\x18\x03 \x01(\x06\x12\"\n\nowner_soid\x18\x04 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x12\n\nservice_id\x18\x05 \x01(\r\x12\x14\n\x0cservice_list\x18\x06 \x03(\r\x12\x14\n\x0csync_version\x18\x07 \x01(\x06\x1a\x36\n\x0eSubscribedType\x12\x0f\n\x07type_id\x18\x01 \x01(\x05\x12\x13\n\x0bobject_data\x18\x02 \x03(\x0c\"\x94\x01\n\x1d\x43MsgSOCacheSubscribedUpToDate\x12\x0f\n\x07version\x18\x01 \x01(\x06\x12\"\n\nowner_soid\x18\x02 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x12\n\nservice_id\x18\x03 \x01(\r\x12\x14\n\x0cservice_list\x18\x04 \x03(\r\x12\x14\n\x0csync_version\x18\x05 \x01(\x06\"=\n\x17\x43MsgSOCacheUnsubscribed\x12\"\n\nowner_soid\x18\x02 \x01(\x0b\x32\x0e.CMsgSOIDOwner\"\x93\x01\n\x1c\x43MsgSOCacheSubscriptionCheck\x12\x0f\n\x07version\x18\x02 \x01(\x06\x12\"\n\nowner_soid\x18\x03 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x12\n\nservice_id\x18\x04 \x01(\r\x12\x14\n\x0cservice_list\x18\x05 \x03(\r\x12\x14\n\x0csync_version\x18\x06 \x01(\x06\"D\n\x1e\x43MsgSOCacheSubscriptionRefresh\x12\"\n\nowner_soid\x18\x02 \x01(\x0b\x32\x0e.CMsgSOIDOwner\"%\n\x12\x43MsgSOCacheVersion\x12\x0f\n\x07version\x18\x01 \x01(\x06\"L\n\x16\x43MsgGCMultiplexMessage\x12\x0f\n\x07msgtype\x18\x01 \x01(\r\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x10\n\x08steamids\x18\x03 \x03(\x06\"0\n\x17\x43MsgGCToGCSubGCStarting\x12\x15\n\tdir_index\x18\x01 \x01(\x05:\x02-1\"\xc3\x01\n\x13\x43GCToGCMsgMasterAck\x12\x15\n\tdir_index\x18\x01 \x01(\x05:\x02-1\x12\x14\n\x0cmachine_name\x18\x03 \x01(\t\x12\x14\n\x0cprocess_name\x18\x04 \x01(\t\x12/\n\tdirectory\x18\x06 \x03(\x0b\x32\x1c.CGCToGCMsgMasterAck.Process\x1a\x38\n\x07Process\x12\x15\n\tdir_index\x18\x01 \x01(\x05:\x02-1\x12\x16\n\x0etype_instances\x18\x02 \x03(\r\"2\n\x1c\x43GCToGCMsgMasterAck_Response\x12\x12\n\x07\x65result\x18\x01 \x01(\x05:\x01\x32\"7\n\x19\x43MsgGCToGCUniverseStartup\x12\x1a\n\x12is_initial_startup\x18\x01 \x01(\x08\"4\n!CMsgGCToGCUniverseStartupResponse\x12\x0f\n\x07\x65result\x18\x01 \x01(\x05\"\x92\x01\n\x1f\x43GCToGCMsgMasterStartupComplete\x12\x38\n\x07gc_info\x18\x01 \x03(\x0b\x32\'.CGCToGCMsgMasterStartupComplete.GCInfo\x1a\x35\n\x06GCInfo\x12\x15\n\tdir_index\x18\x01 \x01(\x05:\x02-1\x12\x14\n\x0cmachine_name\x18\x02 \x01(\t\"L\n\x10\x43GCToGCMsgRouted\x12\x10\n\x08msg_type\x18\x01 \x01(\r\x12\x11\n\tsender_id\x18\x02 \x01(\x06\x12\x13\n\x0bnet_message\x18\x03 \x01(\x0c\">\n\x15\x43GCToGCMsgRoutedReply\x12\x10\n\x08msg_type\x18\x01 \x01(\r\x12\x13\n\x0bnet_message\x18\x02 \x01(\x0c\"\x95\x01\n\x1c\x43MsgGCUpdateSubGCSessionInfo\x12\x39\n\x07updates\x18\x01 \x03(\x0b\x32(.CMsgGCUpdateSubGCSessionInfo.CMsgUpdate\x1a:\n\nCMsgUpdate\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\n\n\x02ip\x18\x02 \x01(\x07\x12\x0f\n\x07trusted\x18\x03 \x01(\x08\"0\n\x1d\x43MsgGCRequestSubGCSessionInfo\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\"c\n%CMsgGCRequestSubGCSessionInfoResponse\x12\n\n\x02ip\x18\x01 \x01(\x07\x12\x0f\n\x07trusted\x18\x02 \x01(\x08\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x0f\n\x07success\x18\x04 \x01(\x08\"x\n\x16\x43MsgSOCacheHaveVersion\x12\x1c\n\x04soid\x18\x01 \x01(\x0b\x32\x0e.CMsgSOIDOwner\x12\x0f\n\x07version\x18\x02 \x01(\x06\x12\x12\n\nservice_id\x18\x03 \x01(\r\x12\x1b\n\x13\x63\x61\x63hed_file_version\x18\x04 \x01(\r\"\xff\x04\n\x0f\x43MsgClientHello\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x36\n\x15socache_have_versions\x18\x02 \x03(\x0b\x32\x17.CMsgSOCacheHaveVersion\x12\x1b\n\x13\x63lient_session_need\x18\x03 \x01(\r\x12:\n\x0f\x63lient_launcher\x18\x04 \x01(\x0e\x32\x13.PartnerAccountType:\x0cPARTNER_NONE\x12\x12\n\nsecret_key\x18\x05 \x01(\t\x12\x17\n\x0f\x63lient_language\x18\x06 \x01(\r\x12-\n\x06\x65ngine\x18\x07 \x01(\x0e\x32\x0e.ESourceEngine:\rk_ESE_Source1\x12\x1b\n\x13steamdatagram_login\x18\x08 \x01(\x0c\x12\x13\n\x0bplatform_id\x18\t \x01(\r\x12\x10\n\x08game_msg\x18\n \x01(\x0c\x12\x0f\n\x07os_type\x18\x0b \x01(\x05\x12\x15\n\rrender_system\x18\x0c \x01(\r\x12\x19\n\x11render_system_req\x18\r \x01(\r\x12\x14\n\x0cscreen_width\x18\x0e \x01(\r\x12\x15\n\rscreen_height\x18\x0f \x01(\r\x12\x16\n\x0escreen_refresh\x18\x10 \x01(\r\x12\x14\n\x0crender_width\x18\x11 \x01(\r\x12\x15\n\rrender_height\x18\x12 \x01(\r\x12\x12\n\nswap_width\x18\x13 \x01(\r\x12\x13\n\x0bswap_height\x18\x14 \x01(\r\x12\x16\n\x0eis_steam_china\x18\x16 \x01(\x08\x12\x1d\n\x15is_steam_china_client\x18\x18 \x01(\x08\x12\x15\n\rplatform_name\x18\x17 \x01(\t\"\x82\x05\n\x11\x43MsgClientWelcome\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x11\n\tgame_data\x18\x02 \x01(\x0c\x12;\n\x1boutofdate_subscribed_caches\x18\x03 \x03(\x0b\x32\x16.CMsgSOCacheSubscribed\x12\x41\n\x1auptodate_subscribed_caches\x18\x04 \x03(\x0b\x32\x1d.CMsgSOCacheSubscriptionCheck\x12-\n\x08location\x18\x05 \x01(\x0b\x32\x1b.CMsgClientWelcome.Location\x12\x1f\n\x17gc_socache_file_version\x18\t \x01(\r\x12\x18\n\x10txn_country_code\x18\n \x01(\t\x12\x12\n\ngame_data2\x18\x0b \x01(\x0c\x12$\n\x1crtime32_gc_welcome_timestamp\x18\x0c \x01(\r\x12\x10\n\x08\x63urrency\x18\r \x01(\r\x12\x0f\n\x07\x62\x61lance\x18\x0e \x01(\r\x12\x13\n\x0b\x62\x61lance_url\x18\x0f \x01(\t\x12\x1e\n\x16has_accepted_china_ssa\x18\x10 \x01(\x08\x12\x1d\n\x15is_banned_steam_china\x18\x11 \x01(\x08\x12\x30\n\x17\x61\x64\x64itional_welcome_msgs\x18\x12 \x01(\x0b\x32\x0f.CExtraMsgBlock\x12:\n\x17steam_learn_server_info\x18\x14 \x01(\x0b\x32\x19.CMsgSteamLearnServerInfo\x1a@\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\"\xe5\x01\n\x14\x43MsgConnectionStatus\x12\x44\n\x06status\x18\x01 \x01(\x0e\x32\x13.GCConnectionStatus:\x1fGCConnectionStatus_HAVE_SESSION\x12\x1b\n\x13\x63lient_session_need\x18\x02 \x01(\r\x12\x16\n\x0equeue_position\x18\x03 \x01(\x05\x12\x12\n\nqueue_size\x18\x04 \x01(\x05\x12\x14\n\x0cwait_seconds\x18\x05 \x01(\x05\x12(\n estimated_wait_seconds_remaining\x18\x06 \x01(\x05\"\xf8\x01\n\x1a\x43MsgGCToGCSOCacheSubscribe\x12\x12\n\nsubscriber\x18\x01 \x01(\x06\x12\x17\n\x0fsubscribe_to_id\x18\x02 \x01(\x06\x12\x14\n\x0csync_version\x18\x03 \x01(\x06\x12\x43\n\rhave_versions\x18\x04 \x03(\x0b\x32,.CMsgGCToGCSOCacheSubscribe.CMsgHaveVersions\x12\x19\n\x11subscribe_to_type\x18\x05 \x01(\r\x1a\x37\n\x10\x43MsgHaveVersions\x12\x12\n\nservice_id\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\x04\"n\n\x1c\x43MsgGCToGCSOCacheUnsubscribe\x12\x12\n\nsubscriber\x18\x01 \x01(\x06\x12\x1b\n\x13unsubscribe_from_id\x18\x02 \x01(\x06\x12\x1d\n\x15unsubscribe_from_type\x18\x03 \x01(\r\"\x12\n\x10\x43MsgGCClientPing\"\x8a\x01\n\x1f\x43MsgGCToGCForwardAccountDetails\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x41\n\x0f\x61\x63\x63ount_details\x18\x02 \x01(\x0b\x32(.CGCSystemMsg_GetAccountDetails_Response\x12\x13\n\x0b\x61ge_seconds\x18\x03 \x01(\r\"u\n\x1c\x43MsgGCToGCLoadSessionSOCache\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x41\n\x17\x66orward_account_details\x18\x02 \x01(\x0b\x32 .CMsgGCToGCForwardAccountDetails\"&\n$CMsgGCToGCLoadSessionSOCacheResponse\"f\n\x1c\x43MsgGCToGCUpdateSessionStats\x12\x15\n\ruser_sessions\x18\x01 \x01(\r\x12\x17\n\x0fserver_sessions\x18\x02 \x01(\r\x12\x16\n\x0ein_logon_surge\x18\x03 \x01(\x08\"\x1e\n\x1c\x43MsgGCToClientRequestDropped\"\xed\x02\n*CWorkshop_PopulateItemDescriptions_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\\\n\tlanguages\x18\x02 \x03(\x0b\x32I.CWorkshop_PopulateItemDescriptions_Request.ItemDescriptionsLanguageBlock\x1a\x45\n\x15SingleItemDescription\x12\x12\n\ngameitemid\x18\x01 \x01(\r\x12\x18\n\x10item_description\x18\x02 \x01(\t\x1a\x8a\x01\n\x1dItemDescriptionsLanguageBlock\x12\x10\n\x08language\x18\x01 \x01(\t\x12W\n\x0c\x64\x65scriptions\x18\x02 \x03(\x0b\x32\x41.CWorkshop_PopulateItemDescriptions_Request.SingleItemDescription\"F\n!CWorkshop_GetContributors_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\ngameitemid\x18\x02 \x01(\r\":\n\"CWorkshop_GetContributors_Response\x12\x14\n\x0c\x63ontributors\x18\x01 \x03(\x06\"\xf5\x05\n%CWorkshop_SetItemPaymentRules_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x12\n\ngameitemid\x18\x02 \x01(\r\x12\x61\n\x19\x61ssociated_workshop_files\x18\x03 \x03(\x0b\x32>.CWorkshop_SetItemPaymentRules_Request.WorkshopItemPaymentRule\x12W\n\x10partner_accounts\x18\x04 \x03(\x0b\x32=.CWorkshop_SetItemPaymentRules_Request.PartnerItemPaymentRule\x12\x15\n\rvalidate_only\x18\x05 \x01(\x08\x12(\n make_workshop_files_subscribable\x18\x06 \x01(\x08\x12v\n,associated_workshop_file_for_direct_payments\x18\x07 \x01(\x0b\x32@.CWorkshop_SetItemPaymentRules_Request.WorkshopDirectPaymentRule\x1a\x7f\n\x17WorkshopItemPaymentRule\x12\x18\n\x10workshop_file_id\x18\x01 \x01(\x04\x12\x1a\n\x12revenue_percentage\x18\x02 \x01(\x02\x12\x18\n\x10rule_description\x18\x03 \x01(\t\x12\x14\n\trule_type\x18\x04 \x01(\r:\x01\x31\x1aO\n\x19WorkshopDirectPaymentRule\x12\x18\n\x10workshop_file_id\x18\x01 \x01(\x04\x12\x18\n\x10rule_description\x18\x02 \x01(\t\x1a\x62\n\x16PartnerItemPaymentRule\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x1a\n\x12revenue_percentage\x18\x02 \x01(\x02\x12\x18\n\x10rule_description\x18\x03 \x01(\t\"C\n&CWorkshop_SetItemPaymentRules_Response\x12\x19\n\x11validation_errors\x18\x01 \x03(\t\"\xf4\x01\n\x1f\x43\x43ommunity_ClanAnnouncementInfo\x12\x0b\n\x03gid\x18\x01 \x01(\x04\x12\x0e\n\x06\x63lanid\x18\x02 \x01(\x04\x12\x10\n\x08posterid\x18\x03 \x01(\x04\x12\x10\n\x08headline\x18\x04 \x01(\t\x12\x10\n\x08posttime\x18\x05 \x01(\r\x12\x12\n\nupdatetime\x18\x06 \x01(\r\x12\x0c\n\x04\x62ody\x18\x07 \x01(\t\x12\x14\n\x0c\x63ommentcount\x18\x08 \x01(\x05\x12\x0c\n\x04tags\x18\t \x03(\t\x12\x10\n\x08language\x18\n \x01(\x05\x12\x0e\n\x06hidden\x18\x0b \x01(\x08\x12\x16\n\x0e\x66orum_topic_id\x18\x0c \x01(\x06\"\xc6\x02\n\'CCommunity_GetClanAnnouncements_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x04\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x10\n\x08maxchars\x18\x04 \x01(\r\x12\x12\n\nstrip_html\x18\x05 \x01(\x08\x12\x15\n\rrequired_tags\x18\x06 \x03(\t\x12\x17\n\x0frequire_no_tags\x18\x07 \x01(\x08\x12\x1b\n\x13language_preference\x18\x08 \x03(\r\x12\x13\n\x0bhidden_only\x18\t \x01(\x08\x12\x10\n\x08only_gid\x18\n \x01(\x08\x12\x19\n\x11rtime_oldest_date\x18\x0b \x01(\r\x12\x16\n\x0einclude_hidden\x18\x0c \x01(\x08\x12\x1e\n\x16include_partner_events\x18\r \x01(\x08\"\x89\x01\n(CCommunity_GetClanAnnouncements_Response\x12\x10\n\x08maxchars\x18\x01 \x01(\r\x12\x12\n\nstrip_html\x18\x02 \x01(\x08\x12\x37\n\rannouncements\x18\x03 \x03(\x0b\x32 .CCommunity_ClanAnnouncementInfo\"p\n$CBroadcast_PostGameDataFrame_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\x02 \x01(\x06\x12\x14\n\x0c\x62roadcast_id\x18\x03 \x01(\x06\x12\x12\n\nframe_data\x18\x04 \x01(\x0c\"\xfc\x02\n\x15\x43MsgSerializedSOCache\x12\x14\n\x0c\x66ile_version\x18\x01 \x01(\r\x12,\n\x06\x63\x61\x63hes\x18\x02 \x03(\x0b\x32\x1c.CMsgSerializedSOCache.Cache\x12\x1f\n\x17gc_socache_file_version\x18\x03 \x01(\r\x1a>\n\tTypeCache\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07objects\x18\x02 \x03(\x0c\x12\x12\n\nservice_id\x18\x03 \x01(\r\x1a\xbd\x01\n\x05\x43\x61\x63he\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x36\n\x08versions\x18\x03 \x03(\x0b\x32$.CMsgSerializedSOCache.Cache.Version\x12\x35\n\x0btype_caches\x18\x04 \x03(\x0b\x32 .CMsgSerializedSOCache.TypeCache\x1a+\n\x07Version\x12\x0f\n\x07service\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\x04\"G\n\x1f\x43MsgGCToClientPollConvarRequest\x12\x13\n\x0b\x63onvar_name\x18\x01 \x01(\t\x12\x0f\n\x07poll_id\x18\x02 \x01(\r\"I\n CMsgGCToClientPollConvarResponse\x12\x0f\n\x07poll_id\x18\x01 \x01(\r\x12\x14\n\x0c\x63onvar_value\x18\x02 \x01(\t\"E\n\x1b\x43GCMsgCompressedMsgToClient\x12\x0e\n\x06msg_id\x18\x01 \x01(\r\x12\x16\n\x0e\x63ompressed_msg\x18\x02 \x01(\x0c\"\x8e\x01\n CMsgGCToGCMasterBroadcastMessage\x12\x18\n\x10users_per_second\x18\x01 \x01(\r\x12\x15\n\rsend_to_users\x18\x02 \x01(\x08\x12\x17\n\x0fsend_to_servers\x18\x03 \x01(\x08\x12\x0e\n\x06msg_id\x18\x04 \x01(\r\x12\x10\n\x08msg_data\x18\x05 \x01(\x0c\"n\n CMsgGCToGCMasterSubscribeToCache\x12\x11\n\tsoid_type\x18\x01 \x01(\r\x12\x0f\n\x07soid_id\x18\x02 \x01(\x06\x12\x13\n\x0b\x61\x63\x63ount_ids\x18\x03 \x03(\r\x12\x11\n\tsteam_ids\x18\x04 \x03(\x06\"*\n(CMsgGCToGCMasterSubscribeToCacheResponse\"a\n%CMsgGCToGCMasterSubscribeToCacheAsync\x12\x38\n\rsubscribe_msg\x18\x01 \x01(\x0b\x32!.CMsgGCToGCMasterSubscribeToCache\"r\n$CMsgGCToGCMasterUnsubscribeFromCache\x12\x11\n\tsoid_type\x18\x01 \x01(\r\x12\x0f\n\x07soid_id\x18\x02 \x01(\x06\x12\x13\n\x0b\x61\x63\x63ount_ids\x18\x03 \x03(\r\x12\x11\n\tsteam_ids\x18\x04 \x03(\x06\"B\n\x1c\x43MsgGCToGCMasterDestroyCache\x12\x11\n\tsoid_type\x18\x01 \x01(\r\x12\x0f\n\x07soid_id\x18\x02 \x01(\x06*5\n\rESourceEngine\x12\x11\n\rk_ESE_Source1\x10\x00\x12\x11\n\rk_ESE_Source2\x10\x01*V\n\x12PartnerAccountType\x12\x10\n\x0cPARTNER_NONE\x10\x00\x12\x19\n\x15PARTNER_PERFECT_WORLD\x10\x01\x12\x13\n\x0fPARTNER_INVALID\x10\x03*\xa0\x02\n\x12GCConnectionStatus\x12#\n\x1fGCConnectionStatus_HAVE_SESSION\x10\x00\x12$\n GCConnectionStatus_GC_GOING_DOWN\x10\x01\x12!\n\x1dGCConnectionStatus_NO_SESSION\x10\x02\x12\x30\n,GCConnectionStatus_NO_SESSION_IN_LOGON_QUEUE\x10\x03\x12\x1f\n\x1bGCConnectionStatus_NO_STEAM\x10\x04\x12 \n\x1cGCConnectionStatus_SUSPENDED\x10\x05\x12\'\n#GCConnectionStatus_STEAM_GOING_DOWN\x10\x06')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gcsdk_gcmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CMSGSOMULTIPLEOBJECTS_SINGLEOBJECT']._loaded_options = None
  _globals['_CMSGSOMULTIPLEOBJECTS_SINGLEOBJECT']._serialized_options = b'\200\246\035\200\002\210\246\035\200\010'
  _globals['_ESOURCEENGINE']._serialized_start=8866
  _globals['_ESOURCEENGINE']._serialized_end=8919
  _globals['_PARTNERACCOUNTTYPE']._serialized_start=8921
  _globals['_PARTNERACCOUNTTYPE']._serialized_end=9007
  _globals['_GCCONNECTIONSTATUS']._serialized_start=9010
  _globals['_GCCONNECTIONSTATUS']._serialized_end=9298
  _globals['_CEXTRAMSGBLOCK']._serialized_start=93
  _globals['_CEXTRAMSGBLOCK']._serialized_end=185
  _globals['_CMSGSTEAMLEARNSERVERINFO']._serialized_start=188
  _globals['_CMSGSTEAMLEARNSERVERINFO']._serialized_end=492
  _globals['_CMSGSTEAMLEARNSERVERINFO_PROJECTINFO']._serialized_start=331
  _globals['_CMSGSTEAMLEARNSERVERINFO_PROJECTINFO']._serialized_end=492
  _globals['_CMSGGCASSERTJOBDATA']._serialized_start=494
  _globals['_CMSGGCASSERTJOBDATA']._serialized_end=559
  _globals['_CMSGGCCONCOMMAND']._serialized_start=561
  _globals['_CMSGGCCONCOMMAND']._serialized_end=596
  _globals['_CMSGSDOASSERT']._serialized_start=598
  _globals['_CMSGSDOASSERT']._serialized_end=721
  _globals['_CMSGSDOASSERT_REQUEST']._serialized_start=675
  _globals['_CMSGSDOASSERT_REQUEST']._serialized_end=721
  _globals['_CMSGSOIDOWNER']._serialized_start=723
  _globals['_CMSGSOIDOWNER']._serialized_end=764
  _globals['_CMSGSOSINGLEOBJECT']._serialized_start=767
  _globals['_CMSGSOSINGLEOBJECT']._serialized_end=898
  _globals['_CMSGSOMULTIPLEOBJECTS']._serialized_start=901
  _globals['_CMSGSOMULTIPLEOBJECTS']._serialized_end=1248
  _globals['_CMSGSOMULTIPLEOBJECTS_SINGLEOBJECT']._serialized_start=1184
  _globals['_CMSGSOMULTIPLEOBJECTS_SINGLEOBJECT']._serialized_end=1248
  _globals['_CMSGSOCACHESUBSCRIBED']._serialized_start=1251
  _globals['_CMSGSOCACHESUBSCRIBED']._serialized_end=1503
  _globals['_CMSGSOCACHESUBSCRIBED_SUBSCRIBEDTYPE']._serialized_start=1449
  _globals['_CMSGSOCACHESUBSCRIBED_SUBSCRIBEDTYPE']._serialized_end=1503
  _globals['_CMSGSOCACHESUBSCRIBEDUPTODATE']._serialized_start=1506
  _globals['_CMSGSOCACHESUBSCRIBEDUPTODATE']._serialized_end=1654
  _globals['_CMSGSOCACHEUNSUBSCRIBED']._serialized_start=1656
  _globals['_CMSGSOCACHEUNSUBSCRIBED']._serialized_end=1717
  _globals['_CMSGSOCACHESUBSCRIPTIONCHECK']._serialized_start=1720
  _globals['_CMSGSOCACHESUBSCRIPTIONCHECK']._serialized_end=1867
  _globals['_CMSGSOCACHESUBSCRIPTIONREFRESH']._serialized_start=1869
  _globals['_CMSGSOCACHESUBSCRIPTIONREFRESH']._serialized_end=1937
  _globals['_CMSGSOCACHEVERSION']._serialized_start=1939
  _globals['_CMSGSOCACHEVERSION']._serialized_end=1976
  _globals['_CMSGGCMULTIPLEXMESSAGE']._serialized_start=1978
  _globals['_CMSGGCMULTIPLEXMESSAGE']._serialized_end=2054
  _globals['_CMSGGCTOGCSUBGCSTARTING']._serialized_start=2056
  _globals['_CMSGGCTOGCSUBGCSTARTING']._serialized_end=2104
  _globals['_CGCTOGCMSGMASTERACK']._serialized_start=2107
  _globals['_CGCTOGCMSGMASTERACK']._serialized_end=2302
  _globals['_CGCTOGCMSGMASTERACK_PROCESS']._serialized_start=2246
  _globals['_CGCTOGCMSGMASTERACK_PROCESS']._serialized_end=2302
  _globals['_CGCTOGCMSGMASTERACK_RESPONSE']._serialized_start=2304
  _globals['_CGCTOGCMSGMASTERACK_RESPONSE']._serialized_end=2354
  _globals['_CMSGGCTOGCUNIVERSESTARTUP']._serialized_start=2356
  _globals['_CMSGGCTOGCUNIVERSESTARTUP']._serialized_end=2411
  _globals['_CMSGGCTOGCUNIVERSESTARTUPRESPONSE']._serialized_start=2413
  _globals['_CMSGGCTOGCUNIVERSESTARTUPRESPONSE']._serialized_end=2465
  _globals['_CGCTOGCMSGMASTERSTARTUPCOMPLETE']._serialized_start=2468
  _globals['_CGCTOGCMSGMASTERSTARTUPCOMPLETE']._serialized_end=2614
  _globals['_CGCTOGCMSGMASTERSTARTUPCOMPLETE_GCINFO']._serialized_start=2561
  _globals['_CGCTOGCMSGMASTERSTARTUPCOMPLETE_GCINFO']._serialized_end=2614
  _globals['_CGCTOGCMSGROUTED']._serialized_start=2616
  _globals['_CGCTOGCMSGROUTED']._serialized_end=2692
  _globals['_CGCTOGCMSGROUTEDREPLY']._serialized_start=2694
  _globals['_CGCTOGCMSGROUTEDREPLY']._serialized_end=2756
  _globals['_CMSGGCUPDATESUBGCSESSIONINFO']._serialized_start=2759
  _globals['_CMSGGCUPDATESUBGCSESSIONINFO']._serialized_end=2908
  _globals['_CMSGGCUPDATESUBGCSESSIONINFO_CMSGUPDATE']._serialized_start=2850
  _globals['_CMSGGCUPDATESUBGCSESSIONINFO_CMSGUPDATE']._serialized_end=2908
  _globals['_CMSGGCREQUESTSUBGCSESSIONINFO']._serialized_start=2910
  _globals['_CMSGGCREQUESTSUBGCSESSIONINFO']._serialized_end=2958
  _globals['_CMSGGCREQUESTSUBGCSESSIONINFORESPONSE']._serialized_start=2960
  _globals['_CMSGGCREQUESTSUBGCSESSIONINFORESPONSE']._serialized_end=3059
  _globals['_CMSGSOCACHEHAVEVERSION']._serialized_start=3061
  _globals['_CMSGSOCACHEHAVEVERSION']._serialized_end=3181
  _globals['_CMSGCLIENTHELLO']._serialized_start=3184
  _globals['_CMSGCLIENTHELLO']._serialized_end=3823
  _globals['_CMSGCLIENTWELCOME']._serialized_start=3826
  _globals['_CMSGCLIENTWELCOME']._serialized_end=4468
  _globals['_CMSGCLIENTWELCOME_LOCATION']._serialized_start=4404
  _globals['_CMSGCLIENTWELCOME_LOCATION']._serialized_end=4468
  _globals['_CMSGCONNECTIONSTATUS']._serialized_start=4471
  _globals['_CMSGCONNECTIONSTATUS']._serialized_end=4700
  _globals['_CMSGGCTOGCSOCACHESUBSCRIBE']._serialized_start=4703
  _globals['_CMSGGCTOGCSOCACHESUBSCRIBE']._serialized_end=4951
  _globals['_CMSGGCTOGCSOCACHESUBSCRIBE_CMSGHAVEVERSIONS']._serialized_start=4896
  _globals['_CMSGGCTOGCSOCACHESUBSCRIBE_CMSGHAVEVERSIONS']._serialized_end=4951
  _globals['_CMSGGCTOGCSOCACHEUNSUBSCRIBE']._serialized_start=4953
  _globals['_CMSGGCTOGCSOCACHEUNSUBSCRIBE']._serialized_end=5063
  _globals['_CMSGGCCLIENTPING']._serialized_start=5065
  _globals['_CMSGGCCLIENTPING']._serialized_end=5083
  _globals['_CMSGGCTOGCFORWARDACCOUNTDETAILS']._serialized_start=5086
  _globals['_CMSGGCTOGCFORWARDACCOUNTDETAILS']._serialized_end=5224
  _globals['_CMSGGCTOGCLOADSESSIONSOCACHE']._serialized_start=5226
  _globals['_CMSGGCTOGCLOADSESSIONSOCACHE']._serialized_end=5343
  _globals['_CMSGGCTOGCLOADSESSIONSOCACHERESPONSE']._serialized_start=5345
  _globals['_CMSGGCTOGCLOADSESSIONSOCACHERESPONSE']._serialized_end=5383
  _globals['_CMSGGCTOGCUPDATESESSIONSTATS']._serialized_start=5385
  _globals['_CMSGGCTOGCUPDATESESSIONSTATS']._serialized_end=5487
  _globals['_CMSGGCTOCLIENTREQUESTDROPPED']._serialized_start=5489
  _globals['_CMSGGCTOCLIENTREQUESTDROPPED']._serialized_end=5519
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST']._serialized_start=5522
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST']._serialized_end=5887
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST_SINGLEITEMDESCRIPTION']._serialized_start=5677
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST_SINGLEITEMDESCRIPTION']._serialized_end=5746
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST_ITEMDESCRIPTIONSLANGUAGEBLOCK']._serialized_start=5749
  _globals['_CWORKSHOP_POPULATEITEMDESCRIPTIONS_REQUEST_ITEMDESCRIPTIONSLANGUAGEBLOCK']._serialized_end=5887
  _globals['_CWORKSHOP_GETCONTRIBUTORS_REQUEST']._serialized_start=5889
  _globals['_CWORKSHOP_GETCONTRIBUTORS_REQUEST']._serialized_end=5959
  _globals['_CWORKSHOP_GETCONTRIBUTORS_RESPONSE']._serialized_start=5961
  _globals['_CWORKSHOP_GETCONTRIBUTORS_RESPONSE']._serialized_end=6019
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST']._serialized_start=6022
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST']._serialized_end=6779
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_WORKSHOPITEMPAYMENTRULE']._serialized_start=6471
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_WORKSHOPITEMPAYMENTRULE']._serialized_end=6598
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_WORKSHOPDIRECTPAYMENTRULE']._serialized_start=6600
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_WORKSHOPDIRECTPAYMENTRULE']._serialized_end=6679
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_PARTNERITEMPAYMENTRULE']._serialized_start=6681
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_REQUEST_PARTNERITEMPAYMENTRULE']._serialized_end=6779
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_RESPONSE']._serialized_start=6781
  _globals['_CWORKSHOP_SETITEMPAYMENTRULES_RESPONSE']._serialized_end=6848
  _globals['_CCOMMUNITY_CLANANNOUNCEMENTINFO']._serialized_start=6851
  _globals['_CCOMMUNITY_CLANANNOUNCEMENTINFO']._serialized_end=7095
  _globals['_CCOMMUNITY_GETCLANANNOUNCEMENTS_REQUEST']._serialized_start=7098
  _globals['_CCOMMUNITY_GETCLANANNOUNCEMENTS_REQUEST']._serialized_end=7424
  _globals['_CCOMMUNITY_GETCLANANNOUNCEMENTS_RESPONSE']._serialized_start=7427
  _globals['_CCOMMUNITY_GETCLANANNOUNCEMENTS_RESPONSE']._serialized_end=7564
  _globals['_CBROADCAST_POSTGAMEDATAFRAME_REQUEST']._serialized_start=7566
  _globals['_CBROADCAST_POSTGAMEDATAFRAME_REQUEST']._serialized_end=7678
  _globals['_CMSGSERIALIZEDSOCACHE']._serialized_start=7681
  _globals['_CMSGSERIALIZEDSOCACHE']._serialized_end=8061
  _globals['_CMSGSERIALIZEDSOCACHE_TYPECACHE']._serialized_start=7807
  _globals['_CMSGSERIALIZEDSOCACHE_TYPECACHE']._serialized_end=7869
  _globals['_CMSGSERIALIZEDSOCACHE_CACHE']._serialized_start=7872
  _globals['_CMSGSERIALIZEDSOCACHE_CACHE']._serialized_end=8061
  _globals['_CMSGSERIALIZEDSOCACHE_CACHE_VERSION']._serialized_start=8018
  _globals['_CMSGSERIALIZEDSOCACHE_CACHE_VERSION']._serialized_end=8061
  _globals['_CMSGGCTOCLIENTPOLLCONVARREQUEST']._serialized_start=8063
  _globals['_CMSGGCTOCLIENTPOLLCONVARREQUEST']._serialized_end=8134
  _globals['_CMSGGCTOCLIENTPOLLCONVARRESPONSE']._serialized_start=8136
  _globals['_CMSGGCTOCLIENTPOLLCONVARRESPONSE']._serialized_end=8209
  _globals['_CGCMSGCOMPRESSEDMSGTOCLIENT']._serialized_start=8211
  _globals['_CGCMSGCOMPRESSEDMSGTOCLIENT']._serialized_end=8280
  _globals['_CMSGGCTOGCMASTERBROADCASTMESSAGE']._serialized_start=8283
  _globals['_CMSGGCTOGCMASTERBROADCASTMESSAGE']._serialized_end=8425
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHE']._serialized_start=8427
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHE']._serialized_end=8537
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHERESPONSE']._serialized_start=8539
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHERESPONSE']._serialized_end=8581
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHEASYNC']._serialized_start=8583
  _globals['_CMSGGCTOGCMASTERSUBSCRIBETOCACHEASYNC']._serialized_end=8680
  _globals['_CMSGGCTOGCMASTERUNSUBSCRIBEFROMCACHE']._serialized_start=8682
  _globals['_CMSGGCTOGCMASTERUNSUBSCRIBEFROMCACHE']._serialized_end=8796
  _globals['_CMSGGCTOGCMASTERDESTROYCACHE']._serialized_start=8798
  _globals['_CMSGGCTOGCMASTERDESTROYCACHE']._serialized_end=8864
# @@protoc_insertion_point(module_scope)
