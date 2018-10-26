# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: repl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='repl.proto',
  package='coop.rchain.node.model',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nrepl.proto\x12\x16\x63oop.rchain.node.model\"\x1a\n\nCmdRequest\x12\x0c\n\x04line\x18\x01 \x01(\t\"\x1e\n\x0b\x45valRequest\x12\x0f\n\x07program\x18\x01 \x01(\t\"\x1e\n\x0cReplResponse\x12\x0e\n\x06output\x18\x01 \x01(\t2\xae\x01\n\x04Repl\x12Q\n\x03Run\x12\".coop.rchain.node.model.CmdRequest\x1a$.coop.rchain.node.model.ReplResponse\"\x00\x12S\n\x04\x45val\x12#.coop.rchain.node.model.EvalRequest\x1a$.coop.rchain.node.model.ReplResponse\"\x00\x62\x06proto3')
)




_CMDREQUEST = _descriptor.Descriptor(
  name='CmdRequest',
  full_name='coop.rchain.node.model.CmdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line', full_name='coop.rchain.node.model.CmdRequest.line', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=64,
)


_EVALREQUEST = _descriptor.Descriptor(
  name='EvalRequest',
  full_name='coop.rchain.node.model.EvalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='program', full_name='coop.rchain.node.model.EvalRequest.program', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=96,
)


_REPLRESPONSE = _descriptor.Descriptor(
  name='ReplResponse',
  full_name='coop.rchain.node.model.ReplResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='coop.rchain.node.model.ReplResponse.output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['CmdRequest'] = _CMDREQUEST
DESCRIPTOR.message_types_by_name['EvalRequest'] = _EVALREQUEST
DESCRIPTOR.message_types_by_name['ReplResponse'] = _REPLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdRequest = _reflection.GeneratedProtocolMessageType('CmdRequest', (_message.Message,), dict(
  DESCRIPTOR = _CMDREQUEST,
  __module__ = 'repl_pb2'
  # @@protoc_insertion_point(class_scope:coop.rchain.node.model.CmdRequest)
  ))
_sym_db.RegisterMessage(CmdRequest)

EvalRequest = _reflection.GeneratedProtocolMessageType('EvalRequest', (_message.Message,), dict(
  DESCRIPTOR = _EVALREQUEST,
  __module__ = 'repl_pb2'
  # @@protoc_insertion_point(class_scope:coop.rchain.node.model.EvalRequest)
  ))
_sym_db.RegisterMessage(EvalRequest)

ReplResponse = _reflection.GeneratedProtocolMessageType('ReplResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLRESPONSE,
  __module__ = 'repl_pb2'
  # @@protoc_insertion_point(class_scope:coop.rchain.node.model.ReplResponse)
  ))
_sym_db.RegisterMessage(ReplResponse)



_REPL = _descriptor.ServiceDescriptor(
  name='Repl',
  full_name='coop.rchain.node.model.Repl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=131,
  serialized_end=305,
  methods=[
  _descriptor.MethodDescriptor(
    name='Run',
    full_name='coop.rchain.node.model.Repl.Run',
    index=0,
    containing_service=None,
    input_type=_CMDREQUEST,
    output_type=_REPLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Eval',
    full_name='coop.rchain.node.model.Repl.Eval',
    index=1,
    containing_service=None,
    input_type=_EVALREQUEST,
    output_type=_REPLRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPL)

DESCRIPTOR.services_by_name['Repl'] = _REPL

# @@protoc_insertion_point(module_scope)