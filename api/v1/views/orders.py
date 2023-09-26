from api.v1.forms import ApiOrderForm
from api.v1.mixins import ApiListViewMixin, ApiFilteringMixin, ApiDetailsMixin
from bookshop.models import Order


class ApiOrdersListView(ApiListViewMixin):
  """
  Views for list of customer orders
  """
  model = Order
  form = ApiOrderForm


class ApiOrdersWhereView(ApiFilteringMixin):
  model = Order
  form = ApiOrderForm


class ApiOrderDetailsView(ApiDetailsMixin):
  model = Order
  form = ApiOrderForm
