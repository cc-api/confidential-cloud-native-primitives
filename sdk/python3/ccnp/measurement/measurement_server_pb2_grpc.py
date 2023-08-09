# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ccnp.measurement import measurement_server_pb2 as measurement__server__pb2


class MeasurementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMeasurement = channel.unary_unary(
                '/measurement.Measurement/GetMeasurement',
                request_serializer=measurement__server__pb2.GetMeasurementRequest.SerializeToString,
                response_deserializer=measurement__server__pb2.GetMeasurementReply.FromString,
                )


class MeasurementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMeasurement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeasurementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMeasurement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasurement,
                    request_deserializer=measurement__server__pb2.GetMeasurementRequest.FromString,
                    response_serializer=measurement__server__pb2.GetMeasurementReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'measurement.Measurement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Measurement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMeasurement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/measurement.Measurement/GetMeasurement',
            measurement__server__pb2.GetMeasurementRequest.SerializeToString,
            measurement__server__pb2.GetMeasurementReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)