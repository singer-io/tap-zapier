from tap_zapier.streams.abstracts import FullTableStream

class Actions(FullTableStream):
    tap_stream_id = "actions"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "v2/actions"
    parent = "apps"

