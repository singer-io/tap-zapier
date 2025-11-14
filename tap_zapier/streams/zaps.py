from tap_zapier.streams.abstracts import IncrementalStream

class Zaps(IncrementalStream):
    tap_stream_id = "zaps"
    key_properties = ["id"]
    replication_method = "INCREMENTAL"
    replication_keys = ["updated_at"]
    data_key = "data"
    path = "v2/zaps"

