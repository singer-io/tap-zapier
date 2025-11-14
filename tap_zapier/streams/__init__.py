from tap_zapier.streams.apps import Apps
from tap_zapier.streams.actions import Actions
from tap_zapier.streams.action_runs import ActionRuns
from tap_zapier.streams.categories import Categories
from tap_zapier.streams.promotions import Promotions
from tap_zapier.streams.zap_templates import ZapTemplates
from tap_zapier.streams.zaps import Zaps

STREAMS = {
    "apps": Apps,
    "actions": Actions,
    "action_runs": ActionRuns,
    "categories": Categories,
    "promotions": Promotions,
    "zap_templates": ZapTemplates,
    "zaps": Zaps,
}

