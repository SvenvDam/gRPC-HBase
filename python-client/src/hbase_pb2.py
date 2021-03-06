# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hbase.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hbase.proto',
  package='hbase',
  syntax='proto3',
  serialized_options=b'\n\037com.svenvandam.hbase.grpc.protoB\016HBaseGRPCProtoP\001',
  serialized_pb=b'\n\x0bhbase.proto\x12\x05hbase\x1a\x1egoogle/protobuf/wrappers.proto\"(\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\"\x18\n\x06\x46\x61mily\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\"+\n\x06\x43olumn\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\x11\n\tqualifier\x18\x02 \x01(\t\"M\n\x0cValueVersion\x12\r\n\x05value\x18\x01 \x01(\x0c\x12.\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"R\n\x0c\x43olumnValues\x12\x1d\n\x06\x63olumn\x18\x01 \x01(\x0b\x32\r.hbase.Column\x12#\n\x06values\x18\x02 \x03(\x0b\x32\x13.hbase.ValueVersion\";\n\x06Result\x12\x0b\n\x03row\x18\x01 \x01(\t\x12$\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x13.hbase.ColumnValues\"_\n\x0b\x43olumnQuery\x12\x1f\n\x06\x63olumn\x18\x01 \x01(\x0b\x32\r.hbase.ColumnH\x00\x12\x1f\n\x06\x66\x61mily\x18\x02 \x01(\x0b\x32\r.hbase.FamilyH\x00\x42\x0e\n\x0csealed_value\"\x87\x02\n\nGetRequest\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12\x0b\n\x03row\x18\x02 \x01(\t\x12\x31\n\x0cmax_versions\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08min_time\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08max_time\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12#\n\x07\x63olumns\x18\x06 \x03(\x0b\x32\x12.hbase.ColumnQuery\x12\x19\n\x11include_timestamp\x18\x07 \x01(\x08\"\x8a\x03\n\x0bScanRequest\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12/\n\tstart_row\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08stop_row\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06prefix\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0cmax_versions\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08min_time\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08max_time\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12#\n\x07\x63olumns\x18\x08 \x03(\x0b\x32\x12.hbase.ColumnQuery\x12\x19\n\x11include_timestamp\x18\t \x01(\x08\"[\n\nPutRequest\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12\x0b\n\x03row\x18\x02 \x01(\t\x12#\n\x06values\x18\x03 \x03(\x0b\x32\x13.hbase.ColumnValues\"^\n\rColumnVersion\x12\x1d\n\x06\x63olumn\x18\x01 \x01(\x0b\x32\r.hbase.Column\x12.\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"x\n\rDeleteRequest\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12\x0b\n\x03row\x18\x02 \x01(\t\x12\x16\n\x0esingle_version\x18\x03 \x01(\x08\x12%\n\x07\x63olumns\x18\x04 \x03(\x0b\x32\x14.hbase.ColumnVersion\"\x04\n\x02OK2\xbc\x01\n\x0cHBaseService\x12)\n\x03Get\x12\x11.hbase.GetRequest\x1a\r.hbase.Result\"\x00\x12-\n\x04Scan\x12\x12.hbase.ScanRequest\x1a\r.hbase.Result\"\x00\x30\x01\x12+\n\x06\x44\x65lete\x12\x14.hbase.DeleteRequest\x1a\t.hbase.OK\"\x00\x12%\n\x03Put\x12\x11.hbase.PutRequest\x1a\t.hbase.OK\"\x00\x42\x33\n\x1f\x63om.svenvandam.hbase.grpc.protoB\x0eHBaseGRPCProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='hbase.Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hbase.Table.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='hbase.Table.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=54,
  serialized_end=94,
)


_FAMILY = _descriptor.Descriptor(
  name='Family',
  full_name='hbase.Family',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='hbase.Family.family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=96,
  serialized_end=120,
)


_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='hbase.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='hbase.Column.family', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qualifier', full_name='hbase.Column.qualifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=122,
  serialized_end=165,
)


_VALUEVERSION = _descriptor.Descriptor(
  name='ValueVersion',
  full_name='hbase.ValueVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='hbase.ValueVersion.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hbase.ValueVersion.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=167,
  serialized_end=244,
)


_COLUMNVALUES = _descriptor.Descriptor(
  name='ColumnValues',
  full_name='hbase.ColumnValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='hbase.ColumnValues.column', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='hbase.ColumnValues.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=246,
  serialized_end=328,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='hbase.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.Result.row', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.Result.columns', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=330,
  serialized_end=389,
)


_COLUMNQUERY = _descriptor.Descriptor(
  name='ColumnQuery',
  full_name='hbase.ColumnQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='hbase.ColumnQuery.column', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family', full_name='hbase.ColumnQuery.family', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='sealed_value', full_name='hbase.ColumnQuery.sealed_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=391,
  serialized_end=486,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='hbase.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.GetRequest.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.GetRequest.row', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_versions', full_name='hbase.GetRequest.max_versions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_time', full_name='hbase.GetRequest.min_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_time', full_name='hbase.GetRequest.max_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.GetRequest.columns', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_timestamp', full_name='hbase.GetRequest.include_timestamp', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=489,
  serialized_end=752,
)


_SCANREQUEST = _descriptor.Descriptor(
  name='ScanRequest',
  full_name='hbase.ScanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.ScanRequest.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_row', full_name='hbase.ScanRequest.start_row', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_row', full_name='hbase.ScanRequest.stop_row', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='hbase.ScanRequest.prefix', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_versions', full_name='hbase.ScanRequest.max_versions', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_time', full_name='hbase.ScanRequest.min_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_time', full_name='hbase.ScanRequest.max_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.ScanRequest.columns', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_timestamp', full_name='hbase.ScanRequest.include_timestamp', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=755,
  serialized_end=1149,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='hbase.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.PutRequest.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.PutRequest.row', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='hbase.PutRequest.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1151,
  serialized_end=1242,
)


