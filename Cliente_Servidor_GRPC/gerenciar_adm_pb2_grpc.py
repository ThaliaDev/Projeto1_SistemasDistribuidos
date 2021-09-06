# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gerenciar_adm_pb2 as gerenciar__adm__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/User/login',
                request_serializer=gerenciar__adm__pb2.LoginRequest.SerializeToString,
                response_deserializer=gerenciar__adm__pb2.LoginResponse.FromString,
                )
        self.cadastro = channel.unary_unary(
                '/User/cadastro',
                request_serializer=gerenciar__adm__pb2.CadastroRequest.SerializeToString,
                response_deserializer=gerenciar__adm__pb2.CadastroResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cadastro(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=gerenciar__adm__pb2.LoginRequest.FromString,
                    response_serializer=gerenciar__adm__pb2.LoginResponse.SerializeToString,
            ),
            'cadastro': grpc.unary_unary_rpc_method_handler(
                    servicer.cadastro,
                    request_deserializer=gerenciar__adm__pb2.CadastroRequest.FromString,
                    response_serializer=gerenciar__adm__pb2.CadastroResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/login',
            gerenciar__adm__pb2.LoginRequest.SerializeToString,
            gerenciar__adm__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cadastro(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/User/cadastro',
            gerenciar__adm__pb2.CadastroRequest.SerializeToString,
            gerenciar__adm__pb2.CadastroResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)