# -*- coding: utf-8 -*-

from shiba.accountingmanagement import AccountingManagement
from shiba.marketplacemanagement import MarketplaceManagement
from shiba.shibaconnection import ShibaConnection

from settings import LOGIN, TOKEN

connection = ShibaConnection(LOGIN, TOKEN, sandbox=True)

print AccountingManagement(connection).get_operations(u'').content
print MarketplaceManagement(connection).get_category_map().content
print MarketplaceManagement(connection).get_product_list().content
