# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import kama_pb2 as kama__pb2


class KamaDatabaseStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListEntities = channel.unary_stream(
        '/kama.KamaDatabase/ListEntities',
        request_serializer=kama__pb2.Entity.SerializeToString,
        response_deserializer=kama__pb2.Entity.FromString,
        )
    self.GetEntity = channel.unary_unary(
        '/kama.KamaDatabase/GetEntity',
        request_serializer=kama__pb2.Entity.SerializeToString,
        response_deserializer=kama__pb2.Entity.FromString,
        )
    self.CreateEntity = channel.unary_unary(
        '/kama.KamaDatabase/CreateEntity',
        request_serializer=kama__pb2.CreateEntityRequest.SerializeToString,
        response_deserializer=kama__pb2.Entity.FromString,
        )
    self.DeleteEntity = channel.unary_unary(
        '/kama.KamaDatabase/DeleteEntity',
        request_serializer=kama__pb2.Entity.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.UpdateEntity = channel.unary_unary(
        '/kama.KamaDatabase/UpdateEntity',
        request_serializer=kama__pb2.Entity.SerializeToString,
        response_deserializer=kama__pb2.Entity.FromString,
        )
    self.AddAttribute = channel.unary_unary(
        '/kama.KamaDatabase/AddAttribute',
        request_serializer=kama__pb2.Attribute.SerializeToString,
        response_deserializer=kama__pb2.Attribute.FromString,
        )
    self.DeleteAttributes = channel.unary_unary(
        '/kama.KamaDatabase/DeleteAttributes',
        request_serializer=kama__pb2.Attribute.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.AddLink = channel.unary_unary(
        '/kama.KamaDatabase/AddLink',
        request_serializer=kama__pb2.Link.SerializeToString,
        response_deserializer=kama__pb2.Link.FromString,
        )
    self.DeleteLink = channel.unary_unary(
        '/kama.KamaDatabase/DeleteLink',
        request_serializer=kama__pb2.Link.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.AddPermission = channel.unary_unary(
        '/kama.KamaDatabase/AddPermission',
        request_serializer=kama__pb2.Permission.SerializeToString,
        response_deserializer=kama__pb2.Permission.FromString,
        )
    self.DeletePermission = channel.unary_unary(
        '/kama.KamaDatabase/DeletePermission',
        request_serializer=kama__pb2.Permission.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class KamaDatabaseServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListEntities(self, request, context):
    """ListEntities returns all Entities matching any of the non-null fields
    given in the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntity(self, request, context):
    """GetEntity will try to find an entity with the given uuid, name, and
    kind, allowing wildcard searches for any of the fields that aren't set.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateEntity(self, request, context):
    """CreateEntity will create a new Entity with the given name and kind and
    return a new UUID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEntity(self, request, context):
    """DeleteEntity will delete the Entity with the given UUID. Other fields
    are ignored.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateEntity(self, request, context):
    """UpdateEntity currently only supports changing the entity's name. It uses
    the uuid to determine what existing object is being updated. All other
    fields are ignored.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddAttribute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddLink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteLink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddPermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KamaDatabaseServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListEntities': grpc.unary_stream_rpc_method_handler(
          servicer.ListEntities,
          request_deserializer=kama__pb2.Entity.FromString,
          response_serializer=kama__pb2.Entity.SerializeToString,
      ),
      'GetEntity': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntity,
          request_deserializer=kama__pb2.Entity.FromString,
          response_serializer=kama__pb2.Entity.SerializeToString,
      ),
      'CreateEntity': grpc.unary_unary_rpc_method_handler(
          servicer.CreateEntity,
          request_deserializer=kama__pb2.CreateEntityRequest.FromString,
          response_serializer=kama__pb2.Entity.SerializeToString,
      ),
      'DeleteEntity': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEntity,
          request_deserializer=kama__pb2.Entity.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'UpdateEntity': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateEntity,
          request_deserializer=kama__pb2.Entity.FromString,
          response_serializer=kama__pb2.Entity.SerializeToString,
      ),
      'AddAttribute': grpc.unary_unary_rpc_method_handler(
          servicer.AddAttribute,
          request_deserializer=kama__pb2.Attribute.FromString,
          response_serializer=kama__pb2.Attribute.SerializeToString,
      ),
      'DeleteAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAttributes,
          request_deserializer=kama__pb2.Attribute.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'AddLink': grpc.unary_unary_rpc_method_handler(
          servicer.AddLink,
          request_deserializer=kama__pb2.Link.FromString,
          response_serializer=kama__pb2.Link.SerializeToString,
      ),
      'DeleteLink': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLink,
          request_deserializer=kama__pb2.Link.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'AddPermission': grpc.unary_unary_rpc_method_handler(
          servicer.AddPermission,
          request_deserializer=kama__pb2.Permission.FromString,
          response_serializer=kama__pb2.Permission.SerializeToString,
      ),
      'DeletePermission': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePermission,
          request_deserializer=kama__pb2.Permission.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kama.KamaDatabase', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
