# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strategy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='strategy.proto',
  package='strategy_proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0estrategy.proto\x12\x0estrategy_proto\x1a\x1cgoogle/protobuf/struct.proto\"+\n\rHistoryParams\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0e\n\x06Length\x18\x02 \x01(\x05\"(\n\nTimeSeries\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x03(\x01\"1\n\x07History\x12&\n\x02TS\x18\x01 \x03(\x0b\x32\x1a.strategy_proto.TimeSeries\"\x1e\n\x03Tmp\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0b\n\x03tmp\x18\x02 \x01(\x05\"\x9f\x01\n\tSelection\x12\n\n\x02ID\x18\x01 \x01(\t\x12\r\n\x05\x41sset\x18\x02 \x01(\t\x12\x10\n\x08Strategy\x18\x03 \x01(\t\x12+\n\nParameters\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07\x43\x61pital\x18\x05 \x01(\x05\x12\x12\n\nInstrument\x18\x06 \x01(\t\x12\x13\n\x0bGranularity\x18\x07 \x01(\t\"!\n\x13StartAlgorithmParam\x12\n\n\x02ID\x18\x01 \x01(\t\"\'\n\x16StartAlgorithmResponse\x12\r\n\x05\x45rror\x18\x01 \x01(\t\" \n\x12StopAlgorithmParam\x12\n\n\x02ID\x18\x01 \x01(\t\"&\n\x15StopAlgorithmResponse\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"\x1d\n\x0fGetBalanceParam\x12\n\n\x02ID\x18\x01 \x01(\t\" \n\rGetBalanceRes\x12\x0f\n\x07\x42\x61lance\x18\x01 \x01(\x01\"\xed\x01\n\nStatistics\x12\t\n\x01v\x18\x01 \x01(\x01\x12\t\n\x01t\x18\x02 \x01(\x01\x12\t\n\x01o\x18\x03 \x01(\x01\x12\t\n\x01h\x18\x04 \x01(\x01\x12\t\n\x01l\x18\x05 \x01(\x01\x12\t\n\x01\x63\x18\x06 \x01(\x01\x12\x0e\n\x06\x61\x63tion\x18\x07 \x01(\x01\x12\x16\n\x0e\x62\x61lance_change\x18\x08 \x01(\x01\x12\r\n\x05stock\x18\t \x01(\x01\x12\x0f\n\x07\x62\x61lance\x18\n \x01(\x01\x12\x0e\n\x06return\x18\x0b \x01(\x01\x12\r\n\x05\x61lpha\x18\x0c \x01(\x01\x12\x0e\n\x06sharpe\x18\r \x01(\x01\x12\x15\n\rannual_sharpe\x18\x0e \x01(\x01\x12\x0f\n\x07sortino\x18\x0f \x01(\x01\x32\xcb\x05\n\x0fStrategyService\x12N\n\x13InitialiseAlgorithm\x12\x19.strategy_proto.Selection\x1a\x1a.strategy_proto.Statistics\"\x00\x12_\n\x0eStartAlgorithm\x12#.strategy_proto.StartAlgorithmParam\x1a&.strategy_proto.StartAlgorithmResponse\"\x00\x12\\\n\rStopAlgorithm\x12\".strategy_proto.StopAlgorithmParam\x1a%.strategy_proto.StopAlgorithmResponse\"\x00\x12\x38\n\x03\x41\x63t\x12\x13.strategy_proto.Tmp\x1a\x1a.strategy_proto.Statistics\"\x00\x12\x42\n\rGetStatistics\x12\x13.strategy_proto.Tmp\x1a\x1a.strategy_proto.Statistics\"\x00\x12\x43\n\x07GetData\x12\x1d.strategy_proto.HistoryParams\x1a\x17.strategy_proto.History\"\x00\x12I\n\rGetIndicators\x12\x1d.strategy_proto.HistoryParams\x1a\x17.strategy_proto.History\"\x00\x12K\n\x0fGetPerformances\x12\x1d.strategy_proto.HistoryParams\x1a\x17.strategy_proto.History\"\x00\x12N\n\nGetBalance\x12\x1f.strategy_proto.GetBalanceParam\x1a\x1d.strategy_proto.GetBalanceRes\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_HISTORYPARAMS = _descriptor.Descriptor(
  name='HistoryParams',
  full_name='strategy_proto.HistoryParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.HistoryParams.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Length', full_name='strategy_proto.HistoryParams.Length', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=107,
)


_TIMESERIES = _descriptor.Descriptor(
  name='TimeSeries',
  full_name='strategy_proto.TimeSeries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Key', full_name='strategy_proto.TimeSeries.Key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='strategy_proto.TimeSeries.Value', index=1,
      number=2, type=1, cpp_type=5, label=3,
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
  serialized_start=109,
  serialized_end=149,
)


