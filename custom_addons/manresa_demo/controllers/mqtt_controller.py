from odoo import http
from odoo.http import request
import json
from .. import mqtt_client


class MqttValueController(http.Controller):
    @http.route(
        "/mqtt/value",
        type="http",
        auth="public",
        methods=[
            "GET",
        ],
        csrf=False,
    )
    def get_latest_mqtt_value(self):
        value = mqtt_client.latest_value["message"]

        return http.Response(
            json.dumps({"value": value}), content_type="application/json", status=200
        )


class MqttDashboard(http.Controller):

    @http.route('/mqtt/dashboard', type='http', auth='public', website=True)
    def mqtt_dashboard(self, **kw):
        return request.render("manresa_demo.mqtt_dashboard", {})