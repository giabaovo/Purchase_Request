from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class PurchaseInherit(models.Model):
    _inherit = 'purchase.order'
    name = fields.Char(string="Request Reference")

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Purchase Request'
    _order = "id desc"


    name = fields.Char(string="Request Reference", required=True, track_visibility="always")
    description = fields.Text(string="Description", track_visibility="always")
    requested_by = fields.Char(string="Requested by", required=True, track_visibility="always")
    date_start = fields.Date(string="Creation date", default=fields.Date.context_today)
    name_seq = fields.Char(string="Purchase Request", required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    pr_lines = fields.One2many('purchase.request.lines', 'pr_id', string='Purchase Request Line')
    state = fields.Selection([
        ('draft','Draft'),
        ('tobeapprove', 'To Be Approve'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done'),
    ], string="Status", readonly=True, default="draft")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('purchase.request') or _('New')
            result = super(PurchaseRequest, self).create(vals)
            return result

    def action_confirm(self):
        for rec in self:
            rec.state = 'tobeapprove'


class PurchaseRequestLines(models.Model):
    _name = 'purchase.request.lines'
    _description = 'Purchase Request Lines'

    product_id = fields.Many2one('product.product',string='Product')
    product_qty = fields.Integer(string='Quantity')
    pr_id = fields.Many2one('purchase.request', string='Purchase Request ID')







