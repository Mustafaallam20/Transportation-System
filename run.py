from flask import Flask

from app.controllers.tickets.reserve_ticket import reserve_ticket

from app.controllers.Session.register import register_manage

from app.controllers.tickets.ticket_manage import ticket_manage

from app.controllers.Session.login import login_manage

from app.controllers.Session.logout import logout_manage

from app.controllers.trips.schedule import schedule_manage

from app.controllers.Statistics.statistics import statistics_manage

from app.controllers.tickets.edit_ticket import edit_ticket

from app.controllers.tickets.history import history

from app.controllers.index import index_manage

from app.controllers.Dashboards.Manage_Dashboard import manage_dashboard

from app.controllers.trips.add_trip import add_trip_manage

from app.controllers.trips.trip_manage import trip_manage

from app.controllers.employee.employee_manage import employee_manage

APP = Flask(__name__)
APP.secret_key = 'secret'
APP.register_blueprint(reserve_ticket)
APP.register_blueprint(register_manage)
APP.register_blueprint(ticket_manage)
APP.register_blueprint(schedule_manage)
APP.register_blueprint(login_manage)
APP.register_blueprint(logout_manage)
APP.register_blueprint(statistics_manage)
APP.register_blueprint(edit_ticket)
APP.register_blueprint(history)
APP.register_blueprint(index_manage)
APP.register_blueprint(manage_dashboard)
APP.register_blueprint(add_trip_manage)
APP.register_blueprint(trip_manage)
APP.register_blueprint(employee_manage)

if __name__ == "__main__":
    APP.run(debug=True)