_HISTORY = _descriptor.Descriptor(
  name='History',
  full_name='strategy_proto.History',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='TS', full_name='strategy_proto.History.TS', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=151,
  serialized_end=200,
)


_TMP = _descriptor.Descriptor(
  name='Tmp',
  full_name='strategy_proto.Tmp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.Tmp.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tmp', full_name='strategy_proto.Tmp.tmp', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=202,
  serialized_end=232,
)


_SELECTION = _descriptor.Descriptor(
  name='Selection',
  full_name='strategy_proto.Selection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.Selection.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Asset', full_name='strategy_proto.Selection.Asset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Strategy', full_name='strategy_proto.Selection.Strategy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Parameters', full_name='strategy_proto.Selection.Parameters', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Capital', full_name='strategy_proto.Selection.Capital', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Instrument', full_name='strategy_proto.Selection.Instrument', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Granularity', full_name='strategy_proto.Selection.Granularity', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=235,
  serialized_end=394,
)


_STARTALGORITHMPARAM = _descriptor.Descriptor(
  name='StartAlgorithmParam',
  full_name='strategy_proto.StartAlgorithmParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.StartAlgorithmParam.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=396,
  serialized_end=429,
)


_STARTALGORITHMRESPONSE = _descriptor.Descriptor(
  name='StartAlgorithmResponse',
  full_name='strategy_proto.StartAlgorithmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='strategy_proto.StartAlgorithmResponse.Error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=431,
  serialized_end=470,
)


_STOPALGORITHMPARAM = _descriptor.Descriptor(
  name='StopAlgorithmParam',
  full_name='strategy_proto.StopAlgorithmParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.StopAlgorithmParam.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=472,
  serialized_end=504,
)


_STOPALGORITHMRESPONSE = _descriptor.Descriptor(
  name='StopAlgorithmResponse',
  full_name='strategy_proto.StopAlgorithmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Error', full_name='strategy_proto.StopAlgorithmResponse.Error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=506,
  serialized_end=544,
)


_GETBALANCEPARAM = _descriptor.Descriptor(
  name='GetBalanceParam',
  full_name='strategy_proto.GetBalanceParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='strategy_proto.GetBalanceParam.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=546,
  serialized_end=575,
)


_GETBALANCERES = _descriptor.Descriptor(
  name='GetBalanceRes',
  full_name='strategy_proto.GetBalanceRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Balance', full_name='strategy_proto.GetBalanceRes.Balance', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=577,
  serialized_end=609,
)


_STATISTICS = _descriptor.Descriptor(
  name='Statistics',
  full_name='strategy_proto.Statistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='v', full_name='strategy_proto.Statistics.v', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='t', full_name='strategy_proto.Statistics.t', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='o', full_name='strategy_proto.Statistics.o', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='strategy_proto.Statistics.h', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l', full_name='strategy_proto.Statistics.l', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c', full_name='strategy_proto.Statistics.c', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='strategy_proto.Statistics.action', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance_change', full_name='strategy_proto.Statistics.balance_change', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stock', full_name='strategy_proto.Statistics.stock', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='strategy_proto.Statistics.balance', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return', full_name='strategy_proto.Statistics.return', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='strategy_proto.Statistics.alpha', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sharpe', full_name='strategy_proto.Statistics.sharpe', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annual_sharpe', full_name='strategy_proto.Statistics.annual_sharpe', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sortino', full_name='strategy_proto.Statistics.sortino', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=612,
  serialized_end=849,
)

_HISTORY.fields_by_name['TS'].message_type = _TIMESERIES
_SELECTION.fields_by_name['Parameters'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['HistoryParams'] = _HISTORYPARAMS
DESCRIPTOR.message_types_by_name['TimeSeries'] = _TIMESERIES
DESCRIPTOR.message_types_by_name['History'] = _HISTORY
DESCRIPTOR.message_types_by_name['Tmp'] = _TMP
DESCRIPTOR.message_types_by_name['Selection'] = _SELECTION
DESCRIPTOR.message_types_by_name['StartAlgorithmParam'] = _STARTALGORITHMPARAM
DESCRIPTOR.message_types_by_name['StartAlgorithmResponse'] = _STARTALGORITHMRESPONSE
DESCRIPTOR.message_types_by_name['StopAlgorithmParam'] = _STOPALGORITHMPARAM
DESCRIPTOR.message_types_by_name['StopAlgorithmResponse'] = _STOPALGORITHMRESPONSE
DESCRIPTOR.message_types_by_name['GetBalanceParam'] = _GETBALANCEPARAM
DESCRIPTOR.message_types_by_name['GetBalanceRes'] = _GETBALANCERES
DESCRIPTOR.message_types_by_name['Statistics'] = _STATISTICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HistoryParams = _reflection.GeneratedProtocolMessageType('HistoryParams', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYPARAMS,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.HistoryParams)
  })
