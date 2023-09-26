from api.v1.forms import ApiAddressForm
from api.v1.mixins import ApiListViewMixin, ApiFilteringMixin, ApiDetailsMixin
from bookshop.models import Address


class ApiAddressesListView(ApiListViewMixin):
  model = Address
  form = ApiAddressForm


class ApiAddressesWhereView(ApiFilteringMixin):
  model = Address
  form = ApiAddressForm


class ApiAddressDetailsView(ApiDetailsMixin):
  model = Address
  form = ApiAddressForm
