from odoo import api, fields, models


class ResourceBooking(models.Model):
    _inherit = "resource.booking"

    product_template_ids = fields.Many2many(
        comodel_name="product.template",
        relation="product_template_resource_booking_rel",
        string="Show in Timeline",
    )

    # duration_in_timeline = fields.Float(
    #     string="Duration in timeline",
    #     default=0.5,  # 30 minutes
    # )

    # @api.onchange("duration_in_timeline")
    # def _onchange_duration_in_timeline(self):
    #     self.duration = self.duration_in_timeline
