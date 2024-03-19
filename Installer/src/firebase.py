import grpc
from protos.user_pb2_grpc import UserStub
from protos.user_pb2 import SignInSignUpRequest

def create_account(username, password):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = UserStub(channel)
        request = SignInSignUpRequest(email=username, password=password)
        response = stub.SignUp(request)