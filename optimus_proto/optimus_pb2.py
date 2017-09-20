# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optimus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='optimus.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\roptimus.proto\"\xc5\x01\n\x05Point\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1d\n\x06status\x18\x03 \x01(\x0e\x32\r.Point.Status\x12\r\n\x05point\x18\x04 \x01(\t\x12\x14\n\x0cmetric_value\x18\x05 \x01(\x01\x12\x10\n\x08metadata\x18\x06 \x01(\t\"I\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\n\n\x06PULLED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\r\n\tCOMPLETED\x10\x04\"&\n\x0cListOfPoints\x12\x16\n\x06points\x18\x01 \x03(\x0b\x32\x06.Point\"\x1b\n\rRequestWithId\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x11ListPointsRequest\x12\x10\n\x08how_many\x18\x01 \x01(\r2\xa4\x01\n\x07Optimus\x12\x1f\n\x0b\x43reatePoint\x12\x06.Point\x1a\x06.Point\"\x00\x12$\n\x08GetPoint\x12\x0e.RequestWithId\x1a\x06.Point\"\x00\x12\x31\n\nListPoints\x12\x12.ListPointsRequest\x1a\r.ListOfPoints\"\x00\x12\x1f\n\x0bModifyPoint\x12\x06.Point\x1a\x06.Point\"\x00\x62\x06proto3')
)



_POINT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Point.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PULLED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=142,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_POINT_STATUS)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='Point.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Point.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Point.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='Point.point', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_value', full_name='Point.metric_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Point.metadata', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POINT_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=215,
)


_LISTOFPOINTS = _descriptor.Descriptor(
  name='ListOfPoints',
  full_name='ListOfPoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='ListOfPoints.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=255,
)


_REQUESTWITHID = _descriptor.Descriptor(
  name='RequestWithId',
  full_name='RequestWithId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RequestWithId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=284,
)


_LISTPOINTSREQUEST = _descriptor.Descriptor(
  name='ListPointsRequest',
  full_name='ListPointsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='how_many', full_name='ListPointsRequest.how_many', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=323,
)

_POINT.fields_by_name['status'].enum_type = _POINT_STATUS
_POINT_STATUS.containing_type = _POINT
_LISTOFPOINTS.fields_by_name['points'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['ListOfPoints'] = _LISTOFPOINTS
DESCRIPTOR.message_types_by_name['RequestWithId'] = _REQUESTWITHID
DESCRIPTOR.message_types_by_name['ListPointsRequest'] = _LISTPOINTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'optimus_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  ))
_sym_db.RegisterMessage(Point)

ListOfPoints = _reflection.GeneratedProtocolMessageType('ListOfPoints', (_message.Message,), dict(
  DESCRIPTOR = _LISTOFPOINTS,
  __module__ = 'optimus_pb2'
  # @@protoc_insertion_point(class_scope:ListOfPoints)
  ))
_sym_db.RegisterMessage(ListOfPoints)

RequestWithId = _reflection.GeneratedProtocolMessageType('RequestWithId', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTWITHID,
  __module__ = 'optimus_pb2'
  # @@protoc_insertion_point(class_scope:RequestWithId)
  ))
_sym_db.RegisterMessage(RequestWithId)

ListPointsRequest = _reflection.GeneratedProtocolMessageType('ListPointsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPOINTSREQUEST,
  __module__ = 'optimus_pb2'
  # @@protoc_insertion_point(class_scope:ListPointsRequest)
  ))
_sym_db.RegisterMessage(ListPointsRequest)



_OPTIMUS = _descriptor.ServiceDescriptor(
  name='Optimus',
  full_name='Optimus',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=326,
  serialized_end=490,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePoint',
    full_name='Optimus.CreatePoint',
    index=0,
    containing_service=None,
    input_type=_POINT,
    output_type=_POINT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPoint',
    full_name='Optimus.GetPoint',
    index=1,
    containing_service=None,
    input_type=_REQUESTWITHID,
    output_type=_POINT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListPoints',
    full_name='Optimus.ListPoints',
    index=2,
    containing_service=None,
    input_type=_LISTPOINTSREQUEST,
    output_type=_LISTOFPOINTS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyPoint',
    full_name='Optimus.ModifyPoint',
    index=3,
    containing_service=None,
    input_type=_POINT,
    output_type=_POINT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OPTIMUS)

