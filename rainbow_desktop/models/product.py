# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_vault_product = fields.Boolean(copy=False)
    vault_server = fields.Char(
        string='Vault Server',
        copy=False,
    )
    vault_master_id = fields.Integer(
        string='Vault Master Id',
        copy=False,
    )
    vault_internal_id = fields.Integer(
        string='Vault Id',
        copy=False,
    )
    vault_last_update = fields.Datetime(
        string='Last update on Vault',
        copy=False,
    )
    vault_revision = fields.Char(
        string='Vault Revision',
        copy=False,
    )
    is_old_revision = fields.Boolean(string="Is old revision?", copy=False)
    vault_web_link = fields.Char(
        string="Vault Web link",
    )
    vault_desktop_link = fields.Char(
        string="Vault Desktop link",
    )
