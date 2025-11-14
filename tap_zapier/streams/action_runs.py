from tap_zapier.streams.abstracts import FullTableStream

class ActionRuns(FullTableStream):
    tap_stream_id = "action_runs"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "v2/action-runs/{id}"
    parent = "actions"

