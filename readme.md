## dota_crypto

Implementation of the decryption algorithm for CDOTAMatchPrivateMetadata — extended match statistics data in Dota 2.


### Overview

Among other features, Dota Plus subscription includes access to extended match stats.
This data is always stored in protobuf, but it is encrypted.

The encryption uses a simple homegrown old-school cryptosystem. To be honest, it's nice to see something like this —
such approaches are quite rare nowadays. Although this topic has been discussed several times, 
no one has yet looked into it in detail.


### Technical Details

To decrypt the data you need:
1. Get the protobuf file
2. Extract the private key

This data is contained in the GSMatchDetailsRequest response from the Game Coordinator.

From GCMatchDetailsResponse, you need to extract `private_metadata_key` (private key) and several other fields
to construct the protobuf URL. The downloaded file needs to be decompressed.
`http://replay{cluster}.valve.net/570/{match_id}_{replay_salt}.meta.bz2`

I won't go into the algorithm details, just mention that a 32-bit key is used to generate a keystream,
which is then used to select values from the `DECRYPT_TABLE`. `DECRYPT_TABLE` is generated dynamically, 
but using hardcoded values. These values could change in future client updates, but so far they haven't.


The `protobuf` folder contains compiled schemas. Original schemas are available in [SteamDatabase/GameTracking-Dota2](https://github.com/SteamDatabase/GameTracking-Dota2/tree/master).

Game traffic can be viewed using [NetHook2](https://github.com/SteamRE/SteamKit/tree/master/Resources/NetHook2) + NetHookAnalyzer2.


### Acknowledgments
Thanks to myself for reverse and [ezhevita](https://github.com/ezhevita) for refactoring the code.
