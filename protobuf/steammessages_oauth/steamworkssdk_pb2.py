# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_oauth.steamworkssdk.proto
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
    'steammessages_oauth.steamworkssdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamworkssdk_pb2 as steammessages__unified__base_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'steammessages_oauth.steamworkssdk.proto\x1a.steammessages_unified_base.steamworkssdk.proto\"{\n)COAuthToken_ImplicitGrantNoPrompt_Request\x12N\n\x08\x63lientid\x18\x01 \x01(\tB<\x82\xb5\x18\x38\x43lient ID for which to count the number of issued tokens\"\xb7\x01\n*COAuthToken_ImplicitGrantNoPrompt_Response\x12\x39\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tB#\x82\xb5\x18\x1fOAuth Token, granted on success\x12N\n\x0credirect_uri\x18\x02 \x01(\tB8\x82\xb5\x18\x34Redirection URI provided during client registration.2\xb1\x02\n\nOAuthToken\x12\xeb\x01\n\x15ImplicitGrantNoPrompt\x12*.COAuthToken_ImplicitGrantNoPrompt_Request\x1a+.COAuthToken_ImplicitGrantNoPrompt_Response\"y\x82\xb5\x18uGrants an implicit OAuth token (grant type \'token\') for the specified client ID on behalf of a user without prompting\x1a\x35\x82\xb5\x18\x31Service containing methods to manage OAuth tokens')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_oauth.steamworkssdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_REQUEST'].fields_by_name['clientid']._loaded_options = None
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_REQUEST'].fields_by_name['clientid']._serialized_options = b'\202\265\0308Client ID for which to count the number of issued tokens'
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE'].fields_by_name['access_token']._loaded_options = None
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE'].fields_by_name['access_token']._serialized_options = b'\202\265\030\037OAuth Token, granted on success'
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE'].fields_by_name['redirect_uri']._loaded_options = None
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE'].fields_by_name['redirect_uri']._serialized_options = b'\202\265\0304Redirection URI provided during client registration.'
  _globals['_OAUTHTOKEN']._loaded_options = None
  _globals['_OAUTHTOKEN']._serialized_options = b'\202\265\0301Service containing methods to manage OAuth tokens'
  _globals['_OAUTHTOKEN'].methods_by_name['ImplicitGrantNoPrompt']._loaded_options = None
  _globals['_OAUTHTOKEN'].methods_by_name['ImplicitGrantNoPrompt']._serialized_options = b'\202\265\030uGrants an implicit OAuth token (grant type \'token\') for the specified client ID on behalf of a user without prompting'
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_REQUEST']._serialized_start=91
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_REQUEST']._serialized_end=214
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE']._serialized_start=217
  _globals['_COAUTHTOKEN_IMPLICITGRANTNOPROMPT_RESPONSE']._serialized_end=400
  _globals['_OAUTHTOKEN']._serialized_start=403
  _globals['_OAUTHTOKEN']._serialized_end=708
# @@protoc_insertion_point(module_scope)
