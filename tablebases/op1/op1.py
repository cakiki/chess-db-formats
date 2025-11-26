# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
from zstd import Zstd


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Op1(KaitaiStruct):

    class Compression(IntEnum):
        none = 0
        zstd = 2

    class MetricType(IntEnum):
        dtc = 1

    class Side(IntEnum):
        white = 0
        black = 1
    def __init__(self, _io, _parent=None, _root=None):
        super(Op1, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.header = Op1.Header(self._io, self, self._root)
        self.offsets = []
        for i in range(self.header.num_blocks + 1):
            self.offsets.append(self._io.read_u8le())

        self.blocks = []
        for i in range(self.header.num_blocks):
            self.blocks.append(Op1.CompressedBlock(i, self._io, self, self._root))



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.offsets)):
            pass

        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class CompressedBlock(KaitaiStruct):
        def __init__(self, idx, _io, _parent=None, _root=None):
            super(Op1.CompressedBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.idx = idx
            self._read()

        def _read(self):
            self._raw_data = self._io.read_bytes(self._root.offsets[self.idx + 1] - self._root.offsets[self.idx])
            _process = Zstd()
            self.data = _process.decode(self._raw_data)


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            super(Op1.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.unused = []
            for i in range(16):
                self.unused.append(self._io.read_u1())

            self.basename = (self._io.read_bytes(16)).decode(u"ASCII")
            self.num_elements = self._io.read_u8le()
            self.kk_index = self._io.read_u4le()
            self.max_dtc = self._io.read_u4le()
            self.block_size = self._io.read_u4le()
            self.num_blocks = self._io.read_u4le()
            self.nrows = self._io.read_u1()
            self.ncols = self._io.read_u1()
            self.side = KaitaiStream.resolve_enum(Op1.Side, self._io.read_u1())
            self.metric = self._io.read_u1()
            self.compression = KaitaiStream.resolve_enum(Op1.Compression, self._io.read_u1())
            self.index_size = self._io.read_u1()
            self.format_type = self._io.read_u1()
            self.list_element_size = self._io.read_u1()


        def _fetch_instances(self):
            pass
            for i in range(len(self.unused)):
                pass




