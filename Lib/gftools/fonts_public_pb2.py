# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fonts_public.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fonts_public.proto',
  package='google.fonts',
  syntax='proto2',
  serialized_options=_b('\n\026com.google.fonts.protoB\013FontsPublic'),
  serialized_pb=_b('\n\x12\x66onts_public.proto\x12\x0cgoogle.fonts\"\xc0\x03\n\x0b\x46\x61milyProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x64\x65signer\x18\x02 \x02(\t\x12\x0f\n\x07license\x18\x03 \x02(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x02(\t\x12\x12\n\ndate_added\x18\x05 \x02(\t\x12&\n\x05\x66onts\x18\x06 \x03(\x0b\x32\x17.google.fonts.FontProto\x12\x0f\n\x07\x61liases\x18\x07 \x03(\t\x12\x0f\n\x07subsets\x18\x08 \x03(\t\x12\x19\n\x11ttf_autohint_args\x18\t \x01(\t\x12,\n\x04\x61xes\x18\n \x03(\x0b\x32\x1e.google.fonts.AxisSegmentProto\x12[\n\x1aregistry_default_overrides\x18\x0b \x03(\x0b\x32\x37.google.fonts.FamilyProto.RegistryDefaultOverridesEntry\x12)\n\x06source\x18\x0c \x01(\x0b\x32\x19.google.fonts.SourceProto\x1a?\n\x1dRegistryDefaultOverridesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x8a\x01\n\tFontProto\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05style\x18\x02 \x02(\t\x12\x0e\n\x06weight\x18\x03 \x02(\x05\x12\x10\n\x08\x66ilename\x18\x04 \x02(\t\x12\x18\n\x10post_script_name\x18\x05 \x02(\t\x12\x11\n\tfull_name\x18\x06 \x02(\t\x12\x11\n\tcopyright\x18\x07 \x01(\t\"Z\n\x10\x41xisSegmentProto\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x02\x12\x11\n\tmax_value\x18\x04 \x01(\x02J\x04\x08\x03\x10\x04R\rdefault_value\"5\n\x0bSourceProto\x12\x16\n\x0erepository_url\x18\x01 \x01(\t\x12\x0e\n\x06\x63ommit\x18\x02 \x01(\tB%\n\x16\x63om.google.fonts.protoB\x0b\x46ontsPublic')
)




_FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY = _descriptor.Descriptor(
  name='RegistryDefaultOverridesEntry',
  full_name='google.fonts.FamilyProto.RegistryDefaultOverridesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.fonts.FamilyProto.RegistryDefaultOverridesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.fonts.FamilyProto.RegistryDefaultOverridesEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=485,
)

_FAMILYPROTO = _descriptor.Descriptor(
  name='FamilyProto',
  full_name='google.fonts.FamilyProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.fonts.FamilyProto.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='designer', full_name='google.fonts.FamilyProto.designer', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='license', full_name='google.fonts.FamilyProto.license', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='google.fonts.FamilyProto.category', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_added', full_name='google.fonts.FamilyProto.date_added', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fonts', full_name='google.fonts.FamilyProto.fonts', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='google.fonts.FamilyProto.aliases', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subsets', full_name='google.fonts.FamilyProto.subsets', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttf_autohint_args', full_name='google.fonts.FamilyProto.ttf_autohint_args', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='axes', full_name='google.fonts.FamilyProto.axes', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_default_overrides', full_name='google.fonts.FamilyProto.registry_default_overrides', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.fonts.FamilyProto.source', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=485,
)


_FONTPROTO = _descriptor.Descriptor(
  name='FontProto',
  full_name='google.fonts.FontProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.fonts.FontProto.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='google.fonts.FontProto.style', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='google.fonts.FontProto.weight', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='google.fonts.FontProto.filename', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_script_name', full_name='google.fonts.FontProto.post_script_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='google.fonts.FontProto.full_name', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='google.fonts.FontProto.copyright', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=626,
)


_AXISSEGMENTPROTO = _descriptor.Descriptor(
  name='AxisSegmentProto',
  full_name='google.fonts.AxisSegmentProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='google.fonts.AxisSegmentProto.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='google.fonts.AxisSegmentProto.min_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='google.fonts.AxisSegmentProto.max_value', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=718,
)


_SOURCEPROTO = _descriptor.Descriptor(
  name='SourceProto',
  full_name='google.fonts.SourceProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository_url', full_name='google.fonts.SourceProto.repository_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit', full_name='google.fonts.SourceProto.commit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=720,
  serialized_end=773,
)

_FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY.containing_type = _FAMILYPROTO
_FAMILYPROTO.fields_by_name['fonts'].message_type = _FONTPROTO
_FAMILYPROTO.fields_by_name['axes'].message_type = _AXISSEGMENTPROTO
_FAMILYPROTO.fields_by_name['registry_default_overrides'].message_type = _FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY
_FAMILYPROTO.fields_by_name['source'].message_type = _SOURCEPROTO
DESCRIPTOR.message_types_by_name['FamilyProto'] = _FAMILYPROTO
DESCRIPTOR.message_types_by_name['FontProto'] = _FONTPROTO
DESCRIPTOR.message_types_by_name['AxisSegmentProto'] = _AXISSEGMENTPROTO
DESCRIPTOR.message_types_by_name['SourceProto'] = _SOURCEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FamilyProto = _reflection.GeneratedProtocolMessageType('FamilyProto', (_message.Message,), dict(

  RegistryDefaultOverridesEntry = _reflection.GeneratedProtocolMessageType('RegistryDefaultOverridesEntry', (_message.Message,), dict(
    DESCRIPTOR = _FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY,
    __module__ = 'fonts_public_pb2'
    # @@protoc_insertion_point(class_scope:google.fonts.FamilyProto.RegistryDefaultOverridesEntry)
    ))
  ,
  DESCRIPTOR = _FAMILYPROTO,
  __module__ = 'fonts_public_pb2'
  # @@protoc_insertion_point(class_scope:google.fonts.FamilyProto)
  ))
_sym_db.RegisterMessage(FamilyProto)
_sym_db.RegisterMessage(FamilyProto.RegistryDefaultOverridesEntry)

FontProto = _reflection.GeneratedProtocolMessageType('FontProto', (_message.Message,), dict(
  DESCRIPTOR = _FONTPROTO,
  __module__ = 'fonts_public_pb2'
  # @@protoc_insertion_point(class_scope:google.fonts.FontProto)
  ))
_sym_db.RegisterMessage(FontProto)

AxisSegmentProto = _reflection.GeneratedProtocolMessageType('AxisSegmentProto', (_message.Message,), dict(
  DESCRIPTOR = _AXISSEGMENTPROTO,
  __module__ = 'fonts_public_pb2'
  # @@protoc_insertion_point(class_scope:google.fonts.AxisSegmentProto)
  ))
_sym_db.RegisterMessage(AxisSegmentProto)

SourceProto = _reflection.GeneratedProtocolMessageType('SourceProto', (_message.Message,), dict(
  DESCRIPTOR = _SOURCEPROTO,
  __module__ = 'fonts_public_pb2'
  # @@protoc_insertion_point(class_scope:google.fonts.SourceProto)
  ))
_sym_db.RegisterMessage(SourceProto)


DESCRIPTOR._options = None
_FAMILYPROTO_REGISTRYDEFAULTOVERRIDESENTRY._options = None
# @@protoc_insertion_point(module_scope)
