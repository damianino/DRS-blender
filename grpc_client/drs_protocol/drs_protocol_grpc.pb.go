// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v3.20.1
// source: drs_protocol.proto

package drs_protocol

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// JobsManagerClient is the client API for JobsManager service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type JobsManagerClient interface {
	ConnectRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
	RenderRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
	JobPollRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*JobPollResponseMessage, error)
	UpdateRoleRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
	ReportProgressRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error)
}

type jobsManagerClient struct {
	cc grpc.ClientConnInterface
}

func NewJobsManagerClient(cc grpc.ClientConnInterface) JobsManagerClient {
	return &jobsManagerClient{cc}
}

func (c *jobsManagerClient) ConnectRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/drs_protocol.JobsManager/ConnectRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *jobsManagerClient) RenderRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/drs_protocol.JobsManager/RenderRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *jobsManagerClient) JobPollRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*JobPollResponseMessage, error) {
	out := new(JobPollResponseMessage)
	err := c.cc.Invoke(ctx, "/drs_protocol.JobsManager/JobPollRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *jobsManagerClient) UpdateRoleRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/drs_protocol.JobsManager/UpdateRoleRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *jobsManagerClient) ReportProgressRequest(ctx context.Context, in *Request, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/drs_protocol.JobsManager/ReportProgressRequest", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// JobsManagerServer is the server API for JobsManager service.
// All implementations must embed UnimplementedJobsManagerServer
// for forward compatibility
type JobsManagerServer interface {
	ConnectRequest(context.Context, *Request) (*Response, error)
	RenderRequest(context.Context, *Request) (*Response, error)
	JobPollRequest(context.Context, *Request) (*JobPollResponseMessage, error)
	UpdateRoleRequest(context.Context, *Request) (*Response, error)
	ReportProgressRequest(context.Context, *Request) (*Response, error)
	mustEmbedUnimplementedJobsManagerServer()
}

// UnimplementedJobsManagerServer must be embedded to have forward compatible implementations.
type UnimplementedJobsManagerServer struct {
}

func (UnimplementedJobsManagerServer) ConnectRequest(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ConnectRequest not implemented")
}
func (UnimplementedJobsManagerServer) RenderRequest(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RenderRequest not implemented")
}
func (UnimplementedJobsManagerServer) JobPollRequest(context.Context, *Request) (*JobPollResponseMessage, error) {
	return nil, status.Errorf(codes.Unimplemented, "method JobPollRequest not implemented")
}
func (UnimplementedJobsManagerServer) UpdateRoleRequest(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateRoleRequest not implemented")
}
func (UnimplementedJobsManagerServer) ReportProgressRequest(context.Context, *Request) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReportProgressRequest not implemented")
}
func (UnimplementedJobsManagerServer) mustEmbedUnimplementedJobsManagerServer() {}

// UnsafeJobsManagerServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to JobsManagerServer will
// result in compilation errors.
type UnsafeJobsManagerServer interface {
	mustEmbedUnimplementedJobsManagerServer()
}

func RegisterJobsManagerServer(s grpc.ServiceRegistrar, srv JobsManagerServer) {
	s.RegisterService(&JobsManager_ServiceDesc, srv)
}

func _JobsManager_ConnectRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(JobsManagerServer).ConnectRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/drs_protocol.JobsManager/ConnectRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(JobsManagerServer).ConnectRequest(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _JobsManager_RenderRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(JobsManagerServer).RenderRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/drs_protocol.JobsManager/RenderRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(JobsManagerServer).RenderRequest(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _JobsManager_JobPollRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(JobsManagerServer).JobPollRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/drs_protocol.JobsManager/JobPollRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(JobsManagerServer).JobPollRequest(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _JobsManager_UpdateRoleRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(JobsManagerServer).UpdateRoleRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/drs_protocol.JobsManager/UpdateRoleRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(JobsManagerServer).UpdateRoleRequest(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

func _JobsManager_ReportProgressRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(JobsManagerServer).ReportProgressRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/drs_protocol.JobsManager/ReportProgressRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(JobsManagerServer).ReportProgressRequest(ctx, req.(*Request))
	}
	return interceptor(ctx, in, info, handler)
}

// JobsManager_ServiceDesc is the grpc.ServiceDesc for JobsManager service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var JobsManager_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "drs_protocol.JobsManager",
	HandlerType: (*JobsManagerServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ConnectRequest",
			Handler:    _JobsManager_ConnectRequest_Handler,
		},
		{
			MethodName: "RenderRequest",
			Handler:    _JobsManager_RenderRequest_Handler,
		},
		{
			MethodName: "JobPollRequest",
			Handler:    _JobsManager_JobPollRequest_Handler,
		},
		{
			MethodName: "UpdateRoleRequest",
			Handler:    _JobsManager_UpdateRoleRequest_Handler,
		},
		{
			MethodName: "ReportProgressRequest",
			Handler:    _JobsManager_ReportProgressRequest_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "drs_protocol.proto",
}
