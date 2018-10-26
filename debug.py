import os
import sys

ROOT = os.curdir
GENERATED = os.path.join(ROOT, 'generated')
sys.path.append(GENERATED)

import CasperMessage_pb2  # isort:skip
import CasperMessage_pb2_grpc  # isort:skip
import RhoTypes_pb2  # isort:skip
import RhoTypes_pb2_grpc  # isort:skip

from generated.CasperMessage_pb2 import DataAtNameQuery
from generated.RhoTypes_pb2 import Par, Expr
par = Par()
par.exprs.extend([Expr(g_string='myname')])
channel = DataAtNameQuery(depth=1, name=par)
