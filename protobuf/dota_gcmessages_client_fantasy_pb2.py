# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_gcmessages_client_fantasy.proto
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
    'dota_gcmessages_client_fantasy.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dota_shared_enums_pb2 as dota__shared__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$dota_gcmessages_client_fantasy.proto\x1a\x17\x64ota_shared_enums.proto\"\x85\x05\n\x12\x43MsgDOTAPlayerInfo\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12<\n\x0c\x66\x61ntasy_role\x18\x04 \x01(\x0e\x32\x0e.Fantasy_Roles:\x16\x46\x41NTASY_ROLE_UNDEFINED\x12\x0f\n\x07team_id\x18\x05 \x01(\r\x12\x11\n\tteam_name\x18\x06 \x01(\t\x12\x10\n\x08team_tag\x18\x07 \x01(\t\x12\x0f\n\x07sponsor\x18\x08 \x01(\t\x12\x11\n\tis_locked\x18\t \x01(\x08\x12\x0e\n\x06is_pro\x18\n \x01(\x08\x12\x11\n\treal_name\x18\x0b \x01(\t\x12\x16\n\x0etotal_earnings\x18\r \x01(\r\x12,\n\x07results\x18\x0e \x03(\x0b\x32\x1b.CMsgDOTAPlayerInfo.Results\x12\x15\n\rteam_url_logo\x18\x0f \x01(\t\x12\x35\n\raudit_entries\x18\x10 \x03(\x0b\x32\x1e.CMsgDOTAPlayerInfo.AuditEntry\x12\x19\n\x11team_abbreviation\x18\x11 \x01(\t\x1a\x41\n\x07Results\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x11\n\tplacement\x18\x02 \x01(\r\x12\x10\n\x08\x65\x61rnings\x18\x03 \x01(\r\x1a\x89\x01\n\nAuditEntry\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\r\x12\x15\n\rend_timestamp\x18\x02 \x01(\r\x12\x0f\n\x07team_id\x18\x03 \x01(\r\x12\x11\n\tteam_name\x18\x04 \x01(\t\x12\x10\n\x08team_tag\x18\x05 \x01(\t\x12\x15\n\rteam_url_logo\x18\x06 \x01(\t\"C\n\x16\x43MsgDOTAPlayerInfoList\x12)\n\x0cplayer_infos\x18\x01 \x03(\x0b\x32\x13.CMsgDOTAPlayerInfo\"n\n\x12\x43MsgDOTATeamRoster\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x0f\n\x07team_id\x18\x02 \x01(\r\x12\x1a\n\x12member_account_ids\x18\x03 \x03(\r\x12\x18\n\x10\x63oach_account_id\x18\x04 \x01(\r\"\x8b\x03\n\x16\x43MsgDOTADPCProfileInfo\x12(\n\x0bplayer_info\x18\x01 \x01(\x0b\x32\x13.CMsgDOTAPlayerInfo\x12?\n\x0fprediction_info\x18\x02 \x01(\x0b\x32&.CMsgDOTADPCProfileInfo.PredictionInfo\x12\x39\n\x0c\x66\x61ntasy_info\x18\x03 \x01(\x0b\x32#.CMsgDOTADPCProfileInfo.FantasyInfo\x12\x1e\n\x16\x64isabled_notifications\x18\x04 \x03(\r\x1a\x39\n\x0ePredictionInfo\x12\x0f\n\x07percent\x18\x01 \x01(\r\x12\x16\n\x0eshard_winnings\x18\x02 \x01(\x05\x1ap\n\x0b\x46\x61ntasyInfo\x12\x17\n\x0ftop_90_finishes\x18\x01 \x01(\r\x12\x17\n\x0ftop_75_finishes\x18\x02 \x01(\r\x12\x17\n\x0ftop_50_finishes\x18\x03 \x01(\r\x12\x16\n\x0eshard_winnings\x18\x04 \x01(\r\"\x91\x01\n\x14\x43MsgDOTALeaderboards\x12=\n\x0cleaderboards\x18\x02 \x03(\x0b\x32\'.CMsgDOTALeaderboards.RegionLeaderboard\x1a:\n\x11RegionLeaderboard\x12\x10\n\x08\x64ivision\x18\x01 \x01(\r\x12\x13\n\x0b\x61\x63\x63ount_ids\x18\x02 \x03(\r\"Z\n\x1d\x43MsgDOTAPassportVoteTeamGuess\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x11\n\twinner_id\x18\x02 \x01(\r\x12\x13\n\x0brunnerup_id\x18\x03 \x01(\r\"\x91\x01\n$CMsgDOTAPassportVoteGenericSelection\x12V\n\x0fselection_index\x18\x01 \x01(\x0e\x32\".DOTA_2013PassportSelectionIndices:\x19PP13_SEL_ALLSTAR_PLAYER_0\x12\x11\n\tselection\x18\x02 \x01(\r\"F\n\x1d\x43MsgDOTAPassportStampedPlayer\x12\x10\n\x08steam_id\x18\x01 \x01(\x04\x12\x13\n\x0bstamp_level\x18\x02 \x01(\r\";\n#CMsgDOTAPassportPlayerCardChallenge\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\r\"\x8c\x02\n\x14\x43MsgDOTAPassportVote\x12\x32\n\nteam_votes\x18\x01 \x03(\x0b\x32\x1e.CMsgDOTAPassportVoteTeamGuess\x12\x41\n\x12generic_selections\x18\x02 \x03(\x0b\x32%.CMsgDOTAPassportVoteGenericSelection\x12\x37\n\x0fstamped_players\x18\x03 \x03(\x0b\x32\x1e.CMsgDOTAPassportStampedPlayer\x12\x44\n\x16player_card_challenges\x18\x04 \x03(\x0b\x32$.CMsgDOTAPassportPlayerCardChallenge\"a\n(CMsgClientToGCGetPlayerCardRosterRequest\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\"\n\x0e\x66\x61ntasy_period\x18\x03 \x01(\r:\n4294967295\"\xb2\x02\n)CMsgClientToGCGetPlayerCardRosterResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32\x31.CMsgClientToGCGetPlayerCardRosterResponse.Result:\x07SUCCESS\x12\x1b\n\x13player_card_item_id\x18\x02 \x03(\x04\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x11\n\tfinalized\x18\x04 \x01(\x08\x12\x12\n\npercentile\x18\x05 \x01(\x02\"f\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12\x15\n\x11\x45RROR_UNSPECIFIED\x10\x01\x12\x1b\n\x17\x45RROR_INVALID_LEAGUE_ID\x10\x02\x12\x1b\n\x17\x45RROR_INVALID_TIMESTAMP\x10\x03\"\xd4\x01\n-CMsgClientToGCBatchGetPlayerCardRosterRequest\x12Y\n\x11league_timestamps\x18\x01 \x03(\x0b\x32>.CMsgClientToGCBatchGetPlayerCardRosterRequest.LeagueTimestamp\x1aH\n\x0fLeagueTimestamp\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\"\n\x0e\x66\x61ntasy_period\x18\x03 \x01(\r:\n4294967295\"\xf7\x03\n.CMsgClientToGCBatchGetPlayerCardRosterResponse\x12Q\n\tresponses\x18\x01 \x03(\x0b\x32>.CMsgClientToGCBatchGetPlayerCardRosterResponse.RosterResponse\x1a\x89\x02\n\x0eRosterResponse\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x1c\n\x14\x64\x65precated_timestamp\x18\x02 \x01(\r\x12O\n\x06result\x18\x03 \x01(\x0e\x32\x36.CMsgClientToGCBatchGetPlayerCardRosterResponse.Result:\x07SUCCESS\x12\x1b\n\x13player_card_item_id\x18\x04 \x03(\x04\x12\r\n\x05score\x18\x05 \x01(\x02\x12\x11\n\tfinalized\x18\x06 \x01(\x08\x12\x12\n\npercentile\x18\x07 \x01(\x02\x12\"\n\x0e\x66\x61ntasy_period\x18\x08 \x01(\r:\n4294967295\"f\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12\x15\n\x11\x45RROR_UNSPECIFIED\x10\x01\x12\x1b\n\x17\x45RROR_INVALID_LEAGUE_ID\x10\x02\x12\x1b\n\x17\x45RROR_INVALID_TIMESTAMP\x10\x03\"\xbc\x01\n(CMsgClientToGCSetPlayerCardRosterRequest\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x1c\n\x14\x64\x65precated_timestamp\x18\x02 \x01(\r\x12\x0c\n\x04slot\x18\x03 \x01(\r\x12\x1b\n\x13player_card_item_id\x18\x04 \x01(\x04\x12\x10\n\x08\x65vent_id\x18\x05 \x01(\r\x12\"\n\x0e\x66\x61ntasy_period\x18\x06 \x01(\r:\n4294967295\"\xac\x03\n)CMsgClientToGCSetPlayerCardRosterResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32\x31.CMsgClientToGCSetPlayerCardRosterResponse.Result:\x07SUCCESS\"\xb2\x02\n\x06Result\x12\x0b\n\x07SUCCESS\x10\x00\x12\x15\n\x11\x45RROR_UNSPECIFIED\x10\x01\x12\x1b\n\x17\x45RROR_INVALID_LEAGUE_ID\x10\x02\x12\x1b\n\x17\x45RROR_INVALID_TIMESTAMP\x10\x03\x12\x1f\n\x1b\x45RROR_PLAYER_CARD_NOT_OWNED\x10\x04\x12\x16\n\x12\x45RROR_INVALID_SLOT\x10\x05\x12\x1a\n\x16\x45RROR_FAILED_CARD_INFO\x10\x06\x12\x1b\n\x17\x45RROR_ACCOUNT_DUPLICATE\x10\x07\x12\x1a\n\x16\x45RROR_LOCKED_TIMESTAMP\x10\x08\x12#\n\x1f\x45RROR_INVALID_LEAGUE_FOR_PERIOD\x10\t\x12\x17\n\x13\x45RROR_INVALID_EVENT\x10\n\"\xe9\x02\n\x1e\x43MsgDOTAFantasyDPCLeagueStatus\x12@\n\x0cleague_infos\x18\x01 \x03(\x0b\x32*.CMsgDOTAFantasyDPCLeagueStatus.LeagueInfo\x1a\xc2\x01\n\nLeagueInfo\x12\x11\n\tleague_id\x18\x01 \x01(\r\x12\x13\n\x0bleague_name\x18\x02 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x03 \x01(\r\x12\x15\n\rend_timestamp\x18\x04 \x01(\r\x12\x16\n\x0e\x64\x61y_timestamps\x18\x05 \x03(\r\x12\x44\n\x06status\x18\x08 \x01(\x0e\x32-.CMsgDOTAFantasyDPCLeagueStatus.ERosterStatus:\x05UNSET\"@\n\rERosterStatus\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\x12\r\n\tCONCLUDED\x10\x03\"\xe1\x03\n\x18\x43MsgDOTADPCSearchResults\x12\x31\n\x07players\x18\x01 \x03(\x0b\x32 .CMsgDOTADPCSearchResults.Player\x12-\n\x05teams\x18\x02 \x03(\x0b\x32\x1e.CMsgDOTADPCSearchResults.Team\x12\x31\n\x07leagues\x18\x03 \x03(\x0b\x32 .CMsgDOTADPCSearchResults.League\x1a\x35\n\x06Player\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\treal_name\x18\x03 \x01(\t\x1a-\n\x04Team\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x1a\"\n\x06League\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xa5\x01\n\x15\x45SearchResultsDesired\x12#\n\x1fk_ESearchResultsDesired_Players\x10\x01\x12!\n\x1dk_ESearchResultsDesired_Teams\x10\x02\x12#\n\x1fk_ESearchResultsDesired_Leagues\x10\x04\x12\x1f\n\x1bk_ESearchResultsDesired_All\x10\x07\"\x83\x01\n\x1f\x43MsgDOTADPCTeamFavoriteRankings\x12\x34\n\x05teams\x18\x01 \x03(\x0b\x32%.CMsgDOTADPCTeamFavoriteRankings.Team\x1a*\n\x04Team\x12\x0f\n\x07team_id\x18\x01 \x01(\r\x12\x11\n\tfavorites\x18\x02 \x01(\r\"\xba\x04\n\'CMsgDotaFantasyCraftingTabletPeriodData\x12\"\n\x0e\x66\x61ntasy_period\x18\x01 \x01(\r:\n4294967295\x12@\n\x07tablets\x18\x02 \x03(\x0b\x32/.CMsgDotaFantasyCraftingTabletPeriodData.Tablet\x1a\xa2\x01\n\x03Gem\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32\x11.Fantasy_Gem_Type:\x15\x46\x41NTASY_GEM_TYPE_RUBY\x12\x0c\n\x04slot\x18\x02 \x01(\r\x12\r\n\x05shape\x18\x03 \x01(\r\x12\x0f\n\x07quality\x18\x04 \x01(\r\x12\x35\n\x04stat\x18\x05 \x01(\x0e\x32\x10.Fantasy_Scoring:\x15\x46\x41NTASY_SCORING_KILLS\x1a\x83\x02\n\x06Tablet\x12\x11\n\ttablet_id\x18\x01 \x01(\r\x12\x14\n\x0ctablet_level\x18\x02 \x01(\r\x12<\n\x0c\x66\x61ntasy_role\x18\x03 \x01(\x0e\x32\x0e.Fantasy_Roles:\x16\x46\x41NTASY_ROLE_UNDEFINED\x12\x12\n\naccount_id\x18\x04 \x01(\r\x12\x0e\n\x06prefix\x18\x05 \x01(\r\x12\x0e\n\x06suffix\x18\x06 \x01(\r\x12:\n\x04gems\x18\x07 \x03(\x0b\x32,.CMsgDotaFantasyCraftingTabletPeriodData.Gem\x12\r\n\x05score\x18\x08 \x01(\x02\x12\x13\n\x0b\x62\x65st_series\x18\t \x01(\r\"\xd8\x01\n!CMsgDotaFantasyCraftingTabletData\x12T\n\x12tablet_period_data\x18\x01 \x03(\x0b\x32\x38.CMsgDotaFantasyCraftingTabletData.TabletPeriodDataEntry\x1a]\n\x15TabletPeriodDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.CMsgDotaFantasyCraftingTabletPeriodData\"\xa5\x03\n\x1f\x43MsgDotaFantasyCraftingUserData\x12\x17\n\x0f\x61vailable_rolls\x18\x01 \x03(\r\x12R\n\x12period_roll_tokens\x18\x02 \x03(\x0b\x32\x36.CMsgDotaFantasyCraftingUserData.PeriodRollTokensEntry\x12I\n\rperiod_scores\x18\x03 \x03(\x0b\x32\x32.CMsgDotaFantasyCraftingUserData.PeriodScoresEntry\x1a\x36\n\x0bPeriodScore\x12\x13\n\x0btotal_score\x18\x01 \x01(\x02\x12\x12\n\npercentile\x18\x02 \x01(\x02\x1a\x33\n\x15PeriodRollTokensEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\x1a]\n\x11PeriodScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.CMsgDotaFantasyCraftingUserData.PeriodScore\"\xe0\x01\n CMsgDotaFantasyCraftingDataCache\x12\x43\n\rcache_entries\x18\x01 \x03(\x0b\x32,.CMsgDotaFantasyCraftingDataCache.CacheEntry\x1aw\n\nCacheEntry\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x16\n\x0e\x66\x61ntasy_league\x18\x02 \x01(\r\x12=\n\ncache_data\x18\x03 \x01(\x0b\x32).CMsgGCToClientFantasyCraftingDataUpdated\"R\n$CMsgClientToGCFantasyCraftingGetData\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x12\n\naccount_id\x18\x02 \x01(\r\"\xf3\x02\n,CMsgClientToGCFantasyCraftingGetDataResponse\x12[\n\x08response\x18\x01 \x01(\x0e\x32\x37.CMsgClientToGCFantasyCraftingGetDataResponse.EResponse:\x10k_eInternalError\x12\x33\n\tuser_data\x18\x02 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\x12\x37\n\x0btablet_data\x18\x04 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"x\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\"\x84\x01\n-CMsgClientToGCFantasyCraftingPerformOperation\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x11\n\ttablet_id\x18\x02 \x01(\r\x12\x14\n\x0coperation_id\x18\x03 \x01(\r\x12\x12\n\nextra_data\x18\x04 \x01(\x04\"\xb1\x05\n5CMsgClientToGCFantasyCraftingPerformOperationResponse\x12\x64\n\x08response\x18\x01 \x01(\x0e\x32@.CMsgClientToGCFantasyCraftingPerformOperationResponse.EResponse:\x10k_eInternalError\x12\x14\n\x0coperation_id\x18\x02 \x01(\r\x12\x11\n\ttablet_id\x18\x07 \x01(\r\x12\x33\n\tuser_data\x18\x08 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\x12\x37\n\x0btablet_data\x18\t \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\x12\x16\n\x0eplayer_choices\x18\x03 \x03(\r\x12\x16\n\x0eprefix_choices\x18\x04 \x03(\r\x12\x16\n\x0esuffix_choices\x18\x05 \x03(\r\x12Y\n\rtitle_choices\x18\x06 \x03(\x0b\x32\x42.CMsgClientToGCFantasyCraftingPerformOperationResponse.TitleChoice\x1a;\n\x0bTitleChoice\x12\x15\n\rprefix_choice\x18\x01 \x01(\r\x12\x15\n\rsuffix_choice\x18\x02 \x01(\r\"\x9a\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\x12\x0f\n\x0bk_eNoTokens\x10\x06\x12\x0f\n\x0bk_eMoreInfo\x10\x07\"\xb0\x01\n(CMsgGCToClientFantasyCraftingDataUpdated\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x33\n\tuser_data\x18\x02 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\x12\x37\n\x0btablet_data\x18\x04 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"\xb0\x01\n,CMsgClientToGCFantasyCraftingDevModifyTablet\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x14\n\x0creset_tablet\x18\x02 \x01(\x08\x12\x15\n\rmodify_tokens\x18\x03 \x01(\r\x12\x17\n\x0fupgrade_tablets\x18\x06 \x01(\x08\x12\"\n\x0e\x66\x61ntasy_period\x18\x05 \x01(\r:\n4294967295\"\x83\x03\n4CMsgClientToGCFantasyCraftingDevModifyTabletResponse\x12\x63\n\x08response\x18\x01 \x01(\x0e\x32?.CMsgClientToGCFantasyCraftingDevModifyTabletResponse.EResponse:\x10k_eInternalError\x12\x33\n\tuser_data\x18\x02 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\x12\x37\n\x0btablet_data\x18\x03 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"x\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\"W\n)CMsgClientToGCFantasyCraftingSelectPlayer\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x12\n\naccount_id\x18\x02 \x01(\r\"\xdf\x02\n1CMsgClientToGCFantasyCraftingSelectPlayerResponse\x12`\n\x08response\x18\x01 \x01(\x0e\x32<.CMsgClientToGCFantasyCraftingSelectPlayerResponse.EResponse:\x10k_eInternalError\x12\x37\n\x0btablet_data\x18\x02 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"\x8e\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\x12\x14\n\x10k_eInvalidPlayer\x10\x06\"[\n,CMsgClientToGCFantasyCraftingGenerateTablets\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\x12\x13\n\x0b\x61\x63\x63ount_ids\x18\x02 \x03(\r\"\x9a\x03\n4CMsgClientToGCFantasyCraftingGenerateTabletsResponse\x12\x63\n\x08response\x18\x01 \x01(\x0e\x32?.CMsgClientToGCFantasyCraftingGenerateTabletsResponse.EResponse:\x10k_eInternalError\x12\x33\n\tuser_data\x18\x02 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\x12\x37\n\x0btablet_data\x18\x03 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"\x8e\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\x12\x14\n\x10k_eInvalidPlayer\x10\x06\"E\n+CMsgClientToGcFantasyCraftingUpgradeTablets\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\"\xcc\x02\n3CMsgClientToGcFantasyCraftingUpgradeTabletsResponse\x12\x62\n\x08response\x18\x01 \x01(\x0e\x32>.CMsgClientToGcFantasyCraftingUpgradeTabletsResponse.EResponse:\x10k_eInternalError\x12\x37\n\x0btablet_data\x18\x03 \x01(\x0b\x32\".CMsgDotaFantasyCraftingTabletData\"x\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\"D\n*CMsgClientToGCFantasyCraftingRerollOptions\x12\x16\n\x0e\x66\x61ntasy_league\x18\x01 \x01(\r\"\xe2\x02\n2CMsgClientToGCFantasyCraftingRerollOptionsResponse\x12\x61\n\x08response\x18\x01 \x01(\x0e\x32=.CMsgClientToGCFantasyCraftingRerollOptionsResponse.EResponse:\x10k_eInternalError\x12\x33\n\tuser_data\x18\x02 \x01(\x0b\x32 .CMsgDotaFantasyCraftingUserData\"\x93\x01\n\tEResponse\x12\x14\n\x10k_eInternalError\x10\x00\x12\x0e\n\nk_eSuccess\x10\x01\x12\x0e\n\nk_eTooBusy\x10\x02\x12\x0f\n\x0bk_eDisabled\x10\x03\x12\x0e\n\nk_eTimeout\x10\x04\x12\x14\n\x10k_eInvalidLeague\x10\x05\x12\x19\n\x15k_eInsufficientTokens\x10\x06*\xa3\x15\n!DOTA_2013PassportSelectionIndices\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_0\x10\x00\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_1\x10\x01\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_2\x10\x02\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_3\x10\x03\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_4\x10\x04\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_5\x10\x05\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_6\x10\x06\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_7\x10\x07\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_8\x10\x08\x12\x1d\n\x19PP13_SEL_ALLSTAR_PLAYER_9\x10\t\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_0\x10\n\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_1\x10\x0b\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_2\x10\x0c\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_3\x10\r\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_4\x10\x0e\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_5\x10\x0f\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_6\x10\x10\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_7\x10\x11\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_8\x10\x12\x12\x1c\n\x18PP13_SEL_QUALPRED_WEST_9\x10\x13\x12\x1d\n\x19PP13_SEL_QUALPRED_WEST_10\x10\x14\x12\x1d\n\x19PP13_SEL_QUALPRED_WEST_11\x10\x15\x12\x1d\n\x19PP13_SEL_QUALPRED_WEST_12\x10\x16\x12\x1d\n\x19PP13_SEL_QUALPRED_WEST_13\x10\x17\x12\x1d\n\x19PP13_SEL_QUALPRED_WEST_14\x10\x18\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_0\x10\x19\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_1\x10\x1a\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_2\x10\x1b\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_3\x10\x1c\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_4\x10\x1d\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_5\x10\x1e\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_6\x10\x1f\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_7\x10 \x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_8\x10!\x12\x1c\n\x18PP13_SEL_QUALPRED_EAST_9\x10\"\x12\x1d\n\x19PP13_SEL_QUALPRED_EAST_10\x10#\x12\x1d\n\x19PP13_SEL_QUALPRED_EAST_11\x10$\x12\x1d\n\x19PP13_SEL_QUALPRED_EAST_12\x10%\x12\x1d\n\x19PP13_SEL_QUALPRED_EAST_13\x10&\x12\x1d\n\x19PP13_SEL_QUALPRED_EAST_14\x10\'\x12\x19\n\x15PP13_SEL_TEAMCUP_TEAM\x10(\x12\x1b\n\x17PP13_SEL_TEAMCUP_PLAYER\x10)\x12\x1e\n\x1aPP13_SEL_TEAMCUP_TEAM_LOCK\x10*\x12 \n\x1cPP13_SEL_TEAMCUP_PLAYER_LOCK\x10+\x12\x18\n\x14PP13_SEL_EVENTPRED_0\x10,\x12\x18\n\x14PP13_SEL_EVENTPRED_1\x10-\x12\x18\n\x14PP13_SEL_EVENTPRED_2\x10.\x12\x18\n\x14PP13_SEL_EVENTPRED_3\x10/\x12\x18\n\x14PP13_SEL_EVENTPRED_4\x10\x30\x12\x18\n\x14PP13_SEL_EVENTPRED_5\x10\x31\x12\x18\n\x14PP13_SEL_EVENTPRED_6\x10\x32\x12\x18\n\x14PP13_SEL_EVENTPRED_7\x10\x33\x12\x18\n\x14PP13_SEL_EVENTPRED_8\x10\x34\x12\x18\n\x14PP13_SEL_EVENTPRED_9\x10\x35\x12\x19\n\x15PP13_SEL_EVENTPRED_10\x10\x36\x12\x19\n\x15PP13_SEL_EVENTPRED_11\x10\x37\x12\x19\n\x15PP13_SEL_EVENTPRED_12\x10\x38\x12\x19\n\x15PP13_SEL_EVENTPRED_13\x10\x39\x12\x19\n\x15PP13_SEL_EVENTPRED_14\x10:\x12\x19\n\x15PP13_SEL_EVENTPRED_15\x10;\x12\x19\n\x15PP13_SEL_EVENTPRED_16\x10<\x12\x19\n\x15PP13_SEL_EVENTPRED_17\x10=\x12\x19\n\x15PP13_SEL_EVENTPRED_18\x10>\x12\x19\n\x15PP13_SEL_EVENTPRED_19\x10?\x12\x19\n\x15PP13_SEL_EVENTPRED_20\x10@\x12\x19\n\x15PP13_SEL_EVENTPRED_21\x10\x41\x12\x19\n\x15PP13_SEL_EVENTPRED_22\x10\x42\x12\x19\n\x15PP13_SEL_EVENTPRED_23\x10\x43\x12\x19\n\x15PP13_SEL_EVENTPRED_24\x10\x44\x12\x19\n\x15PP13_SEL_EVENTPRED_25\x10\x45\x12\x19\n\x15PP13_SEL_EVENTPRED_26\x10\x46\x12\x19\n\x15PP13_SEL_EVENTPRED_27\x10G\x12\x19\n\x15PP13_SEL_EVENTPRED_28\x10H\x12\x19\n\x15PP13_SEL_EVENTPRED_29\x10I\x12\x19\n\x15PP13_SEL_EVENTPRED_30\x10J\x12\x19\n\x15PP13_SEL_EVENTPRED_31\x10K\x12\x19\n\x15PP13_SEL_EVENTPRED_32\x10L\x12\x19\n\x15PP13_SEL_EVENTPRED_33\x10M\x12\x19\n\x15PP13_SEL_EVENTPRED_34\x10N\x12\x19\n\x15PP13_SEL_EVENTPRED_35\x10O\x12\x19\n\x15PP13_SEL_EVENTPRED_36\x10P\x12\x19\n\x15PP13_SEL_EVENTPRED_37\x10Q\x12\x19\n\x15PP13_SEL_EVENTPRED_38\x10R\x12\x19\n\x15PP13_SEL_EVENTPRED_39\x10S\x12\x19\n\x15PP13_SEL_EVENTPRED_40\x10T\x12\x19\n\x15PP13_SEL_EVENTPRED_41\x10U\x12\x19\n\x15PP13_SEL_EVENTPRED_42\x10V\x12\x19\n\x15PP13_SEL_EVENTPRED_43\x10W\x12\x13\n\x0fPP13_SEL_SOLO_0\x10X\x12\x13\n\x0fPP13_SEL_SOLO_1\x10Y\x12\x13\n\x0fPP13_SEL_SOLO_2\x10Z\x12\x13\n\x0fPP13_SEL_SOLO_3\x10[\x12\x13\n\x0fPP13_SEL_SOLO_4\x10\\\x12\x13\n\x0fPP13_SEL_SOLO_5\x10]\x12\x13\n\x0fPP13_SEL_SOLO_6\x10^\x12\x13\n\x0fPP13_SEL_SOLO_7\x10_')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_gcmessages_client_fantasy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOTA_2013PASSPORTSELECTIONINDICES']._serialized_start=10076
  _globals['_DOTA_2013PASSPORTSELECTIONINDICES']._serialized_end=12799
  _globals['_CMSGDOTAPLAYERINFO']._serialized_start=66
  _globals['_CMSGDOTAPLAYERINFO']._serialized_end=711
  _globals['_CMSGDOTAPLAYERINFO_RESULTS']._serialized_start=506
  _globals['_CMSGDOTAPLAYERINFO_RESULTS']._serialized_end=571
  _globals['_CMSGDOTAPLAYERINFO_AUDITENTRY']._serialized_start=574
  _globals['_CMSGDOTAPLAYERINFO_AUDITENTRY']._serialized_end=711
  _globals['_CMSGDOTAPLAYERINFOLIST']._serialized_start=713
  _globals['_CMSGDOTAPLAYERINFOLIST']._serialized_end=780
  _globals['_CMSGDOTATEAMROSTER']._serialized_start=782
  _globals['_CMSGDOTATEAMROSTER']._serialized_end=892
  _globals['_CMSGDOTADPCPROFILEINFO']._serialized_start=895
  _globals['_CMSGDOTADPCPROFILEINFO']._serialized_end=1290
  _globals['_CMSGDOTADPCPROFILEINFO_PREDICTIONINFO']._serialized_start=1119
  _globals['_CMSGDOTADPCPROFILEINFO_PREDICTIONINFO']._serialized_end=1176
  _globals['_CMSGDOTADPCPROFILEINFO_FANTASYINFO']._serialized_start=1178
  _globals['_CMSGDOTADPCPROFILEINFO_FANTASYINFO']._serialized_end=1290
  _globals['_CMSGDOTALEADERBOARDS']._serialized_start=1293
  _globals['_CMSGDOTALEADERBOARDS']._serialized_end=1438
  _globals['_CMSGDOTALEADERBOARDS_REGIONLEADERBOARD']._serialized_start=1380
  _globals['_CMSGDOTALEADERBOARDS_REGIONLEADERBOARD']._serialized_end=1438
  _globals['_CMSGDOTAPASSPORTVOTETEAMGUESS']._serialized_start=1440
  _globals['_CMSGDOTAPASSPORTVOTETEAMGUESS']._serialized_end=1530
  _globals['_CMSGDOTAPASSPORTVOTEGENERICSELECTION']._serialized_start=1533
  _globals['_CMSGDOTAPASSPORTVOTEGENERICSELECTION']._serialized_end=1678
  _globals['_CMSGDOTAPASSPORTSTAMPEDPLAYER']._serialized_start=1680
  _globals['_CMSGDOTAPASSPORTSTAMPEDPLAYER']._serialized_end=1750
  _globals['_CMSGDOTAPASSPORTPLAYERCARDCHALLENGE']._serialized_start=1752
  _globals['_CMSGDOTAPASSPORTPLAYERCARDCHALLENGE']._serialized_end=1811
  _globals['_CMSGDOTAPASSPORTVOTE']._serialized_start=1814
  _globals['_CMSGDOTAPASSPORTVOTE']._serialized_end=2082
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERREQUEST']._serialized_start=2084
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERREQUEST']._serialized_end=2181
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERRESPONSE']._serialized_start=2184
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERRESPONSE']._serialized_end=2490
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_start=2388
  _globals['_CMSGCLIENTTOGCGETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_end=2490
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERREQUEST']._serialized_start=2493
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERREQUEST']._serialized_end=2705
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERREQUEST_LEAGUETIMESTAMP']._serialized_start=2633
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERREQUEST_LEAGUETIMESTAMP']._serialized_end=2705
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE']._serialized_start=2708
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE']._serialized_end=3211
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE_ROSTERRESPONSE']._serialized_start=2842
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE_ROSTERRESPONSE']._serialized_end=3107
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_start=2388
  _globals['_CMSGCLIENTTOGCBATCHGETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_end=2490
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERREQUEST']._serialized_start=3214
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERREQUEST']._serialized_end=3402
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERRESPONSE']._serialized_start=3405
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERRESPONSE']._serialized_end=3833
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_start=3527
  _globals['_CMSGCLIENTTOGCSETPLAYERCARDROSTERRESPONSE_RESULT']._serialized_end=3833
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS']._serialized_start=3836
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS']._serialized_end=4197
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS_LEAGUEINFO']._serialized_start=3937
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS_LEAGUEINFO']._serialized_end=4131
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS_EROSTERSTATUS']._serialized_start=4133
  _globals['_CMSGDOTAFANTASYDPCLEAGUESTATUS_EROSTERSTATUS']._serialized_end=4197
  _globals['_CMSGDOTADPCSEARCHRESULTS']._serialized_start=4200
  _globals['_CMSGDOTADPCSEARCHRESULTS']._serialized_end=4681
  _globals['_CMSGDOTADPCSEARCHRESULTS_PLAYER']._serialized_start=4377
  _globals['_CMSGDOTADPCSEARCHRESULTS_PLAYER']._serialized_end=4430
  _globals['_CMSGDOTADPCSEARCHRESULTS_TEAM']._serialized_start=4432
  _globals['_CMSGDOTADPCSEARCHRESULTS_TEAM']._serialized_end=4477
  _globals['_CMSGDOTADPCSEARCHRESULTS_LEAGUE']._serialized_start=4479
  _globals['_CMSGDOTADPCSEARCHRESULTS_LEAGUE']._serialized_end=4513
  _globals['_CMSGDOTADPCSEARCHRESULTS_ESEARCHRESULTSDESIRED']._serialized_start=4516
  _globals['_CMSGDOTADPCSEARCHRESULTS_ESEARCHRESULTSDESIRED']._serialized_end=4681
  _globals['_CMSGDOTADPCTEAMFAVORITERANKINGS']._serialized_start=4684
  _globals['_CMSGDOTADPCTEAMFAVORITERANKINGS']._serialized_end=4815
  _globals['_CMSGDOTADPCTEAMFAVORITERANKINGS_TEAM']._serialized_start=4773
  _globals['_CMSGDOTADPCTEAMFAVORITERANKINGS_TEAM']._serialized_end=4815
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA']._serialized_start=4818
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA']._serialized_end=5388
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA_GEM']._serialized_start=4964
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA_GEM']._serialized_end=5126
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA_TABLET']._serialized_start=5129
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETPERIODDATA_TABLET']._serialized_end=5388
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETDATA']._serialized_start=5391
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETDATA']._serialized_end=5607
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETDATA_TABLETPERIODDATAENTRY']._serialized_start=5514
  _globals['_CMSGDOTAFANTASYCRAFTINGTABLETDATA_TABLETPERIODDATAENTRY']._serialized_end=5607
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA']._serialized_start=5610
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA']._serialized_end=6031
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODSCORE']._serialized_start=5829
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODSCORE']._serialized_end=5883
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODROLLTOKENSENTRY']._serialized_start=5885
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODROLLTOKENSENTRY']._serialized_end=5936
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODSCORESENTRY']._serialized_start=5938
  _globals['_CMSGDOTAFANTASYCRAFTINGUSERDATA_PERIODSCORESENTRY']._serialized_end=6031
  _globals['_CMSGDOTAFANTASYCRAFTINGDATACACHE']._serialized_start=6034
  _globals['_CMSGDOTAFANTASYCRAFTINGDATACACHE']._serialized_end=6258
  _globals['_CMSGDOTAFANTASYCRAFTINGDATACACHE_CACHEENTRY']._serialized_start=6139
  _globals['_CMSGDOTAFANTASYCRAFTINGDATACACHE_CACHEENTRY']._serialized_end=6258
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATA']._serialized_start=6260
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATA']._serialized_end=6342
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATARESPONSE']._serialized_start=6345
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATARESPONSE']._serialized_end=6716
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATARESPONSE_ERESPONSE']._serialized_start=6596
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGETDATARESPONSE_ERESPONSE']._serialized_end=6716
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATION']._serialized_start=6719
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATION']._serialized_end=6851
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE']._serialized_start=6854
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE']._serialized_end=7543
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE_TITLECHOICE']._serialized_start=7327
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE_TITLECHOICE']._serialized_end=7386
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE_ERESPONSE']._serialized_start=7389
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGPERFORMOPERATIONRESPONSE_ERESPONSE']._serialized_end=7543
  _globals['_CMSGGCTOCLIENTFANTASYCRAFTINGDATAUPDATED']._serialized_start=7546
  _globals['_CMSGGCTOCLIENTFANTASYCRAFTINGDATAUPDATED']._serialized_end=7722
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLET']._serialized_start=7725
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLET']._serialized_end=7901
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLETRESPONSE']._serialized_start=7904
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLETRESPONSE']._serialized_end=8291
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLETRESPONSE_ERESPONSE']._serialized_start=6596
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGDEVMODIFYTABLETRESPONSE_ERESPONSE']._serialized_end=6716
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYER']._serialized_start=8293
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYER']._serialized_end=8380
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYERRESPONSE']._serialized_start=8383
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYERRESPONSE']._serialized_end=8734
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYERRESPONSE_ERESPONSE']._serialized_start=8592
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGSELECTPLAYERRESPONSE_ERESPONSE']._serialized_end=8734
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETS']._serialized_start=8736
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETS']._serialized_end=8827
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETSRESPONSE']._serialized_start=8830
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETSRESPONSE']._serialized_end=9240
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETSRESPONSE_ERESPONSE']._serialized_start=8592
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGGENERATETABLETSRESPONSE_ERESPONSE']._serialized_end=8734
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETS']._serialized_start=9242
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETS']._serialized_end=9311
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETSRESPONSE']._serialized_start=9314
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETSRESPONSE']._serialized_end=9646
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETSRESPONSE_ERESPONSE']._serialized_start=6596
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGUPGRADETABLETSRESPONSE_ERESPONSE']._serialized_end=6716
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONS']._serialized_start=9648
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONS']._serialized_end=9716
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONSRESPONSE']._serialized_start=9719
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONSRESPONSE']._serialized_end=10073
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONSRESPONSE_ERESPONSE']._serialized_start=9926
  _globals['_CMSGCLIENTTOGCFANTASYCRAFTINGREROLLOPTIONSRESPONSE_ERESPONSE']._serialized_end=10073
# @@protoc_insertion_point(module_scope)
