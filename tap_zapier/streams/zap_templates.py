from tap_zapier.streams.abstracts import FullTableStream

class ZapTemplates(FullTableStream):
    tap_stream_id = "zap_templates"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "steps"
    path = "v1/zap-templates"

