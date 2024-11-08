# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_player.steamworkssdk.proto
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
    'steammessages_player.steamworkssdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamworkssdk_pb2 as steammessages__unified__base_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(steammessages_player.steamworkssdk.proto\x1a.steammessages_unified_base.steamworkssdk.proto\"4\n2CPlayer_GetMutualFriendsForIncomingInvites_Request\"\\\n&CPlayer_IncomingInviteMutualFriendList\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12!\n\x19mutual_friend_account_ids\x18\x02 \x03(\r\"\x8c\x01\n3CPlayer_GetMutualFriendsForIncomingInvites_Response\x12U\n$incoming_invite_mutual_friends_lists\x18\x01 \x03(\x0b\x32\'.CPlayer_IncomingInviteMutualFriendList\"7\n&CPlayer_GetFriendsGameplayInfo_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\xee\x05\n\'CPlayer_GetFriendsGameplayInfo_Response\x12K\n\tyour_info\x18\x01 \x01(\x0b\x32\x38.CPlayer_GetFriendsGameplayInfo_Response.OwnGameplayInfo\x12M\n\x07in_game\x18\x02 \x03(\x0b\x32<.CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo\x12U\n\x0fplayed_recently\x18\x03 \x03(\x0b\x32<.CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo\x12Q\n\x0bplayed_ever\x18\x04 \x03(\x0b\x32<.CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo\x12J\n\x04owns\x18\x05 \x03(\x0b\x32<.CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo\x12Q\n\x0bin_wishlist\x18\x06 \x03(\x0b\x32<.CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo\x1a^\n\x13\x46riendsGameplayInfo\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x16\n\x0eminutes_played\x18\x02 \x01(\r\x12\x1e\n\x16minutes_played_forever\x18\x03 \x01(\r\x1a~\n\x0fOwnGameplayInfo\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\x16\n\x0eminutes_played\x18\x02 \x01(\r\x12\x1e\n\x16minutes_played_forever\x18\x03 \x01(\r\x12\x13\n\x0bin_wishlist\x18\x04 \x01(\x08\x12\r\n\x05owned\x18\x05 \x01(\x08\"3\n\"CPlayer_GetGameBadgeLevels_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\xb5\x01\n#CPlayer_GetGameBadgeLevels_Response\x12\x14\n\x0cplayer_level\x18\x01 \x01(\r\x12:\n\x06\x62\x61\x64ges\x18\x02 \x03(\x0b\x32*.CPlayer_GetGameBadgeLevels_Response.Badge\x1a<\n\x05\x42\x61\x64ge\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0e\n\x06series\x18\x02 \x01(\x05\x12\x14\n\x0c\x62order_color\x18\x03 \x01(\r\"\x82\x01\n\"CPlayer_GetLastPlayedTimes_Request\x12\\\n\x0fmin_last_played\x18\x01 \x01(\rBC\x82\xb5\x18?The most recent last-played time the client already knows about\"\xd8\x01\n#CPlayer_GetLastPlayedTimes_Response\x12\x38\n\x05games\x18\x01 \x03(\x0b\x32).CPlayer_GetLastPlayedTimes_Response.Game\x1aw\n\x04Game\x12\r\n\x05\x61ppid\x18\x01 \x01(\x05\x12\x15\n\rlast_playtime\x18\x02 \x01(\r\x12\x17\n\x0fplaytime_2weeks\x18\x03 \x01(\x05\x12\x18\n\x10playtime_forever\x18\x04 \x01(\x05\x12\x16\n\x0e\x66irst_playtime\x18\x05 \x01(\r\"\x1b\n\x19\x43Player_AcceptSSA_Request\"\x1c\n\x1a\x43Player_AcceptSSA_Response\"!\n\x1f\x43Player_GetNicknameList_Request\"\x9e\x01\n CPlayer_GetNicknameList_Response\x12\x43\n\tnicknames\x18\x01 \x03(\x0b\x32\x30.CPlayer_GetNicknameList_Response.PlayerNickname\x1a\x35\n\x0ePlayerNickname\x12\x11\n\taccountid\x18\x01 \x01(\x07\x12\x10\n\x08nickname\x18\x02 \x01(\t\")\n\'CPlayer_GetPerFriendPreferences_Request\"\xd1\x05\n\x14PerFriendPreferences\x12\x11\n\taccountid\x18\x01 \x01(\x07\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12_\n\x18notifications_showingame\x18\x03 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12_\n\x18notifications_showonline\x18\x04 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12\x61\n\x1anotifications_showmessages\x18\x05 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12X\n\x11sounds_showingame\x18\x06 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12X\n\x11sounds_showonline\x18\x07 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12Z\n\x13sounds_showmessages\x18\x08 \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\x12_\n\x18notifications_sendmobile\x18\t \x01(\x0e\x32\x15.ENotificationSetting:&k_ENotificationSettingNotifyUseDefault\"V\n(CPlayer_GetPerFriendPreferences_Response\x12*\n\x0bpreferences\x18\x01 \x03(\x0b\x32\x15.PerFriendPreferences\"U\n\'CPlayer_SetPerFriendPreferences_Request\x12*\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x15.PerFriendPreferences\"*\n(CPlayer_SetPerFriendPreferences_Response\"c\n\x19\x43Player_AddFriend_Request\x12\x46\n\x07steamid\x18\x01 \x01(\x06\x42\x35\x82\xb5\x18\x31Steam ID of user to whom to send a friend invite.\"\xf6\x01\n\x1a\x43Player_AddFriend_Response\x12O\n\x0binvite_sent\x18\x01 \x01(\x08\x42:\x82\xb5\x18\x36True if the operation was successful, false otherwise.\x12\x86\x01\n\x13\x66riend_relationship\x18\x02 \x01(\rBi\x82\xb5\x18\x65the resulting relationship.  Depending on state, may move directly to friends rather than invite sent\"R\n\x1c\x43Player_RemoveFriend_Request\x12\x32\n\x07steamid\x18\x01 \x01(\x06\x42!\x82\xb5\x18\x1dSteam ID of friend to remove.\"\\\n\x1d\x43Player_RemoveFriend_Response\x12;\n\x13\x66riend_relationship\x18\x01 \x01(\rB\x1e\x82\xb5\x18\x1athe resulting relationship\"\x7f\n\x1c\x43Player_IgnoreFriend_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12N\n\x08unignore\x18\x02 \x01(\x08\x42<\x82\xb5\x18\x38If set, remove from ignore/block list instead of adding \"\\\n\x1d\x43Player_IgnoreFriend_Response\x12;\n\x13\x66riend_relationship\x18\x01 \x01(\rB\x1e\x82\xb5\x18\x1athe resulting relationship\")\n\'CPlayer_GetCommunityPreferences_Request\"\xb1\x01\n\x1c\x43Player_CommunityPreferences\x12)\n\x1bhide_adult_content_violence\x18\x01 \x01(\x08:\x04true\x12$\n\x16hide_adult_content_sex\x18\x02 \x01(\x08:\x04true\x12%\n\x16parenthesize_nicknames\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11timestamp_updated\x18\x03 \x01(\r\"^\n(CPlayer_GetCommunityPreferences_Response\x12\x32\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x1d.CPlayer_CommunityPreferences\"]\n\'CPlayer_SetCommunityPreferences_Request\x12\x32\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x1d.CPlayer_CommunityPreferences\"*\n(CPlayer_SetCommunityPreferences_Response\"@\n,CPlayer_GetNewSteamAnnouncementState_Request\x12\x10\n\x08language\x18\x01 \x01(\x05\"\xa6\x01\n-CPlayer_GetNewSteamAnnouncementState_Response\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x1d\n\x15\x61nnouncement_headline\x18\x02 \x01(\t\x12\x18\n\x10\x61nnouncement_url\x18\x03 \x01(\t\x12\x13\n\x0btime_posted\x18\x04 \x01(\r\x12\x18\n\x10\x61nnouncement_gid\x18\x05 \x01(\x04\"`\n/CPlayer_UpdateSteamAnnouncementLastRead_Request\x12\x18\n\x10\x61nnouncement_gid\x18\x01 \x01(\x04\x12\x13\n\x0btime_posted\x18\x02 \x01(\r\"2\n0CPlayer_UpdateSteamAnnouncementLastRead_Response*\x85\x01\n\x14\x45NotificationSetting\x12*\n&k_ENotificationSettingNotifyUseDefault\x10\x00\x12 \n\x1ck_ENotificationSettingAlways\x10\x01\x12\x1f\n\x1bk_ENotificationSettingNever\x10\x02\x32\xad\x14\n\x06Player\x12\xef\x01\n\"GetMutualFriendsForIncomingInvites\x12\x33.CPlayer_GetMutualFriendsForIncomingInvites_Request\x1a\x34.CPlayer_GetMutualFriendsForIncomingInvites_Response\"^\x82\xb5\x18ZGet me the mutual friends for each of my pending incoming invites (individuals and clans).\x12\xb8\x01\n\x16GetFriendsGameplayInfo\x12\'.CPlayer_GetFriendsGameplayInfo_Request\x1a(.CPlayer_GetFriendsGameplayInfo_Response\"K\x82\xb5\x18GGet a list of friends who are playing, have played, own, or want a game\x12\xb6\x01\n\x12GetGameBadgeLevels\x12#.CPlayer_GetGameBadgeLevels_Request\x1a$.CPlayer_GetGameBadgeLevels_Response\"U\x82\xb5\x18QReturns the Steam Level of a user, the Badge level for the game, and if it\'s foil\x12\x95\x01\n\x18\x43lientGetLastPlayedTimes\x12#.CPlayer_GetLastPlayedTimes_Request\x1a$.CPlayer_GetLastPlayedTimes_Response\".\x82\xb5\x18*Gets the last-played times for the account\x12\x63\n\tAcceptSSA\x12\x1a.CPlayer_AcceptSSA_Request\x1a\x1b.CPlayer_AcceptSSA_Response\"\x1d\x82\xb5\x18\x19User is accepting the SSA\x12\x94\x01\n\x0fGetNicknameList\x12 .CPlayer_GetNicknameList_Request\x1a!.CPlayer_GetNicknameList_Response\"<\x82\xb5\x18\x38Gets the list of nicknames this user has for other users\x12\xbd\x01\n\x17GetPerFriendPreferences\x12(.CPlayer_GetPerFriendPreferences_Request\x1a).CPlayer_GetPerFriendPreferences_Response\"M\x82\xb5\x18IGets the list of per-friend preferences this user has set for other users\x12\xb7\x01\n\x17SetPerFriendPreferences\x12(.CPlayer_SetPerFriendPreferences_Request\x1a).CPlayer_SetPerFriendPreferences_Response\"G\x82\xb5\x18\x43Sets the logged in user\'s per-friend preferences for the given user\x12s\n\tAddFriend\x12\x1a.CPlayer_AddFriend_Request\x1a\x1b.CPlayer_AddFriend_Response\"-\x82\xb5\x18)Invites another Steam user to be a friend\x12\x82\x01\n\x0cRemoveFriend\x12\x1d.CPlayer_RemoveFriend_Request\x1a\x1e.CPlayer_RemoveFriend_Response\"3\x82\xb5\x18/Removes a friend or ignores a friend suggestion\x12\xa6\x01\n\x0cIgnoreFriend\x12\x1d.CPlayer_IgnoreFriend_Request\x1a\x1e.CPlayer_IgnoreFriend_Response\"W\x82\xb5\x18SBlocks or unblocks communication with the user.  Despite name, can be a non-friend.\x12\x9e\x01\n\x17GetCommunityPreferences\x12(.CPlayer_GetCommunityPreferences_Request\x1a).CPlayer_GetCommunityPreferences_Response\".\x82\xb5\x18*Returns the player\'s community preferences\x12\x9b\x01\n\x17SetCommunityPreferences\x12(.CPlayer_SetCommunityPreferences_Request\x1a).CPlayer_SetCommunityPreferences_Response\"+\x82\xb5\x18\'Sets the player\'s community preferences\x12\xde\x01\n\x1cGetNewSteamAnnouncementState\x12-.CPlayer_GetNewSteamAnnouncementState_Request\x1a..CPlayer_GetNewSteamAnnouncementState_Response\"_\x82\xb5\x18[Calculates and returns what to display for UI that renders new steam announcement available\x12\xbc\x01\n\x1fUpdateSteamAnnouncementLastRead\x12\x30.CPlayer_UpdateSteamAnnouncementLastRead_Request\x1a\x31.CPlayer_UpdateSteamAnnouncementLastRead_Response\"4\x82\xb5\x18\x30Marks latest announcement timestamp read by user\x1a-\x82\xb5\x18)A service for accessing Steam player dataB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_player.steamworkssdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_REQUEST'].fields_by_name['min_last_played']._loaded_options = None
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_REQUEST'].fields_by_name['min_last_played']._serialized_options = b'\202\265\030?The most recent last-played time the client already knows about'
  _globals['_CPLAYER_ADDFRIEND_REQUEST'].fields_by_name['steamid']._loaded_options = None
  _globals['_CPLAYER_ADDFRIEND_REQUEST'].fields_by_name['steamid']._serialized_options = b'\202\265\0301Steam ID of user to whom to send a friend invite.'
  _globals['_CPLAYER_ADDFRIEND_RESPONSE'].fields_by_name['invite_sent']._loaded_options = None
  _globals['_CPLAYER_ADDFRIEND_RESPONSE'].fields_by_name['invite_sent']._serialized_options = b'\202\265\0306True if the operation was successful, false otherwise.'
  _globals['_CPLAYER_ADDFRIEND_RESPONSE'].fields_by_name['friend_relationship']._loaded_options = None
  _globals['_CPLAYER_ADDFRIEND_RESPONSE'].fields_by_name['friend_relationship']._serialized_options = b'\202\265\030ethe resulting relationship.  Depending on state, may move directly to friends rather than invite sent'
  _globals['_CPLAYER_REMOVEFRIEND_REQUEST'].fields_by_name['steamid']._loaded_options = None
  _globals['_CPLAYER_REMOVEFRIEND_REQUEST'].fields_by_name['steamid']._serialized_options = b'\202\265\030\035Steam ID of friend to remove.'
  _globals['_CPLAYER_REMOVEFRIEND_RESPONSE'].fields_by_name['friend_relationship']._loaded_options = None
  _globals['_CPLAYER_REMOVEFRIEND_RESPONSE'].fields_by_name['friend_relationship']._serialized_options = b'\202\265\030\032the resulting relationship'
  _globals['_CPLAYER_IGNOREFRIEND_REQUEST'].fields_by_name['unignore']._loaded_options = None
  _globals['_CPLAYER_IGNOREFRIEND_REQUEST'].fields_by_name['unignore']._serialized_options = b'\202\265\0308If set, remove from ignore/block list instead of adding '
  _globals['_CPLAYER_IGNOREFRIEND_RESPONSE'].fields_by_name['friend_relationship']._loaded_options = None
  _globals['_CPLAYER_IGNOREFRIEND_RESPONSE'].fields_by_name['friend_relationship']._serialized_options = b'\202\265\030\032the resulting relationship'
  _globals['_PLAYER']._loaded_options = None
  _globals['_PLAYER']._serialized_options = b'\202\265\030)A service for accessing Steam player data'
  _globals['_PLAYER'].methods_by_name['GetMutualFriendsForIncomingInvites']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetMutualFriendsForIncomingInvites']._serialized_options = b'\202\265\030ZGet me the mutual friends for each of my pending incoming invites (individuals and clans).'
  _globals['_PLAYER'].methods_by_name['GetFriendsGameplayInfo']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetFriendsGameplayInfo']._serialized_options = b'\202\265\030GGet a list of friends who are playing, have played, own, or want a game'
  _globals['_PLAYER'].methods_by_name['GetGameBadgeLevels']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetGameBadgeLevels']._serialized_options = b'\202\265\030QReturns the Steam Level of a user, the Badge level for the game, and if it\'s foil'
  _globals['_PLAYER'].methods_by_name['ClientGetLastPlayedTimes']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['ClientGetLastPlayedTimes']._serialized_options = b'\202\265\030*Gets the last-played times for the account'
  _globals['_PLAYER'].methods_by_name['AcceptSSA']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['AcceptSSA']._serialized_options = b'\202\265\030\031User is accepting the SSA'
  _globals['_PLAYER'].methods_by_name['GetNicknameList']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetNicknameList']._serialized_options = b'\202\265\0308Gets the list of nicknames this user has for other users'
  _globals['_PLAYER'].methods_by_name['GetPerFriendPreferences']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetPerFriendPreferences']._serialized_options = b'\202\265\030IGets the list of per-friend preferences this user has set for other users'
  _globals['_PLAYER'].methods_by_name['SetPerFriendPreferences']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['SetPerFriendPreferences']._serialized_options = b'\202\265\030CSets the logged in user\'s per-friend preferences for the given user'
  _globals['_PLAYER'].methods_by_name['AddFriend']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['AddFriend']._serialized_options = b'\202\265\030)Invites another Steam user to be a friend'
  _globals['_PLAYER'].methods_by_name['RemoveFriend']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['RemoveFriend']._serialized_options = b'\202\265\030/Removes a friend or ignores a friend suggestion'
  _globals['_PLAYER'].methods_by_name['IgnoreFriend']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['IgnoreFriend']._serialized_options = b'\202\265\030SBlocks or unblocks communication with the user.  Despite name, can be a non-friend.'
  _globals['_PLAYER'].methods_by_name['GetCommunityPreferences']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetCommunityPreferences']._serialized_options = b'\202\265\030*Returns the player\'s community preferences'
  _globals['_PLAYER'].methods_by_name['SetCommunityPreferences']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['SetCommunityPreferences']._serialized_options = b'\202\265\030\'Sets the player\'s community preferences'
  _globals['_PLAYER'].methods_by_name['GetNewSteamAnnouncementState']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['GetNewSteamAnnouncementState']._serialized_options = b'\202\265\030[Calculates and returns what to display for UI that renders new steam announcement available'
  _globals['_PLAYER'].methods_by_name['UpdateSteamAnnouncementLastRead']._loaded_options = None
  _globals['_PLAYER'].methods_by_name['UpdateSteamAnnouncementLastRead']._serialized_options = b'\202\265\0300Marks latest announcement timestamp read by user'
  _globals['_ENOTIFICATIONSETTING']._serialized_start=4618
  _globals['_ENOTIFICATIONSETTING']._serialized_end=4751
  _globals['_CPLAYER_GETMUTUALFRIENDSFORINCOMINGINVITES_REQUEST']._serialized_start=92
  _globals['_CPLAYER_GETMUTUALFRIENDSFORINCOMINGINVITES_REQUEST']._serialized_end=144
  _globals['_CPLAYER_INCOMINGINVITEMUTUALFRIENDLIST']._serialized_start=146
  _globals['_CPLAYER_INCOMINGINVITEMUTUALFRIENDLIST']._serialized_end=238
  _globals['_CPLAYER_GETMUTUALFRIENDSFORINCOMINGINVITES_RESPONSE']._serialized_start=241
  _globals['_CPLAYER_GETMUTUALFRIENDSFORINCOMINGINVITES_RESPONSE']._serialized_end=381
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_REQUEST']._serialized_start=383
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_REQUEST']._serialized_end=438
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE']._serialized_start=441
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE']._serialized_end=1191
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE_FRIENDSGAMEPLAYINFO']._serialized_start=969
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE_FRIENDSGAMEPLAYINFO']._serialized_end=1063
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE_OWNGAMEPLAYINFO']._serialized_start=1065
  _globals['_CPLAYER_GETFRIENDSGAMEPLAYINFO_RESPONSE_OWNGAMEPLAYINFO']._serialized_end=1191
  _globals['_CPLAYER_GETGAMEBADGELEVELS_REQUEST']._serialized_start=1193
  _globals['_CPLAYER_GETGAMEBADGELEVELS_REQUEST']._serialized_end=1244
  _globals['_CPLAYER_GETGAMEBADGELEVELS_RESPONSE']._serialized_start=1247
  _globals['_CPLAYER_GETGAMEBADGELEVELS_RESPONSE']._serialized_end=1428
  _globals['_CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE']._serialized_start=1368
  _globals['_CPLAYER_GETGAMEBADGELEVELS_RESPONSE_BADGE']._serialized_end=1428
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_REQUEST']._serialized_start=1431
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_REQUEST']._serialized_end=1561
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE']._serialized_start=1564
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE']._serialized_end=1780
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME']._serialized_start=1661
  _globals['_CPLAYER_GETLASTPLAYEDTIMES_RESPONSE_GAME']._serialized_end=1780
  _globals['_CPLAYER_ACCEPTSSA_REQUEST']._serialized_start=1782
  _globals['_CPLAYER_ACCEPTSSA_REQUEST']._serialized_end=1809
  _globals['_CPLAYER_ACCEPTSSA_RESPONSE']._serialized_start=1811
  _globals['_CPLAYER_ACCEPTSSA_RESPONSE']._serialized_end=1839
  _globals['_CPLAYER_GETNICKNAMELIST_REQUEST']._serialized_start=1841
  _globals['_CPLAYER_GETNICKNAMELIST_REQUEST']._serialized_end=1874
  _globals['_CPLAYER_GETNICKNAMELIST_RESPONSE']._serialized_start=1877
  _globals['_CPLAYER_GETNICKNAMELIST_RESPONSE']._serialized_end=2035
  _globals['_CPLAYER_GETNICKNAMELIST_RESPONSE_PLAYERNICKNAME']._serialized_start=1982
  _globals['_CPLAYER_GETNICKNAMELIST_RESPONSE_PLAYERNICKNAME']._serialized_end=2035
  _globals['_CPLAYER_GETPERFRIENDPREFERENCES_REQUEST']._serialized_start=2037
  _globals['_CPLAYER_GETPERFRIENDPREFERENCES_REQUEST']._serialized_end=2078
  _globals['_PERFRIENDPREFERENCES']._serialized_start=2081
  _globals['_PERFRIENDPREFERENCES']._serialized_end=2802
  _globals['_CPLAYER_GETPERFRIENDPREFERENCES_RESPONSE']._serialized_start=2804
  _globals['_CPLAYER_GETPERFRIENDPREFERENCES_RESPONSE']._serialized_end=2890
  _globals['_CPLAYER_SETPERFRIENDPREFERENCES_REQUEST']._serialized_start=2892
  _globals['_CPLAYER_SETPERFRIENDPREFERENCES_REQUEST']._serialized_end=2977
  _globals['_CPLAYER_SETPERFRIENDPREFERENCES_RESPONSE']._serialized_start=2979
  _globals['_CPLAYER_SETPERFRIENDPREFERENCES_RESPONSE']._serialized_end=3021
  _globals['_CPLAYER_ADDFRIEND_REQUEST']._serialized_start=3023
  _globals['_CPLAYER_ADDFRIEND_REQUEST']._serialized_end=3122
  _globals['_CPLAYER_ADDFRIEND_RESPONSE']._serialized_start=3125
  _globals['_CPLAYER_ADDFRIEND_RESPONSE']._serialized_end=3371
  _globals['_CPLAYER_REMOVEFRIEND_REQUEST']._serialized_start=3373
  _globals['_CPLAYER_REMOVEFRIEND_REQUEST']._serialized_end=3455
  _globals['_CPLAYER_REMOVEFRIEND_RESPONSE']._serialized_start=3457
  _globals['_CPLAYER_REMOVEFRIEND_RESPONSE']._serialized_end=3549
  _globals['_CPLAYER_IGNOREFRIEND_REQUEST']._serialized_start=3551
  _globals['_CPLAYER_IGNOREFRIEND_REQUEST']._serialized_end=3678
  _globals['_CPLAYER_IGNOREFRIEND_RESPONSE']._serialized_start=3680
  _globals['_CPLAYER_IGNOREFRIEND_RESPONSE']._serialized_end=3772
  _globals['_CPLAYER_GETCOMMUNITYPREFERENCES_REQUEST']._serialized_start=3774
  _globals['_CPLAYER_GETCOMMUNITYPREFERENCES_REQUEST']._serialized_end=3815
  _globals['_CPLAYER_COMMUNITYPREFERENCES']._serialized_start=3818
  _globals['_CPLAYER_COMMUNITYPREFERENCES']._serialized_end=3995
  _globals['_CPLAYER_GETCOMMUNITYPREFERENCES_RESPONSE']._serialized_start=3997
  _globals['_CPLAYER_GETCOMMUNITYPREFERENCES_RESPONSE']._serialized_end=4091
  _globals['_CPLAYER_SETCOMMUNITYPREFERENCES_REQUEST']._serialized_start=4093
  _globals['_CPLAYER_SETCOMMUNITYPREFERENCES_REQUEST']._serialized_end=4186
  _globals['_CPLAYER_SETCOMMUNITYPREFERENCES_RESPONSE']._serialized_start=4188
  _globals['_CPLAYER_SETCOMMUNITYPREFERENCES_RESPONSE']._serialized_end=4230
  _globals['_CPLAYER_GETNEWSTEAMANNOUNCEMENTSTATE_REQUEST']._serialized_start=4232
  _globals['_CPLAYER_GETNEWSTEAMANNOUNCEMENTSTATE_REQUEST']._serialized_end=4296
  _globals['_CPLAYER_GETNEWSTEAMANNOUNCEMENTSTATE_RESPONSE']._serialized_start=4299
  _globals['_CPLAYER_GETNEWSTEAMANNOUNCEMENTSTATE_RESPONSE']._serialized_end=4465
  _globals['_CPLAYER_UPDATESTEAMANNOUNCEMENTLASTREAD_REQUEST']._serialized_start=4467
  _globals['_CPLAYER_UPDATESTEAMANNOUNCEMENTLASTREAD_REQUEST']._serialized_end=4563
  _globals['_CPLAYER_UPDATESTEAMANNOUNCEMENTLASTREAD_RESPONSE']._serialized_start=4565
  _globals['_CPLAYER_UPDATESTEAMANNOUNCEMENTLASTREAD_RESPONSE']._serialized_end=4615
  _globals['_PLAYER']._serialized_start=4754
  _globals['_PLAYER']._serialized_end=7359
# @@protoc_insertion_point(module_scope)
