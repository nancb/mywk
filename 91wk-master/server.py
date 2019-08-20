from apps import app
from views import app_user
from views.app_bannerinfo import bannerinfo_blue
from views.app_card import card_blue
from views.app_cart import blue_cart
from views.app_goods import bule_goods
from views.app_lend import lend_blue
from views.app_member import members_blue
from views.app_order import blue_order
from views.app_product import product_blue
from views.app_verify import verify_blue

APP_CONFIG={
    'host': 'localhost',
    'port': 9001,
    'debug': True
}
if __name__ == '__main__':
    app.register_blueprint(app_user.blue)
    app.register_blueprint(product_blue)
    app.register_blueprint(bule_goods)
    app.register_blueprint(blue_cart)
    app.register_blueprint(blue_order)
    app.register_blueprint(members_blue)
    app.register_blueprint(bannerinfo_blue)
    app.register_blueprint(verify_blue)
    app.register_blueprint(card_blue)
    app.register_blueprint(lend_blue)



    app.run(**APP_CONFIG)