from flask import request
from flask_restful import Resource

from App.ext import cache
from App.models import Hall, MoviePlan, Ticket


class SeatResource(Resource):
    def get(self):
        # 获取排挡ID
        planid = request.args.get("planid")
        # 获取排挡信息
        movie_plan = MoviePlan.query.get(planid)
        # 从大厅中获取信息座位
        hall = Hall.query.get(movie_plan.mp_hall)

        order_list = cache.get(planid)
        if not order_list:
            hall_data = {
                "h_count": hall.h_count,
                "h_seat": hall.seats
            }
        else:
            hall_seats =hall.seats
            hall_seat_list = hall_seats.split('#')
            for order_id in order_list:
                ticket = Ticket.query.filtert(Ticket.t_order == order_id)
                for tickets in ticket:
                    # 移除大厅中对应的位置
                    hall_seat_list.remove(tickets.t_seat)

            hall_data = {
                "h_count": hall.h_count,
                "h_seat": hall.seat_list.join("#")
            }

            data = {
                "returnCode": "0",
                "returnValue": hall_data
            }
            return data