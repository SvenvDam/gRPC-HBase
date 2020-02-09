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
  serialized_pb=b'\n\x0bhbase.proto\x12\x05hbase\x1a\x1egoogle/protobuf/wrappers.proto\"(\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\"\x1a\n\x07\x43olumns\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\"\xaa\x02\n\x03Get\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12\x0b\n\x03row\x18\x02 \x01(\t\x12\x31\n\x0cmax_versions\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08min_time\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08max_time\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12(\n\x07\x63olumns\x18\x06 \x03(\x0b\x32\x17.hbase.Get.ColumnsEntry\x1a>\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.hbase.Columns:\x02\x38\x01\"\xae\x03\n\x04Scan\x12\x1b\n\x05table\x18\x01 \x01(\x0b\x32\x0c.hbase.Table\x12/\n\tstart_row\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08stop_row\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06prefix\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0cmax_versions\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08min_time\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08max_time\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12)\n\x07\x63olumns\x18\x08 \x03(\x0b\x32\x18.hbase.Scan.ColumnsEntry\x1a>\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.hbase.Columns:\x02\x38\x01\"X\n\x04\x43\x65ll\x12\x0b\n\x03row\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\x11\n\tqualifier\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\r\n\x05value\x18\x05 \x01(\x0c\"$\n\x06Result\x12\x1a\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x0b.hbase.Cell2X\n\x0cHBaseService\x12\"\n\x03get\x12\n.hbase.Get\x1a\x0b.hbase.Cell\"\x00\x30\x01\x12$\n\x04scan\x12\x0b.hbase.Scan\x1a\x0b.hbase.Cell\"\x00\x30\x01\x42\x33\n\x1f\x63om.svenvandam.hbase.grpc.protoB\x0eHBaseGRPCProtoP\x01\x62\x06proto3'
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


_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='hbase.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.Columns.columns', index=0,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=96,
  serialized_end=122,
)


_GET_COLUMNSENTRY = _descriptor.Descriptor(
  name='ColumnsEntry',
  full_name='hbase.Get.ColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hbase.Get.ColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='hbase.Get.ColumnsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=423,
)

_GET = _descriptor.Descriptor(
  name='Get',
  full_name='hbase.Get',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.Get.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.Get.row', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_versions', full_name='hbase.Get.max_versions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_time', full_name='hbase.Get.min_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_time', full_name='hbase.Get.max_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.Get.columns', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GET_COLUMNSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=423,
)


_SCAN_COLUMNSENTRY = _descriptor.Descriptor(
  name='ColumnsEntry',
  full_name='hbase.Scan.ColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hbase.Scan.ColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='hbase.Scan.ColumnsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=423,
)

_SCAN = _descriptor.Descriptor(
  name='Scan',
  full_name='hbase.Scan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='hbase.Scan.table', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_row', full_name='hbase.Scan.start_row', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_row', full_name='hbase.Scan.stop_row', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='hbase.Scan.prefix', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_versions', full_name='hbase.Scan.max_versions', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_time', full_name='hbase.Scan.min_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_time', full_name='hbase.Scan.max_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='hbase.Scan.columns', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCAN_COLUMNSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=856,
)


_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='hbase.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='hbase.Cell.row', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family', full_name='hbase.Cell.family', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qualifier', full_name='hbase.Cell.qualifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hbase.Cell.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='hbase.Cell.value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=858,
  serialized_end=946,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='hbase.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='hbase.Result.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=948,
  serialized_end=984,
)

_GET_COLUMNSENTRY.fields_by_name['value'].message_type = _COLUMNS
_GET_COLUMNSENTRY.containing_type = _GET
_GET.fields_by_name['table'].message_type = _TABLE
_GET.fields_by_name['max_versions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_GET.fields_by_name['min_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GET.fields_by_name['max_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_GET.fields_by_name['columns'].message_type = _GET_COLUMNSENTRY
_SCAN_COLUMNSENTRY.fields_by_name['value'].message_type = _COLUMNS
_SCAN_COLUMNSENTRY.containing_type = _SCAN
_SCAN.fields_by_name['table'].message_type = _TABLE
_SCAN.fields_by_name['start_row'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCAN.fields_by_name['stop_row'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCAN.fields_by_name['prefix'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SCAN.fields_by_name['max_versions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SCAN.fields_by_name['min_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SCAN.fields_by_name['max_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SCAN.fields_by_name['columns'].message_type = _SCAN_COLUMNSENTRY
_RESULT.fields_by_name['cells'].message_type = _CELL
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['Columns'] = _COLUMNS
DESCRIPTOR.message_types_by_name['Get'] = _GET
DESCRIPTOR.message_types_by_name['Scan'] = _SCAN
DESCRIPTOR.message_types_by_name['Cell'] = _CELL
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Table)
  })
_sym_db.RegisterMessage(Table)

Columns = _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNS,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Columns)
  })
_sym_db.RegisterMessage(Columns)

Get = _reflection.GeneratedProtocolMessageType('Get', (_message.Message,), {

  'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GET_COLUMNSENTRY,
    '__module__' : 'hbase_pb2'
    # @@protoc_insertion_point(class_scope:hbase.Get.ColumnsEntry)
    })
  ,
  'DESCRIPTOR' : _GET,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Get)
  })
_sym_db.RegisterMessage(Get)
_sym_db.RegisterMessage(Get.ColumnsEntry)

Scan = _reflection.GeneratedProtocolMessageType('Scan', (_message.Message,), {

  'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCAN_COLUMNSENTRY,
    '__module__' : 'hbase_pb2'
    # @@protoc_insertion_point(class_scope:hbase.Scan.ColumnsEntry)
    })
  ,
  'DESCRIPTOR' : _SCAN,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Scan)
  })
_sym_db.RegisterMessage(Scan)
_sym_db.RegisterMessage(Scan.ColumnsEntry)

Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), {
  'DESCRIPTOR' : _CELL,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Cell)
  })
_sym_db.RegisterMessage(Cell)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'hbase_pb2'
  # @@protoc_insertion_point(class_scope:hbase.Result)
  })
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None
_GET_COLUMNSENTRY._options = None
_SCAN_COLUMNSENTRY._options = None

_HBASESERVICE = _descriptor.ServiceDescriptor(
  name='HBaseService',
  full_name='hbase.HBaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=986,
  serialized_end=1074,
  methods=[
  _descriptor.MethodDescriptor(
    name='get',
    full_name='hbase.HBaseService.get',
    index=0,
    containing_service=None,
    input_type=_GET,
    output_type=_CELL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='scan',
    full_name='hbase.HBaseService.scan',
    index=1,
    containing_service=None,
    input_type=_SCAN,
    output_type=_CELL,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HBASESERVICE)

DESCRIPTOR.services_by_name['HBaseService'] = _HBASESERVICE

# @@protoc_insertion_point(module_scope)