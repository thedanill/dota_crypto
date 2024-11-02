# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_gcmessages_client_team.proto
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
    'dota_gcmessages_client_team.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dota_shared_enums_pb2 as dota__shared__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!dota_gcmessages_client_team.proto\x1a\x17\x64ota_shared_enums.proto\"\x9f\r\n\x10\x43MsgDOTATeamInfo\x12)\n\x07members\x18\x01 \x03(\x0b\x32\x18.CMsgDOTATeamInfo.Member\x12\x0f\n\x07team_id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x04 \x01(\t\x12\x14\n\x0ctime_created\x18\x05 \x01(\r\x12\x0b\n\x03pro\x18\x06 \x01(\x08\x12\x13\n\x0bpickup_team\x18\x08 \x01(\x08\x12\x10\n\x08ugc_logo\x18\t \x01(\x04\x12\x15\n\rugc_base_logo\x18\n \x01(\x04\x12\x17\n\x0fugc_banner_logo\x18\x0b \x01(\x04\x12\x18\n\x10ugc_sponsor_logo\x18\x0c \x01(\x04\x12\x14\n\x0c\x63ountry_code\x18\r \x01(\t\x12\x0b\n\x03url\x18\x0e \x01(\t\x12\x0c\n\x04wins\x18\x0f \x01(\r\x12\x0e\n\x06losses\x18\x10 \x01(\r\x12\x1a\n\x12games_played_total\x18\x13 \x01(\r\x12 \n\x18games_played_matchmaking\x18\x14 \x01(\r\x12\x10\n\x08url_logo\x18\x18 \x01(\t\x12%\n\x1dregistered_member_account_ids\x18\x1e \x03(\r\x12\x18\n\x10\x63oach_account_id\x18$ \x01(\r\x12\x33\n\raudit_entries\x18\x1f \x03(\x0b\x32\x1c.CMsgDOTATeamInfo.AuditEntry\x12\x33\n\x06region\x18\x1d \x01(\x0e\x32\x0e.ELeagueRegion:\x13LEAGUE_REGION_UNSET\x12\x14\n\x0c\x61\x62\x62reviation\x18  \x01(\t\x12\x33\n\x0cmember_stats\x18! \x03(\x0b\x32\x1d.CMsgDOTATeamInfo.MemberStats\x12/\n\nteam_stats\x18\" \x01(\x0b\x32\x1b.CMsgDOTATeamInfo.TeamStats\x12\x30\n\x0b\x64pc_results\x18# \x03(\x0b\x32\x1b.CMsgDOTATeamInfo.DPCResult\x12\x15\n\rcolor_primary\x18% \x01(\t\x12\x17\n\x0f\x63olor_secondary\x18& \x01(\t\x12\x14\n\x0cteam_captain\x18\' \x01(\r\x1a\xa5\x01\n\tHeroStats\x12\x0f\n\x07hero_id\x18\x01 \x01(\x05\x12\r\n\x05picks\x18\x02 \x01(\r\x12\x0c\n\x04wins\x18\x03 \x01(\r\x12\x0c\n\x04\x62\x61ns\x18\x04 \x01(\r\x12\x11\n\tavg_kills\x18\x05 \x01(\x02\x12\x12\n\navg_deaths\x18\x06 \x01(\x02\x12\x13\n\x0b\x61vg_assists\x18\x07 \x01(\x02\x12\x0f\n\x07\x61vg_gpm\x18\x08 \x01(\x02\x12\x0f\n\x07\x61vg_xpm\x18\t \x01(\x02\x1a\xc0\x01\n\x0bMemberStats\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x16\n\x0ewins_with_team\x18\x02 \x01(\r\x12\x18\n\x10losses_with_team\x18\x03 \x01(\r\x12/\n\ntop_heroes\x18\x04 \x03(\x0b\x32\x1b.CMsgDOTATeamInfo.HeroStats\x12\x11\n\tavg_kills\x18\x05 \x01(\x02\x12\x12\n\navg_deaths\x18\x06 \x01(\x02\x12\x13\n\x0b\x61vg_assists\x18\x07 \x01(\x02\x1a\xb4\x01\n\tTeamStats\x12\x32\n\rplayed_heroes\x18\x01 \x03(\x0b\x32\x1b.CMsgDOTATeamInfo.HeroStats\x12\x0f\n\x07\x66\x61rming\x18\x02 \x01(\x02\x12\x10\n\x08\x66ighting\x18\x03 \x01(\x02\x12\x13\n\x0bversatility\x18\x04 \x01(\x02\x12\x11\n\tavg_kills\x18\x05 \x01(\x02\x12\x12\n\navg_deaths\x18\x06 \x01(\x02\x12\x14\n\x0c\x61vg_duration\x18\x07 \x01(\x02\x1a\x65\n\tDPCResult\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x10\n\x08standing\x18\x02 \x01(\r\x12\x0e\n\x06points\x18\x03 \x01(\r\x12\x10\n\x08\x65\x61rnings\x18\x04 \x01(\r\x12\x11\n\ttimestamp\x18\x05 \x01(\r\x1a\x9b\x01\n\x06Member\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x13\n\x0btime_joined\x18\x02 \x01(\r\x12\r\n\x05\x61\x64min\x18\x03 \x01(\x08\x12\x10\n\x08pro_name\x18\x06 \x01(\t\x12\x34\n\x04role\x18\x08 \x01(\x0e\x32\x0e.Fantasy_Roles:\x16\x46\x41NTASY_ROLE_UNDEFINED\x12\x11\n\treal_name\x18\t \x01(\t\x1aI\n\nAuditEntry\x12\x14\n\x0c\x61udit_action\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x12\n\naccount_id\x18\x03 \x01(\r\"H\n\x11\x43MsgDOTATeamsInfo\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12 \n\x05teams\x18\x02 \x03(\x0b\x32\x11.CMsgDOTATeamInfo\"8\n\x14\x43MsgDOTATeamInfoList\x12 \n\x05teams\x18\x01 \x03(\x0b\x32\x11.CMsgDOTATeamInfo\"Z\n\x15\x43MsgDOTATeamInfoCache\x12\x17\n\x0f\x63\x61\x63he_timestamp\x18\x01 \x01(\r\x12(\n\tteam_list\x18\x02 \x01(\x0b\x32\x15.CMsgDOTATeamInfoList\"\x1b\n\x19\x43MsgDOTAMyTeamInfoRequest\"\xc9\x01\n\x12\x43MsgDOTACreateTeam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x0c\n\x04logo\x18\x03 \x01(\x04\x12\x11\n\tbase_logo\x18\x04 \x01(\x04\x12\x13\n\x0b\x62\x61nner_logo\x18\x05 \x01(\x04\x12\x14\n\x0csponsor_logo\x18\x06 \x01(\x04\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\t\x12\x0b\n\x03url\x18\x08 \x01(\t\x12\x13\n\x0bpickup_team\x18\t \x01(\x08\x12\x14\n\x0c\x61\x62\x62reviation\x18\n \x01(\t\"\x97\x04\n\x1a\x43MsgDOTACreateTeamResponse\x12;\n\x06result\x18\x01 \x01(\x0e\x32\".CMsgDOTACreateTeamResponse.Result:\x07INVALID\x12\x0f\n\x07team_id\x18\x02 \x01(\r\"\xaa\x03\n\x06Result\x12\x14\n\x07INVALID\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0e\n\nNAME_EMPTY\x10\x01\x12\x17\n\x13NAME_BAD_CHARACTERS\x10\x02\x12\x0e\n\nNAME_TAKEN\x10\x03\x12\x11\n\rNAME_TOO_LONG\x10\x04\x12\r\n\tTAG_EMPTY\x10\x05\x12\x16\n\x12TAG_BAD_CHARACTERS\x10\x06\x12\r\n\tTAG_TAKEN\x10\x07\x12\x10\n\x0cTAG_TOO_LONG\x10\x08\x12\x10\n\x0c\x43REATOR_BUSY\x10\t\x12\x15\n\x11UNSPECIFIED_ERROR\x10\n\x12\x1e\n\x1a\x43REATOR_TEAM_LIMIT_REACHED\x10\x0b\x12\x0b\n\x07NO_LOGO\x10\x0c\x12\"\n\x1e\x43REATOR_TEAM_CREATION_COOLDOWN\x10\r\x12\x16\n\x12LOGO_UPLOAD_FAILED\x10\x0e\x12\x1d\n\x19NAME_CHANGED_TOO_RECENTLY\x10\x0f\x12\x1e\n\x1a\x43REATOR_INSUFFICIENT_LEVEL\x10\x10\x12\x18\n\x14INVALID_ACCOUNT_TYPE\x10\x11\"\xe3\x01\n\x17\x43MsgDOTAEditTeamDetails\x12\x0f\n\x07team_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\x04\x12\x11\n\tbase_logo\x18\x05 \x01(\x04\x12\x13\n\x0b\x62\x61nner_logo\x18\x06 \x01(\x04\x12\x14\n\x0csponsor_logo\x18\x07 \x01(\x04\x12\x14\n\x0c\x63ountry_code\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\t \x01(\t\x12\x17\n\x0fin_use_by_party\x18\n \x01(\x08\x12\x14\n\x0c\x61\x62\x62reviation\x18\x0b \x01(\t\"\xed\x01\n\x1f\x43MsgDOTAEditTeamDetailsResponse\x12@\n\x06result\x18\x01 \x01(\x0e\x32\'.CMsgDOTAEditTeamDetailsResponse.Result:\x07SUCCESS\"\x87\x01\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12 \n\x1c\x46\x41ILURE_INVALID_ACCOUNT_TYPE\x10\x01\x12\x16\n\x12\x46\x41ILURE_NOT_MEMBER\x10\x02\x12\x17\n\x13\x46\x41ILURE_TEAM_LOCKED\x10\x03\x12\x1d\n\x19\x46\x41ILURE_UNSPECIFIED_ERROR\x10\x04\"E\n\x1e\x43MsgDOTATeamInvite_InviterToGC\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0f\n\x07team_id\x18\x02 \x01(\r\"\x9c\x01\n/CMsgDOTATeamInvite_GCImmediateResponseToInviter\x12\x37\n\x06result\x18\x01 \x01(\x0e\x32\x12.ETeamInviteResult:\x13TEAM_INVITE_SUCCESS\x12\x14\n\x0cinvitee_name\x18\x02 \x01(\t\x12\x1a\n\x12required_play_time\x18\x03 \x01(\r\"v\n%CMsgDOTATeamInvite_GCRequestToInvitee\x12\x1a\n\x12inviter_account_id\x18\x01 \x01(\r\x12\x11\n\tteam_name\x18\x02 \x01(\t\x12\x10\n\x08team_tag\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\x04\"a\n&CMsgDOTATeamInvite_InviteeResponseToGC\x12\x37\n\x06result\x18\x01 \x01(\x0e\x32\x12.ETeamInviteResult:\x13TEAM_INVITE_SUCCESS\"w\n&CMsgDOTATeamInvite_GCResponseToInviter\x12\x37\n\x06result\x18\x01 \x01(\x0e\x32\x12.ETeamInviteResult:\x13TEAM_INVITE_SUCCESS\x12\x14\n\x0cinvitee_name\x18\x02 \x01(\t\"t\n&CMsgDOTATeamInvite_GCResponseToInvitee\x12\x37\n\x06result\x18\x01 \x01(\x0e\x32\x12.ETeamInviteResult:\x13TEAM_INVITE_SUCCESS\x12\x11\n\tteam_name\x18\x02 \x01(\t\"=\n\x16\x43MsgDOTAKickTeamMember\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0f\n\x07team_id\x18\x02 \x01(\r\"\x90\x02\n\x1e\x43MsgDOTAKickTeamMemberResponse\x12?\n\x06result\x18\x01 \x01(\x0e\x32&.CMsgDOTAKickTeamMemberResponse.Result:\x07SUCCESS\"\xac\x01\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12 \n\x1c\x46\x41ILURE_INVALID_ACCOUNT_TYPE\x10\x01\x12\x1c\n\x18\x46\x41ILURE_KICKER_NOT_ADMIN\x10\x02\x12\x1d\n\x19\x46\x41ILURE_KICKEE_NOT_MEMBER\x10\x03\x12\x17\n\x13\x46\x41ILURE_TEAM_LOCKED\x10\x04\x12\x1d\n\x19\x46\x41ILURE_UNSPECIFIED_ERROR\x10\x05\"J\n\x19\x43MsgDOTATransferTeamAdmin\x12\x1c\n\x14new_admin_account_id\x18\x01 \x01(\r\x12\x0f\n\x07team_id\x18\x02 \x01(\r\"\x89\x02\n!CMsgDOTATransferTeamAdminResponse\x12\x42\n\x06result\x18\x01 \x01(\x0e\x32).CMsgDOTATransferTeamAdminResponse.Result:\x07SUCCESS\"\x9f\x01\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12 \n\x1c\x46\x41ILURE_INVALID_ACCOUNT_TYPE\x10\x01\x12\x15\n\x11\x46\x41ILURE_NOT_ADMIN\x10\x02\x12\x18\n\x14\x46\x41ILURE_SAME_ACCOUNT\x10\x03\x12\x16\n\x12\x46\x41ILURE_NOT_MEMBER\x10\x04\x12\x1d\n\x19\x46\x41ILURE_UNSPECIFIED_ERROR\x10\x05\"$\n\x11\x43MsgDOTALeaveTeam\x12\x0f\n\x07team_id\x18\x01 \x01(\r\"\xbe\x01\n\x19\x43MsgDOTALeaveTeamResponse\x12:\n\x06result\x18\x01 \x01(\x0e\x32!.CMsgDOTALeaveTeamResponse.Result:\x07SUCCESS\"e\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12\x16\n\x12\x46\x41ILURE_NOT_MEMBER\x10\x01\x12\x17\n\x13\x46\x41ILURE_TEAM_LOCKED\x10\x02\x12\x1d\n\x19\x46\x41ILURE_UNSPECIFIED_ERROR\x10\x03\"2\n\x19\x43MsgDOTABetaParticipation\x12\x15\n\raccess_rights\x18\x01 \x01(\r*\xde\x04\n\x11\x45TeamInviteResult\x12\x17\n\x13TEAM_INVITE_SUCCESS\x10\x00\x12\'\n#TEAM_INVITE_FAILURE_INVITE_REJECTED\x10\x01\x12&\n\"TEAM_INVITE_FAILURE_INVITE_TIMEOUT\x10\x02\x12*\n&TEAM_INVITE_ERROR_TEAM_AT_MEMBER_LIMIT\x10\x03\x12!\n\x1dTEAM_INVITE_ERROR_TEAM_LOCKED\x10\x04\x12+\n\'TEAM_INVITE_ERROR_INVITEE_NOT_AVAILABLE\x10\x05\x12\"\n\x1eTEAM_INVITE_ERROR_INVITEE_BUSY\x10\x06\x12,\n(TEAM_INVITE_ERROR_INVITEE_ALREADY_MEMBER\x10\x07\x12+\n\'TEAM_INVITE_ERROR_INVITEE_AT_TEAM_LIMIT\x10\x08\x12\x34\n0TEAM_INVITE_ERROR_INVITEE_INSUFFICIENT_PLAY_TIME\x10\t\x12\x32\n.TEAM_INVITE_ERROR_INVITER_INVALID_ACCOUNT_TYPE\x10\n\x12\'\n#TEAM_INVITE_ERROR_INVITER_NOT_ADMIN\x10\x0b\x12.\n*TEAM_INVITE_ERROR_INCORRECT_USER_RESPONDED\x10\x0c\x12!\n\x1dTEAM_INVITE_ERROR_UNSPECIFIED\x10\r')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_gcmessages_client_team_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ETEAMINVITERESULT']._serialized_start=4879
  _globals['_ETEAMINVITERESULT']._serialized_end=5485
  _globals['_CMSGDOTATEAMINFO']._serialized_start=63
  _globals['_CMSGDOTATEAMINFO']._serialized_end=1758
  _globals['_CMSGDOTATEAMINFO_HEROSTATS']._serialized_start=879
  _globals['_CMSGDOTATEAMINFO_HEROSTATS']._serialized_end=1044
  _globals['_CMSGDOTATEAMINFO_MEMBERSTATS']._serialized_start=1047
  _globals['_CMSGDOTATEAMINFO_MEMBERSTATS']._serialized_end=1239
  _globals['_CMSGDOTATEAMINFO_TEAMSTATS']._serialized_start=1242
  _globals['_CMSGDOTATEAMINFO_TEAMSTATS']._serialized_end=1422
  _globals['_CMSGDOTATEAMINFO_DPCRESULT']._serialized_start=1424
  _globals['_CMSGDOTATEAMINFO_DPCRESULT']._serialized_end=1525
  _globals['_CMSGDOTATEAMINFO_MEMBER']._serialized_start=1528
  _globals['_CMSGDOTATEAMINFO_MEMBER']._serialized_end=1683
  _globals['_CMSGDOTATEAMINFO_AUDITENTRY']._serialized_start=1685
  _globals['_CMSGDOTATEAMINFO_AUDITENTRY']._serialized_end=1758
  _globals['_CMSGDOTATEAMSINFO']._serialized_start=1760
  _globals['_CMSGDOTATEAMSINFO']._serialized_end=1832
  _globals['_CMSGDOTATEAMINFOLIST']._serialized_start=1834
  _globals['_CMSGDOTATEAMINFOLIST']._serialized_end=1890
  _globals['_CMSGDOTATEAMINFOCACHE']._serialized_start=1892
  _globals['_CMSGDOTATEAMINFOCACHE']._serialized_end=1982
  _globals['_CMSGDOTAMYTEAMINFOREQUEST']._serialized_start=1984
  _globals['_CMSGDOTAMYTEAMINFOREQUEST']._serialized_end=2011
  _globals['_CMSGDOTACREATETEAM']._serialized_start=2014
  _globals['_CMSGDOTACREATETEAM']._serialized_end=2215
  _globals['_CMSGDOTACREATETEAMRESPONSE']._serialized_start=2218
  _globals['_CMSGDOTACREATETEAMRESPONSE']._serialized_end=2753
  _globals['_CMSGDOTACREATETEAMRESPONSE_RESULT']._serialized_start=2327
  _globals['_CMSGDOTACREATETEAMRESPONSE_RESULT']._serialized_end=2753
  _globals['_CMSGDOTAEDITTEAMDETAILS']._serialized_start=2756
  _globals['_CMSGDOTAEDITTEAMDETAILS']._serialized_end=2983
  _globals['_CMSGDOTAEDITTEAMDETAILSRESPONSE']._serialized_start=2986
  _globals['_CMSGDOTAEDITTEAMDETAILSRESPONSE']._serialized_end=3223
  _globals['_CMSGDOTAEDITTEAMDETAILSRESPONSE_RESULT']._serialized_start=3088
  _globals['_CMSGDOTAEDITTEAMDETAILSRESPONSE_RESULT']._serialized_end=3223
  _globals['_CMSGDOTATEAMINVITE_INVITERTOGC']._serialized_start=3225
  _globals['_CMSGDOTATEAMINVITE_INVITERTOGC']._serialized_end=3294
  _globals['_CMSGDOTATEAMINVITE_GCIMMEDIATERESPONSETOINVITER']._serialized_start=3297
  _globals['_CMSGDOTATEAMINVITE_GCIMMEDIATERESPONSETOINVITER']._serialized_end=3453
  _globals['_CMSGDOTATEAMINVITE_GCREQUESTTOINVITEE']._serialized_start=3455
  _globals['_CMSGDOTATEAMINVITE_GCREQUESTTOINVITEE']._serialized_end=3573
  _globals['_CMSGDOTATEAMINVITE_INVITEERESPONSETOGC']._serialized_start=3575
  _globals['_CMSGDOTATEAMINVITE_INVITEERESPONSETOGC']._serialized_end=3672
  _globals['_CMSGDOTATEAMINVITE_GCRESPONSETOINVITER']._serialized_start=3674
  _globals['_CMSGDOTATEAMINVITE_GCRESPONSETOINVITER']._serialized_end=3793
  _globals['_CMSGDOTATEAMINVITE_GCRESPONSETOINVITEE']._serialized_start=3795
  _globals['_CMSGDOTATEAMINVITE_GCRESPONSETOINVITEE']._serialized_end=3911
  _globals['_CMSGDOTAKICKTEAMMEMBER']._serialized_start=3913
  _globals['_CMSGDOTAKICKTEAMMEMBER']._serialized_end=3974
  _globals['_CMSGDOTAKICKTEAMMEMBERRESPONSE']._serialized_start=3977
  _globals['_CMSGDOTAKICKTEAMMEMBERRESPONSE']._serialized_end=4249
  _globals['_CMSGDOTAKICKTEAMMEMBERRESPONSE_RESULT']._serialized_start=4077
  _globals['_CMSGDOTAKICKTEAMMEMBERRESPONSE_RESULT']._serialized_end=4249
  _globals['_CMSGDOTATRANSFERTEAMADMIN']._serialized_start=4251
  _globals['_CMSGDOTATRANSFERTEAMADMIN']._serialized_end=4325
  _globals['_CMSGDOTATRANSFERTEAMADMINRESPONSE']._serialized_start=4328
  _globals['_CMSGDOTATRANSFERTEAMADMINRESPONSE']._serialized_end=4593
  _globals['_CMSGDOTATRANSFERTEAMADMINRESPONSE_RESULT']._serialized_start=4434
  _globals['_CMSGDOTATRANSFERTEAMADMINRESPONSE_RESULT']._serialized_end=4593
  _globals['_CMSGDOTALEAVETEAM']._serialized_start=4595
  _globals['_CMSGDOTALEAVETEAM']._serialized_end=4631
  _globals['_CMSGDOTALEAVETEAMRESPONSE']._serialized_start=4634
  _globals['_CMSGDOTALEAVETEAMRESPONSE']._serialized_end=4824
  _globals['_CMSGDOTALEAVETEAMRESPONSE_RESULT']._serialized_start=4723
  _globals['_CMSGDOTALEAVETEAMRESPONSE_RESULT']._serialized_end=4824
  _globals['_CMSGDOTABETAPARTICIPATION']._serialized_start=4826
  _globals['_CMSGDOTABETAPARTICIPATION']._serialized_end=4876
# @@protoc_insertion_point(module_scope)
