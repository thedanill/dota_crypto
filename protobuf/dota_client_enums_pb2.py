# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dota_client_enums.proto
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
    'dota_client_enums.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dota_shared_enums_pb2 as dota__shared__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64ota_client_enums.proto\x1a\x17\x64ota_shared_enums.proto*^\n\x13\x45TournamentTemplate\x12\x1e\n\x1ak_ETournamentTemplate_None\x10\x00\x12\'\n#k_ETournamentTemplate_AutomatedWin3\x10\x01*\xa8\x03\n\x14\x45TournamentGameState\x12\"\n\x1ek_ETournamentGameState_Unknown\x10\x00\x12#\n\x1fk_ETournamentGameState_Canceled\x10\x01\x12$\n k_ETournamentGameState_Scheduled\x10\x02\x12!\n\x1dk_ETournamentGameState_Active\x10\x03\x12%\n!k_ETournamentGameState_RadVictory\x10\x14\x12&\n\"k_ETournamentGameState_DireVictory\x10\x15\x12.\n*k_ETournamentGameState_RadVictoryByForfeit\x10\x16\x12/\n+k_ETournamentGameState_DireVictoryByForfeit\x10\x17\x12(\n$k_ETournamentGameState_ServerFailure\x10(\x12$\n k_ETournamentGameState_NotNeeded\x10)*\xe7\x06\n\x14\x45TournamentTeamState\x12\"\n\x1ek_ETournamentTeamState_Unknown\x10\x00\x12 \n\x1ck_ETournamentTeamState_Node1\x10\x01\x12#\n\x1ek_ETournamentTeamState_NodeMax\x10\x80\x08\x12&\n!k_ETournamentTeamState_Eliminated\x10\xb3m\x12%\n k_ETournamentTeamState_Forfeited\x10\xb4m\x12\'\n\"k_ETournamentTeamState_Finished1st\x10\x99u\x12\'\n\"k_ETournamentTeamState_Finished2nd\x10\x9au\x12\'\n\"k_ETournamentTeamState_Finished3rd\x10\x9bu\x12\'\n\"k_ETournamentTeamState_Finished4th\x10\x9cu\x12\'\n\"k_ETournamentTeamState_Finished5th\x10\x9du\x12\'\n\"k_ETournamentTeamState_Finished6th\x10\x9eu\x12\'\n\"k_ETournamentTeamState_Finished7th\x10\x9fu\x12\'\n\"k_ETournamentTeamState_Finished8th\x10\xa0u\x12\'\n\"k_ETournamentTeamState_Finished9th\x10\xa1u\x12(\n#k_ETournamentTeamState_Finished10th\x10\xa2u\x12(\n#k_ETournamentTeamState_Finished11th\x10\xa3u\x12(\n#k_ETournamentTeamState_Finished12th\x10\xa4u\x12(\n#k_ETournamentTeamState_Finished13th\x10\xa5u\x12(\n#k_ETournamentTeamState_Finished14th\x10\xa6u\x12(\n#k_ETournamentTeamState_Finished15th\x10\xa7u\x12(\n#k_ETournamentTeamState_Finished16th\x10\xa8u*\xec\x03\n\x10\x45TournamentState\x12\x1e\n\x1ak_ETournamentState_Unknown\x10\x00\x12&\n\"k_ETournamentState_CanceledByAdmin\x10\x01\x12 \n\x1ck_ETournamentState_Completed\x10\x02\x12\x1d\n\x19k_ETournamentState_Merged\x10\x03\x12$\n k_ETournamentState_ServerFailure\x10\x04\x12$\n k_ETournamentState_TeamAbandoned\x10\x05\x12)\n%k_ETournamentState_TeamTimeoutForfeit\x10\x06\x12(\n$k_ETournamentState_TeamTimeoutRefund\x10\x07\x12\x32\n.k_ETournamentState_ServerFailureGrantedVictory\x10\x08\x12\x30\n,k_ETournamentState_TeamTimeoutGrantedVictory\x10\t\x12!\n\x1dk_ETournamentState_InProgress\x10\x64\x12%\n!k_ETournamentState_WaitingToMerge\x10\x65*\xcc\x04\n\x14\x45TournamentNodeState\x12\"\n\x1ek_ETournamentNodeState_Unknown\x10\x00\x12#\n\x1fk_ETournamentNodeState_Canceled\x10\x01\x12.\n*k_ETournamentNodeState_TeamsNotYetAssigned\x10\x02\x12)\n%k_ETournamentNodeState_InBetweenGames\x10\x03\x12)\n%k_ETournamentNodeState_GameInProgress\x10\x04\x12 \n\x1ck_ETournamentNodeState_A_Won\x10\x05\x12 \n\x1ck_ETournamentNodeState_B_Won\x10\x06\x12)\n%k_ETournamentNodeState_A_WonByForfeit\x10\x07\x12)\n%k_ETournamentNodeState_B_WonByForfeit\x10\x08\x12 \n\x1ck_ETournamentNodeState_A_Bye\x10\t\x12&\n\"k_ETournamentNodeState_A_Abandoned\x10\n\x12(\n$k_ETournamentNodeState_ServerFailure\x10\x0b\x12+\n\'k_ETournamentNodeState_A_TimeoutForfeit\x10\x0c\x12*\n&k_ETournamentNodeState_A_TimeoutRefund\x10\r*\xc7\x03\n\x15\x45\x44OTAGroupMergeResult\x12\x1e\n\x1ak_EDOTAGroupMergeResult_OK\x10\x00\x12*\n&k_EDOTAGroupMergeResult_FAILED_GENERIC\x10\x01\x12&\n\"k_EDOTAGroupMergeResult_NOT_LEADER\x10\x02\x12,\n(k_EDOTAGroupMergeResult_TOO_MANY_PLAYERS\x10\x03\x12,\n(k_EDOTAGroupMergeResult_TOO_MANY_COACHES\x10\x04\x12+\n\'k_EDOTAGroupMergeResult_ENGINE_MISMATCH\x10\x05\x12)\n%k_EDOTAGroupMergeResult_NO_SUCH_GROUP\x10\x06\x12\x30\n,k_EDOTAGroupMergeResult_OTHER_GROUP_NOT_OPEN\x10\x07\x12+\n\'k_EDOTAGroupMergeResult_ALREADY_INVITED\x10\x08\x12\'\n#k_EDOTAGroupMergeResult_NOT_INVITED\x10\t*U\n\x10\x45PartyBeaconType\x12 \n\x1ck_EPartyBeaconType_Available\x10\x00\x12\x1f\n\x1bk_EPartyBeaconType_Joinable\x10\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_client_enums_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ETOURNAMENTTEMPLATE']._serialized_start=52
  _globals['_ETOURNAMENTTEMPLATE']._serialized_end=146
  _globals['_ETOURNAMENTGAMESTATE']._serialized_start=149
  _globals['_ETOURNAMENTGAMESTATE']._serialized_end=573
  _globals['_ETOURNAMENTTEAMSTATE']._serialized_start=576
  _globals['_ETOURNAMENTTEAMSTATE']._serialized_end=1447
  _globals['_ETOURNAMENTSTATE']._serialized_start=1450
  _globals['_ETOURNAMENTSTATE']._serialized_end=1942
  _globals['_ETOURNAMENTNODESTATE']._serialized_start=1945
  _globals['_ETOURNAMENTNODESTATE']._serialized_end=2533
  _globals['_EDOTAGROUPMERGERESULT']._serialized_start=2536
  _globals['_EDOTAGROUPMERGERESULT']._serialized_end=2991
  _globals['_EPARTYBEACONTYPE']._serialized_start=2993
  _globals['_EPARTYBEACONTYPE']._serialized_end=3078
# @@protoc_insertion_point(module_scope)