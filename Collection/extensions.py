from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_login import AnonymousUserMixin

class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'


csrf = CSRFProtect()
moment = Moment()
migrate = Migrate()
bootstrap = Bootstrap()
login_manager= LoginManager()
login_manager.login_view='user.login'   #如果没有登录，则会跳转到user蓝图下的login
login_manager.anonymous_user = Anonymous


