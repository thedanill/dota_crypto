# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: te.proto
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
    'te.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import networkbasetypes_pb2 as networkbasetypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08te.proto\x1a\x16networkbasetypes.proto\"I\n\x13\x43MsgTEArmorRicochet\x12\x18\n\x03pos\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x03\x64ir\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\"\xe1\x01\n\x0e\x43MsgTEBaseBeam\x12\x12\n\nmodelindex\x18\x01 \x01(\x06\x12\x11\n\thaloindex\x18\x02 \x01(\x06\x12\x12\n\nstartframe\x18\x03 \x01(\r\x12\x11\n\tframerate\x18\x04 \x01(\r\x12\x0c\n\x04life\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x02\x12\x10\n\x08\x65ndwidth\x18\x07 \x01(\x02\x12\x12\n\nfadelength\x18\x08 \x01(\r\x12\x11\n\tamplitude\x18\t \x01(\x02\x12\r\n\x05\x63olor\x18\n \x01(\x07\x12\r\n\x05speed\x18\x0b \x01(\r\x12\r\n\x05\x66lags\x18\x0c \x01(\r\"\x91\x01\n\x12\x43MsgTEBeamEntPoint\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CMsgTEBaseBeam\x12\x13\n\x0bstartentity\x18\x02 \x01(\r\x12\x11\n\tendentity\x18\x03 \x01(\r\x12\x1a\n\x05start\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x03\x65nd\x18\x05 \x01(\x0b\x32\x0b.CMsgVector\"W\n\x0e\x43MsgTEBeamEnts\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CMsgTEBaseBeam\x12\x13\n\x0bstartentity\x18\x02 \x01(\r\x12\x11\n\tendentity\x18\x03 \x01(\r\"g\n\x10\x43MsgTEBeamPoints\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CMsgTEBaseBeam\x12\x1a\n\x05start\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\"W\n\x0e\x43MsgTEBeamRing\x12\x1d\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x0f.CMsgTEBaseBeam\x12\x13\n\x0bstartentity\x18\x02 \x01(\r\x12\x11\n\tendentity\x18\x03 \x01(\r\"\x89\x01\n\x0e\x43MsgTEBSPDecal\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06normal\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05saxis\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x12\n\x06\x65ntity\x18\x04 \x01(\x05:\x02-1\x12\r\n\x05index\x18\x05 \x01(\r\"s\n\rCMsgTEBubbles\x12\x19\n\x04mins\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x19\n\x04maxs\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x0e\n\x06height\x18\x03 \x01(\x02\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x12\r\n\x05speed\x18\x05 \x01(\x02\"w\n\x11\x43MsgTEBubbleTrail\x12\x19\n\x04mins\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x19\n\x04maxs\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x0e\n\x06waterz\x18\x03 \x01(\x02\x12\r\n\x05\x63ount\x18\x04 \x01(\r\x12\r\n\x05speed\x18\x05 \x01(\x02\"y\n\x0b\x43MsgTEDecal\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05start\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x12\n\x06\x65ntity\x18\x03 \x01(\x05:\x02-1\x12\x0e\n\x06hitbox\x18\x04 \x01(\r\x12\r\n\x05index\x18\x05 \x01(\r\"\xb1\x03\n\x0e\x43MsgEffectData\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05start\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06normal\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x61ngles\x18\x04 \x01(\x0b\x32\x0b.CMsgQAngle\x12\x18\n\x06\x65ntity\x18\x05 \x01(\x07:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\x1d\n\x0botherentity\x18\x06 \x01(\x07:\x08\x31\x36\x37\x37\x37\x32\x31\x35\x12\r\n\x05scale\x18\x07 \x01(\x02\x12\x11\n\tmagnitude\x18\x08 \x01(\x02\x12\x0e\n\x06radius\x18\t \x01(\x02\x12\x13\n\x0bsurfaceprop\x18\n \x01(\x07\x12\x13\n\x0b\x65\x66\x66\x65\x63tindex\x18\x0b \x01(\x06\x12\x12\n\ndamagetype\x18\x0c \x01(\r\x12\x10\n\x08material\x18\r \x01(\r\x12\x0e\n\x06hitbox\x18\x0e \x01(\r\x12\r\n\x05\x63olor\x18\x0f \x01(\r\x12\r\n\x05\x66lags\x18\x10 \x01(\r\x12\x17\n\x0f\x61ttachmentindex\x18\x11 \x01(\x05\x12\x12\n\neffectname\x18\x12 \x01(\r\x12\x16\n\x0e\x61ttachmentname\x18\x13 \x01(\r\";\n\x14\x43MsgTEEffectDispatch\x12#\n\neffectdata\x18\x01 \x01(\x0b\x32\x0f.CMsgEffectData\"[\n\x12\x43MsgTEEnergySplash\x12\x18\n\x03pos\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x18\n\x03\x64ir\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x11\n\texplosive\x18\x03 \x01(\x08\"B\n\nCMsgTEFizz\x12\x12\n\x06\x65ntity\x18\x01 \x01(\x05:\x02-1\x12\x0f\n\x07\x64\x65nsity\x18\x02 \x01(\r\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x05\"\xf9\x01\n\x14\x43MsgTEShatterSurface\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x61ngles\x18\x02 \x01(\x0b\x32\x0b.CMsgQAngle\x12\x1a\n\x05\x66orce\x18\x03 \x01(\x0b\x32\x0b.CMsgVector\x12\x1d\n\x08\x66orcepos\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\x12\r\n\x05width\x18\x05 \x01(\x02\x12\x0e\n\x06height\x18\x06 \x01(\x02\x12\x11\n\tshardsize\x18\x07 \x01(\x02\x12\x13\n\x0bsurfacetype\x18\x08 \x01(\r\x12\x12\n\nfrontcolor\x18\t \x01(\x07\x12\x11\n\tbackcolor\x18\n \x01(\x07\"`\n\x10\x43MsgTEGlowSprite\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\r\n\x05scale\x18\x02 \x01(\x02\x12\x0c\n\x04life\x18\x03 \x01(\x02\x12\x12\n\nbrightness\x18\x04 \x01(\r\"V\n\x0c\x43MsgTEImpact\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06normal\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x0c\n\x04type\x18\x03 \x01(\r\"j\n\x11\x43MsgTEMuzzleFlash\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x61ngles\x18\x02 \x01(\x0b\x32\x0b.CMsgQAngle\x12\r\n\x05scale\x18\x03 \x01(\x02\x12\x0c\n\x04type\x18\x04 \x01(\r\"o\n\x11\x43MsgTEBloodStream\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1e\n\tdirection\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\r\n\x05\x63olor\x18\x03 \x01(\x07\x12\x0e\n\x06\x61mount\x18\x04 \x01(\r\"\xd2\x02\n\x0f\x43MsgTEExplosion\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x11\n\tframerate\x18\x02 \x01(\r\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x1b\n\x06normal\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\x12\x14\n\x0cmaterialtype\x18\x05 \x01(\r\x12\x0e\n\x06radius\x18\x06 \x01(\r\x12\x11\n\tmagnitude\x18\x07 \x01(\r\x12\r\n\x05scale\x18\x08 \x01(\x02\x12\x17\n\x0f\x61\x66\x66\x65\x63t_ragdolls\x18\t \x01(\x08\x12\x13\n\x0b\x65\x66\x66\x65\x63t_name\x18\n \x01(\t\x12\x16\n\x0e\x65xplosion_type\x18\x0b \x01(\r\x12\x15\n\rcreate_debris\x18\x0c \x01(\x08\x12\"\n\rdebris_origin\x18\r \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x12\x64\x65\x62ris_surfaceprop\x18\x0e \x01(\x07\"f\n\nCMsgTEDust\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x0c\n\x04size\x18\x02 \x01(\x02\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x1e\n\tdirection\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\"B\n\x11\x43MsgTELargeFunnel\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x10\n\x08reversed\x18\x02 \x01(\r\"n\n\x0c\x43MsgTESparks\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x11\n\tmagnitude\x18\x02 \x01(\r\x12\x0e\n\x06length\x18\x03 \x01(\r\x12\x1e\n\tdirection\x18\x04 \x01(\x0b\x32\x0b.CMsgVector\"\xbc\x02\n\x11\x43MsgTEPhysicsProp\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1d\n\x08velocity\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x61ngles\x18\x03 \x01(\x0b\x32\x0b.CMsgQAngle\x12\x0c\n\x04skin\x18\x04 \x01(\x07\x12\r\n\x05\x66lags\x18\x05 \x01(\r\x12\x0f\n\x07\x65\x66\x66\x65\x63ts\x18\x06 \x01(\r\x12\r\n\x05\x63olor\x18\x07 \x01(\x07\x12\x12\n\nmodelindex\x18\x08 \x01(\x06\x12#\n\x1bunused_breakmodelsnottomake\x18\t \x01(\r\x12\r\n\x05scale\x18\n \x01(\x02\x12\x1b\n\x06\x64mgpos\x18\x0b \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x64mgdir\x18\x0c \x01(\x0b\x32\x0b.CMsgVector\x12\x0f\n\x07\x64mgtype\x18\r \x01(\x05\"X\n\x11\x43MsgTEPlayerDecal\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x12\n\x06player\x18\x02 \x01(\x05:\x02-1\x12\x12\n\x06\x65ntity\x18\x03 \x01(\x05:\x02-1\"q\n\x14\x43MsgTEProjectedDecal\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06\x61ngles\x18\x02 \x01(\x0b\x32\x0b.CMsgQAngle\x12\r\n\x05index\x18\x03 \x01(\r\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\"9\n\x0b\x43MsgTESmoke\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\r\n\x05scale\x18\x02 \x01(\x02\"[\n\x10\x43MsgTEWorldDecal\x12\x1b\n\x06origin\x18\x01 \x01(\x0b\x32\x0b.CMsgVector\x12\x1b\n\x06normal\x18\x02 \x01(\x0b\x32\x0b.CMsgVector\x12\r\n\x05index\x18\x03 \x01(\r*\xbd\x04\n\x0e\x45TEProtobufIds\x12\x18\n\x13TE_EffectDispatchId\x10\x90\x03\x12\x17\n\x12TE_ArmorRicochetId\x10\x91\x03\x12\x16\n\x11TE_BeamEntPointId\x10\x92\x03\x12\x12\n\rTE_BeamEntsId\x10\x93\x03\x12\x14\n\x0fTE_BeamPointsId\x10\x94\x03\x12\x12\n\rTE_BeamRingId\x10\x95\x03\x12\x12\n\rTE_BSPDecalId\x10\x97\x03\x12\x11\n\x0cTE_BubblesId\x10\x98\x03\x12\x15\n\x10TE_BubbleTrailId\x10\x99\x03\x12\x0f\n\nTE_DecalId\x10\x9a\x03\x12\x14\n\x0fTE_WorldDecalId\x10\x9b\x03\x12\x16\n\x11TE_EnergySplashId\x10\x9c\x03\x12\x0e\n\tTE_FizzId\x10\x9d\x03\x12\x18\n\x13TE_ShatterSurfaceId\x10\x9e\x03\x12\x14\n\x0fTE_GlowSpriteId\x10\x9f\x03\x12\x10\n\x0bTE_ImpactId\x10\xa0\x03\x12\x15\n\x10TE_MuzzleFlashId\x10\xa1\x03\x12\x15\n\x10TE_BloodStreamId\x10\xa2\x03\x12\x13\n\x0eTE_ExplosionId\x10\xa3\x03\x12\x0e\n\tTE_DustId\x10\xa4\x03\x12\x15\n\x10TE_LargeFunnelId\x10\xa5\x03\x12\x10\n\x0bTE_SparksId\x10\xa6\x03\x12\x15\n\x10TE_PhysicsPropId\x10\xa7\x03\x12\x15\n\x10TE_PlayerDecalId\x10\xa8\x03\x12\x18\n\x13TE_ProjectedDecalId\x10\xa9\x03\x12\x0f\n\nTE_SmokeId\x10\xaa\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'te_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ETEPROTOBUFIDS']._serialized_start=3890
  _globals['_ETEPROTOBUFIDS']._serialized_end=4463
  _globals['_CMSGTEARMORRICOCHET']._serialized_start=36
  _globals['_CMSGTEARMORRICOCHET']._serialized_end=109
  _globals['_CMSGTEBASEBEAM']._serialized_start=112
  _globals['_CMSGTEBASEBEAM']._serialized_end=337
  _globals['_CMSGTEBEAMENTPOINT']._serialized_start=340
  _globals['_CMSGTEBEAMENTPOINT']._serialized_end=485
  _globals['_CMSGTEBEAMENTS']._serialized_start=487
  _globals['_CMSGTEBEAMENTS']._serialized_end=574
  _globals['_CMSGTEBEAMPOINTS']._serialized_start=576
  _globals['_CMSGTEBEAMPOINTS']._serialized_end=679
  _globals['_CMSGTEBEAMRING']._serialized_start=681
  _globals['_CMSGTEBEAMRING']._serialized_end=768
  _globals['_CMSGTEBSPDECAL']._serialized_start=771
  _globals['_CMSGTEBSPDECAL']._serialized_end=908
  _globals['_CMSGTEBUBBLES']._serialized_start=910
  _globals['_CMSGTEBUBBLES']._serialized_end=1025
  _globals['_CMSGTEBUBBLETRAIL']._serialized_start=1027
  _globals['_CMSGTEBUBBLETRAIL']._serialized_end=1146
  _globals['_CMSGTEDECAL']._serialized_start=1148
  _globals['_CMSGTEDECAL']._serialized_end=1269
  _globals['_CMSGEFFECTDATA']._serialized_start=1272
  _globals['_CMSGEFFECTDATA']._serialized_end=1705
  _globals['_CMSGTEEFFECTDISPATCH']._serialized_start=1707
  _globals['_CMSGTEEFFECTDISPATCH']._serialized_end=1766
  _globals['_CMSGTEENERGYSPLASH']._serialized_start=1768
  _globals['_CMSGTEENERGYSPLASH']._serialized_end=1859
  _globals['_CMSGTEFIZZ']._serialized_start=1861
  _globals['_CMSGTEFIZZ']._serialized_end=1927
  _globals['_CMSGTESHATTERSURFACE']._serialized_start=1930
  _globals['_CMSGTESHATTERSURFACE']._serialized_end=2179
  _globals['_CMSGTEGLOWSPRITE']._serialized_start=2181
  _globals['_CMSGTEGLOWSPRITE']._serialized_end=2277
  _globals['_CMSGTEIMPACT']._serialized_start=2279
  _globals['_CMSGTEIMPACT']._serialized_end=2365
  _globals['_CMSGTEMUZZLEFLASH']._serialized_start=2367
  _globals['_CMSGTEMUZZLEFLASH']._serialized_end=2473
  _globals['_CMSGTEBLOODSTREAM']._serialized_start=2475
  _globals['_CMSGTEBLOODSTREAM']._serialized_end=2586
  _globals['_CMSGTEEXPLOSION']._serialized_start=2589
  _globals['_CMSGTEEXPLOSION']._serialized_end=2927
  _globals['_CMSGTEDUST']._serialized_start=2929
  _globals['_CMSGTEDUST']._serialized_end=3031
  _globals['_CMSGTELARGEFUNNEL']._serialized_start=3033
  _globals['_CMSGTELARGEFUNNEL']._serialized_end=3099
  _globals['_CMSGTESPARKS']._serialized_start=3101
  _globals['_CMSGTESPARKS']._serialized_end=3211
  _globals['_CMSGTEPHYSICSPROP']._serialized_start=3214
  _globals['_CMSGTEPHYSICSPROP']._serialized_end=3530
  _globals['_CMSGTEPLAYERDECAL']._serialized_start=3532
  _globals['_CMSGTEPLAYERDECAL']._serialized_end=3620
  _globals['_CMSGTEPROJECTEDDECAL']._serialized_start=3622
  _globals['_CMSGTEPROJECTEDDECAL']._serialized_end=3735
  _globals['_CMSGTESMOKE']._serialized_start=3737
  _globals['_CMSGTESMOKE']._serialized_end=3794
  _globals['_CMSGTEWORLDDECAL']._serialized_start=3796
  _globals['_CMSGTEWORLDDECAL']._serialized_end=3887
# @@protoc_insertion_point(module_scope)