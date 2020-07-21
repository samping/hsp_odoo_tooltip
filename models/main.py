# -*- coding: utf-8 -*-
from odoo import models, api, fields
import collections
import datetime
import dateutil
import fnmatch
import functools
import itertools
import io
import logging
import operator
import pytz
import re
import logging
_logger = logging.getLogger(__name__)

class BaseModel(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        """ fields_get([fields][, attributes])

        Return the definition of each field.

        The returned value is a dictionary (indexed by field name) of
        dictionaries. The _inherits'd fields are included. The string, help,
        and selection (if present) attributes are translated.

        :param allfields: list of fields to document, all if empty or not provided
        :param attributes: list of description attributes to return for each field, all if empty or not provided
        """
        has_access = functools.partial(self.check_access_rights, raise_exception=False)
        readonly = not (has_access('write') or has_access('create'))

        res = {}
        for fname, field in self._fields.items():
            if allfields and fname not in allfields:
                continue
            if field.groups and not self.env.su and not self.user_has_groups(field.groups):
                continue

            description = field.get_description(self.env)
            # _logger.info(field._modules)
            tem = ''
            for module in field._modules:
                if tem == '':
                    tem = module
                else :
                    tem = tem + ',' +module
            description['modules'] = tem
            if readonly:
                description['readonly'] = True
                description['states'] = {}
            if attributes:
                description = {key: val
                               for key, val in description.items()
                               if key in attributes}
            res[fname] = description

        return res

