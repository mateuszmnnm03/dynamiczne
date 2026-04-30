import grpc
from grpc_reflection.v1alpha import reflection_pb2, reflection_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")

stub = reflection_pb2_grpc.ServerReflectionStub(channel)

request = reflection_pb2.ServerReflectionRequest(
    list_services=""
)

response = stub.ServerReflectionInfo(iter([request]))

for res in response:
    print(res)

method = "/calculator.Calculator/Add"

a = int(input("Podaj arg1: "))
b = int(input("Podaj arg2: "))
request_bytes = bytes([0x08, a, 0x10, b])
response = channel.unary_unary(method)(request_bytes)

print("Raw response:", response)
print("Wynik:", response[1])

method = "/calculator.Calculator/Subtract"

a = int(input("Podaj arg1: "))
b = int(input("Podaj arg2: "))


request_bytes = bytes([0x08, a, 0x10, b])

response = channel.unary_unary(method)(request_bytes)

print("Raw response:", response)
print("Wynik:", response[1])

method = "/streaming.StreamTester/GeneratePrimeNumbers"


request_bytes = b'\x08\x0e' 

response_iterator = channel.unary_stream(method)(request_bytes)

print("Prime numbers:")
for res in response_iterator:
    print(res)