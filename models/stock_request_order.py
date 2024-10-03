from odoo import models, fields

class StockRequestOrder(models.Model):
    _inherit = 'stock.request.order'

    analytic_account_ids = fields.Many2many(
        'account.analytic.account',
        string='Analytic Accounts',
        help='Analytic accounts to assign to the stock picking when this request is confirmed.'
    )

    def action_confirm(self):
        super(StockRequestOrder, self).action_confirm()

        # Asignar las cuentas analíticas al picking generado
        for request in self:
            if request.analytic_account_ids:
                # Buscar los pickings relacionados con esta solicitud
                for picking in request.picking_ids:
                    picking.analytic_account_ids = [(6, 0, request.analytic_account_ids.ids)]
