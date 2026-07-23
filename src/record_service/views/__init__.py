"""View catalogue.

Each view subclasses :class:`~record_service.views.base.View` and is
registered in :data:`REGISTRY` under its CLI slug.
"""

from .active_view import ActiveView
from .base import View
from .region_view import RegionView
from .site_view import SiteView
from .tagged_view import TaggedView

REGISTRY: dict[str, type[View]] = {
    "region-north": RegionView,
    "site": SiteView,
    "tagged": TaggedView,
    "active": ActiveView,
}

__all__ = [
    "View",
    "REGISTRY",
    "RegionView",
    "SiteView",
    "TaggedView",
    "ActiveView",
]