_sym_db.RegisterMessage(HistoryParams)

TimeSeries = _reflection.GeneratedProtocolMessageType('TimeSeries', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIES,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.TimeSeries)
  })
_sym_db.RegisterMessage(TimeSeries)

History = _reflection.GeneratedProtocolMessageType('History', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.History)
  })
_sym_db.RegisterMessage(History)

Tmp = _reflection.GeneratedProtocolMessageType('Tmp', (_message.Message,), {
  'DESCRIPTOR' : _TMP,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.Tmp)
  })
_sym_db.RegisterMessage(Tmp)

Selection = _reflection.GeneratedProtocolMessageType('Selection', (_message.Message,), {
  'DESCRIPTOR' : _SELECTION,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.Selection)
  })
_sym_db.RegisterMessage(Selection)

StartAlgorithmParam = _reflection.GeneratedProtocolMessageType('StartAlgorithmParam', (_message.Message,), {
  'DESCRIPTOR' : _STARTALGORITHMPARAM,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.StartAlgorithmParam)
  })
_sym_db.RegisterMessage(StartAlgorithmParam)

StartAlgorithmResponse = _reflection.GeneratedProtocolMessageType('StartAlgorithmResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTALGORITHMRESPONSE,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.StartAlgorithmResponse)
  })
_sym_db.RegisterMessage(StartAlgorithmResponse)

StopAlgorithmParam = _reflection.GeneratedProtocolMessageType('StopAlgorithmParam', (_message.Message,), {
  'DESCRIPTOR' : _STOPALGORITHMPARAM,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.StopAlgorithmParam)
  })
_sym_db.RegisterMessage(StopAlgorithmParam)

StopAlgorithmResponse = _reflection.GeneratedProtocolMessageType('StopAlgorithmResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPALGORITHMRESPONSE,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.StopAlgorithmResponse)
  })
_sym_db.RegisterMessage(StopAlgorithmResponse)

GetBalanceParam = _reflection.GeneratedProtocolMessageType('GetBalanceParam', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCEPARAM,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.GetBalanceParam)
  })
_sym_db.RegisterMessage(GetBalanceParam)

GetBalanceRes = _reflection.GeneratedProtocolMessageType('GetBalanceRes', (_message.Message,), {
  'DESCRIPTOR' : _GETBALANCERES,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.GetBalanceRes)
  })
_sym_db.RegisterMessage(GetBalanceRes)

Statistics = _reflection.GeneratedProtocolMessageType('Statistics', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICS,
  '__module__' : 'strategy_pb2'
  # @@protoc_insertion_point(class_scope:strategy_proto.Statistics)
  })
_sym_db.RegisterMessage(Statistics)



_STRATEGYSERVICE = _descriptor.ServiceDescriptor(
  name='StrategyService',
  full_name='strategy_proto.StrategyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=852,
  serialized_end=1567,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitialiseAlgorithm',
    full_name='strategy_proto.StrategyService.InitialiseAlgorithm',
    index=0,
    containing_service=None,
    input_type=_SELECTION,
    output_type=_STATISTICS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StartAlgorithm',
    full_name='strategy_proto.StrategyService.StartAlgorithm',
    index=1,
    containing_service=None,
    input_type=_STARTALGORITHMPARAM,
    output_type=_STARTALGORITHMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopAlgorithm',
    full_name='strategy_proto.StrategyService.StopAlgorithm',
    index=2,
    containing_service=None,
    input_type=_STOPALGORITHMPARAM,
    output_type=_STOPALGORITHMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Act',
    full_name='strategy_proto.StrategyService.Act',
    index=3,
    containing_service=None,
    input_type=_TMP,
    output_type=_STATISTICS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatistics',
    full_name='strategy_proto.StrategyService.GetStatistics',
    index=4,
    containing_service=None,
    input_type=_TMP,
    output_type=_STATISTICS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='strategy_proto.StrategyService.GetData',
    index=5,
    containing_service=None,
    input_type=_HISTORYPARAMS,
    output_type=_HISTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetIndicators',
    full_name='strategy_proto.StrategyService.GetIndicators',
    index=6,
    containing_service=None,
    input_type=_HISTORYPARAMS,
    output_type=_HISTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPerformances',
    full_name='strategy_proto.StrategyService.GetPerformances',
    index=7,
    containing_service=None,
    input_type=_HISTORYPARAMS,
    output_type=_HISTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBalance',
    full_name='strategy_proto.StrategyService.GetBalance',
    index=8,
    containing_service=None,
    input_type=_GETBALANCEPARAM,
    output_type=_GETBALANCERES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STRATEGYSERVICE)

DESCRIPTOR.services_by_name['StrategyService'] = _STRATEGYSERVICE

# @@protoc_insertion_point(module_scope)
