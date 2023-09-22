import pytz
from datetime import timedelta

from odoo import api, fields, models


class ResourceBooking(models.Model):
    _inherit = "resource.booking"

    available_product_tmpl_ids = fields.Many2many(
        comodel_name="product.template",
        relation="available_booking_interval_for_product_template_rel",
        string="Products available for this interval",
    )

    # duration_in_timeline = fields.Float(
    #     string="Duration in timeline",
    #     default=0.5,  # 30 minutes
    # )

    # @api.onchange("duration_in_timeline")
    # def _onchange_duration_in_timeline(self):
    #     self.duration = self.duration_in_timeline

    def _get_available_slots(self, start_dt, end_dt):
        # If available times are registered on the product of the booking,
        # then restrict to these available times.
        result = super()._get_available_slots(start_dt, end_dt)
        restrict_to_these_available_times = self.product_id.timeline_booking_ids
        if restrict_to_these_available_times:
            for result_date, result_dts in result.items():
                new_dts = []
                for result_dt in result_dts:
                    start = result_dt.astimezone(pytz.utc).replace(tzinfo=None)
                    stop = start + timedelta(hours=self.duration)
                    for available in restrict_to_these_available_times:
                        if available.start <= start < available.stop and available.start < stop <= available.stop:
                            new_dts.append(result_dt)
                result[result_date] = new_dts
        return result
