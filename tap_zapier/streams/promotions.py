from tap_zapier.streams.abstracts import FullTableStream

class Promotions(FullTableStream):
    tap_stream_id = "promotions"
    key_properties = ["promotion_id"]
    replication_method = "FULL_TABLE"
    path = "v2/promotions/{enrollment_id}"