DESCRIPTOR.services_by_name['Optimus'] = _OPTIMUS

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class OptimusStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.CreatePoint = channel.unary_unary(
          '/Optimus/CreatePoint',
          request_serializer=Point.SerializeToString,
          response_deserializer=Point.FromString,
          )
      self.GetPoint = channel.unary_unary(
          '/Optimus/GetPoint',
          request_serializer=RequestWithId.SerializeToString,
          response_deserializer=Point.FromString,
          )
      self.ListPoints = channel.unary_unary(
          '/Optimus/ListPoints',
          request_serializer=ListPointsRequest.SerializeToString,
          response_deserializer=ListOfPoints.FromString,
          )
      self.ModifyPoint = channel.unary_unary(
          '/Optimus/ModifyPoint',
          request_serializer=Point.SerializeToString,
          response_deserializer=Point.FromString,
          )


  class OptimusServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CreatePoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetPoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ListPoints(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ModifyPoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_OptimusServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreatePoint': grpc.unary_unary_rpc_method_handler(
            servicer.CreatePoint,
            request_deserializer=Point.FromString,
            response_serializer=Point.SerializeToString,
        ),
        'GetPoint': grpc.unary_unary_rpc_method_handler(
            servicer.GetPoint,
            request_deserializer=RequestWithId.FromString,
            response_serializer=Point.SerializeToString,
        ),
        'ListPoints': grpc.unary_unary_rpc_method_handler(
            servicer.ListPoints,
            request_deserializer=ListPointsRequest.FromString,
            response_serializer=ListOfPoints.SerializeToString,
        ),
        'ModifyPoint': grpc.unary_unary_rpc_method_handler(
            servicer.ModifyPoint,
            request_deserializer=Point.FromString,
            response_serializer=Point.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Optimus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaOptimusServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CreatePoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetPoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ListPoints(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ModifyPoint(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaOptimusStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def CreatePoint(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    CreatePoint.future = None
    def GetPoint(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetPoint.future = None
    def ListPoints(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    ListPoints.future = None
    def ModifyPoint(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    ModifyPoint.future = None


  def beta_create_Optimus_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Optimus', 'CreatePoint'): Point.FromString,
      ('Optimus', 'GetPoint'): RequestWithId.FromString,
      ('Optimus', 'ListPoints'): ListPointsRequest.FromString,
      ('Optimus', 'ModifyPoint'): Point.FromString,
    }
    response_serializers = {
      ('Optimus', 'CreatePoint'): Point.SerializeToString,
      ('Optimus', 'GetPoint'): Point.SerializeToString,
      ('Optimus', 'ListPoints'): ListOfPoints.SerializeToString,
      ('Optimus', 'ModifyPoint'): Point.SerializeToString,
    }
    method_implementations = {
      ('Optimus', 'CreatePoint'): face_utilities.unary_unary_inline(servicer.CreatePoint),
      ('Optimus', 'GetPoint'): face_utilities.unary_unary_inline(servicer.GetPoint),
      ('Optimus', 'ListPoints'): face_utilities.unary_unary_inline(servicer.ListPoints),
      ('Optimus', 'ModifyPoint'): face_utilities.unary_unary_inline(servicer.ModifyPoint),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Optimus_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Optimus', 'CreatePoint'): Point.SerializeToString,
      ('Optimus', 'GetPoint'): RequestWithId.SerializeToString,
      ('Optimus', 'ListPoints'): ListPointsRequest.SerializeToString,
      ('Optimus', 'ModifyPoint'): Point.SerializeToString,
    }
    response_deserializers = {
      ('Optimus', 'CreatePoint'): Point.FromString,
      ('Optimus', 'GetPoint'): Point.FromString,
      ('Optimus', 'ListPoints'): ListOfPoints.FromString,
      ('Optimus', 'ModifyPoint'): Point.FromString,
    }
    cardinalities = {
      'CreatePoint': cardinality.Cardinality.UNARY_UNARY,
      'GetPoint': cardinality.Cardinality.UNARY_UNARY,
      'ListPoints': cardinality.Cardinality.UNARY_UNARY,
      'ModifyPoint': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Optimus', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)