# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63hatservice.proto\"a\n\x12\x43hatMessageRequest\x12\x11\n\tthread_id\x18\x01 \x01(\x04\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x03 \x01(\x04\x12\x14\n\x0crecipient_id\x18\x04 \x01(\x04\"!\n\x13\x43hatMessageResponse\x12\n\n\x02id\x18\x01 \x01(\x04\"f\n\x0b\x43hatMessage\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tthread_id\x18\x02 \x01(\x04\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x11\n\tsender_id\x18\x04 \x01(\x04\x12\x14\n\x0crecipient_id\x18\x05 \x01(\x04\"\"\n\nChatClient\x12\x14\n\x0crecipient_id\x18\x01 \x01(\x04\x32w\n\x0b\x43hatService\x12\x38\n\x0bSendMessage\x12\x13.ChatMessageRequest\x1a\x14.ChatMessageResponse\x12.\n\x0fReceiveMessages\x12\x0b.ChatClient\x1a\x0c.ChatMessage0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHATMESSAGEREQUEST._serialized_start=21
  _CHATMESSAGEREQUEST._serialized_end=118
  _CHATMESSAGERESPONSE._serialized_start=120
  _CHATMESSAGERESPONSE._serialized_end=153
  _CHATMESSAGE._serialized_start=155
  _CHATMESSAGE._serialized_end=257
  _CHATCLIENT._serialized_start=259
  _CHATCLIENT._serialized_end=293
  _CHATSERVICE._serialized_start=295
  _CHATSERVICE._serialized_end=414
# @@protoc_insertion_point(module_scope)
