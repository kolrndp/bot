#from .feedback import router as feedback_router_us
from .start import router as start_router_us
from .spam import router as spam_router_us
from .unknown import router as unknown_router_us
#all_user_routers = [start_router_us, feedback_router_us, spam_router_us]
all_user_routers = [start_router_us, spam_router_us, unknown_router_us]
