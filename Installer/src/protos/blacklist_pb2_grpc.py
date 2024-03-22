# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import blacklist_pb2 as blacklist__pb2


class BlacklistStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PutBlackList = channel.unary_unary(
                '/blacklist.Blacklist/PutBlackList',
                request_serializer=blacklist__pb2.PutBlackListRequest.SerializeToString,
                response_deserializer=blacklist__pb2.PutBlackListReply.FromString,
                )
        self.BlockCountry = channel.unary_unary(
                '/blacklist.Blacklist/BlockCountry',
                request_serializer=blacklist__pb2.BlockCountryRequest.SerializeToString,
                response_deserializer=blacklist__pb2.BlockCountryReply.FromString,
                )
        self.GetBlackList = channel.unary_stream(
                '/blacklist.Blacklist/GetBlackList',
                request_serializer=blacklist__pb2.GetBlackListRequest.SerializeToString,
                response_deserializer=blacklist__pb2.GetBlackListReply.FromString,
                )
        self.GetBlackListUnary = channel.unary_unary(
                '/blacklist.Blacklist/GetBlackListUnary',
                request_serializer=blacklist__pb2.GetBlackListRequest.SerializeToString,
                response_deserializer=blacklist__pb2.GetBlackListReply.FromString,
                )
        self.PutWhiteList = channel.unary_unary(
                '/blacklist.Blacklist/PutWhiteList',
                request_serializer=blacklist__pb2.PutWhiteListRequest.SerializeToString,
                response_deserializer=blacklist__pb2.PutWhiteListReply.FromString,
                )


class BlacklistServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PutBlackList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BlockCountry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlackList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlackListUnary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutWhiteList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BlacklistServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PutBlackList': grpc.unary_unary_rpc_method_handler(
                    servicer.PutBlackList,
                    request_deserializer=blacklist__pb2.PutBlackListRequest.FromString,
                    response_serializer=blacklist__pb2.PutBlackListReply.SerializeToString,
            ),
            'BlockCountry': grpc.unary_unary_rpc_method_handler(
                    servicer.BlockCountry,
                    request_deserializer=blacklist__pb2.BlockCountryRequest.FromString,
                    response_serializer=blacklist__pb2.BlockCountryReply.SerializeToString,
            ),
            'GetBlackList': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBlackList,
                    request_deserializer=blacklist__pb2.GetBlackListRequest.FromString,
                    response_serializer=blacklist__pb2.GetBlackListReply.SerializeToString,
            ),
            'GetBlackListUnary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlackListUnary,
                    request_deserializer=blacklist__pb2.GetBlackListRequest.FromString,
                    response_serializer=blacklist__pb2.GetBlackListReply.SerializeToString,
            ),
            'PutWhiteList': grpc.unary_unary_rpc_method_handler(
                    servicer.PutWhiteList,
                    request_deserializer=blacklist__pb2.PutWhiteListRequest.FromString,
                    response_serializer=blacklist__pb2.PutWhiteListReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blacklist.Blacklist', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Blacklist(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PutBlackList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blacklist.Blacklist/PutBlackList',
            blacklist__pb2.PutBlackListRequest.SerializeToString,
            blacklist__pb2.PutBlackListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BlockCountry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blacklist.Blacklist/BlockCountry',
            blacklist__pb2.BlockCountryRequest.SerializeToString,
            blacklist__pb2.BlockCountryReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlackList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blacklist.Blacklist/GetBlackList',
            blacklist__pb2.GetBlackListRequest.SerializeToString,
            blacklist__pb2.GetBlackListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlackListUnary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blacklist.Blacklist/GetBlackListUnary',
            blacklist__pb2.GetBlackListRequest.SerializeToString,
            blacklist__pb2.GetBlackListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutWhiteList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blacklist.Blacklist/PutWhiteList',
            blacklist__pb2.PutWhiteListRequest.SerializeToString,
            blacklist__pb2.PutWhiteListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)