_COLUMNVERSION = _descriptor.Descriptor(
  name='ColumnVersion',
  full_name='hbase.ColumnVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column', full_name='hbase.ColumnVersion.column', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hbase.ColumnVersion.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1244,
  serialized_end=1338,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='hbase.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.DeleteRequest.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.DeleteRequest.row', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_version', full_name='hbase.DeleteRequest.single_version', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.DeleteRequest.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1340,
  serialized_end=1460,
)


_OK = _descriptor.Descriptor(
  name='OK',
  full_name='hbase.OK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1462,
  serialized_end=1466,
)

_VALUEVERSION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_COLUMNVALUES.fields_by_name['column'].message_type = _COLUMN
_COLUMNVALUES.fields_by_name['values'].message_type = _VALUEVERSION
_RESULT.fields_by_name['columns'].message_type = _COLUMNVALUES
_COLUMNQUERY.fields_by_name['column'].message_type = _COLUMN
_COLUMNQUERY.fields_by_name['family'].message_type = _FAMILY
_COLUMNQUERY.oneofs_by_name['sealed_value'].fields.append(
  _COLUMNQUERY.fields_by_name['column'])
_COLUMNQUERY.fields_by_name['column'].containing_oneof = _COLUMNQUERY.oneofs_by_name['sealed_value']
_COLUMNQUERY.oneofs_by_name['sealed_value'].fields.append(
  _COLUMNQUERY.fields_by_name['family'])
_COLUMNQUERY.fields_by_name['family'].containing_oneof = _COLUMNQUERY.oneofs_by_name['sealed_value']
_GETREQUEST.fields_by_name['table'].message_type = _TABLE
_GETREQUEST.fields_by_name['max_versions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_GETREQUEST.fields_by_name['min_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GETREQUEST.fields_by_name['max_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GETREQUEST.fields_by_name['columns'].message_type = _COLUMNQUERY
_SCANREQUEST.fields_by_name['table'].message_type = _TABLE
_SCANREQUEST.fields_by_name['start_row'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCANREQUEST.fields_by_name['stop_row'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCANREQUEST.fields_by_name['prefix'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCANREQUEST.fields_by_name['max_versions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SCANREQUEST.fields_by_name['min_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SCANREQUEST.fields_by_name['max_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SCANREQUEST.fields_by_name['columns'].message_type = _COLUMNQUERY
_PUTREQUEST.fields_by_name['table'].message_type = _TABLE
_PUTREQUEST.fields_by_name['values'].message_type = _COLUMNVALUES
_COLUMNVERSION.fields_by_name['column'].message_type = _COLUMN
_COLUMNVERSION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_DELETEREQUEST.fields_by_name['table'].message_type = _TABLE
_DELETEREQUEST.fields_by_name['columns'].message_type = _COLUMNVERSION
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['Family'] = _FAMILY
DESCRIPTOR.message_types_by_name['Column'] = _COLUMN
DESCRIPTOR.message_types_by_name['ValueVersion'] = _VALUEVERSION
DESCRIPTOR.message_types_by_name['ColumnValues'] = _COLUMNVALUES
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['ColumnQuery'] = _COLUMNQUERY
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['ScanRequest'] = _SCANREQUEST
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['ColumnVersion'] = _COLUMNVERSION
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['OK'] = _OK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Table)
  })
_sym_db.RegisterMessage(Table)

Family = _reflection.GeneratedProtocolMessageType('Family', (_message.Message,), {
  'DESCRIPTOR' : _FAMILY,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Family)
  })
_sym_db.RegisterMessage(Family)

Column = _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {
  'DESCRIPTOR' : _COLUMN,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Column)
  })
_sym_db.RegisterMessage(Column)

ValueVersion = _reflection.GeneratedProtocolMessageType('ValueVersion', (_message.Message,), {
  'DESCRIPTOR' : _VALUEVERSION,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.ValueVersion)
  })
_sym_db.RegisterMessage(ValueVersion)

ColumnValues = _reflection.GeneratedProtocolMessageType('ColumnValues', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNVALUES,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.ColumnValues)
  })
_sym_db.RegisterMessage(ColumnValues)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Result)
  })
_sym_db.RegisterMessage(Result)

ColumnQuery = _reflection.GeneratedProtocolMessageType('ColumnQuery', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNQUERY,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.ColumnQuery)
  })
_sym_db.RegisterMessage(ColumnQuery)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

ScanRequest = _reflection.GeneratedProtocolMessageType('ScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCANREQUEST,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.ScanRequest)
  })
_sym_db.RegisterMessage(ScanRequest)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

ColumnVersion = _reflection.GeneratedProtocolMessageType('ColumnVersion', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNVERSION,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.ColumnVersion)
  })
_sym_db.RegisterMessage(ColumnVersion)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

OK = _reflection.GeneratedProtocolMessageType('OK', (_message.Message,), {
  'DESCRIPTOR' : _OK,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.OK)
  })
_sym_db.RegisterMessage(OK)


DESCRIPTOR._options = None

_HBASESERVICE = _descriptor.ServiceDescriptor(
  name='HBaseService',
  full_name='hbase.HBaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1469,
  serialized_end=1657,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='hbase.HBaseService.Get',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Scan',
    full_name='hbase.HBaseService.Scan',
    index=1,
    containing_service=None,
    input_type=_SCANREQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='hbase.HBaseService.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_OK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='hbase.HBaseService.Put',
    index=3,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_OK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HBASESERVICE)

DESCRIPTOR.services_by_name['HBaseService'] = _HBASESERVICE

# @@protoc_insertion_point(module_scope)
