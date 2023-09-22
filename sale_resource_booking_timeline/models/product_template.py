from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    available_booking_interval_ids = fields.Many2many(
        comodel_name="resource.booking",
        relation="available_booking_interval_for_product_template_rel",
        string="Intervals available for booking",
    )
