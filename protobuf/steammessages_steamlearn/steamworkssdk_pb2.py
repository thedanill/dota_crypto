# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_steamlearn.steamworkssdk.proto
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
    'steammessages_steamlearn.steamworkssdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamworkssdk_pb2 as steammessages__unified__base_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,steammessages_steamlearn.steamworkssdk.proto\x1a.steammessages_unified_base.steamworkssdk.proto\"\\\n\"CMsgSteamLearnDataSourceDescObject\x12\x36\n\x08\x65lements\x18\x01 \x03(\x0b\x32$.CMsgSteamLearnDataSourceDescElement\"\xbd\x01\n#CMsgSteamLearnDataSourceDescElement\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x44\n\tdata_type\x18\x02 \x01(\x0e\x32\x14.ESteamLearnDataType:\x1bSTEAMLEARN_DATATYPE_INVALID\x12\x33\n\x06object\x18\x03 \x01(\x0b\x32#.CMsgSteamLearnDataSourceDescObject\x12\r\n\x05\x63ount\x18\x04 \x01(\r\"\xd0\x01\n\x18\x43MsgSteamLearnDataSource\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\r\x12\x1a\n\x12source_description\x18\x04 \x01(\t\x12\x36\n\tstructure\x18\x05 \x01(\x0b\x32#.CMsgSteamLearnDataSourceDescObject\x12\x15\n\rstructure_crc\x18\x06 \x01(\r\x12\x1e\n\x16\x63\x61\x63he_duration_seconds\x18\x07 \x01(\r\"H\n\x18\x43MsgSteamLearnDataObject\x12,\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x1a.CMsgSteamLearnDataElement\"\xae\x01\n\x19\x43MsgSteamLearnDataElement\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61ta_int32s\x18\x14 \x03(\x05\x12\x13\n\x0b\x64\x61ta_floats\x18\x15 \x03(\x02\x12\x12\n\ndata_bools\x18\x16 \x03(\x08\x12\x14\n\x0c\x64\x61ta_strings\x18\x17 \x03(\t\x12/\n\x0c\x64\x61ta_objects\x18\x18 \x03(\x0b\x32\x19.CMsgSteamLearnDataObject\"j\n\x12\x43MsgSteamLearnData\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\r\x12\x0c\n\x04keys\x18\x02 \x03(\x04\x12.\n\x0b\x64\x61ta_object\x18\x03 \x01(\x0b\x32\x19.CMsgSteamLearnDataObject\";\n\x16\x43MsgSteamLearnDataList\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.CMsgSteamLearnData\"q\n)CMsgSteamLearn_RegisterDataSource_Request\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12.\n\x0b\x64\x61ta_source\x18\x03 \x01(\x0b\x32\x19.CMsgSteamLearnDataSource\"\xc1\x01\n*CMsgSteamLearn_RegisterDataSource_Response\x12\x63\n\x06result\x18\x01 \x01(\x0e\x32%.ESteammLearnRegisterDataSourceResult:,STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR\x12.\n\x0b\x64\x61ta_source\x18\x02 \x01(\x0b\x32\x19.CMsgSteamLearnDataSource\"[\n CMsgSteamLearn_CacheData_Request\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12!\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x13.CMsgSteamLearnData\"x\n!CMsgSteamLearn_CacheData_Response\x12S\n\x11\x63\x61\x63he_data_result\x18\x01 \x01(\x0e\x32\x1b.ESteamLearnCacheDataResult:\x1bSTEAMLEARN_CACHE_DATA_ERROR\"\xc2\x01\n&CMsgSteamLearn_SnapshotProject_Request\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\r\x12\x19\n\x11published_version\x18\x07 \x01(\r\x12\x0c\n\x04keys\x18\x04 \x03(\x04\x12!\n\x04\x64\x61ta\x18\x05 \x03(\x0b\x32\x13.CMsgSteamLearnData\x12\"\n\x1apending_data_limit_seconds\x18\x06 \x01(\r\"\x88\x01\n\'CMsgSteamLearn_SnapshotProject_Response\x12]\n\x0fsnapshot_result\x18\x01 \x01(\x0e\x32!.ESteamLearnSnapshotProjectResult:!STEAMLEARN_SNAPSHOT_PROJECT_ERROR\"\xea\x01\n%CMsgSteamLearn_BatchOperation_Request\x12>\n\x13\x63\x61\x63he_data_requests\x18\x01 \x03(\x0b\x32!.CMsgSteamLearn_CacheData_Request\x12\x42\n\x11snapshot_requests\x18\x02 \x03(\x0b\x32\'.CMsgSteamLearn_SnapshotProject_Request\x12=\n\x12inference_requests\x18\x03 \x03(\x0b\x32!.CMsgSteamLearn_Inference_Request\"\xf1\x01\n&CMsgSteamLearn_BatchOperation_Response\x12@\n\x14\x63\x61\x63he_data_responses\x18\x01 \x03(\x0b\x32\".CMsgSteamLearn_CacheData_Response\x12\x44\n\x12snapshot_responses\x18\x02 \x03(\x0b\x32(.CMsgSteamLearn_SnapshotProject_Response\x12?\n\x13inference_responses\x18\x03 \x03(\x0b\x32\".CMsgSteamLearn_Inference_Response\"\x9e\x04\n\x1a\x43MsgSteamLearnAccessTokens\x12)\n!register_data_source_access_token\x18\x01 \x01(\t\x12R\n\x18\x63\x61\x63he_data_access_tokens\x18\x02 \x03(\x0b\x32\x30.CMsgSteamLearnAccessTokens.CacheDataAccessToken\x12^\n\x1esnapshot_project_access_tokens\x18\x03 \x03(\x0b\x32\x36.CMsgSteamLearnAccessTokens.SnapshotProjectAccessToken\x12Q\n\x17inference_access_tokens\x18\x04 \x03(\x0b\x32\x30.CMsgSteamLearnAccessTokens.InferenceAccessToken\x1a\x44\n\x14\x43\x61\x63heDataAccessToken\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x1a\x46\n\x1aSnapshotProjectAccessToken\x12\x12\n\nproject_id\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\x1a@\n\x14InferenceAccessToken\x12\x12\n\nproject_id\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\"7\n&CMsgSteamLearn_GetAccessTokens_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\"\xb4\x01\n\'CMsgSteamLearn_GetAccessTokens_Response\x12U\n\x06result\x18\x01 \x01(\x0e\x32!.ESteamLearnGetAccessTokensResult:\"STEAMLEARN_GET_ACCESS_TOKENS_ERROR\x12\x32\n\raccess_tokens\x18\x02 \x01(\x0b\x32\x1b.CMsgSteamLearnAccessTokens\"\xc2\x01\n CMsgSteamLearn_Inference_Request\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\r\x12\x19\n\x11published_version\x18\x04 \x01(\r\x12\x19\n\x11override_train_id\x18\x05 \x01(\r\x12%\n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x17.CMsgSteamLearnDataList\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x07 \x03(\x02\"\x8a\x01\n(CMsgSteamLearn_InferenceMetadata_Request\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\r\x12\x19\n\x11published_version\x18\x04 \x01(\r\x12\x19\n\x11override_train_id\x18\x05 \x01(\r\"W\n/CMsgSteamLearn_InferenceMetadataBackend_Request\x12\x12\n\nproject_id\x18\x01 \x01(\r\x12\x10\n\x08\x66\x65tch_id\x18\x02 \x01(\r\"\xc0\x0c\n)CMsgSteamLearn_InferenceMetadata_Response\x12k\n\x19inference_metadata_result\x18\x01 \x01(\x0e\x32#.ESteamLearnInferenceMetadataResult:#STEAMLEARN_INFERENCE_METADATA_ERROR\x12\x46\n\trow_range\x18\x02 \x01(\x0b\x32\x33.CMsgSteamLearn_InferenceMetadata_Response.RowRange\x12@\n\x06ranges\x18\x03 \x03(\x0b\x32\x30.CMsgSteamLearn_InferenceMetadata_Response.Range\x12\x43\n\x08std_devs\x18\x04 \x03(\x0b\x32\x31.CMsgSteamLearn_InferenceMetadata_Response.StdDev\x12O\n\x0e\x63ompact_tables\x18\x05 \x03(\x0b\x32\x37.CMsgSteamLearn_InferenceMetadata_Response.CompactTable\x12\x41\n\x06kmeans\x18\x06 \x03(\x0b\x32\x31.CMsgSteamLearn_InferenceMetadata_Response.KMeans\x12X\n\x12snapshot_histogram\x18\x07 \x01(\x0b\x32<.CMsgSteamLearn_InferenceMetadata_Response.SnapshotHistogram\x1a,\n\x08RowRange\x12\x0f\n\x07min_row\x18\x01 \x01(\x04\x12\x0f\n\x07max_row\x18\x02 \x01(\x04\x1aH\n\x05Range\x12\x19\n\x11\x64\x61ta_element_path\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x02\x12\x11\n\tmax_value\x18\x03 \x01(\x02\x1a\x42\n\x06StdDev\x12\x19\n\x11\x64\x61ta_element_path\x18\x01 \x01(\t\x12\x0c\n\x04mean\x18\x02 \x01(\x02\x12\x0f\n\x07std_dev\x18\x03 \x01(\x02\x1a\xec\x03\n\x0c\x43ompactTable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12Z\n\nmap_values\x18\x02 \x03(\x0b\x32\x46.CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapValuesEntry\x12^\n\x0cmap_mappings\x18\x03 \x03(\x0b\x32H.CMsgSteamLearn_InferenceMetadata_Response.CompactTable.MapMappingsEntry\x1a\x36\n\x05\x45ntry\x12\r\n\x05value\x18\x01 \x01(\r\x12\x0f\n\x07mapping\x18\x02 \x01(\r\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\x1ak\n\x0eMapValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12L\n\x05value\x18\x02 \x01(\x0b\x32=.CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry\x1am\n\x10MapMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12L\n\x05value\x18\x02 \x01(\x0b\x32=.CMsgSteamLearn_InferenceMetadata_Response.CompactTable.Entry\x1a\xd6\x01\n\x06KMeans\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x08\x63lusters\x18\x02 \x03(\x0b\x32\x39.CMsgSteamLearn_InferenceMetadata_Response.KMeans.Cluster\x1aq\n\x07\x43luster\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0e\n\x06radius\x18\x03 \x01(\x02\x12\x14\n\x0cradius_75pct\x18\x04 \x01(\x02\x12\x14\n\x0cradius_50pct\x18\x05 \x01(\x02\x12\x14\n\x0cradius_25pct\x18\x06 \x01(\x02\x1a\x65\n\x11SnapshotHistogram\x12\x11\n\tmin_value\x18\x01 \x01(\x02\x12\x11\n\tmax_value\x18\x02 \x01(\x02\x12\x13\n\x0bnum_buckets\x18\x03 \x01(\r\x12\x15\n\rbucket_counts\x18\x04 \x03(\r\"\xe6\x05\n(CMsgSteamLearn_InferenceBackend_Response\x12\x41\n\x07outputs\x18\x01 \x03(\x0b\x32\x30.CMsgSteamLearn_InferenceBackend_Response.Output\x1a!\n\x10RegressionOutput\x12\r\n\x05value\x18\x01 \x01(\x02\x1a)\n\x18\x42inaryCrossEntropyOutput\x12\r\n\x05value\x18\x01 \x01(\x02\x1a>\n\x1dMutliBinaryCrossEntropyOutput\x12\x0e\n\x06weight\x18\x01 \x03(\x02\x12\r\n\x05value\x18\x02 \x03(\x02\x1a>\n\x1d\x43\x61tegoricalCrossEntropyOutput\x12\x0e\n\x06weight\x18\x01 \x03(\x02\x12\r\n\x05value\x18\x02 \x03(\x02\x1a\xa8\x03\n\x06Output\x12\x61\n\x13\x62inary_crossentropy\x18\x01 \x01(\x0b\x32\x42.CMsgSteamLearn_InferenceBackend_Response.BinaryCrossEntropyOutputH\x00\x12k\n\x18\x63\x61tegorical_crossentropy\x18\x02 \x01(\x0b\x32G.CMsgSteamLearn_InferenceBackend_Response.CategoricalCrossEntropyOutputH\x00\x12l\n\x19multi_binary_crossentropy\x18\x03 \x01(\x0b\x32G.CMsgSteamLearn_InferenceBackend_Response.MutliBinaryCrossEntropyOutputH\x00\x12P\n\nregression\x18\x04 \x01(\x0b\x32:.CMsgSteamLearn_InferenceBackend_Response.RegressionOutputH\x00\x42\x0e\n\x0cResponseType\"\xc9\x01\n!CMsgSteamLearn_Inference_Response\x12Q\n\x10inference_result\x18\x01 \x01(\x0e\x32\x1b.ESteamLearnInferenceResult:\x1aSTEAMLEARN_INFERENCE_ERROR\x12\x43\n\x10\x62\x61\x63kend_response\x18\x02 \x01(\x0b\x32).CMsgSteamLearn_InferenceBackend_Response\x12\x0c\n\x04keys\x18\x03 \x03(\x04*\xd4\x01\n\x13\x45SteamLearnDataType\x12\x1f\n\x1bSTEAMLEARN_DATATYPE_INVALID\x10\x00\x12\x1d\n\x19STEAMLEARN_DATATYPE_INT32\x10\x01\x12\x1f\n\x1bSTEAMLEARN_DATATYPE_FLOAT32\x10\x02\x12\x1c\n\x18STEAMLEARN_DATATYPE_BOOL\x10\x03\x12\x1e\n\x1aSTEAMLEARN_DATATYPE_STRING\x10\x04\x12\x1e\n\x1aSTEAMLEARN_DATATYPE_OBJECT\x10\x05*\xbc\x05\n$ESteammLearnRegisterDataSourceResult\x12\x30\n,STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR\x10\x00\x12:\n6STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_CREATED\x10\x01\x12\x38\n4STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_SUCCESS_FOUND\x10\x02\x12\x38\n4STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_GENERIC\x10\x03\x12=\n9STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_NAME\x10\x04\x12@\n<STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_VERSION\x10\x05\x12=\n9STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_CHANGED\x10\x06\x12=\n9STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_DATA_INVALID\x10\x07\x12:\n6STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_FORBIDDEN\x10\x08\x12\x42\n>STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_ERROR_INVALID_TIMESTAMP\x10\t\x12\x33\n/STEAMLEARN_REGISTER_DATA_SOURCE_RESULT_DISABLED\x10\n*\xfb\x02\n\x1a\x45SteamLearnCacheDataResult\x12\x1f\n\x1bSTEAMLEARN_CACHE_DATA_ERROR\x10\x00\x12!\n\x1dSTEAMLEARN_CACHE_DATA_SUCCESS\x10\x01\x12\x33\n/STEAMLEARN_CACHE_DATA_ERROR_UNKNOWN_DATA_SOURCE\x10\x02\x12\x34\n0STEAMLEARN_CACHE_DATA_ERROR_UNCACHED_DATA_SOURCE\x10\x03\x12,\n(STEAMLEARN_CACHE_DATA_ERROR_INVALID_KEYS\x10\x04\x12)\n%STEAMLEARN_CACHE_DATA_ERROR_FORBIDDEN\x10\x05\x12\x31\n-STEAMLEARN_CACHE_DATA_ERROR_INVALID_TIMESTAMP\x10\x06\x12\"\n\x1eSTEAMLEARN_CACHE_DATA_DISABLED\x10\x07*\xed\x05\n ESteamLearnSnapshotProjectResult\x12%\n!STEAMLEARN_SNAPSHOT_PROJECT_ERROR\x10\x00\x12.\n*STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_STORED\x10\x01\x12.\n*STEAMLEARN_SNAPSHOT_PROJECT_SUCCESS_QUEUED\x10\x02\x12\x38\n4STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PROJECT_ID\x10\x03\x12\x39\n5STEAMLEARN_SNAPSHOT_PROJECT_ERROR_UNKNOWN_DATA_SOURCE\x10\x04\x12=\n9STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_DATA_SOURCE_KEY\x10\x05\x12<\n8STEAMLEARN_SNAPSHOT_PROJECT_ERROR_MISSING_CACHE_DURATION\x10\x06\x12\x39\n5STEAMLEARN_SNAPSHOT_PROJECT_ERROR_NO_PUBLISHED_CONFIG\x10\x07\x12/\n+STEAMLEARN_SNAPSHOT_PROJECT_ERROR_FORBIDDEN\x10\x08\x12\x37\n3STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_TIMESTAMP\x10\t\x12@\n<STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INTERNAL_DATA_SOURCE_ERROR\x10\n\x12(\n$STEAMLEARN_SNAPSHOT_PROJECT_DISABLED\x10\x0b\x12?\n;STEAMLEARN_SNAPSHOT_PROJECT_ERROR_INVALID_PUBLISHED_VERSION\x10\x0c*t\n ESteamLearnGetAccessTokensResult\x12&\n\"STEAMLEARN_GET_ACCESS_TOKENS_ERROR\x10\x00\x12(\n$STEAMLEARN_GET_ACCESS_TOKENS_SUCCESS\x10\x01*\xf1\x03\n\x1a\x45SteamLearnInferenceResult\x12\x1e\n\x1aSTEAMLEARN_INFERENCE_ERROR\x10\x00\x12 \n\x1cSTEAMLEARN_INFERENCE_SUCCESS\x10\x01\x12\x31\n-STEAMLEARN_INFERENCE_ERROR_INVALID_PROJECT_ID\x10\x02\x12\x39\n5STEAMLEARN_INFERENCE_ERROR_MISSING_CACHED_SCHEMA_DATA\x10\x03\x12\x32\n.STEAMLEARN_INFERENCE_ERROR_NO_PUBLISHED_CONFIG\x10\x04\x12(\n$STEAMLEARN_INFERENCE_ERROR_FORBIDDEN\x10\x05\x12\x30\n,STEAMLEARN_INFERENCE_ERROR_INVALID_TIMESTAMP\x10\x06\x12\x38\n4STEAMLEARN_INFERENCE_ERROR_INVALID_PUBLISHED_VERSION\x10\x07\x12\x30\n,STEAMLEARN_INFERENCE_ERROR_NO_FETCH_ID_FOUND\x10\x08\x12\'\n#STEAMLEARN_INFERENCE_ERROR_TOO_BUSY\x10\t*\xdd\x03\n\"ESteamLearnInferenceMetadataResult\x12\'\n#STEAMLEARN_INFERENCE_METADATA_ERROR\x10\x00\x12)\n%STEAMLEARN_INFERENCE_METADATA_SUCCESS\x10\x01\x12:\n6STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PROJECT_ID\x10\x02\x12;\n7STEAMLEARN_INFERENCE_METADATA_ERROR_NO_PUBLISHED_CONFIG\x10\x03\x12\x31\n-STEAMLEARN_INFERENCE_METADATA_ERROR_FORBIDDEN\x10\x04\x12\x39\n5STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_TIMESTAMP\x10\x05\x12\x41\n=STEAMLEARN_INFERENCE_METADATA_ERROR_INVALID_PUBLISHED_VERSION\x10\x06\x12\x39\n5STEAMLEARN_INFERENCE_METADATA_ERROR_NO_FETCH_ID_FOUND\x10\x07\x32\x93\n\n\nSteamLearn\x12\xbb\x01\n\x12RegisterDataSource\x12*.CMsgSteamLearn_RegisterDataSource_Request\x1a+.CMsgSteamLearn_RegisterDataSource_Response\"L\x82\xb5\x18HRegisters a data desc (or finds a data desc if it\'s already registered).\x12t\n\tCacheData\x12!.CMsgSteamLearn_CacheData_Request\x1a\".CMsgSteamLearn_CacheData_Response\" \x82\xb5\x18\x1cUpdates a cached data entry.\x12\x93\x01\n\x0fSnapshotProject\x12\'.CMsgSteamLearn_SnapshotProject_Request\x1a(.CMsgSteamLearn_SnapshotProject_Response\"-\x82\xb5\x18)Snapshots the current data for a project.\x12\xba\x01\n\x0e\x42\x61tchOperation\x12&.CMsgSteamLearn_BatchOperation_Request\x1a\'.CMsgSteamLearn_BatchOperation_Response\"W\x82\xb5\x18SBatches multiple data updates, snapshots, and inference requests into a single call\x12\xd8\x01\n\x0fGetAccessTokens\x12\'.CMsgSteamLearn_GetAccessTokens_Request\x1a(.CMsgSteamLearn_GetAccessTokens_Response\"r\x82\xb5\x18nGets the access tokens needed for registering data sources, submitting data to them, and snapshotting projects\x12\xa2\x01\n\tInference\x12!.CMsgSteamLearn_Inference_Request\x1a\".CMsgSteamLearn_Inference_Response\"N\x82\xb5\x18JInferences using supplied data, or data associated with the specified key.\x12\xb0\x01\n\x11InferenceMetadata\x12).CMsgSteamLearn_InferenceMetadata_Request\x1a*.CMsgSteamLearn_InferenceMetadata_Response\"D\x82\xb5\x18@Requests the metadata that was generated from a specified fetch.\x1aK\x82\xb5\x18GService for submitting data, training, and inferencing with SteamLearn.')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_steamlearn.steamworkssdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STEAMLEARN']._loaded_options = None
  _globals['_STEAMLEARN']._serialized_options = b'\202\265\030GService for submitting data, training, and inferencing with SteamLearn.'
  _globals['_STEAMLEARN'].methods_by_name['RegisterDataSource']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['RegisterDataSource']._serialized_options = b'\202\265\030HRegisters a data desc (or finds a data desc if it\'s already registered).'
  _globals['_STEAMLEARN'].methods_by_name['CacheData']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['CacheData']._serialized_options = b'\202\265\030\034Updates a cached data entry.'
  _globals['_STEAMLEARN'].methods_by_name['SnapshotProject']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['SnapshotProject']._serialized_options = b'\202\265\030)Snapshots the current data for a project.'
  _globals['_STEAMLEARN'].methods_by_name['BatchOperation']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['BatchOperation']._serialized_options = b'\202\265\030SBatches multiple data updates, snapshots, and inference requests into a single call'
  _globals['_STEAMLEARN'].methods_by_name['GetAccessTokens']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['GetAccessTokens']._serialized_options = b'\202\265\030nGets the access tokens needed for registering data sources, submitting data to them, and snapshotting projects'
  _globals['_STEAMLEARN'].methods_by_name['Inference']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['Inference']._serialized_options = b'\202\265\030JInferences using supplied data, or data associated with the specified key.'
  _globals['_STEAMLEARN'].methods_by_name['InferenceMetadata']._loaded_options = None
  _globals['_STEAMLEARN'].methods_by_name['InferenceMetadata']._serialized_options = b'\202\265\030@Requests the metadata that was generated from a specified fetch.'
  _globals['_ESTEAMLEARNDATATYPE']._serialized_start=6121
  _globals['_ESTEAMLEARNDATATYPE']._serialized_end=6333
  _globals['_ESTEAMMLEARNREGISTERDATASOURCERESULT']._serialized_start=6336
  _globals['_ESTEAMMLEARNREGISTERDATASOURCERESULT']._serialized_end=7036
  _globals['_ESTEAMLEARNCACHEDATARESULT']._serialized_start=7039
  _globals['_ESTEAMLEARNCACHEDATARESULT']._serialized_end=7418
  _globals['_ESTEAMLEARNSNAPSHOTPROJECTRESULT']._serialized_start=7421
  _globals['_ESTEAMLEARNSNAPSHOTPROJECTRESULT']._serialized_end=8170
  _globals['_ESTEAMLEARNGETACCESSTOKENSRESULT']._serialized_start=8172
  _globals['_ESTEAMLEARNGETACCESSTOKENSRESULT']._serialized_end=8288
  _globals['_ESTEAMLEARNINFERENCERESULT']._serialized_start=8291
  _globals['_ESTEAMLEARNINFERENCERESULT']._serialized_end=8788
  _globals['_ESTEAMLEARNINFERENCEMETADATARESULT']._serialized_start=8791
  _globals['_ESTEAMLEARNINFERENCEMETADATARESULT']._serialized_end=9268
  _globals['_CMSGSTEAMLEARNDATASOURCEDESCOBJECT']._serialized_start=96
  _globals['_CMSGSTEAMLEARNDATASOURCEDESCOBJECT']._serialized_end=188
  _globals['_CMSGSTEAMLEARNDATASOURCEDESCELEMENT']._serialized_start=191
  _globals['_CMSGSTEAMLEARNDATASOURCEDESCELEMENT']._serialized_end=380
  _globals['_CMSGSTEAMLEARNDATASOURCE']._serialized_start=383
  _globals['_CMSGSTEAMLEARNDATASOURCE']._serialized_end=591
  _globals['_CMSGSTEAMLEARNDATAOBJECT']._serialized_start=593
  _globals['_CMSGSTEAMLEARNDATAOBJECT']._serialized_end=665
  _globals['_CMSGSTEAMLEARNDATAELEMENT']._serialized_start=668
  _globals['_CMSGSTEAMLEARNDATAELEMENT']._serialized_end=842
  _globals['_CMSGSTEAMLEARNDATA']._serialized_start=844
  _globals['_CMSGSTEAMLEARNDATA']._serialized_end=950
  _globals['_CMSGSTEAMLEARNDATALIST']._serialized_start=952
  _globals['_CMSGSTEAMLEARNDATALIST']._serialized_end=1011
  _globals['_CMSGSTEAMLEARN_REGISTERDATASOURCE_REQUEST']._serialized_start=1013
  _globals['_CMSGSTEAMLEARN_REGISTERDATASOURCE_REQUEST']._serialized_end=1126
  _globals['_CMSGSTEAMLEARN_REGISTERDATASOURCE_RESPONSE']._serialized_start=1129
  _globals['_CMSGSTEAMLEARN_REGISTERDATASOURCE_RESPONSE']._serialized_end=1322
  _globals['_CMSGSTEAMLEARN_CACHEDATA_REQUEST']._serialized_start=1324
  _globals['_CMSGSTEAMLEARN_CACHEDATA_REQUEST']._serialized_end=1415
  _globals['_CMSGSTEAMLEARN_CACHEDATA_RESPONSE']._serialized_start=1417
  _globals['_CMSGSTEAMLEARN_CACHEDATA_RESPONSE']._serialized_end=1537
  _globals['_CMSGSTEAMLEARN_SNAPSHOTPROJECT_REQUEST']._serialized_start=1540
  _globals['_CMSGSTEAMLEARN_SNAPSHOTPROJECT_REQUEST']._serialized_end=1734
  _globals['_CMSGSTEAMLEARN_SNAPSHOTPROJECT_RESPONSE']._serialized_start=1737
  _globals['_CMSGSTEAMLEARN_SNAPSHOTPROJECT_RESPONSE']._serialized_end=1873
  _globals['_CMSGSTEAMLEARN_BATCHOPERATION_REQUEST']._serialized_start=1876
  _globals['_CMSGSTEAMLEARN_BATCHOPERATION_REQUEST']._serialized_end=2110
  _globals['_CMSGSTEAMLEARN_BATCHOPERATION_RESPONSE']._serialized_start=2113
  _globals['_CMSGSTEAMLEARN_BATCHOPERATION_RESPONSE']._serialized_end=2354
  _globals['_CMSGSTEAMLEARNACCESSTOKENS']._serialized_start=2357
  _globals['_CMSGSTEAMLEARNACCESSTOKENS']._serialized_end=2899
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_CACHEDATAACCESSTOKEN']._serialized_start=2693
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_CACHEDATAACCESSTOKEN']._serialized_end=2761
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_SNAPSHOTPROJECTACCESSTOKEN']._serialized_start=2763
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_SNAPSHOTPROJECTACCESSTOKEN']._serialized_end=2833
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_INFERENCEACCESSTOKEN']._serialized_start=2835
  _globals['_CMSGSTEAMLEARNACCESSTOKENS_INFERENCEACCESSTOKEN']._serialized_end=2899
  _globals['_CMSGSTEAMLEARN_GETACCESSTOKENS_REQUEST']._serialized_start=2901
  _globals['_CMSGSTEAMLEARN_GETACCESSTOKENS_REQUEST']._serialized_end=2956
  _globals['_CMSGSTEAMLEARN_GETACCESSTOKENS_RESPONSE']._serialized_start=2959
  _globals['_CMSGSTEAMLEARN_GETACCESSTOKENS_RESPONSE']._serialized_end=3139
  _globals['_CMSGSTEAMLEARN_INFERENCE_REQUEST']._serialized_start=3142
  _globals['_CMSGSTEAMLEARN_INFERENCE_REQUEST']._serialized_end=3336
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_REQUEST']._serialized_start=3339
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_REQUEST']._serialized_end=3477
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATABACKEND_REQUEST']._serialized_start=3479
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATABACKEND_REQUEST']._serialized_end=3566
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE']._serialized_start=3569
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE']._serialized_end=5169
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_ROWRANGE']._serialized_start=4168
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_ROWRANGE']._serialized_end=4212
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_RANGE']._serialized_start=4214
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_RANGE']._serialized_end=4286
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_STDDEV']._serialized_start=4288
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_STDDEV']._serialized_end=4354
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE']._serialized_start=4357
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE']._serialized_end=4849
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_ENTRY']._serialized_start=4575
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_ENTRY']._serialized_end=4629
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_MAPVALUESENTRY']._serialized_start=4631
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_MAPVALUESENTRY']._serialized_end=4738
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_MAPMAPPINGSENTRY']._serialized_start=4740
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_COMPACTTABLE_MAPMAPPINGSENTRY']._serialized_end=4849
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_KMEANS']._serialized_start=4852
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_KMEANS']._serialized_end=5066
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_KMEANS_CLUSTER']._serialized_start=4953
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_KMEANS_CLUSTER']._serialized_end=5066
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_SNAPSHOTHISTOGRAM']._serialized_start=5068
  _globals['_CMSGSTEAMLEARN_INFERENCEMETADATA_RESPONSE_SNAPSHOTHISTOGRAM']._serialized_end=5169
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE']._serialized_start=5172
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE']._serialized_end=5914
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_REGRESSIONOUTPUT']._serialized_start=5283
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_REGRESSIONOUTPUT']._serialized_end=5316
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_BINARYCROSSENTROPYOUTPUT']._serialized_start=5318
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_BINARYCROSSENTROPYOUTPUT']._serialized_end=5359
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_MUTLIBINARYCROSSENTROPYOUTPUT']._serialized_start=5361
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_MUTLIBINARYCROSSENTROPYOUTPUT']._serialized_end=5423
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_CATEGORICALCROSSENTROPYOUTPUT']._serialized_start=5425
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_CATEGORICALCROSSENTROPYOUTPUT']._serialized_end=5487
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_OUTPUT']._serialized_start=5490
  _globals['_CMSGSTEAMLEARN_INFERENCEBACKEND_RESPONSE_OUTPUT']._serialized_end=5914
  _globals['_CMSGSTEAMLEARN_INFERENCE_RESPONSE']._serialized_start=5917
  _globals['_CMSGSTEAMLEARN_INFERENCE_RESPONSE']._serialized_end=6118
  _globals['_STEAMLEARN']._serialized_start=9271
  _globals['_STEAMLEARN']._serialized_end=10570
# @@protoc_insertion_point(module_scope)
