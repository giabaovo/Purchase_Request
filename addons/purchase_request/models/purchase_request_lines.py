from odoo import _, api, fields, models

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Purchase Request Line'
    _order = "id desc"

    name_id = fields.Many2one('purchase.request',string="Request Reference", required=True, track_visibility="always")
    description = fields.Text(string="Description", track_visibility="always", related='name_id.description')
    requested_by = fields.Char(string="Requested by", required=True, track_visibility="always", related='name_id.requested_by')
    date_start = fields.Date(string="Creation date", default=fields.Date.context_today, related='name_id.date_start')
    name_seq = fields.Char(string="Purchase Request", required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('purchase.request.line') or _('New')
            result = super(PurchaseRequestLine, self).create(vals)
            return result