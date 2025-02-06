from odoo import http
from odoo.http import request, Response
import json


class MaterialController(http.Controller):
    @http.route('/api/material/<int:id>', type='json', auth='public', methods=['PUT'])
    def update_material(self, id, **kwargs):
        material = request.env['material.registration'].sudo().browse(id)
        if not material.exists():
            return {
                'status': 'error',
                'message': 'Material not found'
            }

        try:
            material.write({
                'material_code': kwargs.get('material_code', material.material_code),
                'material_name': kwargs.get('material_name', material.material_name),
                'material_type': kwargs.get('material_type', material.material_type),
                'material_buy_price': kwargs.get('material_buy_price', material.material_buy_price),
                'supplier_id': kwargs.get('supplier_id', material.supplier_id.id)
            })
            return {
                'status': 'success',
                'message': 'Material updated successfully'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    @http.route('/api/material/<int:id>', type='json', auth='public', methods=['DELETE'])
    def delete_material(self, id):
        material = request.env['material.registration'].sudo().browse(id)
        if not material.exists():
            return {
                'status': 'error',
                'message': 'Material not found'
            }

        try:
            material.unlink()
            return {
                'status': 'success',
                'message': 'Material deleted successfully'
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
