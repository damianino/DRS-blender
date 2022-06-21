import grpc
import drs_protocol_pb2
import drs_protocol_pb2_grpc
import threading



def main():
    thread = GRPCClient(None)
    thread.start()


class GRPCClient():
    stub = None
    sessionKey = ""

    @classmethod
    def Connect(cls, addr):
        print("Starting grpc client")
        channel =  grpc.insecure_channel(addr)
        cls.stub = drs_protocol_pb2_grpc.JobsManagerStub(channel)
        response = cls.stub.ConnectRequest(drs_protocol_pb2.Request(UserId=11, SessionKey="", Body="fsdf"))
        print(f"client received: {response.Success}, {response.Body}" )
        cls.sessionKey = response.Body

    @classmethod
    def Render(cls):
        response = cls.stub.RenderRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=cls.sessionKey, Body="fsdf"))
        print(f"{response.Success}, {response.Body}" )

    @classmethod
    def JobPoll(cls, uuid):
        response = cls.stub.JobPollRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=cls.sessionKey, Body=uuid))
        print(f"{response.Success}, {response.Body}, {response.FragmentIndexes}" )
        return response


    def clientCLI(self):
        while True:
            command = input()
            match command:
                case "render":
                    response = self.stub.RenderRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=self.sessionKey, Body="fsdf"))
                    
                case "jobpoll":
                    response = self.stub.JobPollRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=sk, Body="fsdf"))
                    print(response.FragmentIndexes)
                    
                case "render":
                    response = self.stub.RenderRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=sk, Body="fsdf"))
                    
                case "render":
                    response = self.stub.RenderRequest(drs_protocol_pb2.Request(UserId=11, SessionKey=sk, Body="fsdf"))
                    
                case "STOP":
                    break
            
            print(f"{response.Success}, {response.Body}" )
    


if __name__ == "__main__":
    main()