# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_publishedfile.steamworkssdk.proto
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
    'steammessages_publishedfile.steamworkssdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steammessages_unified_base import steamworkssdk_pb2 as steammessages__unified__base_dot_steamworkssdk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/steammessages_publishedfile.steamworkssdk.proto\x1a.steammessages_unified_base.steamworkssdk.proto\"t\n CPublishedFile_Subscribe_Request\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\x12\x11\n\tlist_type\x18\x02 \x01(\r\x12\r\n\x05\x61ppid\x18\x03 \x01(\x05\x12\x15\n\rnotify_client\x18\x04 \x01(\x08\"#\n!CPublishedFile_Subscribe_Response\"v\n\"CPublishedFile_Unsubscribe_Request\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\x12\x11\n\tlist_type\x18\x02 \x01(\r\x12\r\n\x05\x61ppid\x18\x03 \x01(\x05\x12\x15\n\rnotify_client\x18\x04 \x01(\x08\"%\n#CPublishedFile_Unsubscribe_Response\"\xcc\n\n\x1e\x43PublishedFile_Publish_Request\x12<\n\x05\x61ppid\x18\x01 \x01(\rB-\x82\xb5\x18)App Id this file is being published FROM.\x12\x43\n\x0e\x63onsumer_appid\x18\x02 \x01(\rB+\x82\xb5\x18\'App Id this file is being published TO.\x12K\n\rcloudfilename\x18\x03 \x01(\tB4\x82\xb5\x18\x30Name of the file to publish in the user\'s cloud.\x12[\n\x15preview_cloudfilename\x18\x04 \x01(\tB<\x82\xb5\x18\x38Name of the file to use as the published file\'s preview.\x12\x35\n\x05title\x18\x05 \x01(\tB&\x82\xb5\x18\"Text title for the published file.\x12\x46\n\x10\x66ile_description\x18\x06 \x01(\tB,\x82\xb5\x18(Text description for the published file.\x12L\n\tfile_type\x18\x07 \x01(\rB9\x82\xb5\x18\x35(EWorkshopFileType) Type of Workshop file to publish.\x12I\n\x16\x63onsumer_shortcut_name\x18\x08 \x01(\tB)\x82\xb5\x18%Shortcut name for the published file.\x12I\n\x10youtube_username\x18\t \x01(\tB/\x82\xb5\x18+(Optional) User\'s YouTube account username.\x12\\\n\x0fyoutube_videoid\x18\n \x01(\tBC\x82\xb5\x18?(Optional) Video Id of a YouTube video for this published file.\x12\x81\x01\n\nvisibility\x18\x0b \x01(\rBm\x82\xb5\x18i(ERemoteStoragePublishedFileVisibility) Visibility of the published file (private, friends, public, etc.)\x12k\n\x0credirect_uri\x18\x0c \x01(\tBU\x82\xb5\x18Q(Optional) If supplied, the resulting published file\'s Id is appended to the URI.\x12\x44\n\x04tags\x18\r \x03(\tB6\x82\xb5\x18\x32\x41rray of text tags to apply to the published file.\x12Y\n\x0f\x63ollection_type\x18\x0e \x01(\tB@\x82\xb5\x18<(Optional) Type of collection the published file represents.\x12M\n\tgame_type\x18\x0f \x01(\tB:\x82\xb5\x18\x36(Optional) Type of game the published file represents.\x12[\n\x03url\x18\x10 \x01(\tBN\x82\xb5\x18J(Optional) If this represents a game, this is the URL to that game\'s page.\"P\n\x1f\x43PublishedFile_Publish_Response\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\x12\x14\n\x0credirect_uri\x18\x02 \x01(\t\"\x84\x05\n!CPublishedFile_GetDetails_Request\x12P\n\x10publishedfileids\x18\x01 \x03(\x06\x42\x36\x82\xb5\x18\x32Set of published file Ids to retrieve details for.\x12Q\n\x0bincludetags\x18\x02 \x01(\x08\x42<\x82\xb5\x18\x38If true, return tag information in the returned details.\x12\x63\n\x19includeadditionalpreviews\x18\x03 \x01(\x08\x42@\x82\xb5\x18<If true, return preview information in the returned details.\x12N\n\x0fincludechildren\x18\x04 \x01(\x08\x42\x35\x82\xb5\x18\x31If true, return children in the returned details.\x12R\n\rincludekvtags\x18\x05 \x01(\x08\x42;\x82\xb5\x18\x37If true, return key value tags in the returned details.\x12L\n\x0cincludevotes\x18\x06 \x01(\x08\x42\x36\x82\xb5\x18\x32If true, return vote data in the returned details.\x12\x63\n\x11short_description\x18\x08 \x01(\x08\x42H\x82\xb5\x18\x44If true, return a short description instead of the full description.\"\x89\x0e\n\x14PublishedFileDetails\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x17\n\x0fpublishedfileid\x18\x02 \x01(\x04\x12\x0f\n\x07\x63reator\x18\x03 \x01(\x06\x12\x15\n\rcreator_appid\x18\x04 \x01(\r\x12\x16\n\x0e\x63onsumer_appid\x18\x05 \x01(\r\x12\x1b\n\x13\x63onsumer_shortcutid\x18\x06 \x01(\r\x12\x10\n\x08\x66ilename\x18\x07 \x01(\t\x12\x11\n\tfile_size\x18\x08 \x01(\x04\x12\x19\n\x11preview_file_size\x18\t \x01(\x04\x12\x10\n\x08\x66ile_url\x18\n \x01(\t\x12\x13\n\x0bpreview_url\x18\x0b \x01(\t\x12\x16\n\x0eyoutubevideoid\x18\x0c \x01(\t\x12\x0b\n\x03url\x18\r \x01(\t\x12\x15\n\rhcontent_file\x18\x0e \x01(\x06\x12\x18\n\x10hcontent_preview\x18\x0f \x01(\x06\x12\r\n\x05title\x18\x10 \x01(\t\x12\x18\n\x10\x66ile_description\x18\x11 \x01(\t\x12\x19\n\x11short_description\x18\x12 \x01(\t\x12\x14\n\x0ctime_created\x18\x13 \x01(\r\x12\x14\n\x0ctime_updated\x18\x14 \x01(\r\x12\x12\n\nvisibility\x18\x15 \x01(\r\x12\r\n\x05\x66lags\x18\x16 \x01(\r\x12\x15\n\rworkshop_file\x18\x17 \x01(\x08\x12\x19\n\x11workshop_accepted\x18\x18 \x01(\x08\x12\x1a\n\x12show_subscribe_all\x18\x19 \x01(\x08\x12\x1e\n\x16num_comments_developer\x18\x1a \x01(\x05\x12\x1b\n\x13num_comments_public\x18\x1b \x01(\x05\x12\x0e\n\x06\x62\x61nned\x18\x1c \x01(\x08\x12\x12\n\nban_reason\x18\x1d \x01(\t\x12\x0e\n\x06\x62\x61nner\x18\x1e \x01(\x06\x12\x16\n\x0e\x63\x61n_be_deleted\x18\x1f \x01(\x08\x12\x14\n\x0cincompatible\x18  \x01(\x08\x12\x10\n\x08\x61pp_name\x18! \x01(\t\x12\x11\n\tfile_type\x18\" \x01(\r\x12\x15\n\rcan_subscribe\x18# \x01(\x08\x12\x15\n\rsubscriptions\x18$ \x01(\r\x12\x11\n\tfavorited\x18% \x01(\r\x12\x11\n\tfollowers\x18& \x01(\r\x12\x1e\n\x16lifetime_subscriptions\x18\' \x01(\r\x12\x1a\n\x12lifetime_favorited\x18( \x01(\r\x12\x1a\n\x12lifetime_followers\x18) \x01(\r\x12\r\n\x05views\x18* \x01(\r\x12\x13\n\x0bimage_width\x18+ \x01(\r\x12\x14\n\x0cimage_height\x18, \x01(\r\x12\x11\n\timage_url\x18- \x01(\t\x12\x13\n\x0bspoiler_tag\x18. \x01(\x08\x12\x12\n\nshortcutid\x18/ \x01(\r\x12\x14\n\x0cshortcutname\x18\x30 \x01(\t\x12\x14\n\x0cnum_children\x18\x31 \x01(\r\x12\x13\n\x0bnum_reports\x18\x32 \x01(\r\x12/\n\x08previews\x18\x33 \x03(\x0b\x32\x1d.PublishedFileDetails.Preview\x12\'\n\x04tags\x18\x34 \x03(\x0b\x32\x19.PublishedFileDetails.Tag\x12-\n\x08\x63hildren\x18\x35 \x03(\x0b\x32\x1b.PublishedFileDetails.Child\x12+\n\x06kvtags\x18\x36 \x03(\x0b\x32\x1b.PublishedFileDetails.KVTag\x12\x31\n\tvote_data\x18\x37 \x01(\x0b\x32\x1e.PublishedFileDetails.VoteData\x12r\n\x0ftime_subscribed\x18\x38 \x01(\rBY\x82\xb5\x18UOnly valid in PublishedFile.GetUserFiles and not normal PublishedFile.GetDetail calls\x1a%\n\x03Tag\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x11\n\tadminonly\x18\x02 \x01(\x08\x1at\n\x07Preview\x12\x11\n\tpreviewid\x18\x01 \x01(\x04\x12\x11\n\tsortorder\x18\x02 \x01(\r\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\r\x12\x10\n\x08\x66ilename\x18\x05 \x01(\t\x12\x16\n\x0eyoutubevideoid\x18\x06 \x01(\t\x1a\x46\n\x05\x43hild\x12\x17\n\x0fpublishedfileid\x18\x01 \x01(\x04\x12\x11\n\tsortorder\x18\x02 \x01(\r\x12\x11\n\tfile_type\x18\x03 \x01(\r\x1a#\n\x05KVTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a?\n\x08VoteData\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x10\n\x08votes_up\x18\x02 \x01(\r\x12\x12\n\nvotes_down\x18\x03 \x01(\r\"Y\n\"CPublishedFile_GetDetails_Response\x12\x33\n\x14publishedfiledetails\x18\x01 \x03(\x0b\x32\x15.PublishedFileDetails\"\xbb\x06\n#CPublishedFile_GetUserFiles_Request\x12;\n\x05\x61ppid\x18\x01 \x01(\rB,\x82\xb5\x18(App Id to retrieve published files from.\x12:\n\x04page\x18\x03 \x01(\r:\x01\x31\x42)\x82\xb5\x18%(Optional) Starting page for results.\x12P\n\nnumperpage\x18\x04 \x01(\r:\x01\x31\x42\x39\x82\xb5\x18\x35(Optional) The number of results, per page to return.\x12Y\n\nsortmethod\x18\x06 \x01(\t:\x0blastupdatedB8\x82\xb5\x18\x34(Optional) Sorting method to use on returned values.\x12i\n\ttotalonly\x18\x07 \x01(\x08\x42V\x82\xb5\x18R(Optional) If true, only return the total number of files that satisfy this query.\x12;\n\x07privacy\x18\t \x01(\rB*\x82\xb5\x18&(optional) Filter by privacy settings.\x12n\n\x08ids_only\x18\n \x01(\x08\x42\\\x82\xb5\x18X(Optional) If true, only return the published file ids of files that satisfy this query.\x12h\n\x0crequiredtags\x18\x0b \x03(\tBR\x82\xb5\x18N(Optional) Tags that must be present on a published file to satisfy the query.\x12l\n\x0c\x65xcludedtags\x18\x0c \x03(\tBV\x82\xb5\x18R(Optional) Tags that must NOT be present on a published file to satisfy the query.\"\x80\x02\n$CPublishedFile_GetUserFiles_Response\x12\r\n\x05total\x18\x01 \x01(\r\x12\x12\n\nstartindex\x18\x02 \x01(\r\x12\x33\n\x14publishedfiledetails\x18\x03 \x03(\x0b\x32\x15.PublishedFileDetails\x12\x37\n\x04\x61pps\x18\x04 \x03(\x0b\x32).CPublishedFile_GetUserFiles_Response.App\x1aG\n\x03\x41pp\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nshortcutid\x18\x03 \x01(\r\x12\x0f\n\x07private\x18\x04 \x01(\x08\"\xcf\x04\n\x1d\x43PublishedFile_Update_Request\x12\x39\n\x05\x61ppid\x18\x01 \x01(\rB*\x82\xb5\x18&App Id this published file belongs to.\x12L\n\x0fpublishedfileid\x18\x02 \x01(\x06\x42\x33\x82\xb5\x18/Published file id of the file we\'d like update.\x12:\n\x05title\x18\x03 \x01(\tB+\x82\xb5\x18\'(Optional) Title of the published file.\x12K\n\x10\x66ile_description\x18\x04 \x01(\tB1\x82\xb5\x18-(Optional) Description of the published file.\x12\x44\n\nvisibility\x18\x05 \x01(\rB0\x82\xb5\x18,(Optional) Visibility of the published file.\x12@\n\x04tags\x18\x06 \x03(\tB2\x82\xb5\x18.(Optional) Set of tags for the published file.\x12\x41\n\x08\x66ilename\x18\x07 \x01(\tB/\x82\xb5\x18+(Optional) Filename for the published file.\x12Q\n\x10preview_filename\x18\x08 \x01(\tB7\x82\xb5\x18\x33(Optional) Preview filename for the published file.\" \n\x1e\x43PublishedFile_Update_Response\"\xbb\x04\n)CPublishedFile_RefreshVotingQueue_Request\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x42\n\x12matching_file_type\x18\x02 \x01(\rB&\x82\xb5\x18\"EPublishedFileInfoMatchingFileType\x12l\n\x04tags\x18\x03 \x03(\tB^\x82\xb5\x18ZInclude files that have all the tags or any of the tags if match_all_tags is set to false.\x12\x95\x01\n\x0ematch_all_tags\x18\x04 \x01(\x08:\x04trueBw\x82\xb5\x18sIf true, then files must have all the tags specified.  If false, then must have at least one of the tags specified.\x12I\n\rexcluded_tags\x18\x05 \x03(\tB2\x82\xb5\x18.Exclude any files that have any of these tags.\x12j\n\x12\x64\x65sired_queue_size\x18\x06 \x01(\rBN\x82\xb5\x18JDesired number of items in the voting queue.  May be clamped by the server\",\n*CPublishedFile_RefreshVotingQueue_Response2\x83\x08\n\rPublishedFile\x12\x81\x01\n\tSubscribe\x12!.CPublishedFile_Subscribe_Request\x1a\".CPublishedFile_Subscribe_Response\"-\x82\xb5\x18)Subscribes the user to the published file\x12\x8b\x01\n\x0bUnsubscribe\x12#.CPublishedFile_Unsubscribe_Request\x1a$.CPublishedFile_Unsubscribe_Response\"1\x82\xb5\x18-Unsubscribes the user from the published file\x12\x80\x01\n\x07Publish\x12\x1f.CPublishedFile_Publish_Request\x1a .CPublishedFile_Publish_Response\"2\x82\xb5\x18.Publishes a clouded user file to the Workshop.\x12\x90\x01\n\nGetDetails\x12\".CPublishedFile_GetDetails_Request\x1a#.CPublishedFile_GetDetails_Response\"9\x82\xb5\x18\x35Retrieves information about a set of published files.\x12\x85\x01\n\x0cGetUserFiles\x12$.CPublishedFile_GetUserFiles_Request\x1a%.CPublishedFile_GetUserFiles_Response\"(\x82\xb5\x18$Retrieves files published by a user.\x12z\n\x06Update\x12\x1e.CPublishedFile_Update_Request\x1a\x1f.CPublishedFile_Update_Response\"/\x82\xb5\x18+Updates information about a published file.\x12\x98\x01\n\x12RefreshVotingQueue\x12*.CPublishedFile_RefreshVotingQueue_Request\x1a+.CPublishedFile_RefreshVotingQueue_Response\")\x82\xb5\x18%Refresh the voting queue for the user\x1a+\x82\xb5\x18\'A service to access published file data')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_publishedfile.steamworkssdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030)App Id this file is being published FROM.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['consumer_appid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['consumer_appid']._serialized_options = b'\202\265\030\'App Id this file is being published TO.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['cloudfilename']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['cloudfilename']._serialized_options = b'\202\265\0300Name of the file to publish in the user\'s cloud.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['preview_cloudfilename']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['preview_cloudfilename']._serialized_options = b'\202\265\0308Name of the file to use as the published file\'s preview.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['title']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['title']._serialized_options = b'\202\265\030\"Text title for the published file.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['file_description']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['file_description']._serialized_options = b'\202\265\030(Text description for the published file.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['file_type']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['file_type']._serialized_options = b'\202\265\0305(EWorkshopFileType) Type of Workshop file to publish.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['consumer_shortcut_name']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['consumer_shortcut_name']._serialized_options = b'\202\265\030%Shortcut name for the published file.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['youtube_username']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['youtube_username']._serialized_options = b'\202\265\030+(Optional) User\'s YouTube account username.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['youtube_videoid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['youtube_videoid']._serialized_options = b'\202\265\030?(Optional) Video Id of a YouTube video for this published file.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['visibility']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['visibility']._serialized_options = b'\202\265\030i(ERemoteStoragePublishedFileVisibility) Visibility of the published file (private, friends, public, etc.)'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['redirect_uri']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['redirect_uri']._serialized_options = b'\202\265\030Q(Optional) If supplied, the resulting published file\'s Id is appended to the URI.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['tags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['tags']._serialized_options = b'\202\265\0302Array of text tags to apply to the published file.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['collection_type']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['collection_type']._serialized_options = b'\202\265\030<(Optional) Type of collection the published file represents.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['game_type']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['game_type']._serialized_options = b'\202\265\0306(Optional) Type of game the published file represents.'
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['url']._loaded_options = None
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST'].fields_by_name['url']._serialized_options = b'\202\265\030J(Optional) If this represents a game, this is the URL to that game\'s page.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['publishedfileids']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['publishedfileids']._serialized_options = b'\202\265\0302Set of published file Ids to retrieve details for.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includetags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includetags']._serialized_options = b'\202\265\0308If true, return tag information in the returned details.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includeadditionalpreviews']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includeadditionalpreviews']._serialized_options = b'\202\265\030<If true, return preview information in the returned details.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includechildren']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includechildren']._serialized_options = b'\202\265\0301If true, return children in the returned details.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includekvtags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includekvtags']._serialized_options = b'\202\265\0307If true, return key value tags in the returned details.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includevotes']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['includevotes']._serialized_options = b'\202\265\0302If true, return vote data in the returned details.'
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['short_description']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST'].fields_by_name['short_description']._serialized_options = b'\202\265\030DIf true, return a short description instead of the full description.'
  _globals['_PUBLISHEDFILEDETAILS'].fields_by_name['time_subscribed']._loaded_options = None
  _globals['_PUBLISHEDFILEDETAILS'].fields_by_name['time_subscribed']._serialized_options = b'\202\265\030UOnly valid in PublishedFile.GetUserFiles and not normal PublishedFile.GetDetail calls'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030(App Id to retrieve published files from.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['page']._serialized_options = b'\202\265\030%(Optional) Starting page for results.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['numperpage']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['numperpage']._serialized_options = b'\202\265\0305(Optional) The number of results, per page to return.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['sortmethod']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['sortmethod']._serialized_options = b'\202\265\0304(Optional) Sorting method to use on returned values.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['totalonly']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['totalonly']._serialized_options = b'\202\265\030R(Optional) If true, only return the total number of files that satisfy this query.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['privacy']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['privacy']._serialized_options = b'\202\265\030&(optional) Filter by privacy settings.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['ids_only']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['ids_only']._serialized_options = b'\202\265\030X(Optional) If true, only return the published file ids of files that satisfy this query.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['requiredtags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['requiredtags']._serialized_options = b'\202\265\030N(Optional) Tags that must be present on a published file to satisfy the query.'
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['excludedtags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST'].fields_by_name['excludedtags']._serialized_options = b'\202\265\030R(Optional) Tags that must NOT be present on a published file to satisfy the query.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['appid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['appid']._serialized_options = b'\202\265\030&App Id this published file belongs to.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['publishedfileid']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['publishedfileid']._serialized_options = b'\202\265\030/Published file id of the file we\'d like update.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['title']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['title']._serialized_options = b'\202\265\030\'(Optional) Title of the published file.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['file_description']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['file_description']._serialized_options = b'\202\265\030-(Optional) Description of the published file.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['visibility']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['visibility']._serialized_options = b'\202\265\030,(Optional) Visibility of the published file.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['tags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['tags']._serialized_options = b'\202\265\030.(Optional) Set of tags for the published file.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['filename']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['filename']._serialized_options = b'\202\265\030+(Optional) Filename for the published file.'
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['preview_filename']._loaded_options = None
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST'].fields_by_name['preview_filename']._serialized_options = b'\202\265\0303(Optional) Preview filename for the published file.'
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['matching_file_type']._loaded_options = None
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['matching_file_type']._serialized_options = b'\202\265\030\"EPublishedFileInfoMatchingFileType'
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['tags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['tags']._serialized_options = b'\202\265\030ZInclude files that have all the tags or any of the tags if match_all_tags is set to false.'
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['match_all_tags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['match_all_tags']._serialized_options = b'\202\265\030sIf true, then files must have all the tags specified.  If false, then must have at least one of the tags specified.'
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['excluded_tags']._loaded_options = None
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['excluded_tags']._serialized_options = b'\202\265\030.Exclude any files that have any of these tags.'
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['desired_queue_size']._loaded_options = None
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST'].fields_by_name['desired_queue_size']._serialized_options = b'\202\265\030JDesired number of items in the voting queue.  May be clamped by the server'
  _globals['_PUBLISHEDFILE']._loaded_options = None
  _globals['_PUBLISHEDFILE']._serialized_options = b'\202\265\030\'A service to access published file data'
  _globals['_PUBLISHEDFILE'].methods_by_name['Subscribe']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['Subscribe']._serialized_options = b'\202\265\030)Subscribes the user to the published file'
  _globals['_PUBLISHEDFILE'].methods_by_name['Unsubscribe']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['Unsubscribe']._serialized_options = b'\202\265\030-Unsubscribes the user from the published file'
  _globals['_PUBLISHEDFILE'].methods_by_name['Publish']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['Publish']._serialized_options = b'\202\265\030.Publishes a clouded user file to the Workshop.'
  _globals['_PUBLISHEDFILE'].methods_by_name['GetDetails']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['GetDetails']._serialized_options = b'\202\265\0305Retrieves information about a set of published files.'
  _globals['_PUBLISHEDFILE'].methods_by_name['GetUserFiles']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['GetUserFiles']._serialized_options = b'\202\265\030$Retrieves files published by a user.'
  _globals['_PUBLISHEDFILE'].methods_by_name['Update']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['Update']._serialized_options = b'\202\265\030+Updates information about a published file.'
  _globals['_PUBLISHEDFILE'].methods_by_name['RefreshVotingQueue']._loaded_options = None
  _globals['_PUBLISHEDFILE'].methods_by_name['RefreshVotingQueue']._serialized_options = b'\202\265\030%Refresh the voting queue for the user'
  _globals['_CPUBLISHEDFILE_SUBSCRIBE_REQUEST']._serialized_start=99
  _globals['_CPUBLISHEDFILE_SUBSCRIBE_REQUEST']._serialized_end=215
  _globals['_CPUBLISHEDFILE_SUBSCRIBE_RESPONSE']._serialized_start=217
  _globals['_CPUBLISHEDFILE_SUBSCRIBE_RESPONSE']._serialized_end=252
  _globals['_CPUBLISHEDFILE_UNSUBSCRIBE_REQUEST']._serialized_start=254
  _globals['_CPUBLISHEDFILE_UNSUBSCRIBE_REQUEST']._serialized_end=372
  _globals['_CPUBLISHEDFILE_UNSUBSCRIBE_RESPONSE']._serialized_start=374
  _globals['_CPUBLISHEDFILE_UNSUBSCRIBE_RESPONSE']._serialized_end=411
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST']._serialized_start=414
  _globals['_CPUBLISHEDFILE_PUBLISH_REQUEST']._serialized_end=1770
  _globals['_CPUBLISHEDFILE_PUBLISH_RESPONSE']._serialized_start=1772
  _globals['_CPUBLISHEDFILE_PUBLISH_RESPONSE']._serialized_end=1852
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST']._serialized_start=1855
  _globals['_CPUBLISHEDFILE_GETDETAILS_REQUEST']._serialized_end=2499
  _globals['_PUBLISHEDFILEDETAILS']._serialized_start=2502
  _globals['_PUBLISHEDFILEDETAILS']._serialized_end=4303
  _globals['_PUBLISHEDFILEDETAILS_TAG']._serialized_start=3974
  _globals['_PUBLISHEDFILEDETAILS_TAG']._serialized_end=4011
  _globals['_PUBLISHEDFILEDETAILS_PREVIEW']._serialized_start=4013
  _globals['_PUBLISHEDFILEDETAILS_PREVIEW']._serialized_end=4129
  _globals['_PUBLISHEDFILEDETAILS_CHILD']._serialized_start=4131
  _globals['_PUBLISHEDFILEDETAILS_CHILD']._serialized_end=4201
  _globals['_PUBLISHEDFILEDETAILS_KVTAG']._serialized_start=4203
  _globals['_PUBLISHEDFILEDETAILS_KVTAG']._serialized_end=4238
  _globals['_PUBLISHEDFILEDETAILS_VOTEDATA']._serialized_start=4240
  _globals['_PUBLISHEDFILEDETAILS_VOTEDATA']._serialized_end=4303
  _globals['_CPUBLISHEDFILE_GETDETAILS_RESPONSE']._serialized_start=4305
  _globals['_CPUBLISHEDFILE_GETDETAILS_RESPONSE']._serialized_end=4394
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST']._serialized_start=4397
  _globals['_CPUBLISHEDFILE_GETUSERFILES_REQUEST']._serialized_end=5224
  _globals['_CPUBLISHEDFILE_GETUSERFILES_RESPONSE']._serialized_start=5227
  _globals['_CPUBLISHEDFILE_GETUSERFILES_RESPONSE']._serialized_end=5483
  _globals['_CPUBLISHEDFILE_GETUSERFILES_RESPONSE_APP']._serialized_start=5412
  _globals['_CPUBLISHEDFILE_GETUSERFILES_RESPONSE_APP']._serialized_end=5483
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST']._serialized_start=5486
  _globals['_CPUBLISHEDFILE_UPDATE_REQUEST']._serialized_end=6077
  _globals['_CPUBLISHEDFILE_UPDATE_RESPONSE']._serialized_start=6079
  _globals['_CPUBLISHEDFILE_UPDATE_RESPONSE']._serialized_end=6111
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST']._serialized_start=6114
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_REQUEST']._serialized_end=6685
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_RESPONSE']._serialized_start=6687
  _globals['_CPUBLISHEDFILE_REFRESHVOTINGQUEUE_RESPONSE']._serialized_end=6731
  _globals['_PUBLISHEDFILE']._serialized_start=6734
  _globals['_PUBLISHEDFILE']._serialized_end=7761
# @@protoc_insertion_point(module_scope)
