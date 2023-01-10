from rest_framework import routers

from ad_unit import views as ad_unit_views
from line_item import views as line_item_views
from creative import views as creative_views

router = routers.DefaultRouter()
router.register(r'ad_unit', ad_unit_views.AdUnitViewset)
router.register(r'creative', creative_views.CreativeViewset)
router.register(r'line_item', line_item_views.LineItemsViewset)
