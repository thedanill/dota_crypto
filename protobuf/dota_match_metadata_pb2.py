# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_match_metadata.proto
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
    'dota_match_metadata.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_gcmessages_pb2 as base__gcmessages__pb2
import dota_gcmessages_common_match_management_pb2 as dota__gcmessages__common__match__management__pb2
import dota_gcmessages_common_lobby_pb2 as dota__gcmessages__common__lobby__pb2
import dota_gcmessages_common_overworld_pb2 as dota__gcmessages__common__overworld__pb2
import dota_gcmessages_common_pb2 as dota__gcmessages__common__pb2
import dota_shared_enums_pb2 as dota__shared__enums__pb2
import gcsdk_gcmessages_pb2 as gcsdk__gcmessages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64ota_match_metadata.proto\x1a\x15\x62\x61se_gcmessages.proto\x1a-dota_gcmessages_common_match_management.proto\x1a\"dota_gcmessages_common_lobby.proto\x1a&dota_gcmessages_common_overworld.proto\x1a\x1c\x64ota_gcmessages_common.proto\x1a\x17\x64ota_shared_enums.proto\x1a\x16gcsdk_gcmessages.proto\"|\n\x16\x43\x44OTAMatchMetadataFile\x12\x0f\n\x07version\x18\x01 \x02(\x05\x12\x10\n\x08match_id\x18\x02 \x02(\x04\x12%\n\x08metadata\x18\x03 \x01(\x0b\x32\x13.CDOTAMatchMetadata\x12\x18\n\x10private_metadata\x18\x05 \x01(\x0c\"\xa4-\n\x12\x43\x44OTAMatchMetadata\x12\'\n\x05teams\x18\x01 \x03(\x0b\x32\x18.CDOTAMatchMetadata.Team\x12\x10\n\x08lobby_id\x18\x03 \x01(\x06\x12\x19\n\x11report_until_time\x18\x04 \x01(\x06\x12\x1f\n\x17\x65vent_game_custom_table\x18\x05 \x01(\x0c\x12\x18\n\x10primary_event_id\x18\x06 \x01(\r\x12\x35\n\x11matchmaking_stats\x18\x08 \x01(\x0b\x32\x1a.CMsgMatchMatchmakingStats\x12\x1b\n\x08mvp_data\x18\t \x01(\x0b\x32\t.CMvpData\x12L\n\x18guild_challenge_progress\x18\n \x03(\x0b\x32*.CDOTAMatchMetadata.GuildChallengeProgress\x12\x1e\n\x16\x63ustom_post_game_table\x18\x0b \x01(\x0c\x12+\n\nmatch_tips\x18\x0c \x03(\x0b\x32\x17.CDOTAMatchMetadata.Tip\x12-\n\x13match_tracked_stats\x18\r \x03(\x0b\x32\x10.CMsgTrackedStat\x1a\x9b\x01\n\x08\x45\x63onItem\x12\x11\n\tdef_index\x18\x01 \x01(\r\x12\x12\n\x07quality\x18\x02 \x01(\r:\x01\x34\x12(\n\tattribute\x18\x03 \x03(\x0b\x32\x15.CSOEconItemAttribute\x12\x10\n\x05style\x18\x04 \x01(\r:\x01\x30\x12,\n\x0e\x65quipped_state\x18\x05 \x03(\x0b\x32\x14.CSOEconItemEquipped\x1a\xad$\n\x04Team\x12\x11\n\tdota_team\x18\x01 \x01(\r\x12\x30\n\x07players\x18\x02 \x03(\x0b\x32\x1f.CDOTAMatchMetadata.Team.Player\x12\x18\n\x10graph_experience\x18\x03 \x03(\x02\x12\x19\n\x11graph_gold_earned\x18\x04 \x03(\x02\x12\x17\n\x0fgraph_net_worth\x18\x05 \x03(\x02\x12\x15\n\rcm_first_pick\x18\x06 \x01(\x08\x12 \n\x14\x63m_captain_player_id\x18\x07 \x01(\x05:\x02-1\x12\x12\n\ncm_penalty\x18\n \x01(\r\x12,\n\x12team_tracked_stats\x18\x0b \x03(\x0b\x32\x10.CMsgTrackedStat\x1a\x30\n\nPlayerKill\x12\x13\n\x0bvictim_slot\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x1a:\n\x0cItemPurchase\x12\x13\n\x07item_id\x18\x01 \x01(\x05:\x02-1\x12\x15\n\rpurchase_time\x18\x02 \x01(\x05\x1a\xad\x01\n\x11InventorySnapshot\x12\x0f\n\x07item_id\x18\x01 \x03(\x05\x12\x11\n\tgame_time\x18\x02 \x01(\x05\x12\r\n\x05kills\x18\x03 \x01(\r\x12\x0e\n\x06\x64\x65\x61ths\x18\x04 \x01(\r\x12\x0f\n\x07\x61ssists\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x18\n\x10\x62\x61\x63kpack_item_id\x18\x07 \x03(\x05\x12\x1b\n\x0fneutral_item_id\x18\x08 \x01(\x05:\x02-1\x1a\x36\n\x11\x41utoStyleCriteria\x12\x12\n\nname_token\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02\x1a\xc6\x01\n\x12StrangeGemProgress\x12\x17\n\x0fkill_eater_type\x18\x01 \x01(\r\x12\x1a\n\x12gem_item_def_index\x18\x02 \x01(\r\x12\x18\n\x10required_hero_id\x18\x03 \x01(\x05\x12\x16\n\x0estarting_value\x18\x04 \x01(\r\x12\x14\n\x0c\x65nding_value\x18\x05 \x01(\r\x12\x1c\n\x14owner_item_def_index\x18\x06 \x01(\r\x12\x15\n\rowner_item_id\x18\x07 \x01(\x04\x1ah\n\x11VictoryPrediction\x12\x0f\n\x07item_id\x18\x01 \x01(\x04\x12\x16\n\x0eitem_def_index\x18\x02 \x01(\r\x12\x16\n\x0estarting_value\x18\x03 \x01(\r\x12\x12\n\nis_victory\x18\x04 \x01(\x08\x1aZ\n\x0cSubChallenge\x12\x0f\n\x07slot_id\x18\x01 \x01(\r\x12\x13\n\x0bstart_value\x18\x02 \x01(\r\x12\x11\n\tend_value\x18\x03 \x01(\r\x12\x11\n\tcompleted\x18\x04 \x01(\x08\x1aU\n\x15\x43\x61vernChallengeResult\x12\x1e\n\x11\x63ompleted_path_id\x18\x01 \x01(\r:\x03\x32\x35\x35\x12\x1c\n\x0f\x63laimed_room_id\x18\x02 \x01(\r:\x03\x32\x35\x35\x1aU\n\x0b\x41\x63tionGrant\x12\x11\n\taction_id\x18\x01 \x01(\r\x12\x10\n\x08quantity\x18\x02 \x01(\r\x12\r\n\x05\x61udit\x18\x03 \x01(\r\x12\x12\n\naudit_data\x18\x05 \x01(\x04\x1a,\n\nCandyGrant\x12\x0e\n\x06points\x18\x01 \x01(\r\x12\x0e\n\x06reason\x18\x02 \x01(\r\x1aT\n\x14PeriodicResourceData\x12\x1c\n\x14periodic_resource_id\x18\x01 \x01(\r\x12\x11\n\tremaining\x18\x02 \x01(\r\x12\x0b\n\x03max\x18\x03 \x01(\r\x1a\x95\x08\n\tEventData\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\r\x12\x14\n\x0c\x65vent_points\x18\x02 \x01(\r\x12\x1d\n\x15\x63hallenge_instance_id\x18\x03 \x01(\r\x12\x1a\n\x12\x63hallenge_quest_id\x18\x04 \x01(\r\x12$\n\x1c\x63hallenge_quest_challenge_id\x18\x05 \x01(\r\x12\x1b\n\x13\x63hallenge_completed\x18\x06 \x01(\x08\x12 \n\x18\x63hallenge_rank_completed\x18\x07 \x01(\r\x12+\n#challenge_rank_previously_completed\x18\x08 \x01(\r\x12\x13\n\x0b\x65vent_owned\x18\t \x01(\x08\x12K\n\x1csub_challenges_with_progress\x18\n \x03(\x0b\x32%.CDOTAMatchMetadata.Team.SubChallenge\x12\x16\n\x0ewager_winnings\x18\x0b \x01(\r\x12\x1f\n\x17\x63\x61vern_challenge_active\x18\x0c \x01(\x08\x12!\n\x19\x63\x61vern_challenge_winnings\x18\r \x01(\r\x12\x16\n\x0e\x61mount_wagered\x18\x0e \x01(\r\x12\"\n\x1aperiodic_point_adjustments\x18\x10 \x01(\r\x12T\n\x1c\x63\x61vern_challenge_map_results\x18\x11 \x03(\x0b\x32..CDOTAMatchMetadata.Team.CavernChallengeResult\x12,\n$cavern_challenge_plus_shard_winnings\x18\x12 \x01(\r\x12=\n\x0f\x61\x63tions_granted\x18\x13 \x03(\x0b\x32$.CDOTAMatchMetadata.Team.ActionGrant\x12%\n\x18\x63\x61vern_crawl_map_variant\x18\x14 \x01(\r:\x03\x32\x35\x35\x12\x1c\n\x14team_wager_bonus_pct\x18\x15 \x01(\r\x12\x18\n\x10wager_streak_pct\x18\x16 \x01(\r\x12\x41\n\x14\x63\x61ndy_points_granted\x18\x17 \x03(\x0b\x32#.CDOTAMatchMetadata.Team.CandyGrant\x12\x18\n\x10\x61\x63tive_season_id\x18\x18 \x01(\r\x12 \n\x18\x63\x61vern_crawl_half_credit\x18\x19 \x01(\x08\x12I\n\x12periodic_resources\x18\x1a \x03(\x0b\x32-.CDOTAMatchMetadata.Team.PeriodicResourceData\x12-\n\x14\x65xtra_event_messages\x18\x1b \x03(\x0b\x32\x0f.CExtraMsgBlock\x1aU\n\x18\x46\x65\x61turedGamemodeProgress\x12\x13\n\x0bstart_value\x18\x01 \x01(\r\x12\x11\n\tend_value\x18\x02 \x01(\r\x12\x11\n\tmax_value\x18\x03 \x01(\r\x1a\x90\x11\n\x06Player\x12\x18\n\x10\x61\x62ility_upgrades\x18\x02 \x03(\x05\x12\x13\n\x0bplayer_slot\x18\x03 \x01(\r\x12\x32\n\x05kills\x18\x05 \x03(\x0b\x32#.CDOTAMatchMetadata.Team.PlayerKill\x12\x34\n\x05items\x18\x06 \x03(\x0b\x32%.CDOTAMatchMetadata.Team.ItemPurchase\x12\x15\n\ravg_kills_x16\x18\x07 \x01(\r\x12\x16\n\x0e\x61vg_deaths_x16\x18\x08 \x01(\r\x12\x17\n\x0f\x61vg_assists_x16\x18\t \x01(\r\x12\x13\n\x0b\x61vg_gpm_x16\x18\n \x01(\r\x12\x13\n\x0b\x61vg_xpm_x16\x18\x0b \x01(\r\x12\x16\n\x0e\x62\x65st_kills_x16\x18\x0c \x01(\r\x12\x18\n\x10\x62\x65st_assists_x16\x18\r \x01(\r\x12\x14\n\x0c\x62\x65st_gpm_x16\x18\x0e \x01(\r\x12\x14\n\x0c\x62\x65st_xpm_x16\x18\x0f \x01(\r\x12\x12\n\nwin_streak\x18\x10 \x01(\r\x12\x17\n\x0f\x62\x65st_win_streak\x18\x11 \x01(\r\x12\x13\n\x0b\x66ight_score\x18\x12 \x01(\x02\x12\x12\n\nfarm_score\x18\x13 \x01(\x02\x12\x15\n\rsupport_score\x18\x14 \x01(\x02\x12\x12\n\npush_score\x18\x15 \x01(\x02\x12\x16\n\x0elevel_up_times\x18\x16 \x03(\r\x12\x17\n\x0fgraph_net_worth\x18\x17 \x03(\x02\x12\x46\n\x12inventory_snapshot\x18\x18 \x03(\x0b\x32*.CDOTAMatchMetadata.Team.InventorySnapshot\x12\x1c\n\x14\x61vg_stats_calibrated\x18\x19 \x01(\x08\x12G\n\x13\x61uto_style_criteria\x18\x1a \x03(\x0b\x32*.CDOTAMatchMetadata.Team.AutoStyleCriteria\x12\x36\n\nevent_data\x18\x1d \x03(\x0b\x32\".CDOTAMatchMetadata.Team.EventData\x12I\n\x14strange_gem_progress\x18\x1e \x03(\x0b\x32+.CDOTAMatchMetadata.Team.StrangeGemProgress\x12\x0f\n\x07hero_xp\x18\x1f \x01(\r\x12\x15\n\rcamps_stacked\x18  \x01(\r\x12\x46\n\x12victory_prediction\x18! \x03(\x0b\x32*.CDOTAMatchMetadata.Team.VictoryPrediction\x12\x1c\n\x14lane_selection_flags\x18\" \x01(\r\x12\x10\n\x08rampages\x18# \x01(\r\x12\x14\n\x0ctriple_kills\x18$ \x01(\r\x12\x16\n\x0e\x61\x65gis_snatched\x18% \x01(\r\x12\x19\n\x11rapiers_purchased\x18& \x01(\r\x12\x17\n\x0f\x63ouriers_killed\x18\' \x01(\r\x12\x16\n\x0enet_worth_rank\x18( \x01(\r\x12\x1a\n\x12support_gold_spent\x18) \x01(\r\x12\x1d\n\x15observer_wards_placed\x18* \x01(\r\x12\x1b\n\x13sentry_wards_placed\x18+ \x01(\r\x12\x16\n\x0ewards_dewarded\x18, \x01(\r\x12\x15\n\rstun_duration\x18- \x01(\x02\x12I\n\x13rank_mmr_boost_type\x18. \x01(\x0e\x32\x12.EDOTAMMRBoostType:\x18k_EDOTAMMRBoostType_None\x12K\n\x11\x63ontract_progress\x18\x30 \x03(\x0b\x32\x30.CDOTAMatchMetadata.Team.Player.ContractProgress\x12\x11\n\tguild_ids\x18\x31 \x03(\r\x12\x19\n\x11graph_hero_damage\x18\x32 \x03(\x02\x12:\n\x0bteam_number\x18\x33 \x01(\x0e\x32\r.DOTA_GC_TEAM:\x16\x44OTA_GC_TEAM_GOOD_GUYS\x12\x11\n\tteam_slot\x18\x34 \x01(\r\x12U\n\x1a\x66\x65\x61tured_gamemode_progress\x18\x35 \x01(\x0b\x32\x31.CDOTAMatchMetadata.Team.FeaturedGamemodeProgress\x12#\n\x1b\x66\x65\x61tured_hero_sticker_index\x18\x36 \x01(\r\x12%\n\x1d\x66\x65\x61tured_hero_sticker_quality\x18\x37 \x01(\r\x12\x39\n\x13\x65quipped_econ_items\x18\x38 \x03(\x0b\x32\x1c.CDOTAMatchMetadata.EconItem\x12\x1a\n\x0egame_player_id\x18\x39 \x01(\x05:\x02-1\x12.\n\x14player_tracked_stats\x18: \x03(\x0b\x32\x10.CMsgTrackedStat\x12K\n\x11overworld_rewards\x18; \x01(\x0b\x32\x30.CDOTAMatchMetadata.Team.Player.OverworldRewards\x1a\xb4\x01\n\x10\x43ontractProgress\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\r\x12\x1d\n\x15\x63hallenge_instance_id\x18\x03 \x01(\r\x12\x1b\n\x13\x63hallenge_parameter\x18\x04 \x01(\r\x12\x16\n\x0e\x63ontract_stars\x18\x05 \x01(\r\x12\x15\n\rcontract_slot\x18\x06 \x01(\r\x12\x11\n\tcompleted\x18\x07 \x01(\x08\x1aU\n\x10OverworldRewards\x12\x14\n\x0coverworld_id\x18\x01 \x01(\r\x12+\n\x06tokens\x18\x02 \x01(\x0b\x32\x1b.CMsgOverworldTokenQuantity\x1a\x93\x03\n\x16GuildChallengeProgress\x12\x10\n\x08guild_id\x18\x01 \x01(\r\x12(\n\x08\x65vent_id\x18\x02 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\x12\x1d\n\x15\x63hallenge_instance_id\x18\x03 \x01(\r\x12\x1b\n\x13\x63hallenge_parameter\x18\x04 \x01(\r\x12\x1b\n\x13\x63hallenge_timestamp\x18\x05 \x01(\r\x12#\n\x1b\x63hallenge_progress_at_start\x18\x06 \x01(\r\x12&\n\x1e\x63hallenge_progress_accumulated\x18\x07 \x01(\r\x12Z\n\x13individual_progress\x18\x08 \x03(\x0b\x32=.CDOTAMatchMetadata.GuildChallengeProgress.IndividualProgress\x1a;\n\x12IndividualProgress\x12\x10\n\x08progress\x18\x02 \x01(\r\x12\x13\n\x0bplayer_slot\x18\x03 \x01(\r\x1a{\n\x03Tip\x12\x1a\n\x12source_player_slot\x18\x01 \x01(\r\x12\x1a\n\x12target_player_slot\x18\x02 \x01(\r\x12\x12\n\ntip_amount\x18\x03 \x01(\r\x12(\n\x08\x65vent_id\x18\x04 \x01(\x0e\x32\x07.EEvent:\rEVENT_ID_NONE\"\xd1\x11\n\x19\x43\x44OTAMatchPrivateMetadata\x12.\n\x05teams\x18\x01 \x03(\x0b\x32\x1f.CDOTAMatchPrivateMetadata.Team\x12\x1d\n\x15graph_win_probability\x18\x02 \x03(\x02\x12;\n\x0cstring_names\x18\x03 \x03(\x0b\x32%.CDOTAMatchPrivateMetadata.StringName\x1a&\n\nStringName\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xff\x0f\n\x04Team\x12\x11\n\tdota_team\x18\x01 \x01(\r\x12\x37\n\x07players\x18\x02 \x03(\x0b\x32&.CDOTAMatchPrivateMetadata.Team.Player\x12;\n\tbuildings\x18\x03 \x03(\x0b\x32(.CDOTAMatchPrivateMetadata.Team.Building\x1a\x86\x0e\n\x06Player\x12\x13\n\x0bplayer_slot\x18\x02 \x01(\r\x12\x17\n\x0fposition_stream\x18\x03 \x01(\x0c\x12M\n\x0f\x63ombat_segments\x18\x04 \x03(\x0b\x32\x34.CDOTAMatchPrivateMetadata.Team.Player.CombatSegment\x12\x19\n\x11\x64\x61mage_unit_names\x18\x05 \x03(\t\x12G\n\x0c\x62uff_records\x18\x06 \x03(\x0b\x32\x31.CDOTAMatchPrivateMetadata.Team.Player.BuffRecord\x12\x13\n\x0bgraph_kills\x18\x07 \x03(\x02\x12\x14\n\x0cgraph_deaths\x18\x08 \x03(\x02\x12\x15\n\rgraph_assists\x18\t \x03(\x02\x12\x16\n\x0egraph_lasthits\x18\n \x03(\x02\x12\x14\n\x0cgraph_denies\x18\x0b \x03(\x02\x12J\n\rgold_received\x18\x0c \x01(\x0b\x32\x33.CDOTAMatchPrivateMetadata.Team.Player.GoldReceived\x12\x46\n\x0bxp_received\x18\r \x01(\x0b\x32\x31.CDOTAMatchPrivateMetadata.Team.Player.XPReceived\x12:\n\x0bteam_number\x18\x0e \x01(\x0e\x32\r.DOTA_GC_TEAM:\x16\x44OTA_GC_TEAM_GOOD_GUYS\x12\x11\n\tteam_slot\x18\x0f \x01(\r\x1a\xb1\x05\n\rCombatSegment\x12\x11\n\tgame_time\x18\x01 \x01(\x05\x12_\n\x11\x64\x61mage_by_ability\x18\x02 \x03(\x0b\x32\x44.CDOTAMatchPrivateMetadata.Team.Player.CombatSegment.DamageByAbility\x12\x61\n\x12healing_by_ability\x18\x03 \x03(\x0b\x32\x45.CDOTAMatchPrivateMetadata.Team.Player.CombatSegment.HealingByAbility\x1a\xe1\x01\n\x0f\x44\x61mageByAbility\x12\x19\n\x11source_unit_index\x18\x03 \x01(\r\x12\x16\n\nability_id\x18\x01 \x01(\x05:\x02-1\x12j\n\x0f\x62y_hero_targets\x18\x02 \x03(\x0b\x32Q.CDOTAMatchPrivateMetadata.Team.Player.CombatSegment.DamageByAbility.ByHeroTarget\x1a/\n\x0c\x42yHeroTarget\x12\x0f\n\x07hero_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x02 \x01(\r\x1a\xe4\x01\n\x10HealingByAbility\x12\x19\n\x11source_unit_index\x18\x03 \x01(\r\x12\x16\n\nability_id\x18\x01 \x01(\x05:\x02-1\x12k\n\x0f\x62y_hero_targets\x18\x02 \x03(\x0b\x32R.CDOTAMatchPrivateMetadata.Team.Player.CombatSegment.HealingByAbility.ByHeroTarget\x1a\x30\n\x0c\x42yHeroTarget\x12\x0f\n\x07hero_id\x18\x01 \x01(\x05\x12\x0f\n\x07healing\x18\x02 \x01(\r\x1a\xec\x01\n\nBuffRecord\x12\x1b\n\x0f\x62uff_ability_id\x18\x01 \x01(\x05:\x02-1\x12\x1a\n\x12\x62uff_modifier_name\x18\x03 \x01(\t\x12W\n\x0f\x62y_hero_targets\x18\x02 \x03(\x0b\x32>.CDOTAMatchPrivateMetadata.Team.Player.BuffRecord.ByHeroTarget\x1aL\n\x0c\x42yHeroTarget\x12\x0f\n\x07hero_id\x18\x01 \x01(\x05\x12\x18\n\x10\x65lapsed_duration\x18\x02 \x01(\x02\x12\x11\n\tis_hidden\x18\x03 \x01(\x08\x1a\x98\x01\n\x0cGoldReceived\x12\r\n\x05\x63reep\x18\x01 \x01(\r\x12\x0e\n\x06heroes\x18\x02 \x01(\r\x12\x14\n\x0c\x62ounty_runes\x18\x03 \x01(\r\x12\x0f\n\x07passive\x18\x04 \x01(\r\x12\x11\n\tbuildings\x18\x05 \x01(\r\x12\x11\n\tabilities\x18\x06 \x01(\r\x12\r\n\x05wards\x18\x07 \x01(\r\x12\r\n\x05other\x18\x08 \x01(\r\x1a\x89\x01\n\nXPReceived\x12\r\n\x05\x63reep\x18\x01 \x01(\r\x12\x0e\n\x06heroes\x18\x02 \x01(\r\x12\x0e\n\x06roshan\x18\x03 \x01(\r\x12\x19\n\x11tome_of_knowledge\x18\x04 \x01(\r\x12\x0f\n\x07outpost\x18\x05 \x01(\r\x12\r\n\x05other\x18\x06 \x01(\r\x12\x11\n\tabilities\x18\x07 \x01(\r\x1a\x65\n\x08\x42uilding\x12\x11\n\tunit_name\x18\x01 \x01(\t\x12\x18\n\x10position_quant_x\x18\x02 \x01(\r\x12\x18\n\x10position_quant_y\x18\x03 \x01(\r\x12\x12\n\ndeath_time\x18\x04 \x01(\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_match_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CDOTAMATCHMETADATAFILE']._serialized_start=254
  _globals['_CDOTAMATCHMETADATAFILE']._serialized_end=378
  _globals['_CDOTAMATCHMETADATA']._serialized_start=381
  _globals['_CDOTAMATCHMETADATA']._serialized_end=6177
  _globals['_CDOTAMATCHMETADATA_ECONITEM']._serialized_start=835
  _globals['_CDOTAMATCHMETADATA_ECONITEM']._serialized_end=990
  _globals['_CDOTAMATCHMETADATA_TEAM']._serialized_start=993
  _globals['_CDOTAMATCHMETADATA_TEAM']._serialized_end=5646
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYERKILL']._serialized_start=1271
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYERKILL']._serialized_end=1319
  _globals['_CDOTAMATCHMETADATA_TEAM_ITEMPURCHASE']._serialized_start=1321
  _globals['_CDOTAMATCHMETADATA_TEAM_ITEMPURCHASE']._serialized_end=1379
  _globals['_CDOTAMATCHMETADATA_TEAM_INVENTORYSNAPSHOT']._serialized_start=1382
  _globals['_CDOTAMATCHMETADATA_TEAM_INVENTORYSNAPSHOT']._serialized_end=1555
  _globals['_CDOTAMATCHMETADATA_TEAM_AUTOSTYLECRITERIA']._serialized_start=1557
  _globals['_CDOTAMATCHMETADATA_TEAM_AUTOSTYLECRITERIA']._serialized_end=1611
  _globals['_CDOTAMATCHMETADATA_TEAM_STRANGEGEMPROGRESS']._serialized_start=1614
  _globals['_CDOTAMATCHMETADATA_TEAM_STRANGEGEMPROGRESS']._serialized_end=1812
  _globals['_CDOTAMATCHMETADATA_TEAM_VICTORYPREDICTION']._serialized_start=1814
  _globals['_CDOTAMATCHMETADATA_TEAM_VICTORYPREDICTION']._serialized_end=1918
  _globals['_CDOTAMATCHMETADATA_TEAM_SUBCHALLENGE']._serialized_start=1920
  _globals['_CDOTAMATCHMETADATA_TEAM_SUBCHALLENGE']._serialized_end=2010
  _globals['_CDOTAMATCHMETADATA_TEAM_CAVERNCHALLENGERESULT']._serialized_start=2012
  _globals['_CDOTAMATCHMETADATA_TEAM_CAVERNCHALLENGERESULT']._serialized_end=2097
  _globals['_CDOTAMATCHMETADATA_TEAM_ACTIONGRANT']._serialized_start=2099
  _globals['_CDOTAMATCHMETADATA_TEAM_ACTIONGRANT']._serialized_end=2184
  _globals['_CDOTAMATCHMETADATA_TEAM_CANDYGRANT']._serialized_start=2186
  _globals['_CDOTAMATCHMETADATA_TEAM_CANDYGRANT']._serialized_end=2230
  _globals['_CDOTAMATCHMETADATA_TEAM_PERIODICRESOURCEDATA']._serialized_start=2232
  _globals['_CDOTAMATCHMETADATA_TEAM_PERIODICRESOURCEDATA']._serialized_end=2316
  _globals['_CDOTAMATCHMETADATA_TEAM_EVENTDATA']._serialized_start=2319
  _globals['_CDOTAMATCHMETADATA_TEAM_EVENTDATA']._serialized_end=3364
  _globals['_CDOTAMATCHMETADATA_TEAM_FEATUREDGAMEMODEPROGRESS']._serialized_start=3366
  _globals['_CDOTAMATCHMETADATA_TEAM_FEATUREDGAMEMODEPROGRESS']._serialized_end=3451
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER']._serialized_start=3454
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER']._serialized_end=5646
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER_CONTRACTPROGRESS']._serialized_start=5379
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER_CONTRACTPROGRESS']._serialized_end=5559
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER_OVERWORLDREWARDS']._serialized_start=5561
  _globals['_CDOTAMATCHMETADATA_TEAM_PLAYER_OVERWORLDREWARDS']._serialized_end=5646
  _globals['_CDOTAMATCHMETADATA_GUILDCHALLENGEPROGRESS']._serialized_start=5649
  _globals['_CDOTAMATCHMETADATA_GUILDCHALLENGEPROGRESS']._serialized_end=6052
  _globals['_CDOTAMATCHMETADATA_GUILDCHALLENGEPROGRESS_INDIVIDUALPROGRESS']._serialized_start=5993
  _globals['_CDOTAMATCHMETADATA_GUILDCHALLENGEPROGRESS_INDIVIDUALPROGRESS']._serialized_end=6052
  _globals['_CDOTAMATCHMETADATA_TIP']._serialized_start=6054
  _globals['_CDOTAMATCHMETADATA_TIP']._serialized_end=6177
  _globals['_CDOTAMATCHPRIVATEMETADATA']._serialized_start=6180
  _globals['_CDOTAMATCHPRIVATEMETADATA']._serialized_end=8437
  _globals['_CDOTAMATCHPRIVATEMETADATA_STRINGNAME']._serialized_start=6349
  _globals['_CDOTAMATCHPRIVATEMETADATA_STRINGNAME']._serialized_end=6387
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM']._serialized_start=6390
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM']._serialized_end=8437
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER']._serialized_start=6536
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER']._serialized_end=8334
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT']._serialized_start=7111
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT']._serialized_end=7800
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_DAMAGEBYABILITY']._serialized_start=7344
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_DAMAGEBYABILITY']._serialized_end=7569
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_DAMAGEBYABILITY_BYHEROTARGET']._serialized_start=7522
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_DAMAGEBYABILITY_BYHEROTARGET']._serialized_end=7569
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_HEALINGBYABILITY']._serialized_start=7572
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_HEALINGBYABILITY']._serialized_end=7800
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_HEALINGBYABILITY_BYHEROTARGET']._serialized_start=7752
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_COMBATSEGMENT_HEALINGBYABILITY_BYHEROTARGET']._serialized_end=7800
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_BUFFRECORD']._serialized_start=7803
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_BUFFRECORD']._serialized_end=8039
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_BUFFRECORD_BYHEROTARGET']._serialized_start=7963
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_BUFFRECORD_BYHEROTARGET']._serialized_end=8039
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_GOLDRECEIVED']._serialized_start=8042
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_GOLDRECEIVED']._serialized_end=8194
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_XPRECEIVED']._serialized_start=8197
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_PLAYER_XPRECEIVED']._serialized_end=8334
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_BUILDING']._serialized_start=8336
  _globals['_CDOTAMATCHPRIVATEMETADATA_TEAM_BUILDING']._serialized_end=8437
# @@protoc_insertion_point(module_scope)