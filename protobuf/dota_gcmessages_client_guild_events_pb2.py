# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_gcmessages_client_guild_events.proto
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
    'dota_gcmessages_client_guild_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dota_shared_enums_pb2 as dota__shared__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dota_gcmessages_client_guild_events.proto\x1a\x17\x64ota_shared_enums.proto\"\xb6\x01\n\x11\x43MsgGuildContract\x12\x13\n\x0b\x63ontract_id\x18\x01 \x01(\x04\x12\x1d\n\x15\x63hallenge_instance_id\x18\x02 \x01(\r\x12\x1b\n\x13\x63hallenge_parameter\x18\x03 \x01(\r\x12\x1b\n\x13\x63hallenge_timestamp\x18\x04 \x01(\r\x12\x1b\n\x13\x61ssigned_account_id\x18\x05 \x01(\r\x12\x16\n\x0e\x63ontract_flags\x18\x06 \x01(\r\"=\n\x15\x43MsgGuildContractSlot\x12$\n\x08\x63ontract\x18\x01 \x01(\x0b\x32\x12.CMsgGuildContract\"\xd9\x02\n\x19\x43MsgAccountGuildEventData\x12\x14\n\x0cguild_points\x18\x01 \x01(\r\x12%\n\x1d\x63ontracts_refreshed_timestamp\x18\x02 \x01(\r\x12.\n\x0e\x63ontract_slots\x18\x03 \x03(\x0b\x32\x16.CMsgGuildContractSlot\x12!\n\x19\x63ompleted_challenge_count\x18\x04 \x01(\r\x12$\n\x1c\x63hallenges_refresh_timestamp\x18\x05 \x01(\r\x12\x1f\n\x17guild_weekly_percentile\x18\x06 \x01(\r\x12#\n\x1bguild_weekly_last_timestamp\x18\x07 \x01(\r\x12\x1e\n\x16last_weekly_claim_time\x18\x08 \x01(\r\x12 \n\x18guild_current_percentile\x18\t \x01(\r\"h\n\x18\x43MsgGuildActiveContracts\x12%\n\x1d\x63ontracts_refreshed_timestamp\x18\x01 \x01(\r\x12%\n\tcontracts\x18\x02 \x03(\x0b\x32\x12.CMsgGuildContract\"\xa2\x01\n\x12\x43MsgGuildChallenge\x12\x1d\n\x15\x63hallenge_instance_id\x18\x01 \x01(\r\x12\x1b\n\x13\x63hallenge_parameter\x18\x02 \x01(\r\x12\x1b\n\x13\x63hallenge_timestamp\x18\x03 \x01(\r\x12\x1a\n\x12\x63hallenge_progress\x18\x04 \x01(\r\x12\x17\n\x0f\x63hallenge_flags\x18\x05 \x01(\r\"G\n\x14\x43MsgGuildEventMember\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x1b\n\x13guild_points_earned\x18\x02 \x01(\r\"h\n*CMsgClientToGCRequestAccountGuildEventData\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\xaa\x03\n2CMsgClientToGCRequestAccountGuildEventDataResponse\x12_\n\x06result\x18\x01 \x01(\x0e\x32=.CMsgClientToGCRequestAccountGuildEventDataResponse.EResponse:\x10k_eInternalError\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12.\n\nevent_data\x18\x03 \x01(\x0b\x32\x1a.CMsgAccountGuildEventData\"\xb8\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\"\xcf\x01\n*CMsgGCToClientAccountGuildEventDataUpdated\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12\x14\n\x0cupdate_flags\x18\x03 \x01(\r\x12\x34\n\x10guild_event_data\x18\x04 \x01(\x0b\x32\x1a.CMsgAccountGuildEventData\x12\x19\n\x11\x63ontracts_updated\x18\x05 \x01(\x08\"g\n)CMsgClientToGCRequestActiveGuildContracts\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\xb3\x03\n1CMsgClientToGCRequestActiveGuildContractsResponse\x12^\n\x06result\x18\x01 \x01(\x0e\x32<.CMsgClientToGCRequestActiveGuildContractsResponse.EResponse:\x10k_eInternalError\x12\x33\n\x10\x61\x63tive_contracts\x18\x02 \x01(\x0b\x32\x19.CMsgGuildActiveContracts\x12.\n\x11\x61\x63tive_challenges\x18\x03 \x01(\x0b\x32\x13.CMsgGuildChallenge\"\xb8\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\"g\n)CMsgGCToClientActiveGuildContractsUpdated\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\x8b\x01\n!CMsgClientToGCSelectGuildContract\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12\x13\n\x0b\x63ontract_id\x18\x03 \x01(\x04\x12\x15\n\rcontract_slot\x18\x04 \x01(\r\"\xa4\x04\n)CMsgClientToGCSelectGuildContractResponse\x12V\n\x06result\x18\x01 \x01(\x0e\x32\x34.CMsgClientToGCSelectGuildContractResponse.EResponse:\x10k_eInternalError\"\x9e\x03\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\x12\x18\n\x14k_eInvalidContractID\x10\t\x12\x16\n\x12k_eAlreadyAssigned\x10\n\x12\x1a\n\x16k_eInvalidContractSlot\x10\x0b\x12\x1e\n\x1ak_eContractSlotLockedGuild\x10\x0c\x12\x1b\n\x17k_eContractSlotCooldown\x10\r\x12\x18\n\x14k_eContractDuplicate\x10\x0e\x12\x1c\n\x18k_eContractSlotTimeError\x10\x0f\x12!\n\x1dk_eContractSlotLockedDotaPlus\x10\x10\"g\n)CMsgClientToGCRequestActiveGuildChallenge\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\xfd\x02\n1CMsgClientToGCRequestActiveGuildChallengeResponse\x12^\n\x06result\x18\x01 \x01(\x0e\x32<.CMsgClientToGCRequestActiveGuildChallengeResponse.EResponse:\x10k_eInternalError\x12-\n\x10\x61\x63tive_challenge\x18\x02 \x01(\x0b\x32\x13.CMsgGuildChallenge\"\xb8\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\"\x96\x01\n)CMsgGCToClientActiveGuildChallengeUpdated\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12-\n\x10\x61\x63tive_challenge\x18\x03 \x01(\x0b\x32\x13.CMsgGuildChallenge\"d\n&CMsgClientToGCRequestGuildEventMembers\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\xf0\x02\n.CMsgClientToGCRequestGuildEventMembersResponse\x12[\n\x06result\x18\x01 \x01(\x0e\x32\x39.CMsgClientToGCRequestGuildEventMembersResponse.EResponse:\x10k_eInternalError\x12&\n\x07members\x18\x02 \x03(\x0b\x32\x15.CMsgGuildEventMember\"\xb8\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\"\xf1\x01\n$CMsgGuildLeaderboardCombinedResponse\x12(\n\x08\x65vent_id\x18\x01 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12\x0e\n\x06region\x18\x02 \x01(\r\x12\x14\n\x0clast_updated\x18\x03 \x01(\r\x12\x14\n\x08guild_id\x18\x04 \x03(\rB\x02\x10\x01\x12\x10\n\x04rank\x18\x05 \x03(\rB\x02\x10\x01\x12\x1e\n\x12\x63urrent_percentile\x18\x06 \x03(\rB\x02\x10\x01\x12\x1d\n\x11weekly_percentile\x18\x07 \x03(\rB\x02\x10\x01\x12\x12\n\x06points\x18\x08 \x03(\rB\x02\x10\x01\"c\n%CMsgClientToGCClaimLeaderboardRewards\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\x8a\x03\n-CMsgClientToGCClaimLeaderboardRewardsResponse\x12Z\n\x06result\x18\x01 \x01(\x0e\x32\x38.CMsgClientToGCClaimLeaderboardRewardsResponse.EResponse:\x10k_eInternalError\x12\x14\n\x0c\x65vent_points\x18\x02 \x01(\r\"\xe6\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x13\n\x0fk_eInvalidEvent\x10\x05\x12\x13\n\x0fk_eInvalidGuild\x10\x06\x12\x10\n\x0ck_eNotMember\x10\x07\x12\x18\n\x14k_eInvalidGuildEvent\x10\x08\x12\x15\n\x11k_eDoesNotQualify\x10\t\x12\x15\n\x11k_eAlreadyClaimed\x10\n*\xb3\x03\n\x16\x45GuildEventAuditAction\x12$\n k_EGuildEventAuditAction_Invalid\x10\x00\x12%\n!k_EGuildEventAuditAction_DevGrant\x10\x01\x12-\n)k_EGuildEventAuditAction_CompleteContract\x10\x02\x12.\n*k_EGuildEventAuditAction_CompleteChallenge\x10\x03\x12\x31\n-k_EGuildEventAuditAction_CompleteMatch_Winner\x10\x04\x12.\n*k_EGuildEventAuditAction_ChallengeProgress\x10\x05\x12\x30\n,k_EGuildEventAuditAction_CompleteMatch_Loser\x10\x06\x12.\n*k_EGuildEventAuditAction_WeeklyLeaderboard\x10\x07\x12(\n$k_EGuildEventAuditAction_ManualGrant\x10\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_gcmessages_client_guild_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['guild_id']._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['guild_id']._serialized_options = b'\020\001'
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['rank']._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['rank']._serialized_options = b'\020\001'
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['current_percentile']._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['current_percentile']._serialized_options = b'\020\001'
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['weekly_percentile']._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['weekly_percentile']._serialized_options = b'\020\001'
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['points']._loaded_options = None
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE'].fields_by_name['points']._serialized_options = b'\020\001'
  _globals['_EGUILDEVENTAUDITACTION']._serialized_start=4954
  _globals['_EGUILDEVENTAUDITACTION']._serialized_end=5389
  _globals['_CMSGGUILDCONTRACT']._serialized_start=71
  _globals['_CMSGGUILDCONTRACT']._serialized_end=253
  _globals['_CMSGGUILDCONTRACTSLOT']._serialized_start=255
  _globals['_CMSGGUILDCONTRACTSLOT']._serialized_end=316
  _globals['_CMSGACCOUNTGUILDEVENTDATA']._serialized_start=319
  _globals['_CMSGACCOUNTGUILDEVENTDATA']._serialized_end=664
  _globals['_CMSGGUILDACTIVECONTRACTS']._serialized_start=666
  _globals['_CMSGGUILDACTIVECONTRACTS']._serialized_end=770
  _globals['_CMSGGUILDCHALLENGE']._serialized_start=773
  _globals['_CMSGGUILDCHALLENGE']._serialized_end=935
  _globals['_CMSGGUILDEVENTMEMBER']._serialized_start=937
  _globals['_CMSGGUILDEVENTMEMBER']._serialized_end=1008
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATA']._serialized_start=1010
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATA']._serialized_end=1114
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATARESPONSE']._serialized_start=1117
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATARESPONSE']._serialized_end=1543
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATARESPONSE_ERESPONSE']._serialized_start=1359
  _globals['_CMSGCLIENTTOGCREQUESTACCOUNTGUILDEVENTDATARESPONSE_ERESPONSE']._serialized_end=1543
  _globals['_CMSGGCTOCLIENTACCOUNTGUILDEVENTDATAUPDATED']._serialized_start=1546
  _globals['_CMSGGCTOCLIENTACCOUNTGUILDEVENTDATAUPDATED']._serialized_end=1753
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTS']._serialized_start=1755
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTS']._serialized_end=1858
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTSRESPONSE']._serialized_start=1861
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTSRESPONSE']._serialized_end=2296
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTSRESPONSE_ERESPONSE']._serialized_start=1359
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCONTRACTSRESPONSE_ERESPONSE']._serialized_end=1543
  _globals['_CMSGGCTOCLIENTACTIVEGUILDCONTRACTSUPDATED']._serialized_start=2298
  _globals['_CMSGGCTOCLIENTACTIVEGUILDCONTRACTSUPDATED']._serialized_end=2401
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACT']._serialized_start=2404
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACT']._serialized_end=2543
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACTRESPONSE']._serialized_start=2546
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACTRESPONSE']._serialized_end=3094
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACTRESPONSE_ERESPONSE']._serialized_start=2680
  _globals['_CMSGCLIENTTOGCSELECTGUILDCONTRACTRESPONSE_ERESPONSE']._serialized_end=3094
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGE']._serialized_start=3096
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGE']._serialized_end=3199
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGERESPONSE']._serialized_start=3202
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGERESPONSE']._serialized_end=3583
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGERESPONSE_ERESPONSE']._serialized_start=1359
  _globals['_CMSGCLIENTTOGCREQUESTACTIVEGUILDCHALLENGERESPONSE_ERESPONSE']._serialized_end=1543
  _globals['_CMSGGCTOCLIENTACTIVEGUILDCHALLENGEUPDATED']._serialized_start=3586
  _globals['_CMSGGCTOCLIENTACTIVEGUILDCHALLENGEUPDATED']._serialized_end=3736
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERS']._serialized_start=3738
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERS']._serialized_end=3838
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERSRESPONSE']._serialized_start=3841
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERSRESPONSE']._serialized_end=4209
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERSRESPONSE_ERESPONSE']._serialized_start=1359
  _globals['_CMSGCLIENTTOGCREQUESTGUILDEVENTMEMBERSRESPONSE_ERESPONSE']._serialized_end=1543
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE']._serialized_start=4212
  _globals['_CMSGGUILDLEADERBOARDCOMBINEDRESPONSE']._serialized_end=4453
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDS']._serialized_start=4455
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDS']._serialized_end=4554
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDSRESPONSE']._serialized_start=4557
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDSRESPONSE']._serialized_end=4951
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDSRESPONSE_ERESPONSE']._serialized_start=4721
  _globals['_CMSGCLIENTTOGCCLAIMLEADERBOARDREWARDSRESPONSE_ERESPONSE']._serialized_end=4951
# @@protoc_insertion_point(module_scope)