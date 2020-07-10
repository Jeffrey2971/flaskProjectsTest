from flask import request
from flask_restful import Resource, abort

from App import models
from App.ext import cache
from App.models import User, Order, Ticket


def login_required(fun):
    def f(*args, **kwargs):
        u_token = request.args.get("u_token")
        print(u_token)
        if u_token:
            user_id = cache.get(u_token)
            if user_id:
                return fun(*args, **kwargs)
            else:
                abort(401, message='用户状态失效或无效')
        else:
            # 未认证
            abort(401, message='请登录')

    return f


def check_permission(dest_permission):
    def check(fun):
        def f(*args, **kwargs):
            u_token = request.form.get('u_token')
            if not u_token:
                abort(401, message='请登录')
            else:
                user_id = cache.get(u_token)
                if not user_id:
                    abort(401, message='用户状态失效')
                else:
                    user = User.query.get(user_id)
                    if user.check_permission(dest_permission):
                        return fun(*args, **kwargs)
                    else:
                        abort(403, message='您没有权限访问本模块')

        return f

    return check


class OrderResource(Resource):
    @login_required
    def get(self):
        return {"msg": "ok"}
        # u_token = request.args.get("u_token")
        # if u_token:
        #     id = cache.get(u_token)
        #     if id:
        #         user = User.query.get(id)
        #
        #     return {"msg": "order ok"}
        # else:
        #
        #     return {"msg": "请登录"}

    #  只要能进入post就意味着用户登入状态有效，并且用户有权限进行此操作
    @check_permission(models.PERMISSION_DELETE)
    def post(self):
        # 直接写操作即可

        # u_token = request.form.get('u_token')
        # if u_token:
        #
        #     user_id = cache.get(u_token)
        #
        #     if user_id:
        #         user = User.query.get(user_id)
        #         if user.check_permission(models.PERMISSION_MODIFCATION):
        #             return {"msg": "post ok"}
        #         else:
        #             abort(403, message='你没有权限访问本模块')
        #     else:
        #         abort(401, message='用户状态失效')
        # else:
        #     abort(401, message='用户未登录')

        return {"msg": "post ok"}

    @check_permission(models.PERMISSION_ORDER)
    def post(self):
        """
        下单
            用户
            排挡（目前没有）
                电影  movieapi
                大厅  None
                    定义一个表
                        大厅类型
                        座位类型（0,0)    (0,1）
                        1 - 16
                        if 一排就是五个位置
                        0   1   2   3   4
                            6   7   8   9
                            11  12  13  14

        """

        u_token = request.form.get("u_token")
        mp = request.form.get("mp")
        seats = request.form.get("seats")

        order = Order()
        order.o_user = cache.get(u_token)
        order.o_movie_plan = mp
        order.save()
        seat_list = seats.split("#")

        for seats_positon in seat_list:
            ticket = Ticket()
            ticket.t_order = order.id
            ticket.t_seat = int(seats_positon)
            ticket.save()

        # 将订单放入缓存中并限定过期时间
        order_list = cache.get(mp)
        if not order_list:
            order_list.append(order.id)
            cache.set(mp, order_list)


        data = {
            "returnCode": "0",
            "returnValue": order.id
        }
        return data




