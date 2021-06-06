# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: posts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='posts.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bposts.proto\"j\n\nUploadPost\x1a?\n\x07Request\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x14\n\x0cpicture_blob\x18\x03 \x01(\x0c\x1a\x1b\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x80\x01\n\x10\x46\x65tchPostDetails\x1a\x1a\n\x07Request\x12\x0f\n\x07post_id\x18\x01 \x01(\x05\x1aP\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x13\n\x0bpictureBlob\x18\x04 \x01(\x0c\"=\n\rFetchKPostIds\x1a\x14\n\x07Request\x12\t\n\x01k\x18\x01 \x01(\x05\x1a\x16\n\x08Response\x12\n\n\x02id\x18\x01 \x03(\x05\x32\xd6\x01\n\x0bPostService\x12\x39\n\nuploadPost\x12\x13.UploadPost.Request\x1a\x14.UploadPost.Response\"\x00\x12K\n\x10\x66\x65tchPostDetails\x12\x19.FetchPostDetails.Request\x1a\x1a.FetchPostDetails.Response\"\x00\x12?\n\nfetchPosts\x12\x16.FetchKPostIds.Request\x1a\x17.FetchKPostIds.Response\"\x00\x62\x06proto3'
)




_UPLOADPOST_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='UploadPost.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='UploadPost.Request.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='UploadPost.Request.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='picture_blob', full_name='UploadPost.Request.picture_blob', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=29,
  serialized_end=92,
)

_UPLOADPOST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='UploadPost.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='UploadPost.Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=94,
  serialized_end=121,
)

_UPLOADPOST = _descriptor.Descriptor(
  name='UploadPost',
  full_name='UploadPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_UPLOADPOST_REQUEST, _UPLOADPOST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=121,
)


_FETCHPOSTDETAILS_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='FetchPostDetails.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='post_id', full_name='FetchPostDetails.Request.post_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=144,
  serialized_end=170,
)

_FETCHPOSTDETAILS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='FetchPostDetails.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='FetchPostDetails.Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='FetchPostDetails.Response.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='FetchPostDetails.Response.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pictureBlob', full_name='FetchPostDetails.Response.pictureBlob', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=172,
  serialized_end=252,
)

_FETCHPOSTDETAILS = _descriptor.Descriptor(
  name='FetchPostDetails',
  full_name='FetchPostDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_FETCHPOSTDETAILS_REQUEST, _FETCHPOSTDETAILS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=252,
)


_FETCHKPOSTIDS_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='FetchKPostIds.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='k', full_name='FetchKPostIds.Request.k', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=271,
  serialized_end=291,
)

_FETCHKPOSTIDS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='FetchKPostIds.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='FetchKPostIds.Response.id', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=293,
  serialized_end=315,
)

_FETCHKPOSTIDS = _descriptor.Descriptor(
  name='FetchKPostIds',
  full_name='FetchKPostIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_FETCHKPOSTIDS_REQUEST, _FETCHKPOSTIDS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=315,
)

_UPLOADPOST_REQUEST.containing_type = _UPLOADPOST
_UPLOADPOST_RESPONSE.containing_type = _UPLOADPOST
_FETCHPOSTDETAILS_REQUEST.containing_type = _FETCHPOSTDETAILS
_FETCHPOSTDETAILS_RESPONSE.containing_type = _FETCHPOSTDETAILS
_FETCHKPOSTIDS_REQUEST.containing_type = _FETCHKPOSTIDS
_FETCHKPOSTIDS_RESPONSE.containing_type = _FETCHKPOSTIDS
DESCRIPTOR.message_types_by_name['UploadPost'] = _UPLOADPOST
DESCRIPTOR.message_types_by_name['FetchPostDetails'] = _FETCHPOSTDETAILS
DESCRIPTOR.message_types_by_name['FetchKPostIds'] = _FETCHKPOSTIDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadPost = _reflection.GeneratedProtocolMessageType('UploadPost', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _UPLOADPOST_REQUEST,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:UploadPost.Request)
    })
  ,

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _UPLOADPOST_RESPONSE,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:UploadPost.Response)
    })
  ,
  'DESCRIPTOR' : _UPLOADPOST,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:UploadPost)
  })
_sym_db.RegisterMessage(UploadPost)
_sym_db.RegisterMessage(UploadPost.Request)
_sym_db.RegisterMessage(UploadPost.Response)

FetchPostDetails = _reflection.GeneratedProtocolMessageType('FetchPostDetails', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _FETCHPOSTDETAILS_REQUEST,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:FetchPostDetails.Request)
    })
  ,

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FETCHPOSTDETAILS_RESPONSE,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:FetchPostDetails.Response)
    })
  ,
  'DESCRIPTOR' : _FETCHPOSTDETAILS,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:FetchPostDetails)
  })
_sym_db.RegisterMessage(FetchPostDetails)
_sym_db.RegisterMessage(FetchPostDetails.Request)
_sym_db.RegisterMessage(FetchPostDetails.Response)

FetchKPostIds = _reflection.GeneratedProtocolMessageType('FetchKPostIds', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _FETCHKPOSTIDS_REQUEST,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:FetchKPostIds.Request)
    })
  ,

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FETCHKPOSTIDS_RESPONSE,
    '__module__' : 'posts_pb2'
    # @@protoc_insertion_point(class_scope:FetchKPostIds.Response)
    })
  ,
  'DESCRIPTOR' : _FETCHKPOSTIDS,
  '__module__' : 'posts_pb2'
  # @@protoc_insertion_point(class_scope:FetchKPostIds)
  })
_sym_db.RegisterMessage(FetchKPostIds)
_sym_db.RegisterMessage(FetchKPostIds.Request)
_sym_db.RegisterMessage(FetchKPostIds.Response)



_POSTSERVICE = _descriptor.ServiceDescriptor(
  name='PostService',
  full_name='PostService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=318,
  serialized_end=532,
  methods=[
  _descriptor.MethodDescriptor(
    name='uploadPost',
    full_name='PostService.uploadPost',
    index=0,
    containing_service=None,
    input_type=_UPLOADPOST_REQUEST,
    output_type=_UPLOADPOST_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='fetchPostDetails',
    full_name='PostService.fetchPostDetails',
    index=1,
    containing_service=None,
    input_type=_FETCHPOSTDETAILS_REQUEST,
    output_type=_FETCHPOSTDETAILS_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='fetchPosts',
    full_name='PostService.fetchPosts',
    index=2,
    containing_service=None,
    input_type=_FETCHKPOSTIDS_REQUEST,
    output_type=_FETCHKPOSTIDS_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTSERVICE)

DESCRIPTOR.services_by_name['PostService'] = _POSTSERVICE

# @@protoc_insertion_point(module_scope)
