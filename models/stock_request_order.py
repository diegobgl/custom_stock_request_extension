from odoo import models, fields

class StockRequestOrder(models.Model):
    _inherit = 'stock.request.order'

    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        help='Analytic account to assign to the stock picking when the request is confirmed.')

    def action_confirm(self):
        res = super(StockRequestOrder, self).action_confirm()
        
        for order in self:
            if order.analytic_account_id:
                # Encontrar el picking relacionado con la solicitud
                for picking in order.picking_ids:
                    # Asignar la cuenta analítica al picking
                    picking.analytic_account_id = order.analytic_account_id
        return res