from tap_zapier.streams.abstracts import FullTableStream

class Apps(FullTableStream):
    tap_stream_id = "apps"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "v2/apps"

