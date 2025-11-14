from tap_zapier.streams.abstracts import FullTableStream

class Categories(FullTableStream):
    tap_stream_id = "categories"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "objects"
    path = "v1/categories"

