import bz2
import sys
import dota_crypto
from google.protobuf.json_format import MessageToJson

sys.path.append('protobuf')
import protobuf.dota_match_metadata_pb2


key = 1812757917  # private_metadata_key
with open('8010031109_796279280.meta', 'rb') as f:  # unzipped protobuf
    binary = f.read()
match_file = protobuf.dota_match_metadata_pb2.CDOTAMatchMetadataFile()
match_file.ParseFromString(binary)

decrypted = dota_crypto.decrypt(key=key, private_metadata=match_file.private_metadata)
unpacked = bz2.decompress(decrypted[4:])  # first 4 bytes are ignored

private_metadata = protobuf.dota_match_metadata_pb2.CDOTAMatchPrivateMetadata()
private_metadata.ParseFromString(unpacked)
print(MessageToJson(private_metadata))
