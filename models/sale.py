from openerp.osv import osv, fields



class SaleOrderLine(osv.osv):
    _inherit = 'sale.order.line'
    _columns = {
	'product_thumbnail': fields.related('product_id', 'image_small', type='binary', string="Preview"),
    }
