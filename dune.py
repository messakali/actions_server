sale_obj = self.pool['sale.order']
sol_obj = self.pool['sale.order.line']


if object.origin:
    sale_ids = sale_obj.search(cr,uid,[('name','=',object.origin)],context=context)
    if sale_ids:
        compteur = 0
        so_id = sale_ids[0]
        sol_ids = sol_obj.search(cr,uid,[('order_id','=',so_id)],context=context)
        sols = sol_obj.browse(cr,uid,sol_ids,context=context)
        for l in object.invoice_line:
            if compteur < len(sols):
                sol = sols[compteur]
                l.write({'x_activity_id':sol.x_activie and sol.x_activie.id or False})
                compteur += 1